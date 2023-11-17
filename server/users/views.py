from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

import pymongo

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

async def async_mongo_pull_user(id):

	load_dotenv()

	uri = os.getenv('connection_string')
	
	client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
	
	db = client.prkings
	
	collection = db.users
	
	document = await collection.find_one({"id": id}, {'_id': False})

	return document

def external_query_database(requst):
	load_dotenv()

	uri = os.getenv('connection_string')
	
	client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
	
	db = client.prkings
	
	collection = db.users

	db_dict = {'db': []}
	for item in collection.find({}, { '_id': 0}):
		db_dict['db'].append(item)

	return JsonResponse(db_dict)

	 
def query_database():
	load_dotenv()

	uri = os.getenv('connection_string')
	
	client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
	
	db = client.prkings
	
	collection = db.users
	 
	return collection.find()




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

	return JsonResponse(asyncio.run(async_mongo_pull_user(id)))

def leaderboard(request):

	requested_lift = request.GET.get('lift', '')
	db = query_database()

	names, lifts = [],[]
	for user in db:
		names.append(user['name'])
		lifts.append(user['lifts'][requested_lift])
	
	return JsonResponse({'leaderboard': [names,lifts]})






if __name__ == '__main__':
	print(query_database())