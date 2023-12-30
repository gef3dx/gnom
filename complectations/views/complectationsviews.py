from django.views.generic.list import ListView
from ..models import Complectation, Receipts, ServiceSmeta, ProductSmeta
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ComplectationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.db.models import Sum



class ComplectationsViewList(LoginRequiredMixin, ListView):
    template_name = 'complectation/home.html'
    model = Complectation
    paginate_by = 15
    context_object_name = 'complectations'
    saldo = 0
    proc = 0
    plus_bal = 0

    def get_queryset(self, **kwargs):
        if self.request.user.is_staff:
            queryset = Complectation.objects.all()
        else:
            queryset = Complectation.objects.filter(users=self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ComplectationsViewList,self).get_context_data(**kwargs)
        
        saldo = 0
        for obj in context['object_list']:

            receipts = Receipts.objects.filter(complectation__slug=obj.slug).aggregate(Sum('price'))
            service = ServiceSmeta.objects.filter(complectation__slug=obj.slug).aggregate(Sum('price_all'))
            procent = ServiceSmeta.objects.filter(complectation__slug=obj.slug).aggregate(Sum('price_procent'))
            procurement = ProductSmeta.objects.filter(complectation__slug=obj.slug).aggregate(Sum('price'))
            vprocess_org = ServiceSmeta.objects.filter(complectation__slug=obj.slug, process_org=True).aggregate(Sum('price_all'))
            
            

            if receipts["price__sum"] is None:
                receipts["price__sum"] = 0
            if service["price_all__sum"] is None:
                service["price_all__sum"] = 0
            if procent["price_procent__sum"] is None:
                procent["price_procent__sum"] = 0
            if procurement["price__sum"] is None:
                procurement["price__sum"] = 0

            if vprocess_org['price_all__sum'] is None:
                vprocess_org['price_all__sum'] = 0
            
            obj.balance = receipts["price__sum"] - (service["price_all__sum"] + procurement["price__sum"])
            obj.procent = procent["price_procent__sum"] - vprocess_org['price_all__sum']
            self.saldo += obj.balance
            self.proc += obj.procent

            
            if obj.balance >= 0:
                self.plus_bal += obj.balance
            
        context['saldo'] =  self.saldo
        context['proc'] =  self.proc 
        context['all'] = self.saldo + self.proc
        context['plus_bal'] = self.plus_bal

        
        return context

class ComplectationsAdd(LoginRequiredMixin, CreateView):
    template_name = "complectation/addcomplet.html"
    model = Complectation
    form_class = ComplectationForm
    success_url = "/"
    
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
    

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return super(ComplectationsAdd, self).form_valid(form)  

class ComplectationsUpdate(LoginRequiredMixin, UpdateView):
    template_name = "complectation/updatecomplect.html"
    model = Complectation
    form_class = ComplectationForm
    success_url = "/"
    
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


class ComplectationsDelete(LoginRequiredMixin, DeleteView):
    model = Complectation
    success_url = "/"
    template_name = "complectation/deletecomplet.html"

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