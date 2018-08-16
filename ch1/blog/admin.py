from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

class PostAdmin(SummernoteModelAdmin):
    # summernote_fields = ('fields',)
    list_display = ['title', 'created_at','category','id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)