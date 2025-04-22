# modular_engine/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('module/', views.module_list, name='module_list'),
    path('module/install/<int:mod_id>/', views.install_module, name='module_install'),
    path('module/uninstall/<int:mod_id>/', views.uninstall_module, name='module_uninstall'),
    path('module/upgrade/<int:mod_id>/', views.upgrade_module, name='module_upgrade'),
]