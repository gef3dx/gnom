from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from ..models import Receipts, Complectation, ServiceSmeta, ProductSmeta, Product
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum

from django.http import HttpResponse
from django.views.generic import View

from complectations.utils import render_to_pdf 

import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# PDF Поступления
class ReceiptsViewPdf(LoginRequiredMixin, ListView):
    template_name = 'pdf/receiptspdf.html'
    model = Receipts
    context_object_name = 'receipts'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Receipts.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ReceiptsViewPdf,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Receipts.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price'))
        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_client:
            self.object = None
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            pdf = render_to_pdf(self.template_name, context)
            
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s.pdf" %(str(self.kwargs['slug']) +"-postuplen"+"-"+ str(get_random_string(20)))
                content = "attachment; filename= %s" %(filename)
                response['Content-Disposition'] = content
                return response
            
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
        
# PDF Услуги
class ServiceViewPdf(LoginRequiredMixin, ListView):
    template_name = 'pdf/servicepdf.html'
    model = ServiceSmeta
    context_object_name = 'service'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ServiceSmeta.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ServiceViewPdf,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['price_all'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price_all'))
        context['price_procent'] = ServiceSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price_procent'))
        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_client:
            self.object = None
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            pdf = render_to_pdf(self.template_name, context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s.pdf" %(str(self.kwargs['slug']) +"-uslug"+"-"+ str(get_random_string(20)))
                content = "attachment; filename= %s" %(filename)
                response['Content-Disposition'] = content
                return response
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

# PDF Закупки       
class ProductSmetaPDFView(LoginRequiredMixin, ListView):
    template_name = 'pdf/purchasespdf.html'
    model = ProductSmeta
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = ProductSmeta.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductSmetaPDFView,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = ProductSmeta.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('price'))

        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_client:
            self.object = None
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            pdf = render_to_pdf(self.template_name, context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s.pdf" %(str(self.kwargs['slug']) +"-zukup"+"-"+ str(get_random_string(20)))
                content = "attachment; filename= %s" %(filename)
                response['Content-Disposition'] = content
                return response
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
        
# PDF Вся комплектация
class ProductCompletPdfView(LoginRequiredMixin, ListView):
    template_name = 'pdf/completpdf.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Product.objects.filter(complectation__slug=slug)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductCompletPdfView,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Product.objects.filter(complectation__slug=self.kwargs['slug']).aggregate(Sum('sum_price_count'))

        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_client:
            self.object = None
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            pdf = render_to_pdf(self.template_name, context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s.pdf" %(str(self.kwargs['slug']) +"-"+ str(get_random_string(20)))
                content = "attachment; filename= %s" %(filename)
                response['Content-Disposition'] = content
                return response
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')

# PDF Комлектации по группам   
class ProductCompletGroupPdfView(LoginRequiredMixin, ListView):
    template_name = 'pdf/completpdf.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        queryset = Product.objects.filter(complectation__slug=slug, group__slug=self.kwargs['group'])
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super(ProductCompletGroupPdfView,self).get_context_data(**kwargs)
        comp = get_object_or_404(Complectation, slug=self.kwargs['slug'])
        context['product_id'] = comp.id
        context['product_name'] = comp.name
        context['product_slug'] = comp.slug
        context['sum'] = Product.objects.filter(complectation__slug=self.kwargs['slug'], group__slug=self.kwargs['group']).aggregate(Sum('sum_price_count'))
        if context['products']:
            context['grouppdf'] = context['products'][0].group
        else:
            context['grouppdf'] = ""
        
        return context
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff or self.request.user.is_client:
            self.object = None
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            pdf = render_to_pdf(self.template_name, context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s.pdf" %(str(self.kwargs['slug']) +"-"+self.kwargs['group']+"-"+ str(get_random_string(20)))
                content = "attachment; filename= %s" %(filename)
                response['Content-Disposition'] = content
                return response
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')