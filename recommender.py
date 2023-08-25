"""
This function takes user input as a dictionary
and recommends movies
"""
import random
MOVIES = [f"movies_{i}" for i in range(1, 300)]
random.shuffle(MOVIES)
def recommend_movies(user_input):
    return MOVIES[:3]

if __name__ == "__main__":
    user_input = {"movie1": 2, "movie2": 5, "movie3":4}
    print(recommend_movies(user_input))

