from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ApplicantProfile
from job_applications.models import JobApplication
from .forms import ApplicantProfileForm, ApplicantProfileFilter
from job_offers.models import JobOffer
# Data processing
import pandas as pd
import numpy as np
import scipy.stats
# Similarity
from sklearn.metrics.pairwise import cosine_similarity
import csv

def applicants_home(request):
    if request.user.is_authenticated and request.user.is_applicant:
        user_id = request.user.id
        
        #Get Recommendations
        recommendations = job_recommendations(user_id)
        recommendations = [x[0] for x in recommendations]
        
        #Get Job Offer Object
        job_offers = JobOffer.objects.filter(id__in=recommendations)
        
        return render(request, "applicants-home.html", {'job_offers' : job_offers})
    else:
        return render(request, "applicants-home.html")

@login_required  # restrict access to authenticated users
def applicant_profile(request, pk):
    # Retrieve the ApplicantProfile instance based on the provided primary key (pk)
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)

    if request.method == 'POST':
        # If the form is submitted, update the instance with the posted data
        form = ApplicantProfileForm(request.POST, instance=applicant_profile)
        if form.is_valid():
            form.save()
            #Succes!
            return redirect('applicants-home')
    else:
        # If it's a GET request, display the form with the existing data
        form = ApplicantProfileForm(instance=applicant_profile)

    context = {
        'form': form,
        'applicant_profile': applicant_profile,
    }

    return render(request, 'applicant-profile.html', context)

def applicant_filter(request, pk, site):
    # Retrieve the ApplicantProfile instance based on the provided primary key (pk)
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)

    if request.method == 'POST':
        # If the form is submitted, update the instance with the posted data
        form = ApplicantProfileFilter(request.POST, instance=applicant_profile)
        if form.is_valid():
            form.save()
            #Succes!
            return redirect('applicants-home')
    else:
        # If it's a GET request, display the form with the existing data
        form = ApplicantProfileFilter(instance=applicant_profile)
        
    context = {
        'form': form,
    }

    return render(request, site, context)

def search_job_offers(request):
    job_title_query = request.GET.get('job_title', '')
    job_offers = JobOffer.objects.filter(job_title__icontains=job_title_query)

    if not job_offers or job_title_query == '':
        return render(request, 'no_results.html', {'job_title_query': job_title_query})
    
    return render(request, 'search_results.html', {'job_offers': job_offers})

def job_recommendations(pk):
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)
    picked_user = applicant_profile.id

    # Recuperar todas las aplicaciones y ofertas de trabajo de la base de datos
    # Exportar JobApplication
    job_applications = JobApplication.objects.all()
    with open('job_applications.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'candidate_id', 'job_offer_id', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for application in job_applications:
            writer.writerow({'id': application.id, 'candidate_id': application.candidate_id, 'job_offer_id': application.job_offer_id, 'status': application.status})

    # Exportar JobOffer
    job_offers = JobOffer.objects.all()
    with open('job_offers.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'job_title', 'description']  # Modifica esto según los campos que tengas en tu modelo JobOffer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for offer in job_offers:
            writer.writerow({'id': offer.id, 'job_title': offer.job_title, 'description': offer.description})  # Modifica esto según los campos que tengas en tu modelo JobOffer

    # 2. Cargar los archivos CSV en DataFrames de pandas
    job_applications = pd.read_csv('job_applications.csv')
    job_offers = pd.read_csv('job_offers.csv')

    #applications_count = job_applications.groupby('job_offer_id').size().reset_index(name='num_applications')
    #job_offers_with_applications_count = pd.merge(job_offers, applications_count, how='left', left_on='id', right_on='job_offer_id')
    
    # Merge job_applications with job_offers to get the relevant data
    merged_data = pd.merge(job_applications, job_offers, how='outer', left_on='job_offer_id', right_on='id')

    # Pivot the merged data to get the matrix format
    matrix = merged_data.pivot(index='candidate_id', columns='job_offer_id', values='status')

    # Replace non-application entries with NaN
    matrix[matrix.notnull()] = 1

    #Get Users with similarities
    #user_similarity = matrix.T.corr()

    # Convert NaN values to 0 (no application) for cosine similarity calculation
    matrix_filled = matrix.fillna(0)

    # Calculate cosine similarity between users
    user_similarity_matrix = cosine_similarity(matrix_filled)

    # Convert the similarity matrix to a DataFrame for easier interpretation
    user_similarity_df = pd.DataFrame(user_similarity_matrix, index=matrix.index, columns=matrix.index)
    
    user_similarity_threshold = 0.3

    # Get top n similar users
    similar_users = user_similarity_df[user_similarity_df[picked_user]>user_similarity_threshold][picked_user].sort_values(ascending=False)

    #print(f'The similar users for user {picked_userid} are', similar_users)

    #Remove the applications that user had applied
    picked_userid = matrix[matrix.index == picked_user].dropna(axis=1, how='all')

    # Applications that similar users applied. Remove applications that none of the similar users have applied to
    similar_user_applications = matrix[matrix.index.isin(similar_users.index)].dropna(axis=1, how='all')

    # Remove the applied application from the application list
    similar_user_applications.drop(picked_userid.columns,axis=1, inplace=True, errors='ignore')

    # A dictionary to store item scores
    item_score = {}

    # Loop through items
    for i in similar_user_applications.columns:
        # Get the ratings for movie i
        rating = similar_user_applications[i]
        # Create a variable to store the score
        total = 0
        # Create a variable to store the number of scores
        count = 0
        # Loop through similar users
        for u in similar_users.index:
            # If the movie has rating
            if pd.isna(rating[u]) == False:
                # Score is the sum of user similarity score multiply by the movie rating
                score = similar_users[u] * rating[u]
                # Add the score to the total score for the movie so far
                total += score
                # Add 1 to the count
                count +=1
        # Get the average score for the item
        item_score[i] = total / count

    # Convert dictionary to pandas dataframe
    item_score = pd.DataFrame(item_score.items(), columns=['job_offer_id', 'job_offer_score'])

    # Guardar los resultados ordenados por 'job_offer_score' en una lista de diccionarios
    recommendations_list = item_score.sort_values(by='job_offer_score', ascending=False).to_records(index=False)

    # Convertir la lista de diccionarios en una lista de tuplas
    recommendations = [(rec['job_offer_id'], rec['job_offer_score']) for rec in recommendations_list]

    return recommendations