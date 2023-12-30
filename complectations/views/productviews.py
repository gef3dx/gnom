from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..models import Product, Complectation, GroupProduct
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ProductForm, GroupProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.urls import reverse
import datetime 


class ProductViewList(LoginRequiredMixin, ListView):
    template_name = 'product/product.html'
    model = Product
    paginate_by = 15
    context_object_name = 'products'


class ProductViewListFromComplet(LoginRequiredMixin, ListView):
    template_name = 'product/productfromcomplet.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Product.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductViewListFromComplet,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Product.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('sum_price_count'))
        context['prepayment'] = Product.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('prepayment'))
        context['remains'] = Product.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('remains'))
        context['date_now'] = datetime.date.today()
        context['date_plus'] = datetime.date.today() + datetime.timedelta(days=7)
        context['groups'] = GroupProduct.objects.all()

        return context
    
class ProductViewListFromCompletAndGroup(LoginRequiredMixin, ListView):
    template_name = 'product/productfromcomplet.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Product.objects.filter(complectation__slug=slug, group__slug=self.kwargs['group'])
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductViewListFromCompletAndGroup,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Product.objects.filter(complectation__slug=self.kwargs['slug'], group__slug=self.kwargs['group']).aggregate(Sum('sum_price_count'))
        context['prepayment'] = Product.objects.filter(complectation__slug=self.kwargs['slug'], group__slug=self.kwargs['group']).aggregate(Sum('prepayment'))
        context['remains'] = Product.objects.filter(complectation__slug=self.kwargs['slug'], group__slug=self.kwargs['group']).aggregate(Sum('remains'))
        context['date_now'] = datetime.date.today()
        context['date_plus'] = datetime.date.today() + datetime.timedelta(days=7)
        context['groups'] = GroupProduct.objects.all()
        if context['products']:
            context['grouppdf'] = context['products'][0].group
            context['grouppdfslug'] = context['products'][0].group.slug
        else:
            context['grouppdf'] = ""

        return context


class ProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = "product/updateproduct.html"
    model = Product
    form_class = ProductForm
    # success_url = "/"

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.sum_price_count = obj.count * obj.price
        obj.remains = obj.prepayment - obj.sum_price_count
        return super(ProductUpdate, self).form_valid(form)
    
    def get_success_url(self):
        slug = get_object_or_404(Product, id = self.kwargs['pk'])
        return reverse('productfromcomplet', kwargs={'slug': slug.complectation.slug})


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product/deleteproduct.html"
    
    def get_success_url(self):
        slug = get_object_or_404(Product, id = self.kwargs['pk'])
        return reverse('productfromcomplet', kwargs={'slug': slug.complectation.slug})


class ProductDetaleView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/productdetale.html'
    context_object_name = 'product'


class ProductAdd(LoginRequiredMixin, CreateView):
    template_name = "product/addproduct.html"
    model = Product
    form_class = ProductForm
    url = ""

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        comp = Complectation.objects.filter(id = self.kwargs['product_id'])
        self.url = comp[0].slug
        obj.complectation = comp[0]
        obj.sum_price_count = obj.count * obj.price
        obj.remains = obj.prepayment - obj.sum_price_count
        return super(ProductAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('productfromcomplet', kwargs={'slug': self.url}) 
    

class GroupProductAddView(LoginRequiredMixin, CreateView):
    template_name = "product/addgroupproduct.html"
    model = GroupProduct
    form_class = GroupProductForm
    success_url = "/group"


class GroupProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/groupproductlist.html'
    model = GroupProduct
    context_object_name = 'grops'


class GroupProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "product/groupproductupdate.html"
    model = GroupProduct
    form_class = GroupProductForm
    success_url = "/group"


class GroupProductDeleteView(LoginRequiredMixin, DeleteView):
    model = GroupProduct
    template_name = "product/groupproductdelete.html"
    success_url = "/group"