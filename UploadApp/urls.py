
from django.urls import path
from .views  import  home,update_keyword_list_func, saveUpload,KeysListView


urlpatterns = [
    path('', home, name='home'),
    path('update_keyord_list/', update_keyword_list_func, name='update_keyword_list_func'),
    path('save_file', saveUpload, name='save_upload'),
    path('downloads',KeysListView.as_view(), name='downloads' ),
]

