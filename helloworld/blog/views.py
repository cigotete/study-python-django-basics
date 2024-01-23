from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post

class BlogListView(ListView):
  model = Post
  template_name = "blog.html"

class BlogDetailView(DetailView):
  model = Post
  template_name = "blog_post.html"

class BlogCreateView(CreateView): # new
  model = Post
  template_name = "blog_post_new.html"
  fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
  model = Post
  template_name = "blog_post_edit.html"
  fields = ["title", "body"]