from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create10/', views.create10, name='create10'),
    path('<int:post_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_id>/comments/<int:comment_id>/update/', views.comments_update, name='comments_update'),
    path('<int:post_id>/like/', views.like, name='like'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)