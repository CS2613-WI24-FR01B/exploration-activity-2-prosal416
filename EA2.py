import numpy as np

# Christopher Nolan movie data (Movie name, ratings out of 10)
nolan_movies_data = [
    ("Oppenheimer", "Drama", 181, 8.3),
    ("Tenet", "Sci-fi", 150, 7.3),
    ("Dunkirk", "War", 107, 7.8),
    ("Interstellar", "Sci-fi", 169, 8.7),
    ("The Dark Knight Rises", "Action", 165, 8.4),
    ("Inception", "Action", 148, 8.8),
    ("The Dark Knight", "Action", 152, 9.0),
    ("The Prestige", "Fantasy", 130, 8.5),
    ("Batman Begins", "Action", 140,8.2),
    ("Insomnia", "Thriller", 118, 7.2),
    ("Memento", "Mystery", 113, 8.4),
    ("Following", "Thriller", 69, 7.5)
]

villneuve_movies_data = [
    ("Dune: Part Two", "Sci-fi", 167, 8.8),
    ("Dune", "Sci-fi", 155, 8.0),
    ("Blade Runner 2049", "Sci-fi", 164, 8.0),
    ("Arrival", "Sci-fi", 116, 7.9),
    ("Sicario", "Crime", 122, 7.7),
    ("Enemy", "Drama", 91, 6.9),
    ("Prisoners", "Drama", 153, 8.2),
    ("Incendies", "War", 131, 8.3),
    ("Polytechnique", "Drama", 77,7.2),
    ("Maelstrom", "Drama", 87,6.7),
    ("August 32nd on Earth", "Drama", 88,6.5)
]

kubrick_movies_data = [
    ("Eyes Wide Shut", "Mystery", 159, 7.5),
    ("Full Metal Jacket", "War", 117, 8.3),
    ("The Shinning", "Horror", 144, 8.4),
    ("Barry Lyndon", "Drama", 185, 8.1),
    ("A Clockwork Orange", "Crime", 137, 8.3),
    ("2001: A Space Odyssey", "Sci-fi", 149, 8.3),
    ("Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "War", 95, 8.4),
    ("Lolita", "Drama", 154, 7.5),
    ("Spartacus", "War", 197,7.9),
    ("Paths of Glory", "War", 88,8.4),
    ("The Killing", "Crime", 85,7.9)
]

def analyze(movies_data):
    movie_names = np.array([movie[0] for movie in movies_data])
    genres = np.array([movie[1] for movie in movies_data])
    durations = np.array([movie[2] for movie in movies_data])
    ratings = np.array([movie[3] for movie in movies_data])

    unique_genres = np.unique(genres)
    genre_avg_ratings = np.array([np.mean(ratings[genres == genre]) for genre in unique_genres])

    duration_rating_corr = np.corrcoef(durations, ratings)[0, 1]

    longest_movie = movie_names[np.argmax(durations)]
    shortest_movie = movie_names[np.argmin(durations)]

    print("Movie Data Analysis:")
    print("--------------------")
    print(f"Total Movies: {len(movies_data)}")
    print(f"Genres: {', '.join(unique_genres)}")
    print(f"Average Ratings by Genre:")
    for genre, avg_rating in zip(unique_genres, genre_avg_ratings):
        print(f"\t{genre}: {avg_rating:.2f}")
    print(f"Correlation between Duration and Rating: {duration_rating_corr:.2f}")
    print(f"Longest Movie: {longest_movie} ({np.max(durations)} minutes)")
    print(f"Shortest Movie: {shortest_movie} ({np.min(durations)} minutes)")

while True:
    print("Which filmography to analyze?")
    print("1. Christopher Nolan")
    print("2. Denis Vilneeuve")
    print("3. Stanley Kubrick")
    print("Enter anything to leave")
    choice=input("Enter your choice: ")
    
    if choice=='1':
        analyze(nolan_movies_data)
    elif choice=='2':
        analyze(villneuve_movies_data)
    elif choice=='3':
        analyze(kubrick_movies_data)
    else:
        break