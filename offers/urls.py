from django.urls import path
from .views import OfferListView,OfferDetailView,OfferCreateView
from . import views

urlpatterns = [
    path('', OfferListView.as_view(),name='offers-page'),
    path('offer/<int:pk>/', OfferDetailView.as_view(),name='offer-detail'),
    path('offer/new/', OfferCreateView.as_view(),name='offer-create'),
]
