from django.shortcuts import render
from home.models import HomeSection


def home_page(request):
    return render(
        request,
        'home/home.html',
        {
            'home_section': HomeSection.objects.first()
        }
    )
