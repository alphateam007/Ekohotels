from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('<uuid:room_id>/', views.rooms_detailed_view, name='rooms_detailed_view'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
