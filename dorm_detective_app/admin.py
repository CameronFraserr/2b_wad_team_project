from django.contrib import admin
from dorm_detective_app.models import University, UserProfile


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'description', 'website')


admin.site.register(University, UniversityAdmin)
admin.site.register(UserProfile)
