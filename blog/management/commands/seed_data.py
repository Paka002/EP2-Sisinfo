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

        category_names = {
            1: "Força",
            2: "Aparência",
            3: "Habilidades",
        }
        categories = {
            name: Category.objects.update_or_create(
                pk=category_id, defaults={"name": name}
            )[0]
            for category_id, name in category_names.items()
        }
        posts = [
            (
                "Golurk: força e imponência",
                "<p>Golurk é um Pokémon forte e resistente, capaz de proteger seus aliados com muita coragem.</p>",
                (),
            ),
            (
                "Golurk é forte e habilidoso",
                "<p>Com seus golpes poderosos e energia misteriosa, Golurk é um dos Pokémon mais impressionantes.</p>",
                ("Força", "Habilidades"),
            ),
            (
                "Golurk é legal e bonito",
                "<p>Além de ser forte, Golurk tem um visual marcante e uma presença muito legal.</p>",
                ("Aparência", "Habilidades"),
            ),
        ]
        created_posts = []
        for index, (title, content, post_category_names) in enumerate(posts, start=1):
            post, _ = Post.objects.update_or_create(
                pk=index,
                defaults={
                    "title": title,
                    "content": content,
                    "published_at": timezone.make_aware(datetime(2026, 1, index, 10, 0)),
                },
            )
            post.categories.set([categories[name] for name in post_category_names])
            created_posts.append(post)

        Comment.objects.filter(post__in=created_posts).delete()
        for post in created_posts[1:]:
            Comment.objects.create(post=post, author=user, text=f"{post.title} é muito legal!")
            Comment.objects.create(post=post, author=user, text="Golurk é forte e bonito.")
        self.stdout.write(self.style.SUCCESS("Dados iniciais criados com sucesso."))
