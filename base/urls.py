from django.urls import path
from .views import PunchList, PunchDetail, PunchCreate, PunchUpdate, DeleteView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('',PunchList.as_view(), name='punches'),
    path('punch/<int:pk>/',PunchDetail.as_view(), name='punch'),
    path('punch-create/',PunchCreate.as_view(), name='punch-create'),
    path('punch-update/<int:pk>/',PunchUpdate.as_view(), name='punch-update'),
    path('punch-delete/<int:pk>/',DeleteView.as_view(), name='punch-delete'),
]

