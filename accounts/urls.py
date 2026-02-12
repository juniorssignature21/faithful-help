from django.urls import path
from .views import register_user, login_user, logout_user, create_profile,edit_profile, view_profile

app_name = "accounts"

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("create-profile/", create_profile, name="create-profile"),
    path("edit-profile/", edit_profile, name="edit-profile"),
    path("profile/", view_profile, name="view-profile"),
]
