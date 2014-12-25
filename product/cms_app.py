# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ProductApp(CMSApp):
    name = _('Product')
    urls = ['product.urls']
    app_name = 'Product'

apphook_pool.register(ProductApp)
