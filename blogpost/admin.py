from django.contrib import admin


from blogpost.models import Post,BlogComment
# Register your models here.
admin.site.register(BlogComment)
admin.site.register(Post)