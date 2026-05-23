from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Gender
    path('gender/list/', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.edit_gender),
    path('gender/delete/<int:genderId>/', views.delete_gender),

    # Users
    path('user/list/', views.user_list, name='user_list'),
    path('user/add/', views.add_user, name='add_user'),
    path('user/edit/<int:userId>/', views.edit_user, name='edit_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)