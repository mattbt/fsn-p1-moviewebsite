import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_year, imdb_rating, movie_storyline, poster_image, trailer_youtube):
        """ Init Movie instance """
        self.title = movie_title
        self.year = movie_year
        self.imdbRating = imdb_rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open movie trailer """
        webbrowser.open(self.trailer_youtube_url)
