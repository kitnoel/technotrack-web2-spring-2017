from django.test import TestCase

from core.models import User
from relationships.models import FriendRequest, Friendship


class TestRelationships(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='u1')
        self.u2 = User.objects.create(username='u2')
        self.request = FriendRequest.objects.create(author=self.u1, to_user=self.u2)

    def test_friendship_accept(self):
        self.assertEqual(Friendship.objects.count(), 0)
        self.request.accept()
        self.assertEqual(Friendship.objects.count(), 2)
        self.assertEqual(Friendship.objects.filter(from_user=self.u1, to_user=self.u2).count(), 1)
        self.assertEqual(Friendship.objects.filter(from_user=self.u2, to_user=self.u1).count(), 1)

    def test_friendship_reject(self):
        self.request.accept()
        self.request.reject()
        self.assertEqual(Friendship.objects.count(), 0)


