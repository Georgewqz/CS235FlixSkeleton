from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie:Movie, review_text : str, rating : int):
        self.__movie = movie
        self.__review_text = review_text
        self.__rating = None
        self.__timestamp = datetime.today()
        if type(rating) is int:
            if rating > 0 and rating <= 10:
                self.__rating = rating
           
    @property
    def movie(self):
        return self.__movie
        
    @property
    def review_text(self):
        return self.__review_text
        
    @property
    def rating(self):
        return self.__rating
        
    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__timestamp}"
        
    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        return False

    def hash(self):
        return hash((self.__movie, self.__timestamp))
