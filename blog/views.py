from django.shortcuts import render
from .models import Blog, Blogger, Comment


def index(request):
    num_blogs = Blog.objects.all().count()
    num_comments = Comment.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    return render(
        request,
        'index.html',
        context=context,
    )
