from django.urls import path

from . import views

urlpatterns = [
    path("user/info/", views.GetUserInfo.as_view()),
    path("user/create/", views.CreateUser.as_view()),
    path("user/home/", views.HomePage.as_view()),
    path("user/training/", views.Training_view.as_view()),
    path("user/getuser/", views.GetUser.as_view()),
    path("user/getmovie/", views.GetMovie.as_view())

    # path("user/fillthemodel/", views.Fillthemodel.as_view())
]
