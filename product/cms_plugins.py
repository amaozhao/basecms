from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from product.models import ProductPlugin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


class ProductPluginForm(ModelForm):

    class Meta:
        model = ProductPlugin


class ProductPlugin(CMSPluginBase):
    model = ProductPlugin
    name = _("Products")
    render_template = "products/product-plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'products': instance.get_products()
        })
        return context

plugin_pool.register_plugin(ProductPlugin)
