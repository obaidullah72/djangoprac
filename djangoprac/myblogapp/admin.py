from django.contrib import admin
from .models import PostModel




class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date_created')


admin.site.register(PostModel, PostModelAdmin)