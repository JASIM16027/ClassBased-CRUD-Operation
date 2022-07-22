from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserAddShowView.as_view(), name = 'addshow' ),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='deletedata'),
    path('<int:update_id>/', views.UserUpdateView.as_view(), name='updateshow'),
  
]
