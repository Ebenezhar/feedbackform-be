from django.urls import path
import api.views as api

urlpatterns = [
    path("feedback", api.FeedBackView.as_view(), name='generate-aml-report'),
]