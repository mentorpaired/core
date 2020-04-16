from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'stacks', views.StackViewSet)
router.register(r'languages', views.SpokenLanguageViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
