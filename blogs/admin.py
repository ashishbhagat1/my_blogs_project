from django.contrib import admin
from .models import Post

# This page working for Admin Pannel to showing data of blogs

# from .models import post #this will work also

# Register your models here.
# 1st Way of Registeration
# admin.site.register(Post)
# 2nd way of Registration
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#    pass
# Standerd Way For Project
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "published_at", "status")
    list_filter = ("status", "created_at", "published_at", "author")
    search_fields = ("title", "content")
    raw_id_fields = ("author",)
    date_hierarchy = "published_at"
    ordering = ("status", "published_at")


# admin.site.register(Post,PostAdmin)
