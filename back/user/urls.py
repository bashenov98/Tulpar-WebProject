from django.urls import path
from user import views
from .views import *
from .views import login, logout
from user.views.generic_cbv import CompanyList, CompanyDetail, EmployeeList, EmployeeDetail, ProjectList, ProjectDetail

urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('companies/<int:pk>/employees/', EmployeeList.as_view()),
    path('companies/<int:pk>/employees/<int:pk>/', EmployeeDetail.as_view()),
    path('companies/<int:pk>/projects/', ProjectList.as_view()),
    path('companies/<int:pk>/projects/<int:pk>/', ProjectDetail.as_view()),
]