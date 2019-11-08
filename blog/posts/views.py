from django.views.generic import DetailView, ListView
from .models import Post

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post