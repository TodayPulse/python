# List of user IDs (some repeated)
visits = [101, 102, 103, 101, 104, 102, 101, 105]

# Using a set to find unique users and a dict for counts
unique_users = set(visits)
visit_counts = {}

for user_id in visits:
    # Safely count: if user_id is not in the dict, start at 0 and add 1
    visit_counts[user_id] = visit_counts.get(user_id,0)

# Output results
print(f"Unique users count: {len(unique_users)}")
print(f"Visit counts per user: {visit_counts}")