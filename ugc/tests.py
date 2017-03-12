from django.test import TestCase

# Create your tests here.
from ugc.models import Post, Comment


class TestUGC(TestCase):

    def setUp(self):
        self.testpost = Post.objects.create()
        print("setup")

    def testNewComment(self):
        self.comment = Comment.objects.create(post=self.testpost)
        assert (len(self.testpost.comments) > 0)

    def tearDown(self):

        print("teardown")

