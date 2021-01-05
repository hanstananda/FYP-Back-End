from django.db import models


# Create your models here.


class SnakeImage(models.Model):
    image = models.ImageField()


class SnakeInfo(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ForeignKey(
        SnakeImage,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.latin_name


class ClassifySnakeRequest(models.Model):
    snake_image = models.ForeignKey(SnakeImage, on_delete=models.CASCADE)
    classification = models.ForeignKey(
        SnakeInfo,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
