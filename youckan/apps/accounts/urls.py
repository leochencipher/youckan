from django.conf.urls import patterns, include, url

from youckan.apps.accounts.views import UserListView, ProfileView, ProfileEditView

urlpatterns = patterns('',

    url(r'^u/$', UserListView.as_view(), name='users'),
    url(r'^u/(?P<slug>[\d\w_-]+)/$', ProfileView.as_view(), name='profile'),

    url(r'^my/profile/$', ProfileEditView.as_view(), name='profile-edit'),
    url(r'^my/password/$', ProfileEditView.as_view(), name='password-change'),
)