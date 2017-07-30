class movie():
    # Connects movie information to a variable
    # The title of the movie is the first input.
    # The second is the poster url image for the movie.
    # The third is the youtube url for the trailer.
    # These variables will be called in fresh_tomatoes
    # to post said information to the web page.
    def __init__(self, title, poster_url, youtube_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
