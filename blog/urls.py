from django.urls import path, include
from . import views

urlpatterns = [
    # home url
    path('', views.PostList.as_view(), name='home'),
    # create form url
    path('create/', views.create, name='create'),
    # postdetail url
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('update/<int:id>', views.update, name='update'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
