from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# Using a router to register the viewsets
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'stacks', views.StackViewSet)
router.register(r'languages', views.SpokenLanguageViewSet)

# API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
