from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r"^$", views.api_root),
    url(r"^snippets/$", views.SnippetList.as_view(), name='snippet-list'),
    url(r"^snippets/(?P<pk>[\d]+)/$", views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r"^users/$", views.UserList.as_view(), name='user-list'),
    url(r"^users/(?P<pk>[\d]+)/$", views.UserDetail.as_view(), name='user-detail'),
    url(r"^snippets/(?P<pk>[\d]+)/highlight/$", views.SnippetHighlight.as_view(), 
                                    name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r"", include('rest_framework.urls', namespace='rest_framework')),
]
