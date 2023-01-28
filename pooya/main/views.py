from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm


# class HomeView(View):

#     def contact(request):
#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 subject = form.cleaned_data['subject']
#                 message = form.cleaned_data['message']
#                 sender = form.cleaned_data['sender']
#                 cc_myself = form.cleaned_data['cc_myself']

#                 recipients = ['info@example.com']
#                 if cc_myself:
#                     recipients.append(sender)

#                 send_mail(subject, message, sender, recipients)
#                 return render(request, 'contact_form/thanks.html')
#         else:
#             form = ContactForm()

#         return render(request, 'contact_form/form.html', {'form': form})


#     def get(self, request):
#         return render(request, 'main/index.html')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['pooya.jv@gmail.com']
            send_mail(name, message, sender, recipients)
            print('0000000000000000000000000000000000000000000000000000000000000000')
            return render(request, 'main/index.html', {'form': form, 'message': 'Thanks for your message'})
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})