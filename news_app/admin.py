from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(PostCategory)
# admin.site.register(PostSubCategory)
# admin.site.register(Post)
admin.site.register(Comment)


@admin.register(PostCategory)
class AdminPostCategory(admin.ModelAdmin): 
    list_display = ['category','icon','active','bangla']

@admin.register(PostSubCategory)
class AdminPostSubCategory(admin.ModelAdmin): 
    list_display = ['sub_name','icon','active','bangla','featured']

@admin.register(Post)
class AdminPost(admin.ModelAdmin): 
    list_display = ['author','title','primary_featured','popular','bangla','featured','active']