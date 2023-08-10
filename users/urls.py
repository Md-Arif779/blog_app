
from django.urls import path
from .views import UserRegisterView,UserEditeView,PasswordsChangeView, ShowProfilePageView,EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
   path('register/', UserRegisterView.as_view(), name="register"),
   path('edit_profile/', UserEditeView.as_view(), name="edit_profile"),
   path('password/',PasswordsChangeView.as_view(), name="password"),
   path('password_success/', views.password_success, name="password_success"),
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="profie_page" ),
   path('<int:pk>/edite_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page" ),
   path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile_page" ),

               ]