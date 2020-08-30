from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title : str, release_year : int):
        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
    
        if title != "":
            self.__title = title
        else:
            self.__title = None
        
        if release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None
        
    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"
       
    def __eq__(self, other):
        return (self.__title == other.__title) and (self.__release_year == other.__release_year)
        
    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        else:
            return self.__title < other.__title

    def __hash__(self):
        return hash((self.__title, self.__release_year))
        
    @property
    def title(self):
        return self.__title

    @property
    def release_year(self):
        return self.__release_year

    @property
    def description(self):
        return self.__description

    @property
    def director(self):
        return self.__director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @description.setter
    def description(self, new_description):
        self.__description = new_description
            
    @director.setter
    def director(self, new_director):
        self.__director = new_director
            
    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime_minutes):
        if new_runtime_minutes > 0:
            self.__runtime_minutes = new_runtime_minutes
        else:
            raise ValueError
        
    def add_actor(self, actor):
        self.__actors.append(actor)
            
    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        self.__genres.append(genre)
            
    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
