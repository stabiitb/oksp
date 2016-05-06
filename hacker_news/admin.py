from django.contrib import admin

# Register your models here.
from .models import New

 
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    class Meta:
        model = New
    
        
admin.site.register(New, NewsAdmin)
