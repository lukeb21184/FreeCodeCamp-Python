class Movie:
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
