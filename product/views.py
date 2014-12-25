from django.views.generic import ListView, DetailView
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/object_list.html'
    paginate_by = 15


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/object_detail.html'
