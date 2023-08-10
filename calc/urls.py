from django.contrib import admin
from django.urls import path
# from .import views
from .views import HomeView, DetailsView, AddCreateView, PostUpdateView, PostDeleteView,AddCategoryView,CategoryView,CategoryListView,LikeView, AddCommentView


urlpatterns = [
   # path('', views.home, name="home"),
   path('', HomeView.as_view(), name="home"),
   path('details/<int:pk>', DetailsView.as_view(), name="details"),
   path('category-list/', CategoryListView, name="category-list"),
   path('add_category/', AddCategoryView.as_view(), name="add_category"),
   path('create/', AddCreateView.as_view(), name="create"),
   path('like/<int:pk>', LikeView, name="like_post"),
   
   path('update/<int:pk>', PostUpdateView.as_view(), name="update"),
   path('delete/<int:pk>', PostDeleteView.as_view(), name="delete"),
   path('category/<str:pets>/', CategoryView, name="category"),
   path('details/<int:pk>/commnet', AddCommentView.as_view(), name="add_comment"),
]