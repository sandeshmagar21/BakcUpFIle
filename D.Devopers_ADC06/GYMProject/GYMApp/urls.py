from django.urls import path
from .import views
from GYMProject.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-GYMApp'),
    path('update/<int:Gym_id>', views.update_Gym),
    path('delete/<int:Gym_id>', views.delete_Gym),
    path('update/', views.update_Gym)
    
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)