from django.urls import path,include
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), #customise the name of the function created
]
