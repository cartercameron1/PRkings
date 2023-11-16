from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

async def mongo_pull_user(id):

	load_dotenv()

	uri = os.getenv('connection_string')
	
	client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
	
	db = client.prkings
	
	collection = db.users
	
	document = await collection.find_one({"id": id}, {'_id': False})

	return document


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
		"deadlift": 1390
	}
}

def sample(request):
	return JsonResponse(sample_user)

def get_user(request):

	id = int(request.GET.get('id', ''))

	return JsonResponse(asyncio.run(mongo_pull_user(id)))



