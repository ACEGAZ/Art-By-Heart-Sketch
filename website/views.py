from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .form import ContactForm
from django.views import generic
from .models import add_art


def index(request):
    return render(request, 'index.html')


class ArtDisplay(generic.ListView):
    model = add_art
    template_name = 'gallery.html'
    paginate_by = 6


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)