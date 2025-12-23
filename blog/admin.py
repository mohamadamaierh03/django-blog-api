from django.contrib import admin
from .models import Post  # Import your Post model

# This line tells Django to show 'Posts' in the admin panel
admin.site.register(Post)
