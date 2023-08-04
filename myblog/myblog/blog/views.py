from django.views import generic
from .models import Post


"""base.html → The main template, the “skeleton” of the templates. 
It includes the header, navigation bar, the content & the footer.
index.html → Extends the base.html template, using Django template language. 
It contains the blog entries in the main page, using the template of post_detail.html. 
It also includes the sidebar.html file.
sidebar.html → A small sidebar added in the main page.
post_detail.html → The detailed view of the blog post."""
class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    