from django.urls import path
from . import api

urlpatterns = [
    # path('ready/', api.KakaoPayReadyView.as_view()),
    # path('ready/', api.kakaoPay),
    path('ready/', api.ready),
]
