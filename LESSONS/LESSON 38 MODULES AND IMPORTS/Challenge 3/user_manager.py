


_USER_DB = {
    101 : {"name" : "Olowu Emmanuel .O." ,"status" : "Active"},
    102 : {"name" : "Adebolawe Moses", "status" : "Inactive"}
}


def fetch_user_data(user_id: int):
    return _USER_DB.get(user_id)

print(fetch_user_data(101)['name'])