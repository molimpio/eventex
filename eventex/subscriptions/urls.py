from django.urls import path
from eventex.subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<uuid:url_identity>/', detail, name='detail'),
]
