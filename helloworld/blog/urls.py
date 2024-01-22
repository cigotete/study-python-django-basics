from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
  path("blog", BlogListView.as_view(), name="blog"),
  path("blog/post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]