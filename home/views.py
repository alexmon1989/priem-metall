from django.shortcuts import render
from home.models import HomeSection, AboutSection, FactsSection, WhyUsSection, SkillsSection, ServicesSection


def home_page(request):
    return render(
        request,
        'home/home.html',
        {
            'home_section': HomeSection.objects.first(),
            'about_section': AboutSection.objects.first(),
            'facts_section': FactsSection.objects.first(),
            'why_us_section': WhyUsSection.objects.first(),
            'skills_section': SkillsSection.objects.first(),
            'services_section': ServicesSection.objects.first(),
        }
    )
