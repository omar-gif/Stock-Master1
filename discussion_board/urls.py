"""discussion_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages-signup.html',views.profileweb,name="profileweb"),
    path('pages-signin.html',views.signinPage,name="signinPage"),
    path('signout',views.signout1,name="signout1"),
    path('accounts/login/',views.signinPage,name = 'signinPage'),
    path('uservald/',views.uservald,name = 'uservald'),
    path('getMainUser/', views.getMainUser,name='getMainUser'),
    path('seclive/',views.seclive,name='seclive'),
    path('lotosearch/',views.lotosearch,name='lotosearch'),
    path('GetUser/', views.GetUser, name='GetUser'),
    path('namesjson/', views.namesjson,name='namesjson'),
    path('adminjson/', views.adminjson,name='adminjson'),
    path('Codoimg/', views.Codoimg, name='Codoimg'),
    path('getFiles2/', views.getFiles2,name='getFiles2'),
    path('getFiles3/', views.getFiles3,name='getFiles3'),
    path('QTYdataBase/', views.QTYdataBase,name='QTYdataBase'),
    path('uploadFiles3/', views.uploadFiles3,name='uploadFiles3'),
    path('block.html', views.block,name='block'),

    path('codevalid/', views.codevalid,name='codevalid'),
    path('Namee/', views.Namee,name='Namee'),
    path('getItemName/', views.getItemName,name='getItemName'),
    path('Removo/', views.Removo,name='Removo'),
    path('UserAssem/', views.UserAssem,name='UserAssem'),
    path('tableRowDel/', views.tableRowDel,name='tableRowDel'),
    path('Notifactions/', views.Notifactions,name='Notifactions'),
    path('ShowUndertest/', views.ShowUndertest,name='ShowUndertest'),
    path('BookUndertest/', views.BookUndertest,name='BookUndertest'),
    path('Hos/', views.Hos,name='Hos'),
    path('Hos1/', views.Hos1,name='Hos1'),
    
    path('QTYdataBaseQTY/', views.QTYdataBaseQTY,name='QTYdataBaseQTY'),
    path('json/', views.Itemjson,name='Item_json'),
    path('priceJson/', views.priceJson,name='priceJson'),
    path('assemJson/', views.assemJson,name='assemJson'),
    path('assemJson1/', views.assemJson1,name="assemJson1"),
    path('UpdateLotQTY/', views.UpdateLotQTY,name='UpdateLotQTY'),
    path('GetPrice/', views.GetPrice,name='GetPrice'),

    path('updateMyProfile/', views.updateMyProfile,name='updateMyProfile'),
    path('pages-my-profile.html', views.myProfile,name='myProfile'),
    path('pages-price-list.html', views.PriceList,name='PriceList'),
    path('index/', views.indexo,name='indexo'),
    path('userProfileajax/', views.userProfileajax,name='userProfileajax'),
    path('UserBookStore/', views.UserBookStore,name='UserBookStore'),

    path('InvoiceNum/', views.InvoiceNum,name='InvoiceNum'),
    path('QuotationNum/', views.QuotationNum,name='QuotationNum'),
    path('layouts-default.html', views.datatabl,name='datatabl'),

    
    path('companiesName/', views.companiesName,name='companiesName'),
    path('analyzerTypes/', views.analyzerTypes,name='analyzerTypes'),
    path('nameOfItem/', views.nameOfItem,name='nameOfItem'),

    path('GetTypes/', views.GetTypes,name='GetTypes'),
    path('GetTypelikechem/', views.GetTypelikechem,name='GetTypelikechem'),
    path('GetTypeOfAnalyzer/', views.GetTypeOfAnalyzer,name='GetTypeOfAnalyzer'),


    
    path('parameter-Name.html', views.ParameteName,name='ParameteName'),
    path('parameter-cat.html', views.CatNum,name='CatNum'),
    path('getParameter/', views.getParameter,name='getParameter'),
    path('getcatNo/', views.getcatNo,name='getcatNo'),

    path('Orgazine-Name.html', views.OrganizationName,name='OrganizationName'),
    path('getOrganize/', views.getOrganize,name='getOrganize'),

    path('pages-create-order.html', views.CreateOrder,name='CreateOrder'),
    path('SaveOrders/', views.SaveOrders,name='SaveOrders'),
    path('SavelementOrder/', views.SavelementOrder,name='SavelementOrder'),
    path('pages-show-order.html', views.ShowOrder,name='ShowOrder'),
    path('getOreders/', views.getOreders,name='getOreders'),
    path('confJson/', views.confJson,name='confJson'),
    path('checkcat/', views.checkcat,name='checkcat'),
    path('checkcatQty/', views.checkcatQty,name='checkcatQty'),
    path('getcompanies/', views.getcompanies,name='getcompanies'),

    path('CheckOrderNum/', views.CheckOrderNum,name='CheckOrderNum'),
    path('CheckOrderNum2/', views.CheckOrderNum2,name='CheckOrderNum2'),
    path('CheckelementNum2/', views.CheckelementNum2,name='CheckelementNum2'),

    path('getOrderElements/', views.getOrderElements,name='getOrderElements'),
    path('UpdateOrderQTy/', views.UpdateOrderQTy,name='UpdateOrderQTy'),

    path('SavconnfOrder1/', views.SavconnfOrder1,name='SavconnfOrder1'),
    path('getcatnum/', views.getcatnum,name='getcatnum'),
    path('getdates/', views.getdates,name='getdates'),

    path('index-reagent.html', views.homeReagent,name='homeReagent'),

    path('parameters/', views.parameters,name='parameters'),

    path('pardata/', views.pardata,name='pardata'),
    path('confdata/', views.confdata,name='confdata'),

    path('checkOrderNumdate/', views.checkOrderNumdate,name='checkOrderNumdate'),

    path('getAllConf/', views.getAllConf,name='getAllConf'),

    path('SavconnfOrder/', views.SavconnfOrder,name='SavconnfOrder'),
    path('CreateConNum/', views.CreateConNum,name='CreateConNum'),
    path('showPrices/', views.showPrices,name='showPrices'),

    path('pages-show-invoices.html', views.ConfInvoice,name='ConfInvoice'),
    path('invTable/', views.invTable,name='invTable'),

    path('progressTable/', views.progressTable,name='progressTable'),
    path('editship/', views.editship,name='editship'),
    path('iteminInvoice/', views.iteminInvoice,name='iteminInvoice'),

    path("importo",views.Import_Excel_pandas,name="Import_Excel_pandas"),
    path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"), 
    path('exceldatatable/', views.exceldatatable,name="exceldatatable"),
    path('uploadItems/', views.uploadItems,name="uploadItems"),
    path('uploadItems6/', views.uploadItems6,name="uploadItems6"),
    path('uploadItems7/', views.uploadItems7,name="uploadItems7"),
    path('uploadItems8/', views.uploadItems8,name="uploadItems8"),
    path('collectinfo/', views.collectinfo,name="collectinfo"),
    path('saveExcelToConf/', views.saveExcelToConf,name="saveExcelToConf"),
    path('cancelExcelToConf/', views.cancelExcelToConf,name="cancelExcelToConf"),

    path('checkShippingCond/', views.checkShippingCond,name="checkShippingCond"),
    path('InvoiceData/', views.InvoiceData,name="InvoiceData"),
    path('SavInvoOrder/', views.SavInvoOrder,name="SavInvoOrder"),
    path('checkDouplicatePara/', views.checkDouplicatePara,name="checkDouplicatePara"),

    path('getAutoconf/', views.getAutoconf,name="getAutoconf"),
    path('delAutoconf/', views.delAutoconf,name="delAutoconf"),

    path('backOrder/', views.backOrder,name="backOrder"),
    path('AutoInvOrder/', views.AutoInvOrder,name="AutoInvOrder"),
    path('updateInvNumber/', views.updateInvNumber,name="updateInvNumber"),
    path('excelbtns/', views.excelbtns,name="excelbtns"),
    path('uploadexcel/', views.uploadexcel,name="uploadexcel"),
    path('uploadexcelnamechick/', views.uploadexcelnamechick,name="uploadexcelnamechick"),
    path('uploadexcelname/', views.uploadexcelname,name="uploadexcelname"),
    path('uploadInvoices/', views.uploadInvoices,name="uploadInvoices"),
    path('uploadOrder/', views.uploadOrder,name="uploadOrder"),
    path('showinginvoices/', views.showinginvoices,name="showinginvoices"),
    path('ckeckInvo/', views.ckeckInvo,name="ckeckInvo"),

    path('getAllOrders/', views.getAllOrders,name="getAllOrders"),
    path('OrdersFiles/', views.OrdersFiles,name="OrdersFiles"),
    path('Ordersinvoices/', views.Ordersinvoices,name="Ordersinvoices"),
    path('getconfirmations/', views.getconfirmations,name="getconfirmations"),
    path('getOrders/', views.getOrders,name="getOrders"),

    path('checkForOrder/', views.checkForOrder,name="checkForOrder"),

    path('base.html/', views.base,name="base"),

    path('importsystem/', views.secProHomePage,name="secProHomePage"),

    path('itemsnumbers/', views.itemsnumbers,name="itemsnumbers"),

    ##################### third project

    ## main Page
    path('', views.mainPage,name="mainPage"),
    path('InputPage/', views.InputPage,name="InputPage"),
    path('InvoicePage/', views.InvoicePage,name="InvoicePage"),
    path('InventoryPage/', views.InventoryPage,name="InventoryPage"),
    path('setupPage/', views.setupPage,name="setupPage"),
    path('Hospitals/', views.HospitalsPage,name="HospitalsPage"),

    ## Invoice Page
    
    path('assemJsonPending/', views.assemJsonPending,name="assemJsonPending"),
    path('HospitalsInvoices/', views.HospitalsInvoices,name="HospitalsInvoices"),
    path('InternationalInvoices/', views.InternationalInvoices,name="InternationalInvoices"),
    path('sendingQuotNum/', views.sendingQuotNum,name="sendingQuotNum"),
    path('sendingInvoiceNum/', views.sendingInvoiceNum,name="sendingInvoiceNum"),


    ## Input Page 
    
    path('ItemPriceFunc/', views.ItemPriceFunc,name="ItemPriceFunc"),
    path('ItemInput3/', views.ItemInput3,name='ItemInput3'),
    path('CheckItemName/', views.CheckItemName,name='CheckItemName'),
    path('subIntrInvoice/', views.subIntrInvoice,name='subIntrInvoice'),
    path('subUnderTest/', views.subUnderTest,name='subUnderTest'),

    ## Stock Page 
    
    path('GetVitros350/', views.GetVitros350,name='GetVitros350'),
    path('GetItem/', views.GetItem,name='GetItem'),
    path('GetItemmc15/', views.GetItemmc15,name='GetItemmc15'),
    path('GetItemr910/', views.GetItemr910,name='GetItemr910'),
    path('SaveBookStore/', views.SaveBookStore,name='SaveBookStore'),
    path('foriphone/', views.foriphone,name='foriphone'),
    path('ItemHopitals/', views.ItemHopitals,name='ItemHopitals'),
    path('GetUnderTest/', views.GetUnderTest,name='GetUnderTest'),

    ## Setup Page 
    path('GetHosName/', views.GetHosName,name='GetHosName'),
    path('ValHosName/', views.ValHosName,name='ValHosName'),
    path('ValSerialNum/', views.ValSerialNum,name='ValSerialNum'),
    path('SubCompForm/', views.SubCompForm,name='SubCompForm'),
    path('SubUserForm/', views.SubUserForm,name='SubUserForm'),
    path('uploadFilesSignup/', views.uploadFilesSignup,name='uploadFilesSignup'),

    ## Hospital Page  
    path('GetFilterHos/', views.GetFilterHos,name='GetFilterHos'),
    path('GetHosJob/', views.GetHosJob,name='GetHosJob'),
    path('GetHosSpare/', views.GetHosSpare,name='GetHosSpare'),
    path('OpenHos/', views.OpenHos,name='OpenHos'),
    path('GetDiaHos/', views.GetDiaHos,name='GetDiaHos'),
    path('SearchOCDHosp/', views.SearchOCDHosp,name='SearchOCDHosp'),
    path('SearchDiaHosp/', views.SearchDiaHosp,name='SearchDiaHosp'),
    path('GetAllGovern/', views.GetAllGovern,name='GetAllGovern'),

    ## index Page 
    path('hosSearch/', views.hosSearch,name='hosSearch'),
    path('GetMySpareParts/', views.GetMySpareParts,name='GetMySpareParts'),
    path('GetPartNumber/', views.GetPartNumber,name='GetPartNumber'),
    path('SendSubmitForm/', views.SendSubmitForm,name='SendSubmitForm'),
    path('GethosName/', views.GethosName,name='GethosName'),
    path('uploadFiles8/', views.uploadFiles8,name='uploadFiles8'),
    path('GetItems/', views.GetItems,name='GetItems'),
    path('GetAllHos/', views.GetAllHos,name='GetAllHos'),
    path('GetAllInvoices/', views.GetAllInvoices,name='GetAllInvoices'),
    path('AddPendingInvo/', views.AddPendingInvo,name='AddPendingInvo'),
    path('GetWorkFlow/', views.GetWorkFlow,name='GetWorkFlow'),
    path('GetWorkFlowUsers/', views.GetWorkFlowUsers,name='GetWorkFlowUsers'),
    path('searchSN/', views.searchSN,name='searchSN'),
    path('returnFun/', views.returnFun,name='returnFun'),


]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)+static(settings.TEMPORARY_URL , document_root = settings.TEMPORARY_ROOT)
