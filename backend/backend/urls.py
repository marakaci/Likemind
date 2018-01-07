"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from users.views import ObtainAuthToken, activate_account, UserDetailView, UserListView



urlpatterns = [
    url(r'^api/obtain-auth-token/$', ObtainAuthToken.as_view()),
    url(r'^api/users/$', UserListView.as_view(), name='user-list'),
    url(r'^api/users/?P<pk>[0-9]+/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^activate_account/(?P<activate_link>.+)/$', activate_account, name='activate-account'),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='LikeMind API'))
]