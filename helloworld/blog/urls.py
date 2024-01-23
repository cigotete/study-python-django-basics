from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
  path("blog", BlogListView.as_view(), name="blog"),
  path("blog/post/new", BlogCreateView.as_view(), name="post_new"),
  path("blog/post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]