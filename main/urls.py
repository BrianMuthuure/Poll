from django.urls import path
from .views import QuestionListView, QuestionDetailView, vote, results


app_name = 'main'

urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:pk>/results/', results, name='results'),
    path('questions/<int:pk>/vote/', vote, name='vote'),
]