from django.urls import path,include
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_json_by_id #customise the name of the function created

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), #customise the name of the function created
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #customise the name of the function created
]
