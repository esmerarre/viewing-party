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
    for movie in watched:
        movie_genre = movie["genre"]
        watched_genre_freq[movie_genre] = watched_genre_freq.get(movie_genre, 0) +1
    
    top_genre = None
    genre_freq = 0

    for genres, freq in watched_genre_freq.items():
        if freq > genre_freq:
            top_genre = genres
            genre_freq = freq
    
    return top_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    not_watched = []
    friend_movie_titles = []
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]

    for index in friends_list:
        list_of_movie_dict_friend = index["watched"]
        for index in list_of_movie_dict_friend:
            friend_movie_titles.append(index.get("title"))            
    
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
        # e.g ['The Lord of the Functions: The Fellowship of the Function']
        user_movie_titles.append(movie_dict.get("title"))
        #print(user_movie_titles)

    # friend is a dictionary of "watched" as key and a list of movie dictionaries as value
    for friend in friends_list:
        print(friend)
        for friend_movie in friend["watched"]:
            title = friend_movie.get("title")
        
            if title not in user_movie_titles and friend_movie not in friends_unique:
                friends_unique.append(friend_movie)

    return friends_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

