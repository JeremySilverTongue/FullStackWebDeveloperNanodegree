import media
import fresh_tomatoes

mad_max = media.Movie("Mad Max", "I wanna die historic on the fury road.",
    "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8"
    )

the_martian = media.Movie("The Martian", "Space piracy. MATT DAAAAAAAAMON",
    "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")


movies = [mad_max, the_martian]
fresh_tomatoes.open_movies_page(movies)
