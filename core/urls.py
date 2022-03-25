import django
from django.conf.urls import url
from django.urls import path, include
from djecommerce.settings.base import *
from django.views.static import serve
from .views import (
    CheckoutView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    search_products, search_category, category_view, payment,  products, ordersummary, home_view
)


app_name = 'core'

handler500 = 'core.views.handler500'

handler403 = 'core.views.handler403'

handler404 = 'core.views.handler404'


urlpatterns = [
    path('', home_view, name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', ordersummary, name='order-summary'),
    path('product/<slug>/', products, name='product'),
    path('search/', search_products, name='search-products'),
    path('category/search/walls_and_foundation', search_category, name='walls-and-foundation-search'),
    path('category/search/roof_and_facade', search_category, name='roof-and-facade-search'),
    path('category/search/finishing_and_decor', search_category, name='finishing-and-decor-search'),
    path('category/walls_and_foundation', category_view, name='walls-and-foundation'),
    path('category/roof_and_facade', category_view, name='roof-and-facade'),
    path('category/finishing_and_decor', category_view, name='finishing-and-decor'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('changelang/', changelang, name='changelang'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    url(r'^payment/', payment),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
        MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
        STATIC_ROOT})
]
