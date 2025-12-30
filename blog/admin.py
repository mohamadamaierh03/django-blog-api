from django.contrib import admin
from .models import Post, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('id', 'title', 'author', 'created_at')
    # Add a search box for title and content
    search_fields = ('title', 'content')
    # Add a filter sidebar for dates and authors
    list_filter = ('created_at', 'author')
    # Order by newest first
    ordering = ('-created_at',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'birth_date')