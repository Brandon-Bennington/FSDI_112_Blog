from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/new.html"
    fields = ['title', 'subtitle', 'body', 'status']  # Removed 'author' field
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensures the logged-in user is set as the author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ['title', 'subtitle', 'status', 'body']
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user