from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/new.html"
    fields = ['title', 'subtitle', 'author', 'body', 'status']
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ['title', 'subtitle', 'status', 'body']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('post_list')
