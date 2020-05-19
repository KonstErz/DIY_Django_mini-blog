from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Blogger, Blog
from django.urls import reverse


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='passwd999')
        test_user.save()
        test_blogger = Blogger.objects.create(name=test_user, bio='Test bio')
        test_blogger.save()

        number_of_blogs = 8

        for blog_num in range(number_of_blogs):
            Blog.objects.create(title=f'Test blog {blog_num}', author=test_blogger,
                                description=f'This is a test blog {blog_num}')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/blogs/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blog_list']) == 5)

    def test_lists_all_blogs(self):
        resp = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blog_list']) == 3)
