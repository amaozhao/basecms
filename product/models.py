from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.models import Image
from cms.models import CMSPlugin


class Product(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    price = models.FloatField(_('price'), default=0.0)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    url = models.URLField(_('url'), default='http://yuelingshan.com/')
    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['-updated']


class ProductPlugin(CMSPlugin):
    title = models.CharField(
        _('title'), max_length=255, default='Product Gallery Title')
    description = models.TextField(
        _('description'), default='Product Gallery Sub-Title.')
    count = models.IntegerField(_('count'), default=4)

    def __unicode__(self):
        return '%s' % self.count

    def get_products(self):
        return Product.objects.all()[:self.count]
