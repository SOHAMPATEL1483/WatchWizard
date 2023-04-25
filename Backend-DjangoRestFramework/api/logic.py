import numpy as np
import json
from .models import Profile, Movies
import pickle
from django.db.models import Q
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


def makeProfile(user):
    logger.warning("makeProfile is successfully called")
    r = []
    lastrating = []
    userprofile = Profile.objects.create(
        user=user, Lastrating=str(lastrating), R=str(r)
    )
    userprofile.save()


def getFeature(user):
    logger.warning("getFeature is successfully called")
    userprofile = None
    try:
        userprofile = Profile.objects.get(user=user)

    except:
        makeProfile(user)

    return getMoviereccomandation(userprofile)


def getMoviereccomandation(userprofile):
    logger.warning("mgetMovierecommandation is successfully called")
    R = json.loads(userprofile.R)
    r = []
    for i in R:
        r.append(i[0])
    LR = json.loads(userprofile.Lastrating)
    movie_ids = []

    lr = sorted(LR, reverse=True)

    for i in lr:
        movie_ids.append(i[2])
        if len(movie_ids) == 4:
            break
    similarity = pickle.load(open("./static/similarity.pkl", "rb"))
    keyToimdb = pickle.load(open("./static/keyToImdb.pkl", "rb"))

    movies = []
    for i in movie_ids:
        cnt = 5
        for j in similarity[i]:
            if j[0] not in r:
                movies.append(keyToimdb[j[0] + 1])
                cnt -= 1
            if cnt == 0:
                break
        if len(movies) == 20:
            break
    moives = getPopularMovies(movies, r)
    return getMovieDetails(moives)


def getPopularMovies(movies, r=[]):
    logger.info("getPopularMovies is successfully called")
    index = 0
    popularity_list = pickle.load(open("./static/popularity_list.pkl", "rb"))
    imdbTokey = pickle.load(open("./static/imdbTokey.pkl", "rb"))
    while len(movies) < 20 and index < 974:
        if imdbTokey[popularity_list[index][0]] - 1 not in r:
            movies.append(popularity_list[index][0])
        index += 1
    return movies


def getMovieDetails(movies):
    logger.warning("getMoiveDetails is successfully called")
    movie_list = []
    for i in movies:
        movie = Movies.objects.get(Imdb_id=i)
        dicc = {
            "Imdb_id": movie.Imdb_id,
            "Title": movie.Title,
            "Poster_path": movie.Poster_path,
        }
        movie_list.append(dicc)
    return movie_list
    return movie_list


def updateRating(movieID, user, rating):
    logger.warning("updateRating is successfully called")
    userprofile = Profile.objects.get(user=user)
    R = json.loads(userprofile.R)
    r = []
    for i in R:
        r.append(i[0])
    LR = json.loads(userprofile.Lastrating)
    imdbTokey = pickle.load(open("./static/imdbTokey.pkl", "rb"))
    lr = [rating, len(LR), imdbTokey[movieID] - 1]
    LR.append(lr)
    if imdbTokey[movieID] - 1 not in r:
        R.append([imdbTokey[movieID] - 1, rating])
    userprofile.R = str(R)
    userprofile.Lastrating = str(LR)
    try:
        userprofile.full_clean()
        userprofile.save()
    except:
        logger.error("Validation Error occur in updateRating method")


def getMovies(moviePrefix):
    logger.warning("getMovies is successfully called")
    movies = Movies.objects.filter(Q(Title__icontains=moviePrefix)).values()
    return movies


def getMovie(movieID, user):
    logger.warning("getMovie is successfully called")
    movie = Movies.objects.filter(Imdb_id__contains=movieID).values()
    dictionary = {}
    keyToImdb = pickle.load(open("./static/keyToImdb.pkl", "rb"))
    if len(movie) > 0:
        dictionary["Movie"] = movie[0]
    if user != None:
        userprofile = Profile.objects.get(user=user)
        R = json.loads(userprofile.R)
        for i in R:
            if keyToImdb[i[0] + 1] == movieID:
                dictionary["Rating"] = i[1]
                break
    return dictionary


def getUser(user):
    logger.warning("getUser is successfully called")
    userprofile = Profile.objects.get(user=user)
    R = json.loads(userprofile.R)
    keyToImdb = pickle.load(open("./static/keyToImdb.pkl", "rb"))
    movie_list = []
    for i in R:
        curr = {}
        print()
        val = i[0]
        val += 1
        imdb_id = keyToImdb[val]
        curr["Imdb_id"] = imdb_id
        movie = Movies.objects.get(Imdb_id=imdb_id)
        curr["Title"] = movie.Title
        curr["Poste_path"] = movie.Poster_path
        curr["Rating"] = i[1]
        movie_list.append(curr)
    return movie_list
