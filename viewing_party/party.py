# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watch_list = user_data["watchlist"]
    
    for movie_dict in watch_list:
        if type(movie_dict) is dict: # To avoid throw an error
            if movie_dict.get("title") == title:
                watch_list.remove(movie_dict)
                user_data["watched"].append(movie_dict)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # user data:{'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
    # 'friends': [{...}, {...}]}
    # Compare watched/titles != friends/titles: add to answer dict
    # return a list of dictionaries(movie_dict)


    # # USER_DATA_3["friends"] =  [
    #     {
    #         "watched": [
    #             FANTASY_1,
    #             FANTASY_3,
    #             FANTASY_4,
    #             HORROR_1,
    #         ]
    #     },
    #     {
    #         "watched": [
    #             FANTASY_1,
    #             ACTION_1,
    #             INTRIGUE_1,
    #             INTRIGUE_3,
    #         ]
    #     }
    # ]

    watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    
    for movie_dict in watched_list:
        if type(movie_dict) is dict: # To avoid throw an error
            if movie_dict.get("title") == :
                watched_list.remove(movie_dict)
                user_data["watched"].append(movie_dict)

    return user_data
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

