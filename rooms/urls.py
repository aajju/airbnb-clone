from django.urls import path
from . import views

app_name = "rooms"

# Fucntion Based View
# urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]

# Class Based View
urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    # path("search/", views.search, name="search"),
    path("search/", views.SearchView.as_view(), name="search"),
]
