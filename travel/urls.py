from django.urls import path
from travel.views import homePageView, projectPageView

app_name = "travel"

urlpatterns = [
    path('', homePageView, name="home"),
    path('/project', projectPageView, name="project"),
]