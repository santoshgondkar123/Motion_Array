"""
URL configuration for Motion_templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin 
from django.urls import path , include
from website import views
from adpanel import views as ad
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.Home, name='home'),
    path('template/',views.Template,name ='template'),
    # path('video_tem',views.Video_Template, name='video_template'),
    path('motion',views.Motion_graphics,name='motion_graphics'),
    path('video/',views.Video, name='video'),
    path('login/',views.Log_in,name='login'),
    path('contact/',views.Contact, name='contact'),
    # path('payment/',views.payment , name="payment"),

    # adpanel urls
    path('admin/',ad.index , name="adpanel"),


    # rozarpay
    path('subscribe/',views.Subscribe,name='subscribe'),
    path('payment-success/',views.Payment_Success,name='payment_success'),

    # real login
    path('accounts/',include('allauth.urls')),
#     path(
#     'subscription/',
#     views.Subscription_Plans,
#     name='subscription'
# ),


]
