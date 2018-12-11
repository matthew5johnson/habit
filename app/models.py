from django.db import models

# Create your models here.
class Emotion(models.Model):
	emotion = models.CharField(max_length=50)
	positive = models.IntegerField(null=0)
	negative = models.IntegerField(null=0)

	def __str__(self):
		return self.emotion



class Color(models.Model):
	color = models.TextField(max_length=50, default='')
	hexa = models.TextField(max_length=10, default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.color

