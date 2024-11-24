from django.urls import path

from apps.general.views import GeneralTemplateView

urlpatterns = [
    path('', GeneralTemplateView.as_view(), name='general_page'),
]
