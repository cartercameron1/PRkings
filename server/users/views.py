from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

sample_user = {'id': 69, 'name': 'A.S. Muncher'}

def sample(request):
    return JsonResponse(sample_user)
