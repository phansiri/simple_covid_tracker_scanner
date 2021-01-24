from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('scan/', views.scan, name='scan'),
    path('set_location/', views.set_location, name='set_location'),
    path('reports/', views.reports, name='reports'),
    path('download_report/', views.download_report, name='download_report'),
    # path('event/<int:pk>/', views.event_detail, name='event_detail'),
    # path('event/new/<int:pk>/', views.event_new, name='event_new'),
    # path('person_list', views.person_list, name='person_list'),
    # path('person/<int:pk>/edit', views.person_edit, name='person_edit'),
]