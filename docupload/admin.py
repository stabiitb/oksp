from django.contrib import admin

# Register your models here.
from .models import Documentation

 
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ["name", "pub_date"]
    list_display_links = ["name"]
    list_filter = ["pub_date"]
    search_fields = ["name"]
    class Meta:
        model = Documentation
    
        
admin.site.register(Documentation, DocumentationAdmin)
