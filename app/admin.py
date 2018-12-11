from django.contrib import admin
from .models import Emotion, Color

# from .models import Emotions, Colors
# # Register your models here.
admin.site.register(Emotion)
admin.site.register(Color)
