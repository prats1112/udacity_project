import media
import fresh_tomatoes

# intializing multiple instances of the class Movie for different movies
# that I want to render on the html page

toy_story = media.Movie("Toy story", "A story about a boy",
                        "http://cdn.skim.gs/image/upload/v1456337778/msi/toy-story-3-teaser_s3punv.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

money_ball = media.Movie("Money Ball", "Story about statistics in sports",
                         "http://www.entertainmentwallpaper.com/images/desktops/movie/moneyball07.jpg",
                         "https://www.youtube.com/watch?v=-4QPVo0UIzc")

chakde = media.Movie("Chakde", "Story of Indian womens hockey team lifiting the world cup",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/Chak_De!_India.jpg",
                     "https://www.youtube.com/watch?v=6a0-dSMWm5g")

dangal = media.Movie("Dangal", "Rise of Indian Women in Wrestling events",
                     "https://i.ytimg.com/vi/x_7YlGv9u1g/maxresdefault.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

ipman = media.Movie("IP MAN", "Chinese martial arts rennaisance",
                    "https://martialartsactionmovies.com/wp-content/uploads/2015/11/Ip-Man-212x300.jpg",
                    "https://www.youtube.com/watch?v=jckXscMwIOI")

darkknight = media.Movie("Dark Knight Rises", '''Dark Knight Rises is the third and final
	installment in Christopher Nolan's Batman film''',
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
                         "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# initilazing an array with the name of the instances to feed it to the html page
movies = [toy_story, money_ball, chakde, dangal, ipman, darkknight]

# calling the function in another script to render the final html page
fresh_tomatoes.open_movies_page(movies)
