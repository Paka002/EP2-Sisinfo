from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Category, Comment, Post


class BlogFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="aluno", password="senha")
        self.category = Category.objects.create(name="Tecnologia")
        self.post = Post.objects.create(
            title="Primeiro post",
            content="<p>Conteúdo seguro.</p>",
            published_at=timezone.make_aware(datetime(2026, 1, 1, 10, 0)),
        )
        self.post.categories.add(self.category)

    def test_post_detail_returns_404_for_unknown_post(self):
        response = self.client.get(reverse("blog:post_detail", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_can_create_comment(self):
        self.client.login(username="aluno", password="senha")
        response = self.client.post(
            reverse("blog:comment_create", kwargs={"pk": self.post.pk}),
            {"text": "Comentário de teste"},
        )
        self.assertRedirects(response, reverse("blog:post_detail", kwargs={"pk": self.post.pk}))
        self.assertTrue(Comment.objects.filter(post=self.post, author=self.user).exists())

    def test_category_page_lists_related_posts(self):
        response = self.client.get(
            reverse("blog:category_detail", kwargs={"pk": self.category.pk})
        )
        self.assertContains(response, self.post.title)
