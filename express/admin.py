from django.contrib import admin
from.models import Hotel,Rating
# Register your models here.

class hotel_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('hotel_name',)}
    list_display =['hotel_name','country_name','city_name']
    
    
admin.site.register(Hotel,hotel_admin)
admin.site.register(Rating)


