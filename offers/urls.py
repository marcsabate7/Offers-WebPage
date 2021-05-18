from django.urls import path
from .views import OfferListView,OfferDetailView,OfferUpdateView,OfferDeleteView
from .views import OfferCreateView
from offers import views as offers_views
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', OfferListView.as_view(),name='offers-page'),
    path('offer/new/',OfferCreateView.as_view(),name='offer-create'),
    path('offer/<int:pk>/', OfferDetailView.as_view(),name='offer-detail'),
    path('offer/<int:pk>/update/', OfferUpdateView.as_view(),name='offer-update'),
    path('offer/<int:pk>/delete/', OfferDeleteView.as_view(),name='offer-delete'),
    path('product/new/', offers_views.createProduct,name='product-create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)