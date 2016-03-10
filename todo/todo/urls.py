from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'todolist.views.index'),
    #url(r'^index/$', 'todolist.views.index', name="index"),
    url(r'^index/register/$', 'todolist.views.register_view'),
    url(r'^index/login/$', 'todolist.views.login_view'),
    url(r'^index/logout/$', 'todolist.views.logout_view'),
    url(r'^index/create/$', 'todolist.views.create_view'),
]
