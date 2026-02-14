from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# ListView to display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# DetailView to show individual blog posts
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView with LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        # Automatically set author based on the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView with LoginRequiredMixin and UserPassesTestMixin
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        # Re-verify the author is set to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Check if current user is the author
        post = self.get_object()
        return self.request.user == post.author

# DeleteView with LoginRequiredMixin and UserPassesTestMixin
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        # Ensure only the author can delete it
        post = self.get_object()
        return self.request.user == post.author