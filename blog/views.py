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


def home(request):
    latestBlogPosts = reversed(Blog.objects.order_by('posted')[:3])
    context = {
        'latestBlogPosts': latestBlogPosts
    }
    return render(request, 'blog/home.html', context)

def archive(request):
    allBlogPosts = reversed(Blog.objects.order_by('posted'))
    context = {
        'latestBlogPosts': allBlogPosts
    }
    return render(request, 'blog/home.html', context)

def blogPost(request, blog_id):
    blog_id = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/archive.html', {'blog_id': blog_id})