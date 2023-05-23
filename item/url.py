from django.urls import path
from . import views
app_name = 'item'
urlpatterns = [
    path('new-item/', views.newItem, name='new-item'),
    path('browse/', views.browse, name='browse'),
    path('<int:id>/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
