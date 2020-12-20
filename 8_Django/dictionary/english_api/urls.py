from django.urls import path
# from .views import WordList
from . import generic_views


urlpatterns = [
    # path('words/', WordList.as_view(), name='word_list'),
    path('', generic_views.ListCreateWord().as_view(), name='word_list'),
    path('<int:pk>', generic_views.RetrieveUpdateDestroyWord().as_view(), name='word_detail'),
]