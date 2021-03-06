from django.db import models
# Create your models here.
class NewsletterSignUp(models.Model):
	email = models.EmailField()
	fullName = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated  = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email