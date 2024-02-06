from django.contrib import admin

from .models import Post,Author,Tag



class PostAdmin(admin.ModelAdmin):
    list_filter=('author','data','tags')
    list_display = ("title",'data','author')
    prepopulated_fields={"slug":("title",)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)