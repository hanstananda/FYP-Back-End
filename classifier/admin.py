from django.contrib import admin

# Register your models here.
from classifier.models import SnakeImage, ClassifySnakeRequest, SnakeInfo

admin.site.register(SnakeImage)
admin.site.register(SnakeInfo)
admin.site.register(ClassifySnakeRequest)
