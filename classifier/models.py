from django.db import models
from django.utils.timezone import now

# Create your models here.


class SnakeImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.__str__()


class SnakeInfo(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    short_desc = models.TextField()
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
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.snake_image.__str__()} classified as {self.classification.__str__()}"


class ExpertClassification(models.Model):
    snake_image = models.ForeignKey(SnakeImage, on_delete=models.CASCADE)
    classification = models.ForeignKey(
        SnakeInfo,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.snake_image.__str__()} classified as {self.classification.__str__()}"


class SnakeReport(models.Model):
    request = models.ForeignKey(
        ClassifySnakeRequest,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.request.__str__()} found at {self.latitude}, {self.longitude}"
