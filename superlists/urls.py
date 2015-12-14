from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Currently not using the admin page
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include('lists.urls'))
]
