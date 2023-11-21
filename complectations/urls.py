from django.urls import path
from .views import (ComplectationsViewList, 
                    ProductViewListFromComplet, 
                    ProductDetaleView, 
                    ComplectationsAdd, 
                    ComplectationsUpdate, 
                    ComplectationsDelete, 
                    ProductAdd, 
                    ProductUpdate, 
                    ProductDelete, 
                    UserViewList, 
                    UserAddView, 
                    UserUpdateView, 
                    DelUserView,
                    ProductSmetaAdd,
                    ProductSmetaViewListFromComplet,
                    ProductSmetaUpdate,
                    ProductSmetaDelete,
                    ProviderAdd,
                    ProviderListView,
                    ProviderUpdateView,
                    ProviderDeleteView,
                    ProductViewListFromCompletAndGroup,
                    GroupProductAddView,
                    GroupProductListView,
                    GroupProductUpdateView,
                    GroupProductDeleteView,
                    ReceiptsViewListFromComplet,
                    ReceiptsAddView,
                    ReceiptsUpdateView,
                    ReceiptsDeleteView,
                    ServiceSmetaAddView,
                    ServiceSmetaViewListFromComplet,
                    ServiceSmetaUpdateView,
                    ServiceSmetaDeleteView,
                    ServiceSmetaViewListFromCompletStatus,
                    ProductSmetaViewListFromCompletStatus,
                    ReceiptsViewPdf,
                    ServiceViewPdf,
                    ProductSmetaPDFView,
                    ProductCompletPdfView,
                    ProductCompletGroupPdfView
                    )

urlpatterns = [
   path('', ComplectationsViewList.as_view(), name='home'),
   
   path('users/', UserViewList.as_view(), name='users'),
   path('users/add/', UserAddView.as_view(), name='adduser'),
   path('users/update/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),
   path('users/delete/<int:pk>/', DelUserView.as_view(), name='deleteuser'),
   
   path('complect/add/', ComplectationsAdd.as_view(), name='addcomplect'),
   path('complect/update/<str:slug>/', ComplectationsUpdate.as_view(), name='updatecomplect'),
   path('complect/delete/<str:slug>/', ComplectationsDelete.as_view(), name='deletecomplect'),

   path('<str:slug>/', ProductViewListFromComplet.as_view(), name='productfromcomplet'),
   
   path('product/<int:pk>/', ProductDetaleView.as_view(), name='productdetele'),
   path('product/add/<int:product_id>/', ProductAdd.as_view(), name='addproduct'),
   path('product/update/<int:pk>/', ProductUpdate.as_view(), name='updateproduct'),
   path('product/delete/<int:pk>/', ProductDelete.as_view(), name='deleteproduct'),
   path('product-pdf/<str:slug>', ProductCompletPdfView.as_view(), name='productpdf'),
   path('product-pdf/<str:slug>/<str:group>/', ProductCompletGroupPdfView.as_view(), name='productgrouppdf'),


   
   path('procurement/add/<int:product_id>/', ProductSmetaAdd.as_view(), name='addproductsmeta'),
   path('procurement/<str:slug>/', ProductSmetaViewListFromComplet.as_view(), name='productsmetafromcomplet'),
   path('procurement/update/<int:pk>/', ProductSmetaUpdate.as_view(), name='updateproductsmeta'),
   path('procurement/delete/<int:pk>/', ProductSmetaDelete.as_view(), name='deleteproductsmeta'),
   path('procurement/<str:slug>/<str:status>/', ProductSmetaViewListFromCompletStatus.as_view(), name='listprocurementstatus'),
   path('procurement-pdf/<str:slug>', ProductSmetaPDFView.as_view(), name='procurementpdf'),



   path('provider/add/', ProviderAdd.as_view(), name='addprovider'),
   path('provider', ProviderListView.as_view(), name='listprovider'),
   path('provider/update/<int:pk>/', ProviderUpdateView.as_view(), name='updateprovider'),
   path('provider/delete/<int:pk>/', ProviderDeleteView.as_view(), name='deleteprovider'),



   
   path('group', GroupProductListView.as_view(), name='listgrop'),
   path('group/update/<int:pk>/', GroupProductUpdateView.as_view(), name='updategroup'),
   path('group/delete/<int:pk>/', GroupProductDeleteView.as_view(), name='deletegroup'),
   path('group/add/', GroupProductAddView.as_view(), name='addgroup'),

   path('receipts/add/<int:product_id>/', ReceiptsAddView.as_view(), name='addreceipts'),
   path('receipts/<str:slug>', ReceiptsViewListFromComplet.as_view(), name='listreceipts'),
   path('receipts/update/<int:pk>/', ReceiptsUpdateView.as_view(), name='updatereceipts'),
   path('receipts/delete/<int:pk>/', ReceiptsDeleteView.as_view(), name='deletereceipts'),
   path('receipts-pdf/<str:slug>', ReceiptsViewPdf.as_view(), name='receiptspdf'),


   path('sevice/add/<int:product_id>/', ServiceSmetaAddView.as_view(), name='addsevice'),
   path('sevice/<str:slug>', ServiceSmetaViewListFromComplet.as_view(), name='listsevice'),
   path('sevice/update/<int:pk>/', ServiceSmetaUpdateView.as_view(), name='updatesevice'),
   path('sevice/delete/<int:pk>/', ServiceSmetaDeleteView.as_view(), name='deletesevice'),
   path('sevice/<str:slug>/<str:status>/', ServiceSmetaViewListFromCompletStatus.as_view(), name='listsevicestatus'),
   path('sevice-pdf/<str:slug>', ServiceViewPdf.as_view(), name='sevicepdf'),



   path('<str:slug>/<str:group>/', ProductViewListFromCompletAndGroup.as_view(), name='productfromcompletandgroup'),
]
