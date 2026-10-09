class Movie:
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
