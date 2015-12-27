from django.contrib import admin

# Register your models here.
from .models import NewsletterSignUp
from .forms import NewsletterSignUpForm

class SignupAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = NewsletterSignUpForm
	# class Meta:
	# 	model = NewsletterSignUp

admin.site.register(NewsletterSignUp, SignupAdmin)