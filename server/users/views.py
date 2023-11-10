from django.shortcuts import render
from django.http import JsonResponse
import json


sample_user = {
	"id": 69,
	"name": "A.S Muncher",
	"gymID": 420,
	"DOB": 70,
	"sex": "male",
	"height": 80,
	"lifts": {
		"bench": 585,
		"squat": 952,
		"deadlift": 139
	}
}

def sample(request):

    return JsonResponse(sample_user)

