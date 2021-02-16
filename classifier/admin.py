from django.contrib import admin

# Register your models here.
from classifier.models import SnakeImage, ClassifySnakeRequest, SnakeInfo, ExpertClassification

admin.site.register(SnakeImage)
admin.site.register(SnakeInfo)
admin.site.register(ClassifySnakeRequest)
admin.site.register(ExpertClassification)