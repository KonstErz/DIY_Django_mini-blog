from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Blogger, Blog, Comment
import datetime


class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='passwd999')
        test_user.save()
        Blogger.objects.create(name=test_user, bio='A test user is created to test the Blogger model.')

    def test_name_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_object_name(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = blogger.name.username
        self.assertEquals(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEquals(blogger.get_absolute_url(), '/blog/blogger/1')


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='passwd999')
        test_user.save()
        test_blogger = Blogger.objects.create(name=test_user, bio='Test bio')
        test_blogger.save()
        Blog.objects.create(title='Test blog', author=test_blogger,
                            description='This is a test blog of test blogger for a test Blog model')

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_post_date_equals_today_date(self):
        blog = Blog.objects.get(id=1)
        post_date = blog.post_date
        self.assertEquals(datetime.date.today(), post_date)

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_object_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEquals(expected_object_name, str(blog))

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEquals(blog.get_absolute_url(), '/blog/blog/1')


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='passwd999')
        test_user.save()
        test_blogger = Blogger.objects.create(name=test_user, bio='Test bio')
        test_blogger.save()
        test_blog = Blog.objects.create(title='Test blog', author=test_blogger,
                                        description='This is a test blog of test blogger for a test Comment model')
        test_blog.save()
        Comment.objects.create(blog=test_blog, author=test_user,
                               description='This is a test comment')

    def test_blog_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label, 'blog')

    def test_description_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_post_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_object_comment_name(self):
        comment = Comment.objects.get(id=1)
        if len(comment.description) > 75:
            expected_object_name = comment.description[:75] + '...'
        else:
            expected_object_name = comment.description
        self.assertEquals(expected_object_name, str(comment))
