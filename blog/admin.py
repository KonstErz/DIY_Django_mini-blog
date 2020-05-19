from django.contrib import admin
from .models import Blog, Blogger, Comment


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    inlines = [BlogInline]


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'author', 'description')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'post_date', 'author', 'description')
