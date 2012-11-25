from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^bobisum$', 'pages.views.homepage', name='home'),
	url(r'^contacts$', 'pages.views.contacts', name='contacts'),
	url(r'^products$', 'products.views.products', name='products'),
	url(r'^register$', 'users.views.register_user', name='register'),
	url(r'^login$', 'users.views.login_user', name='login'),
	url(r'^testow$', 'testowapp.views.avtomobili', name='testow'),
	# url(r'^products$', 'products.views.products', name='products'),
	# url(r'^products$', 'products.views.products', name='products'),
    # url(r'^hello/', include('hello.foo.urls')),

	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls))
)