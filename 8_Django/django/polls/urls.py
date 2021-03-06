from django.urls import path

# from . import views
from .apiviews import QuestionList, QuestionDetail, ChoiceList, CreateVote


# app_name = 'polls'
urlpatterns = [
    path('polls/', QuestionList.as_view(), name="questions_list"),
    path('polls/<int:pk>/', QuestionDetail.as_view(), name="questions_detail"),
    path('choices/', ChoiceList.as_view(), name="choice_list"),
    path('vote/', CreateVote.as_view(), name="create_vote"),
]

# urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]