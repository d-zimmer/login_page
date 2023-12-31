"""
URL configuration for login_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from login_app.views import api_login, get_user_info, login_view
from login_app.urls import urlpatterns as login_app_urls

urlpatterns = [
    path('', include(login_app_urls)),
    
    # path('login/', login_view, name='pagina_de_login'),  # Adicione esta linha para a URL raiz
    path('api/login/', api_login, name='api_login'),
    path('api/user-info/', get_user_info, name='get_user_info'),
    # Adicione outras URLs conforme necessário
]

