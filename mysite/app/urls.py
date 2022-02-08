from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tools/", views.tools, name="tools"),
    path("about/", views.about, name="about"),
    path("weather/", views.weather, name="weather"),
    path("covid/", views.covid, name="covid"),
    path("bmi/", views.bmi, name="bmi"),
    path("notes/", views.notes, name="notes"),
    path("notes_data/", views.notes_data, name="notes_data"),
    path("del_notes/", views.del_notes, name="del_notes"),
    path("stocks/", views.stocks, name="stocks"),
    path("wikipedia/", views.wiki, name="wiki"),
    path("add_favorite/", views.favorite, name="favorite"),
    path("favorites/", views.my_favorite, name="my_favorite"),
    path("delete_bookmarks/", views.del_favs, name="delete_favorites"),
    path("calculator/", views.calc, name="calculator"),
    path("print/", views.print_bmi, name="print_bmi")
]