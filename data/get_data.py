# All the data should be stored in a NOSQL database (mongoDB?)
# A live connection to filter data during the process of running the script should be implemented.
# Meaning during the process of filtering and plotting new data should be
# transferred from the database to the python script / dashboard

# Get dataframe from a .csv file
def get_dataframe_from_csv(filepath):
    df = "csv"
    return df


# Get dataframe from MongoDB
def get_dataframe_from_mongodb(database, query):
    df = "mongo"
    return df
