from django.contrib import admin

# Register your models here.
from classifier.models import *

admin.site.register(SnakeImage)
admin.site.register(SnakeInfo)
admin.site.register(ClassifySnakeRequest)
admin.site.register(ExpertClassification)
admin.site.register(SnakeReport)
