from django.urls import path
from . import views

urlpatterns = [
    # System Info
    path('systeminfo/', views.system_info_list),
    path('systeminfo/create/', views.system_info_create),

    # Schedule
    path('schedule/', views.schedule_list),
    path('schedule/create/', views.schedule_create),

    # Protected
    path('protected/', views.protected_view),
]