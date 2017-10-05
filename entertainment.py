import fresh_tomatoes
import media
toy_story=media.Movie("Toy Story",
					  "A Story About A Boy And His Toys who come to life",
					  "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
					  "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
					  "A Story About A Marine on a different planet and his adventures ",
					  "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
					  "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
BadBoys=media.Movie("BadBoy",
					  "A Story About A Pair of Cops in the DEA ",
					  "https://en.wikipedia.org/wiki/Bad_Boys_(1995_film)#/media/File:Bad_Boys.jpg",
					  "https://www.youtube.com/watch?v=mPQ_uErLwFE")

Oceans11=media.Movie("Oceans11",
					  "A Story About A Gang of 11 robbers who rob a casino ",
					  "https://en.wikipedia.org/wiki/Ocean%27s_Eleven#/media/File:Ocean%27s_Eleven_2001_Poster.jpg",
					  "https://www.youtube.com/watch?v=u7VTkceSsEw")
Oceans12=media.Movie("Oceans12",
					  "A Story About A Gang of 12 robbers who rob a casino ",
					  "https://en.wikipedia.org/wiki/Ocean%27s_Twelve#/media/File:Ocean%27s12Poster1.gif",
					  "https://www.youtube.com/watch?v=k5CZa3X4yF4")
Oceans13=media.Movie("Oceans13",
					  "A Story About A Gang of 13 robbers who rob a casino ",
					  "https://en.wikipedia.org/wiki/Ocean%27s_Thirteen#/media/File:Oceans13Poster1.jpg",
					  "https://www.youtube.com/watch?v=L-EyG12LxME")
movies=[toy_story,avatar,BadBoys,Oceans11,Oceans12,Oceans13]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)