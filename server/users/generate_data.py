import random
from faker import Faker

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

fake = Faker()

def generate_random_lift_records():
    return [
        random.randint(200, 300),
        random.randint(200, 300),
        random.randint(200, 300)
    ]

def generate_random_lift_dates():
    return [
        fake.date_between(start_date="-1y", end_date="today").strftime("%m/%d/%Y"),
        fake.date_between(start_date="-1y", end_date="today").strftime("%m/%d/%Y"),
        fake.date_between(start_date="-1y", end_date="today").strftime("%m/%d/%Y")
    ]


def generate_random_data(id):
    return {
        "id": id,
        "name": fake.name(),
        "gymID": random.randint(1, 1000),
        "age": random.randint(18, 80),
        "sex": random.choice(["male", "female"]),
        "height": random.randint(60, 90),
        "lifts": {
            "bench": random.randint(400, 600),
            "squat": random.randint(800, 1000),
            "deadlift": random.randint(100, 200)
        },
        "overhead_press": [generate_random_lift_records(), generate_random_lift_dates()],
        "barbell_row": [generate_random_lift_records(), generate_random_lift_dates()],
        "leg_press": [generate_random_lift_records(), generate_random_lift_dates()],
        "lat_pulldown": [generate_random_lift_records(), generate_random_lift_dates()]
    }
    
    
if __name__ == '__main__':
    
        
    load_dotenv()

    uri = os.getenv('connection_string')

    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

    db = client.prkings

    collection = db.users

    items_to_insert = []

    for id in range(0,69):
        items_to_insert.append(generate_random_data(id))

    print(items_to_insert)

    collection.insert_many(items_to_insert)
