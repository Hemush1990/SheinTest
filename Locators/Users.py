users = [
    {"email": "hemushpetrosyan@gmail.com", "password": "test1234"},
    {"email": "valid@gmail.com", "password": "MyPassword"},
    {"email": "admin@test.com", "password": "qwert1234"}


]

def get_user(email):
    for user in users:
        return user
    print("\n User" + email + " is not defined, enter a valid user.")