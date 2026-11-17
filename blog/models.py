from django.db import models


class Post(models.Model):
    title = models.CharField("título", max_length=200)
    content = models.TextField("conteúdo")
    published_at = models.DateTimeField("data de publicação")

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title
