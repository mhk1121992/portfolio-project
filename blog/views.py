from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blog': blogs})


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id )
    return render(request, 'blog/detail.html', {'blog': detail_blog})