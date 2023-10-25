from . import views
from django.urls import path


urlpatterns = [
    path('', views.PaintingList.as_view(), name='home'),
    path('addpainting/', views.AddPainting.as_view(), name='add_painting'),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='update_comment'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete_comment'),
    path('like/<slug:slug>', views.LikePainting.as_view(), name='like_painting'),
    path('<slug:slug>', views.PaintingDetail.as_view(), name='painting_detail'),
]
