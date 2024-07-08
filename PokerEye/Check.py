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

    print(f"Attempting to insert: {data}")

    try:
        collection.insert_one(data)
        return f"Inserted record: {data}"
    except errors.DuplicateKeyError:
        print(f"Duplicate record found, updating existing record: {data}")
        # Update the existing record
        result = collection.update_one(
            {'Hand': Hand, 'Combinations': Combinations},
            {'$set': {'Score': Score, 'Time': Time}}
        )
        if result.matched_count:
            return f"Updated record: {data}\n\n"
        else:
            return f"Failed to update record: {data}\n\n"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
tm = datetime.now().strftime('%H:%M')
print(mongoDataBaseUpdater('ddffgg', 'abc', 5, Time=tm))

tm = datetime.now().strftime('%H:%M')
print(mongoDataBaseUpdater('efgh', 'qrt', 5, Time=tm))

# Close the client when you're done with it (if running in a long-lived application, this should be done at shutdown)
client.close()
