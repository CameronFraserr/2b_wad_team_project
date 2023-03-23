from django.contrib import admin
from dorm_detective_app.models import University, Accommodation, UserProfile, Review
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'description', 'website', 'address')
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(University, UniversityAdmin)
admin.site.register(Accommodation)
admin.site.register(Review)
admin.site.register(UserProfile)
