from django.urls import include, path # creates the path object
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]