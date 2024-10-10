from django.db import models


class Post(models.Model):
    """Модель поста"""

    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
    )
    short_description = models.CharField(
        max_length=150,
        verbose_name='Короткое описание',
    )
    content = models.CharField(
        max_length=255,
        verbose_name='Контент',
    )
    img = models.ImageField(
        upload_to = "media",
        null = True,
        blank = True,
        verbose_name='Изображение',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    author = models.ForeignKey(
        'users.User',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
