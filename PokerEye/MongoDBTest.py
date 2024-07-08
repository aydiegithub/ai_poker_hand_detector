from pymongo import MongoClient, errors
from datetime import datetime

# Initialize MongoDB client and collection outside the function
client = MongoClient('mongodb://localhost:27017/')
db = client['PokerEyeTest']
collection = db['PokerEyeTestData']

# Create the unique index if it doesn't exist (this should run once during initialization)
collection.create_index([("Hand", 1), ("Combinations", 1)], unique=True)

def mongoDataBaseUpdater(Hand, Combinations, Score, Time):

    latest = collection.find_one(sort=[('_id', -1)])

    if latest is None:
        latest_id = 1
    else:
        latest_id = latest['_id'] + 1

    data = {
        '_id': latest_id,
        'Hand': Hand,
        'Combinations': Combinations,
        'Score': Score,
        'Time': Time
    }

    #print(f"Attempting to insert: {data}")

    try:
        collection.insert_one(data)
        return f"New Inserted record......"
    except errors.DuplicateKeyError:
        return f"Duplicate Record Found......"
        # Update the existing record
        result = collection.update_one({'Hand': Hand, 'Combinations': Combinations},
                                       {'$set': {'Score': Score, 'Time': Time}})
        if result.matched_count:
            return f"Old Record Updated......\n"
        else:
            return f"Update Failed\n\n"
    except Exception as e:
        return f"An error occurred: {e}"

#client.close()