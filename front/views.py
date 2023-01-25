from django.shortcuts import render, redirect
from front.forms import MessageEmailForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST':
        # message_sent = False
        message_form = MessageEmailForm(request.POST)
        if message_form.is_valid():
            name = message_form.cleaned_data.get('name')
            email = message_form.cleaned_data.get('email')
            subject = message_form.cleaned_data.get('subject')
            body = message_form.cleaned_data.get('body')
            message_form.save()
            

            send_mail(
                subject,  # subject 
                body,  # message   
                email, # from 
                ['seadzcompany@gmail.com'], # To email 
                # "This is the message from  chisquare-connections  contact us page ", 
                fail_silently = False
            )

            # message_sent = True

            messages.success(request, 'Your message was sent successfully !')
            return redirect('email_sent_successf')
            # return HttpResponse('<script> window.alert("Thanks for your comment")</script>')
    else:
        message_form = MessageEmailForm()
        

    context = {
        'message_form': message_form,        
    }
    
    return render(request, 'front/index.html', context)

def email_sent_successfull(request):
    return render(request, 'front/email_sent_successfull.html')

