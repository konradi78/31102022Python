

from pymongo import *

db = MongoClient(
    'mongodb://telrun:tr2022@ab88.space:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1').project




result = db.reports.aggregate([
    {
        '$group': {
            'avg_bugs': {'$avg': '$avg_bugs'},
            'min_bugs': {'$min': '$min_bugs'},
            'max_bugs': {'$max': '$max_bugs'},
            'total_bugs': {'$sum': '$total_bugs'}
        }
    }
]
)

for item in result:
    print(item)

