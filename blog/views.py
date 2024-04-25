from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    queryset = Post.published.order_by("-created_on")
    template_name = "blog/index.html"
    context_object_name = "posts"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
