# You have a list of user IDs who visited a website. Some visited multiple times. 
# Use a set to find how many unique users visited, and a dictionary to count how many times 
# each unique user visited.

# List of user IDs (some repeated)
visits = [101, 102, 103, 101, 104, 102, 101, 105]

unique_visit = len(set(visits))

number_of_visits = {}

for user_id in visits:
    number_of_visits[user_id] = number_of_visits.get(user_id,0) + 1

print(f"Unique users who visited are : {unique_visit} in number")
print(f"visit counts per user : {number_of_visits}")
