from django.core.mail import send_mail
from django.shortcuts import render
from .forms import NewsletterSignUpForm
from django.conf import settings
def home(request):
	title = "Subscribe to my Newsletter"
	form = NewsletterSignUpForm(request.POST or None)
	context = {
		"title" : title,
		"formData" : form,
		"exitMsg":"Subscribe"
	}
	if form.is_valid():
		instance = form.save(commit=False)
		fullName = form.cleaned_data.get("fullName")
		if not fullName:
			fullName = "Anoynymous"
		instance.fullName = fullName
		instance.save()
		context = {
			"title" :"Thanks For Signing Up",
			"exitMsg":"Bye."
		}

		email = form.cleaned_data.get('email')
		subjectContent = "Subscription Confirmation"
		fromEmail = settings.EMAIL_HOST_USER
		toEmail = [email]
		contactMessage = 'Message from %s'%(fromEmail)
		someHTMLMessage = """<h1>Hi <b>%s</b> your have applied for a subscription from E-Mail ID <b>%s</b>, Thanks for Signing Up for our Newsletter, We Appreciate it, Remember Expect the Unexpcted
		via %s</h1>"""%(fullName, email, fromEmail)

		send_mail(subjectContent, 
			contactMessage,
			fromEmail,
			toEmail,
			html_message=someHTMLMessage,
			fail_silently=True)
	return render(request,"base.html",context)
