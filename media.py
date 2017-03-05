import webbrowser


class Movie():
    ''' This class defines the common variables
            and the method to open a trailer on youtube'''

    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer):
		''' This explains the intializing menthod with the common
		variables that'd be accessed across different instances '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer

    def showtrailer(self):
		''' this explains how the trailer would be rendered on the page '''
        webbrowser.open(self.trailer)
