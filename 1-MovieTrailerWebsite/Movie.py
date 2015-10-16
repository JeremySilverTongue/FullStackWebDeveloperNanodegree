class Movie():
    """Struct holding information about a movie"""
    def __init__(
            self, title, storyline, poster_image_url,
            trailer_youtube_url, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating
