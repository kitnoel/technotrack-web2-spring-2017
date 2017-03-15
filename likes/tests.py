from django.test import TestCase

# Create your tests here.
from core.models import User
from likes.models import Like
from ugc.models import Post


class TestLikes(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='u1')
        self.u2 = User.objects.create(username='u2')
        self.u3 = User.objects.create(username='u3')
        self.p = Post.objects.create(author=self.u1, content="aaa")

    def test_add_likes(self):
        self.assertEqual(self.p.likes_count, 0)
        l1 = Like.objects.create(author=self.u2, target=self.p)
        self.assertEqual(self.p.likes_count, 1)
        l2 = Like.objects.create(author=self.u3, target=self.p)
        self.assertEqual(self.p.likes_count, 2)

    def test_delete_likes(self):
        l1 = Like.objects.create(author=self.u2, target=self.p)
        l2 = Like.objects.create(author=self.u3, target=self.p)
        self.assertEqual(self.p.likes_count, 2)
        l1.delete()
        self.assertEqual(self.p.likes_count, 1)
        l2.delete()
        self.assertEqual(self.p.likes_count, 0)
