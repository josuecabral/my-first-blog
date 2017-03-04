from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'boletin.views.inicio', name='inicio'),
    url(r'^registrados/$', 'boletin.views.registrados', name='registrados'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
