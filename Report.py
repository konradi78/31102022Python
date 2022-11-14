# написать функцию добавления в БД нового отчета, которая на входе получает два аргумента:
# bugs_count - кол-во ошибок
# duration_secs - продолжительность тестирования
# и записывает данный отчет в
# - БД: project
# - Коллекция: reports

from pymongo import *

db = MongoClient('mongodb://telrun:tr2022@ab88.space:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1').project



result = db.project.count

print (result)