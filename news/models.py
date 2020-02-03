from django.conf import settings
from django.db import models
import datetime

from django.utils import timezone



class News_Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title_post = models.CharField(max_length=200)
	text_post = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title_post