from django.views.generic import DetailView, ListView
from blog.models import Post


class PostListView(ListView):
    model = Post
    ordering = "-created_at"
    context_object_name = "posts"
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"
