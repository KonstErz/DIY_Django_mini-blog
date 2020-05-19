from django.shortcuts import render
from .models import Blog, Blogger, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse


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


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('description',)

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk']})
