from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import News_Post


def index(request):
	return render(request, 'news/homepage_of_news.html')

def contact(request):
	return render(request, 'news/content.html')

def post(request):
    posts = News_Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/post.html', {'posts': posts})



