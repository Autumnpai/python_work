def build_profile(
        first, last, loooooooooooooooooooooooooooooooooooooooooooooooooooog, 
        **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['long']= loooooooooooooooooooooooooooooooooooooooooooooooooooog
    return user_info

user_profile = build_profile(
    'autumn', 'pai', 'surelong', height='172cm', 
    hobby='reading', dream='freedom')

print(user_profile)