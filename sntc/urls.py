from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    url(r'^$', 'website.views.home', name='home'),
    url(r'^amc/$', 'website.views.amc', name='amc'),
    url(r'^astro/$', 'website.views.astro', name='astro'),
    url(r'^cops/$', 'website.views.cops', name='cops'),
    url(r'^green/$', 'website.views.green', name='green'),
    url(r'^troc/$', 'website.views.troc', name='troc'),
    url(r'^robotics/$', 'website.views.robotics', name='robotics'),
    url(r'^sae/$', 'website.views.sae', name='sae'),
    url(r'^cef/$', 'website.views.cef', name='cef'),
    url(r'^sae-baja/$', 'website.views.sae_baja', name='sae-baja'),
    url(r'^vocowsa/$', 'website.views.vocowsa', name='vocowsa'),
    url(r'^auv/$', 'website.views.auv', name='auv'),
    url(r'^app/$', 'website.views.app', name='app'),
    url(r'^technex/$', 'website.views.technex', name='technex'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
