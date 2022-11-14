from datetime import datetime
from pymongo import *

db = MongoClient('mongodb://telrun:tr2022@ab88.space:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1').project

int bugs_count = 10
int duration_secs = 20

 def func(bugs_count, duration_secs
        ):
     return bugs_count, duration_secs

db.project.update(
bugs_count
duration_secs)




