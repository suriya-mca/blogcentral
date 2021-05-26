from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# importing post model
from .models import Post

# Register your models here.

# registering post and postadmin
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)