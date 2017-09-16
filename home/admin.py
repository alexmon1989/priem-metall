from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from home.models import HomeSection


class HomeSectionAdmin(SingleModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HomeSection, HomeSectionAdmin)
