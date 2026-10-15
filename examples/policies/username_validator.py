def is_valid_username(username):


    if not username:
        return False
    if len(username) < 3:
        return False
    return True
