from django.urls import path
from .views import homePageView

urlpatterns = [
  path("pages", homePageView, name="pages"),
]