# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from product.views import ProductListView, ProductDetailView


urlpatterns = patterns(
    '',
    url(r'^$', ProductListView.as_view(), name='product-latest'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),
)
