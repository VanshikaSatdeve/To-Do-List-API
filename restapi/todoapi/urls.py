from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoListViewSet

router = DefaultRouter()
router.register('',TodoListViewSet,basename='todoapi')
app_name ='todoapi'

urlpatterns=[
    path('',include(router.urls))
]