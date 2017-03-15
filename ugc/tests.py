from django.test import TestCase

# Create your tests here.
from core.models import User
from likes.models import Like
from ugc.models import Post, Comment


class TestUGC(TestCase):

    def setUp(self):
        self.test_user1 = User.objects.create(username='u1')
        self.test_user2 = User.objects.create(username='u2')
        self.test_post = Post.objects.create(author=self.test_user1, content='dsf')
        self.test_comment1 = Comment.objects.create(author=self.test_user2, post=self.test_post, text='fdg')
        self.test_comment2 = Comment.objects.create(author=self.test_user1, post=self.test_post, text='sfd')
        self.like1 = Like.objects.create(author=self.test_user2, target=self.test_post)
        self.like2 = Like.objects.create(author=self.test_user1, target=self.test_comment1)

    def testDeleteComment(self):
        self.assertEqual(self.test_post.comments.count(), 2)
        self.test_comment1.delete()
        self.assertEqual(self.test_post.comments.count(), 1)
        self.assertEqual(self.test_comment1.likes.count(), 0)

    def testDeletePost(self):
        self.assertEqual(self.test_post.comments.count(), 2)
        self.test_post.delete()
        self.assertEqual(self.test_post.likes.count(), 0)
        self.assertEqual(self.test_post.comments.count(), 0)
        self.assertEqual(self.test_comment1.likes.count(), 0)

