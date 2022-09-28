# Maxwell Edwards
from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('techtips+css', views.techtipsCss, name='techtipsCss'),
    path('techtips-css', views.techtipsNoCss, name='techtipsNoCss'),
    path('plan', views.plan, name='plan'),
    path('archive', views.archive, name="archive"),
    path('entry/<int:question_id>/', views.blogPost, name="blogPost")
]