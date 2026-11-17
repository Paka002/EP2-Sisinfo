from django.db import models


class Post(models.Model):
    title = models.CharField("título", max_length=200)
    content = models.TextField("conteúdo")
    published_at = models.DateTimeField("data de publicação")
    categories = models.ManyToManyField("Category", related_name="posts", blank=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField("nome", max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField("texto")
    created_at = models.DateTimeField("data de criação", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "comentário"
        verbose_name_plural = "comentários"

    def __str__(self):
        return f"{self.author} em {self.post}"
