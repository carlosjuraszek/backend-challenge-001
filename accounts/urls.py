"""
Accounts URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include


###
# URL Patterns
###
urlpatterns = [
    url(r'^api/v1/', include('accounts.api.v1.urls')),
    url(r'^api/v1/', include('topic.api.v1.urls'))
]
