# urls.py (inside irrigation app)
from django.urls import path
from .views import (
    system_info_list,
    system_info_create,
    schedule_list,
    schedule_create,
    register_user,
    login_user,
    protected_view
)

urlpatterns = [
    # Authentication
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),

    # System Info
    path('systeminfo/', system_info_list, name='systeminfo-list'),
    path('systeminfo/create/', system_info_create, name='systeminfo-create'),

    # Schedule
    path('schedule/', schedule_list, name='schedule-list'),
    path('schedule/create/', schedule_create, name='schedule-create'),

    # Protected Test
    path('protected/', protected_view, name='protected'),
]