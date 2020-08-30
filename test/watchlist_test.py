import pytest, sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

@pytest.fixture
def watchlist():
    return WatchList()

def test_size(watchlist):
    assert watchlist.size() == 0

def test_add_movie(watchlist):
    watchlist.add_movie(Movie("Black Panther", 2018))
    assert watchlist.size() == 1
    
    watchlist.add_movie(Movie("Black Panther", 2018))
    assert watchlist.size() == 1

def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("Black Panther", 2018))
    watchlist.add_movie(Movie("Tenet", 2020))
    watchlist.add_movie(Movie("Police Story", 1985))
    watchlist.remove_movie(Movie("Police Story", 1985))
    assert watchlist.size() == 2
    
    watchlist.remove_movie(Movie("Police Story", 1985))
    assert watchlist.size() == 2
    
def test_select_movie(watchlist):
    watchlist.add_movie(Movie("Police Story", 1985))
    watchlist.add_movie(Movie("Police Story 2", 1988))
    watchlist.add_movie(Movie("New Police Story", 2004))

    assert repr(watchlist.select_movie(0)) == "<Police Story, 1985>"
    assert repr(watchlist.select_movie(1)) == "<Police Story 2, 1988>"
    assert repr(watchlist.select_movie(2)) == "<New Police Story, 2004>"
    assert repr(watchlist.select_movie(3)) == "None"

def test_select_first_movie(watchlist):
    watchlist.add_movie(Movie("Police Story", 1985))
    watchlist.add_movie(Movie("Police Story 2", 1988))
    watchlist.add_movie(Movie("New Police Story", 2004))

    assert repr(watchlist.first_movie_in_watchlist()) == "<Police Story, 1985>"
    watchlist.remove_movie(Movie("Police Story", 1985))
    assert repr(watchlist.first_movie_in_watchlist()) == "<Police Story 2, 1988>"

def test_iterate(watchlist):
    watchlist.add_movie(Movie("Police Story", 1985))
    watchlist.add_movie(Movie("Police Story 2", 1988))
    watchlist.add_movie(Movie("New Police Story", 2004))
    
    i = 0
    for movie in watchlist:
        assert repr(movie) == repr(watchlist.select_movie(i))
        i += 1

    
