from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# View to list all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# View to see a single post
class PostDetailView(DetailView):
    model = Post

# View to create a post - Required LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Automatically set the author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

# View to update a post - Required LoginRequiredMixin and UserPassesTestMixin
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Ensure the author remains the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Logic to ensure only the author can edit
        post = self.get_object()
        return self.request.user == post.author

# View to delete a post - Required LoginRequiredMixin and UserPassesTestMixin
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to home after deletion

    def test_func(self):
        # Logic to ensure only the author can delete
        post = self.get_object()
        return self.request.user == post.author