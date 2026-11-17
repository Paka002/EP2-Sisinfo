from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Category, Comment, Post


class Command(BaseCommand):
    help = "Popula o banco com os dados mínimos da entrega."

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username="aluno")
        user.set_password("aluno123")
        user.save()

        categories = {
            name: Category.objects.get_or_create(name=name)[0]
            for name in ("Tecnologia", "Pesquisa", "Cultura")
        }
        posts = [
            ("Introdução ao projeto", "<p>Um post sem comentários sobre o projeto.</p>", ()),
            ("Django e dados", "<p>Como organizar dados em uma aplicação Django.</p>", ("Tecnologia", "Pesquisa")),
            ("Cultura digital", "<p>Reflexões sobre cultura e informação.</p>", ("Cultura", "Pesquisa")),
        ]
        created_posts = []
        for index, (title, content, category_names) in enumerate(posts):
            post, _ = Post.objects.update_or_create(
                title=title,
                defaults={
                    "content": content,
                    "published_at": timezone.make_aware(datetime(2026, 1, 1 + index, 10, 0)),
                },
            )
            post.categories.set([categories[name] for name in category_names])
            created_posts.append(post)

        Comment.objects.filter(post__in=created_posts).delete()
        for post in created_posts[1:]:
            Comment.objects.create(post=post, author=user, text=f"Excelente conteúdo sobre {post.title}.")
            Comment.objects.create(post=post, author=user, text="A informação foi muito útil.")
        self.stdout.write(self.style.SUCCESS("Dados iniciais criados com sucesso."))
