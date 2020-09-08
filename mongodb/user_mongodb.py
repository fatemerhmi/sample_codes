from pymongo import MongoClient
import datetime
import configparser

Config = configparser.ConfigParser()
Config.read('./info.conf')
duration = int(Config.get("ttl", "duration"))

client = MongoClient()
# getting the database
db = client.mongodb_insta
#getting a collection
users_collection = db.users

def check_username(username):
    if username==None or username=="":
        print("Error: Username was None or empty")
        return -1
    username = str(username) 
    print("check_username = " + username)
    try:
        user = users_collection.find_one({'username': username})
        if user != None:
            if user["ttl"] > datetime.datetime.utcnow():
                return user['_id']
            else:
                return -2
        return -1
    except Exception as err:
        print("Error(check_username): could not execute the query!")
        print(err)
        return -1

def update_username(id, new_username):
    if new_username==None or new_username=="" or id==None or id=="" :
        print("Error: Username or id was None or empty")
        return -1
    id = str(id)
    new_username = str(new_username)
    try:
        users_collection.update(
            {"_id": id},
            {"$set" : {"username": new_username, "ttl": datetime.datetime.utcnow() + datetime.timedelta(days=duration)}}
        )
        return 1
    except Exception as err:
        print("Error(update_username): could not execute the query!")
        print(err)
        return -1

def add_username(id, username):
    if username==None or username=="" or id==None or id=="" :
        print("Error: Username or id was None or empty!")
        return -1
    id=str(id)
    username = str(username)
    user = {
    "_id" : id,
    "username" : username,
    "ttl": datetime.datetime.utcnow() + datetime.timedelta(days=duration)
    }
    try:
        check_username = users_collection.find_one({'username': username})
        if check_username != None:
            print("Error: This username already exists!")
            return -1
    except: 
        print("Error: could not execute the query!")
    
    try:
        check_id = users_collection.find_one({'_id': id})
        if check_id != None:
            print("Error: This username already exists!")
            return -1
    except:
        print("Error: could not execute the query!")
    try:
        users_collection.insert_one(user)
        return 1
    except:
        print("Error: new user not added!")
        return -1

# print(check_username("x"))
# print(check_username("f"))
# print(check_username("$$"))
# print(check_username(None))
# add_username("39887","hhhh")
# add_username("","")
# update_username("","hhhh")
