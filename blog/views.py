from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, UserSerializer

# --- 1. POSTS API (with Pagination) ---
@api_view(["GET"])
def get_posts(request):
    try:
        # Get pagination params from URL (e.g., ?page=1&limit=5)
        page = int(request.query_params.get("page", 1))
        limit = int(request.query_params.get("limit", 10))
        
        start = (page - 1) * limit
        end = start + limit
        
        # Query database via ORM
        posts = Post.objects.all()[start:end]
        serializer = PostSerializer(posts, many=True)
        
        return Response({
            "page": page,
            "limit": limit,
            "total_count": Post.objects.count(),
            "results": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- 2. USERS API ---
@api_view(["GET"])
def user_list(request):
    try:
        users = User.objects.all()
        # هنا نستخدم السيريالايزر لعرض كل البيانات بما فيها الـ Profile
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)