from django.shortcuts import render
from django.views.decorators.cache import cache_page
from home.models import (HomeSection, AboutSection, FactsSection, WhyUsSection, SkillsSection, ServicesSection,
                         QuoteSection, PricingSection, JobSchemeSection, TestimonialsSection, ContactsSection,
                         HeaderContactsSection)


@cache_page(60 * 15)
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
            'quote_section': QuoteSection.objects.first(),
            'pricing_section': PricingSection.objects.first(),
            'job_scheme_section': JobSchemeSection.objects.first(),
            'testimonials_section': TestimonialsSection.objects.first(),
            'contacts_section': ContactsSection.objects.first(),
            'header_contacts_section': HeaderContactsSection.objects.first(),
        }
    )
