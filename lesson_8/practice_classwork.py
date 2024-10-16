movies: list[dict] = []
genres = {
    1: "horror",
    2: "thriller",
    3: "drama",
    4: "adventure"
}

def add_movie():
     # = input("enter a movie: ")
    title = input("enter a title: ")

    genre_msg = []
    for key, genre in genres.items():
        genre_msg.append(f"{key}) {genre}\n")
    genre_msg = "".join(genre_msg)
    genre_key = int(input(f"enter a genre:\n{genre_msg}"))
    genre = genres[genre_key]
    rating = int(input(f"enter a rating: "))
    movie_data = {
        "title": title,
        "genre": genre,
        "rating": rating
                }
    movies.append(movie_data)





def get_recommendations(all_movies , preferred_genre, min_rating):
    # list_horror = ("Перелом IMDb: 5,6, Лихорадка IMDb: 4,8, Незнакомец IMDb: 4,9, Пруд IMDb: 3,9")
    # if a == "horror":
    #     print("Recommendation: " + list_horror)
    #
    # list_thriller = ("Зуб и ноготь IMDb 4,7, Укус IMDb 4,9, Призрак у маяка MDb 4,6, Последняя остановка IMDb 4,8")
    # if a == "thriller":
    #     print("Recommendation: " + list_thriller)
    #
    # if a == "drama":
    #     print("Я не робот 3.2, Школа Мурим 3.5, Парень и девушка прошлого века 3.1, Полночный ресторан 2.3")
    #
    # if a == "adventure":
    #     print("")
    recommendations = []
    for movie_data in all_movies:
        if movie_data["genre"] == preferred_genre and movie_data["rating"] >= min_rating:
            recommendations.append(movie_data)

    for movie_data in all_movies:
        if movie_data["genre"] != preferred_genre and movie_data["rating"] >= min_rating:
            recommendations.append(movie_data)

    print(recommendations)








def menu():
    user_cmd = ""
    while user_cmd != "exit":
        user_cmd = input()
        if user_cmd == "1":
            add_movie()
        if user_cmd == "2":
            genre_msg = []
            for key, genre in genres.items():
                genre_msg.append(f"{key}) {genre}\n")
            genre_msg = "".join(genre_msg)
            genre_key = int(input(f"enter a genre:\n{genre_msg}"))
            genre = genres[genre_key]
            min_rating = int(input("Rating:"))
            get_recommendations(movies, genre, min_rating)

menu()


