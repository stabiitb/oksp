from django.contrib import admin

# Register your models here.
from .models import New, comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    class Meta:
        model = New

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['text']
    list_display_links = ['text']
    search_fields = ['text']
    class Meta:
        model = comment
    
        
admin.site.register(New, NewsAdmin)
admin.site.register(comment, CommentsAdmin)
