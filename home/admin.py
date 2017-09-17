from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from home.models import HomeSection, AboutSection, FactsSection, WhyUsSection, SkillsSection, ServicesSection


class SectionAdmin(SingleModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HomeSection, SectionAdmin)
admin.site.register(AboutSection, SectionAdmin)
admin.site.register(FactsSection, SectionAdmin)
admin.site.register(WhyUsSection, SectionAdmin)
admin.site.register(SkillsSection, SectionAdmin)
admin.site.register(ServicesSection, SectionAdmin)
