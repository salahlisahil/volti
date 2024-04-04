from django.conf import settings

from django.conf import settings
from django.shortcuts import render


def contact(request):
    contact_information = settings.CONTACT_INFORMATION

    context = {
        'contact_information': contact_information
    }

    return context
