from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Singup_page,name="signup_page"),
    path("signup_logic/",views.Signup_logic,name="signup_logic"),
    path("login_page/",views.Login_page,name="login_page"),
    path("login_logic/",views.Login_logic,name="login_logic"),
    path("user_data/",views.User_data,name="user_data"),
    path("get_data/<int:pk>",views.get_Data,name="get_data"),
    path("update/logic/<int:pk>",views.Update_logic,name="update_logic"),
    path("delete_data/<int:pk>",views.Delete_data,name="delete_data"),
]
