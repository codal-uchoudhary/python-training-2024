from django.contrib import admin

from .models import Post, Tag, Comments, Like


class PostAdmin(admin.ModelAdmin):
    list_filter = ("date", "tags")
    list_display = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Like)
