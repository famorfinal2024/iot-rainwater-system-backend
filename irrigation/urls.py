# urls.py (inside irrigation app)
from django.urls import path
from .views import (
    system_info_list,
    system_info_create,
    system_info_delete,
    system_info_update,
    system_info_partial_update,
    schedule_list,
    schedule_create,
    register_user,
    login_user,
    protected_view
)

urlpatterns = [
    
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login'),

    
    path('systeminfo/', system_info_list, name='systeminfo-list'),
    path('systeminfo/create/', system_info_create, name='systeminfo-create'),
    path('systeminfo/delete/<int:pk>/', system_info_delete, name='systeminfo-delete'),
    path('systeminfo/update/<int:pk>/', system_info_update, name='systeminfo-update'),
    path('systeminfo/partial-update/<int:pk>/', system_info_partial_update, name='systeminfo-partial-update'),
    
    path('schedule/', schedule_list, name='schedule-list'),
    path('schedule/create/', schedule_create, name='schedule-create'),

    
    path('protected/', protected_view, name='protected'),
]