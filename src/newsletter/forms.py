from django import forms
from .models import NewsletterSignUp
class NewsletterSignUpForm(forms.ModelForm):
	class Meta:
		model = NewsletterSignUp
		fields = ['fullName', 'email']
	def clean_email(self):
		email  = self.cleaned_data.get('email')
		emailBase, domain = email.split("@")
		provider, domainType = domain.split(".")
		if not domainType == "com":
			raise forms.ValidationError("Use a valid .com address")
		return email
	def clean_full_name(self):
		full_name = self.cleaned_data.get('fullName')
		return full_name