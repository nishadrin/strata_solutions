from django.db import models


class Comment(models.Model):
    """Модель коммента"""

    name = models.CharField(
        max_length=50,
        verbose_name='Имя автора',
    )
    content = models.CharField(
        max_length=255,
        verbose_name='Содержимое комментария',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    post = models.ForeignKey(
        'posts.Post',
        verbose_name='Пост',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
