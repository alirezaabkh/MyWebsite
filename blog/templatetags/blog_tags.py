from django import template
from blog.models import Post ,Category, Comment
register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def lateposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}



@register.simple_tag(name='comments_counter')
def comments_counter(pid):
    post = Post.objects.get( id=pid, status=1)
    return Comment.objects.filter(post = post.id, approved=True).count()






@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    
    return {'categories':cat_dict}
