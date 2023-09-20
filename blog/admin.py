from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','author','title','text','created_date']
    list_filter=['title']
    search_fields=['title']
    fields=[('author',),'text']
    readonly_fields=['title']