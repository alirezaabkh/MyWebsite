from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/index-latest-posts.html')
def latest_index_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return{'posts':posts}
