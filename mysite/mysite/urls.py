"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path("tools/", include("app.urls")),
    path("weather/", include("app.urls")),
    path("bmi/", include("app.urls")),
    path("covid/", include("app.urls")),
    path("notes/", include("app.urls")),
    path("notes_data/", include("app.urls")),
    path("del_notes/", include("app.urls")),
    path("stocks/", include("app.urls")),
    path("wikipedia/", include("app.urls")),
    path("add_favorite/", include("app.urls")),
    path("favorites/", include("app.urls")),
    path("delete_bookmarks/", include("app.urls")),
    path("calculator/", include("app.urls")),
    path("about/", include("app.urls")),
    path("print/", include("app.urls")),
]