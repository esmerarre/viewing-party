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
def get_watched_avg_rating(user_data):
    watched = user_data.get("watched", [])
    if not watched:
        return 0

    total_rating = 0
    for item in watched:
        total_rating += item.get("rating", 0)

    average = total_rating / len(watched)
    return average

def get_most_watched_genre(user_data):
    watched_genre_freq = {}
    watched = user_data["watched"]
    for movie_dict in watched:
        movie_genre = movie_dict["genre"]
        watched_genre_freq[movie_genre] = watched_genre_freq.get(movie_genre, 0) +1
    
    top_genre = None
    genre_freq = 0

    for genre, freq in watched_genre_freq.items():
        if freq > genre_freq:
            top_genre = genre
            genre_freq = freq
    
    return top_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# Return user watched movie but none of freinds have watched list of dictionary
def get_unique_watched(user_data):
    not_watched = []
    friend_movie_titles = []
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]

    for friend_watched_dict in friends_list:
        list_of_movie_dict_friend = friend_watched_dict["watched"]
        for friend_movie_dict in list_of_movie_dict_friend:
            friend_movie_titles.append(friend_movie_dict.get("title"))            
    
    for movie_dict in watched_list:
        if movie_dict.get("title") not in friend_movie_titles:
            not_watched.append(movie_dict)

    return not_watched

# Determine which movies at least one of the user's friends have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    
    user_movie_titles = []
    friends_unique = []
    
    # Get user watched movie titles(list of string titles)
    for movie_dict in user_watched_list:
        user_movie_titles.append(movie_dict.get("title"))

    # friend is a dictionary of "watched" as key and a list of movie dictionaries as value
    for friend in friends_list:
        for friend_movie in friend["watched"]:
            title = friend_movie.get("title")
        
            if title not in user_movie_titles and friend_movie not in friends_unique:
                friends_unique.append(friend_movie)

    return friends_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    subscription_list = user_data["subscriptions"]
    recommendation_list = []
    user_unwatched = get_friends_unique_watched(user_data)
 
    for movie_dict in user_unwatched:
        if movie_dict["host"] in subscription_list:
            recommendation_list.append(movie_dict)

    return recommendation_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    user_unwatched = get_friends_unique_watched(user_data)
    recommendation_list = []
    user_watched_most_genre = get_most_watched_genre(user_data)

    for movie_dict in user_unwatched:
        if movie_dict["genre"] == user_watched_most_genre:
            recommendation_list.append(movie_dict)
        
    return recommendation_list

def get_rec_from_favorites(user_data):
    favorites_list = user_data["favorites"]
    recommendation_list = []
    friends_unwatched = get_unique_watched(user_data)
    for movie_dict in friends_unwatched:
        if movie_dict in favorites_list:
            recommendation_list.append(movie_dict)

    return recommendation_list
