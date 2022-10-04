from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Blog, Comment
from django.urls import reverse
from django.template import loader


# Create your views here.
def about(request):
    return render(request, 'blog/about.html')


def techtipsCss(request):
    return render(request, 'blog/techtips+css.html')


def techtipsNoCss(request):
    return render(request, 'blog/techtips-css.html')


def plan(request):
    return render(request, 'blog/plan.html')


def home(request):  # index
    latestBlogPosts = (Blog.objects.order_by('posted'))
    context = {
        'latestBlogPosts': latestBlogPosts.reverse()[:3]
    }
    return render(request, 'blog/home.html', context)


def archive(request):  # index
    allBlogPosts = Blog.objects.order_by('posted')
    context = {
        'latestBlogPosts': allBlogPosts.reverse()
    }
    return render(request, 'blog/home.html', context)


def blogPost(request, blog_id):  # detail
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogPost.html', {'post': post})


def addComment(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    try:
        selected_comment = post.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'blog/blogPost.html', {
            'post': post,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_comment.save()
        return HttpResponseRedirect(reverse('blog:home', args=(blog_id,)))
