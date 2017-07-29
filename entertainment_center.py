# Use the file here to make your favorite movie lists through media

import media
import fresh_tomatoes


oblivion = media.movie('Oblivion', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwMDY0MTA4MF5BMl5BanBnXkFtZTcwNzI3MDgxOQ@@._V1_UY1200_CR64,0,630,1200_AL_.jpg', 'https://www.youtube.com/watch?v=XmIIgE7eSak')

pacific_rim = media.movie('Pacific Rim: Uprising', 'https://resizing.flixster.com/MbiJhGRyRcftBfFpMg61V2OuEdQ=/300x300/v1.bTsxMTE3MzkzMztqOzE3NDU0OzEyMDA7ODAwOzEyMDA', 'https://www.youtube.com/watch?v=5guMumPFBag')

interstellar = media.movie('Interstellar', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg', 'https://www.youtube.com/watch?v=0vxOhd4qlnA')

movie_list = [oblivion, pacific_rim, interstellar]

fresh_tomatoes.open_movies_page(movie_list)
