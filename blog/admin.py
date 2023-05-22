from django.contrib import admin
from blog.models import Post, Commit


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
