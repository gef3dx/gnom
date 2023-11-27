from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import ProductSmeta, Complectation, Provider, Receipts, ServiceSmeta
from ..forms import ProductSmetaForm, ProviderForm, ReceiptsForm, ServiceSmetaForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum
from django.views.generic.list import ListView
from decimal import Decimal   

# CRUD view прихода средств
class ReceiptsViewListFromComplet(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/receiptsfromcomplet.html'
    model = Receipts
    context_object_name = 'receipts'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Receipts.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ReceiptsViewListFromComplet,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Receipts.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price'))

        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.role == "Клиент":
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
class ReceiptsAddView(LoginRequiredMixin, CreateView):
    template_name = "productsmeta/receiptsadd.html"
    model = Receipts
    form_class = ReceiptsForm
    url = ""

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        comp = Complectation.objects.filter(id = self.kwargs['product_id'])
        self.url = comp[0].slug
        obj.complectation = comp[0]
        return super(ReceiptsAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listreceipts', kwargs={'slug': self.url})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
class ReceiptsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "productsmeta/receiptsupdate.html"
    model = Receipts
    form_class = ReceiptsForm
    # success_url = "/"

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        return super(ReceiptsUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        slug = get_object_or_404(Receipts, id = self.kwargs['pk'])
        return reverse('listreceipts', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
class ReceiptsDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipts
    template_name = "productsmeta/receiptsdelete.html"
    
    def get_success_url(self):
        slug = get_object_or_404(Receipts, id = self.kwargs['pk'])
        return reverse('listreceipts', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
            
 
# CRUD view Услуг 
class ServiceSmetaAddView(LoginRequiredMixin, CreateView):
    template_name = "productsmeta/serviceadd.html"
    model = ServiceSmeta
    form_class = ServiceSmetaForm
    url = ""

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.price_all = obj.price * obj.count
        obj.price_procent = obj.price_all * (Decimal(obj.procent / 100))
        comp =  Complectation.objects.filter(id = self.kwargs['product_id'])
        self.url = comp[0].slug
        obj.complectation = comp[0]
        return super(ServiceSmetaAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listsevice', kwargs={'slug': self.url})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ServiceSmetaViewListFromComplet(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/servicefromcomplet.html'
    model = ServiceSmeta
    context_object_name = 'service'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ServiceSmeta.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ServiceSmetaViewListFromComplet,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['price_all'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price_all'))
        context['price_procent'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price_procent'))
        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.role == "Клиент":
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
class ServiceSmetaViewListFromCompletStatus(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/servicefromcomplet.html'
    model = ServiceSmeta
    context_object_name = 'service'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ServiceSmeta.objects.filter(complectation__slug=slug, payment_status = self.kwargs['status'])
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ServiceSmetaViewListFromCompletStatus,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['price_all'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug'], payment_status = self.kwargs['status']).aggregate(Sum('price_all'))
        context['price_procent'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug'], payment_status = self.kwargs['status']).aggregate(Sum('price_procent'))
        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ServiceSmetaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "productsmeta/serviceupdate.html"
    model = ServiceSmeta
    form_class = ServiceSmetaForm
    # success_url = "/"

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.price_all = obj.price * obj.count
        obj.price_procent = obj.price_all * (Decimal(obj.procent / 100))
        return super(ServiceSmetaUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        slug = get_object_or_404(ServiceSmeta, id = self.kwargs['pk'])
        return reverse('listsevice', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')


class ServiceSmetaDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceSmeta
    template_name = "productsmeta/servicedelete.html"
    
    def get_success_url(self):
        slug = get_object_or_404(ServiceSmeta, id = self.kwargs['pk'])
        return reverse('listsevice', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

# CRUD view Закупок 
class ProductSmetaAdd(LoginRequiredMixin, CreateView):
    template_name = "productsmeta/addproductsmeta.html"
    model = ProductSmeta
    form_class = ProductSmetaForm
    url = ""

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        comp =  Complectation.objects.filter(id = self.kwargs['product_id'])
        self.url = comp[0].slug
        obj.complectation = comp[0]
        return super(ProductSmetaAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('productsmetafromcomplet', kwargs={'slug': self.url})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ProductSmetaViewListFromComplet(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/productsmetafromcomplet.html'
    model = ProductSmeta
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ProductSmeta.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductSmetaViewListFromComplet,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = ProductSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price'))

        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.role == "Клиент":
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
class ProductSmetaViewListFromCompletStatus(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/productsmetafromcomplet.html'
    model = ProductSmeta
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ProductSmeta.objects.filter(complectation__slug=slug, payment_status = self.kwargs['status'])
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductSmetaViewListFromCompletStatus,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = ProductSmeta.objects.filter(complectation__slug=self.kwargs['slug'], payment_status = self.kwargs['status']).aggregate(Sum('price'))

        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    


class ProductSmetaUpdate(LoginRequiredMixin, UpdateView):
    template_name = "productsmeta/updateproductsmeta.html"
    model = ProductSmeta
    form_class = ProductSmetaForm
    # success_url = "/"

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        return super(ProductSmetaUpdate, self).form_valid(form)
    
    def get_success_url(self):
        slug = get_object_or_404(ProductSmeta, id = self.kwargs['pk'])
        return reverse('productsmetafromcomplet', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')


class ProductSmetaDelete(LoginRequiredMixin, DeleteView):
    model = ProductSmeta
    template_name = "productsmeta/deleteproductsmeta.html"
    
    def get_success_url(self):
        slug = get_object_or_404(ProductSmeta, id = self.kwargs['pk'])
        return reverse('productsmetafromcomplet', kwargs={'slug': slug.complectation.slug})
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
# CRUD view поставщик 
class ProviderAdd(LoginRequiredMixin, CreateView):
    template_name = "productsmeta/addprovider.html"
    model = Provider
    form_class = ProviderForm
    success_url = "/provider"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ProviderListView(LoginRequiredMixin, ListView):
    template_name = 'productsmeta/providerlist.html'
    model = Provider
    context_object_name = 'providers'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ProviderUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "productsmeta/providerupdate.html"
    model = Provider
    form_class = ProviderForm
    success_url = "/provider"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

class ProviderDeleteView(LoginRequiredMixin, DeleteView):
    model = Provider
    template_name = "productsmeta/providerdelete.html"
    success_url = "/provider"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')