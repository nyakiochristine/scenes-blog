from django.contrib import admin


from blogpost.models import Post,BlogComment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    



admin.site.register(BlogComment)
admin.site.register(Post)