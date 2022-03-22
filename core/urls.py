import django
from django.conf.urls import url
from django.urls import path, include
from djecommerce.settings.base import *
from django.views.static import serve
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    search_products, search_category, category_view, payment, changelang
)


app_name = 'core'

handler500 = 'core.views.handler500'

handler403 = 'core.views.handler403'

handler404 = 'core.views.handler404'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('search/', search_products, name='search-products'),
    path('category/search/automotive', search_category, name='automotive-category-search'),
    path('category/search/electrical', search_category, name='electrical-category-search'),
    path('category/search/hand_tools', search_category, name='handtools-category-search'),
    path('category/search/home_hardware', search_category, name='homehardware-category-search'),
    path('category/search/lighting', search_category, name='lighting-category-search'),
    path('caregory/automotive', category_view, name='automotive'),
    path('caregory/electrical', category_view, name='electrical'),
    path('caregory/hand_tools', category_view, name='handtools'),
    path('caregory/home_hardware', category_view, name='homehardware'),
    path('caregory/lighting', category_view, name='lighting'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('changelang/', changelang, name='changelang'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    url(r'^payment/', payment),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
        MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
        STATIC_ROOT})
]
