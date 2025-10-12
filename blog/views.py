from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Comment
from django.core.paginator import Paginator ,PageNotAnInteger, EmptyPage
from website.models import Contact
# Create your views here.


def blog_view(request, cat_name=None, author_username=None, tag_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name = cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)


    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])

    posts = Paginator(posts, 3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    
    context = {'posts':posts}
    return render(request ,'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1)

    comments = Comment.objects.filter(post = post.id, approved=True)

    prev_post = Post.objects.filter(
        published_date__lt=post.published_date, status=1
    ).order_by('-published_date').first()

    next_post = Post.objects.filter(
        published_date__gt=post.published_date, status=1
    ).order_by('published_date').first()

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments':comments
    }

    return render(request, 'blog/blog-single.html', context)



# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name = cat_name)
#     context = {'posts':posts}
#     return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))

    
    context = {'posts':posts}
    return render(request ,'blog/blog-home.html', context)












def test(request):
    

    return render(request, 'test.html')