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
from django.contrib.auth import views as auth_views
from django.contrib import admin 
from django.urls import path , include
from website import views
from adpanel import views as ad

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='home'),
    path('template/',views.Template,name ='template'),
    # path('video_tem',views.Video_Template, name='video_template'),
    path('motion',views.Motion_graphics,name='motion_graphics'),
    path('video/',views.Video, name='video'),
    path('login/',views.Log_in,name='login'),
    path('contact/',views.Contact, name='contact'),
    # path('payment/',views.payment , name="payment"),

    # adpanel urls
    path('adminn/',ad.index , name="adpanel"),


    # rozarpay
    path('subscribe/',views.Subscribe,name='subscribe'),
    path('payment-success/',views.Payment_Success,name='payment_success'),

    # real login
    path('accounts/',include('allauth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('user-login/', views.login_view, name='user_login'),

    # password reset

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='web/password_reset.html',
            email_template_name='web/password_reset_email.html'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='web/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='web/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='web/password_reset_complete.html'
),name='password_reset_complete'    ),

    # admin-login
path('admin-login/',ad.admin_login, name='admin_login'),

    #upload
path('upload-template/',ad.upload_template,name='upload_template'),
path('delete-template/<int:id>/',ad.delete_template,name='delete_template'),
path('edit-template/<int:id>/',ad.edit_template,name='edit_template'),

path('upload-video/',ad.upload_video,    name='upload_video'),
path( 'edit-video/<int:id>/',ad.edit_video, name='edit_video'),
path('delete-video/<int:id>/',ad.delete_video,name='delete_video'),

path('upload-motion/',ad.upload_motion,name='upload_motion'),
 path(
        'edit-motion/<int:id>/',
        ad.edit_motion,
        name='edit_motion'
    ),

    path(
        'delete-motion/<int:id>/',
        ad.delete_motion,
        name='delete_motion'
    ),
path('logout/', views.user_logout, name='logout'),
path(
    'upload-asset/',
    ad.upload_asset,
    name='upload_asset'
),

path(
    'edit-asset/<int:id>/',
    ad.edit_asset,
    name='edit_asset'
),

path(
    'delete-asset/<int:id>/',
    ad.delete_asset,
    name='delete_asset'
),
path(
    'rate-asset/<int:id>/',
    ad.rate_asset,
    name='rate_asset'
),

# user rating
path(
    'rate-asset/<int:id>/',
    ad.rate_asset,
    name='rate_asset'
),
path(
    'download/<int:id>/',
    views.download_asset,
    name='download_asset'
),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

print("DEBUG =", settings.DEBUG)
print("MEDIA_ROOT =", settings.MEDIA_ROOT)