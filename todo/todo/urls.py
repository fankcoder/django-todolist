from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'todolist.views.index'),
    url(r'^index/', 'todolist.views.index', name="index"),
    url(r'^register/$', 'todolist.views.register'),
    url(r'^login/$', 'todolist.views.login'),
]
