from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
url = "mongodb+srv://Prithwish_2003:Prithwish2003@cluster0.1pfkhoz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(url)

# create database name and collection name
DATABASE_NAME="sensorfault"
COLLECTION_NAME="waferfault"

# read the data as a dataframe
df=pd.read_csv(r"D:\ML Project\ML Project For Prithwish Ghosh\Wafer-Sensor-Fault\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)