from rest_framework_simplejwt.views import TokenRefreshView

from ..serializers import CustomTokenRefreshSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
