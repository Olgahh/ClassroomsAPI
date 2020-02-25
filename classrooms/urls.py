from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from classesAPI.views import (
	APIListView, APIDetailsView, APICreateView, APIUpdateView, APIDeleteView, RegisterView
	)
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),
    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    #ClassesAPI
    path('list/', APIListView.as_view(), name='api-classroom-list'),
    path('detail/<int:classroom_id>/', APIDetailsView.as_view(), name='api-classroom-detail'),
    path('create/', APICreateView.as_view(), name='api-classroom-create'),
    path('update/<int:classroom_id>/', APIUpdateView.as_view(), name='api-classroom-update'),
    path('delete/<int:classroom_id>/', APIDeleteView.as_view(), name='api-classroom-delete'),

    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', RegisterView.as_view(), name='api-register'),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
