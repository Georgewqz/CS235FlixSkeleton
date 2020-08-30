from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__start_index = 0

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)
        
    def select_movie_to_watch(self, index):
        if index < 0 or index >= len(self.__watchlist):
            return None
        else:
            return self.__watchlist[index]
        
    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) > 0:
            return self.__watchlist[0]

    def __iter__(self):
        return iter(self.__watchlist)

    def __next__(self):
        if self.__start_index >= self.size()-1:
            raise StopIteration
        else:
            self.__start_index += 1
            return self.__watchlist[self.__start_index]
