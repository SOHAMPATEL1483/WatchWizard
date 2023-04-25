import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .logic import (
    getFeature,
    getMoviereccomandation,
    updateRating,
    getMovies,
    getPopularMovies,
    getUser,
    getMovieDetails,
    makeProfile,
    getMovie,
)
from .models import Movies
import pandas as pd

# Create your views here.


class CreateUser(APIView):
    def post(self, request):
        userinfo = UserSerializer(data=request.data)
        if userinfo.is_valid():
            print(userinfo.validated_data)
            user = userinfo.save()
            makeProfile(user)
            return Response(UserSerializer(user).data)
        return Response(userinfo.errors)


class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userinfo = get_user_model().objects.get(id=request.user.id)
        userinfo = UserSerializer(userinfo)
        return Response(userinfo.data)


class HomePage(APIView):
    def get(self, request):
        name = request.GET.get("name")
        if name == None:
            movie_list = None
            if request.user.is_anonymous:
                movies = []

                movie_list = getPopularMovies(movies=movies)
                movie_list = getMovieDetails(movie_list)
            else:
                movie_list = getFeature(request.user)

            return Response(movie_list)
        else:
            print("sucsessfully worked")
            moviePrefix = request.GET.get("name")
            movies = getMovies(moviePrefix)
            return Response(movies)


class Training_view(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        movieId = request.GET.get("movieId")
        rating = request.GET.get("rating")
        print(f"movieId is : {movieId}")
        print(f"rating is : {rating}")
        print("Succesfully gets data")
        print(type(movieId))
        rating = int(rating)
        print(type(rating))
        dicc = {"sucsess": 200}
        updateRating(user=request.user, movieID=movieId, rating=rating)
        return Response(dicc)


class GetUser(APIView):
    parser_classes = (IsAuthenticated,)

    def get(self, request):
        print("Succsessfully enterd")
        movie_list = getUser(request.user)
        return Response(movie_list)


class GetMovie(APIView):
    def get(self, request):
        user = None
        if request.user.is_anonymous == False:
            user = request.user
        movieID = request.GET.get("movieId")
        movie = getMovie(movieID, user)
        return Response(movie)


# class Fillthemodel(APIView):
#     def get(self, request):
#         movie_info = pd.read_csv('./static/Id_title_path.csv')
#         for i in movie_info.index:
#             curr = movie_info.iloc[i]

#             movie = Movies.objects.create(Imdb_id=json.loads(
#                 curr[1]), Title=json.loads(curr[2]), Poster_path=json.loads(curr[3]))
#             movie.save()
#         dicc = {"sucsess": 200}
#         return Response(dicc)
