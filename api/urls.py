from django.urls import path
from . import views
urlpatterns = [

    path('create/', views.add_items),
    path('all/', views.view_items),
    path('update/<str:pk>/', views.update_items),
    path('history/', views.history),
]