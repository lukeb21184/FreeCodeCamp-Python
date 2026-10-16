class Movie:
    def __init__(self, title, year, director, duration):
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


class MediaCatalogue:
    def __init__(self):
        self.items = []

    def add(self, media_item):
        self.items.append(media_item)

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        for index, item in enumerate(self.items, start=1):
            result += f"{index}. {item}\n"
            
        return result


try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
except ValueError as e:
    print(f'Validation Error: {e}')
