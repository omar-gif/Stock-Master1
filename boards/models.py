from unicodedata import name
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
import os

# Create your models here.
from django.utils.encoding import force_str

def path_and_renameListing1(instance, filename):
    upload_to = 'images/signup/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Role(models.Model):
    name = models.CharField(max_length=500,default=None,null=True)
    cond = models.IntegerField(default=0,null=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(max_length=500, default=None, null=True)
    mobile = models.CharField(max_length=500, default=None, null=True)
    image = models.FileField(upload_to=path_and_renameListing1, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return force_str(self.user)


class ShipperList(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    country = models.CharField(max_length=50,default=None,null=True)
    profileshipper = models.ForeignKey(Profile ,related_name="ownerProfile", on_delete=models.CASCADE,default=None,null=True)
    profileMainAccount = models.ForeignKey(Profile ,related_name="relatedProfile", on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return force_str(self.name)

class VendorList(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    country = models.CharField(max_length=50,default=None,null=True)
    profileVendor = models.ForeignKey(Profile,related_name="ownerProfileShipper", on_delete=models.CASCADE, default=None, null=True)
    shippervendor = models.ForeignKey(ShipperList,related_name="ownerProfileVendor", on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return force_str(self.name)

class FollowerList(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    country = models.CharField(max_length=50,default=None,null=True)
    profileFollower = models.ForeignKey(Profile, related_name="ownerProfileVendors", on_delete=models.CASCADE,
                                      default=None, null=True)
    vendorFollower = models.ForeignKey(VendorList, related_name="ownerProfileFollowr", on_delete=models.CASCADE,
                                      default=None, null=True)

    def __str__(self):
        return force_str(self.name)


class Shipper(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    nationality = models.CharField(max_length=50,default=None,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name


def path_and_renameListing(instance, filename):
    upload_to = 'images/car/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    # else:
    #     # set filename as random string
    #     filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_renameListing2(instance, filename):
    upload_to = 'images/excel/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    # else:
    #     filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

def path_and_renameListing3(instance, filename):
    upload_to = 'images/orderInvoices/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    # else:
    #     filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_renameListing4(instance, filename):
    upload_to = 'images/Item/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_renameListing5(instance, filename):
    upload_to = 'images/JobSheets/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Hospitals(models.Model):
    hospitalName = models.CharField(max_length=250,null=True)

    def __str__(self):
        return force_str(self.hospitalName)



class CompanyName(models.Model):
    companyName = models.CharField(max_length=250,null=True)

    def __str__(self):
        return force_str(self.companyName)

class CompanyUnits(models.Model):
    modelOfAnalyzer = models.CharField(max_length=250,null=True)
    companyName1 = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.modelOfAnalyzer)
    
class WorkFlow(models.Model):
    nameOfWorkFlow = models.CharField(max_length=250,null=True)
    companyAnalyzers = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    companyName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.nameOfWorkFlow)

class Governorate(models.Model):
    GovernorateName = models.CharField(max_length=250,null=True)

    def __str__(self):
        return force_str(self.GovernorateName)

class HospitalsAnalyzers(models.Model):
    SerialNumber = models.CharField(max_length=250,null=True)
    Counter = models.CharField(max_length=250,null=True)
    PM = models.DateField(max_length=250,null=True)
    Ups = models.CharField(max_length=250,null=True)
    Earth = models.CharField(max_length=250,null=True)
    Stab = models.CharField(max_length=250,null=True)
    Software = models.CharField(max_length=250,null=True)
    HosNam = models.ForeignKey(Hospitals,on_delete=models.CASCADE, null=True)
    compNam = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    compUni = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    WorFlo = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)
    Govern = models.ForeignKey(Governorate,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return force_str(self.HosNam)

class OutInvoice(models.Model):
    outInvoiceNumber = models.CharField(max_length=50, default=None, null=True)
    Datao = models.DateField(max_length=50, default=None, null=True)
    CompaniesNAme = models.CharField(max_length=50, default=None, null=True)
    ItemName = models.CharField(max_length=50, default=None, null=True)
    ItemPartNumber = models.CharField(max_length=50, default=None, null=True)
    LtQTY = models.IntegerField( default=None, null=True)
    Lots = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return force_str(self.outInvoiceNumber)
    
    def get_International(self):
        return{   
            'id': self.id,
            'outInvoiceNumber':self.outInvoiceNumber,
            'ItemName': self.ItemName,
            'Datao': self.Datao,
            'ItemPartNumber': self.ItemPartNumber,
            'CompaniesNAme': self.CompaniesNAme,
            'LtQTY': self.LtQTY,
            'Lots': self.Lots,
        }

class Lot(models.Model):
    Loto = models.CharField(max_length=50, default=None, null=True)
    LotQTY = models.IntegerField( default=None, null=True)
    AllLotQTY = models.IntegerField( default=None, null=True)
    JNum = models.CharField(max_length=50, default=None, null=True)
    Lot_outInvoice = models.ForeignKey(OutInvoice,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return force_str(self.Loto)

class ItemInput(models.Model):
    nameOfItem = models.CharField(max_length=255, null=True)
    mainUser = models.CharField(max_length=255,null=True)
    teamLeader = models.CharField(max_length=255, null=True)
    engineerName = models.CharField(max_length=255, null=True)
    dateOfArrival = models.DateField(max_length=50, null=True)
    partNumber = models.CharField(max_length=255, default=None,null=True)
    cost = models.IntegerField(default=0,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    Item_Model_workFlow = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)
    Item_outInvoice = models.ForeignKey(OutInvoice,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.nameOfItem)

class Imag3(models.Model):
    images = models.ImageField(upload_to=path_and_renameListing4, null=True)
    Inpu = models.ForeignKey(ItemInput,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.Inpu)

class TeamLeader(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    role = models.CharField(max_length=50,default=None,null=True)
    profileTeamLeader = models.ForeignKey(Profile ,related_name="TeamLeaderProfile", on_delete=models.CASCADE,default=None,null=True)
    ProfileMainUser = models.ForeignKey(Profile ,related_name="relatedMainProfile", on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return force_str(self.name)

class Engineer(models.Model):
    name = models.CharField(max_length=100,default=None,null=True)
    role = models.CharField(max_length=50,default=None,null=True)
    profileEngineer = models.ForeignKey(Profile,related_name="ownerProfileTeamLeader", on_delete=models.CASCADE, default=None, null=True)
    TLeaderEngineer = models.ForeignKey(TeamLeader,related_name="ownerProfileEngineer", on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return force_str(self.name)

class BookStore(models.Model):
    nameOfUser = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    NameOfItem = models.ForeignKey(ItemInput, on_delete=models.CASCADE, null=True)
    BookedLot = models.ForeignKey(Lot, on_delete=models.CASCADE, null=True)
    QTYOfItem =  models.IntegerField(default=0,null=True)
    StatusOfItem = models.CharField(max_length=50, default=None, null=True)
    RemainingQTY = models.IntegerField(default=0, null=True)
    def __str__(self):
        return force_str(self.nameOfUser)
    
    def get_data(self):
        return{
            'id': self.id,
            'CampNam': self.NameOfItem.Item_Model_compName.companyName,
            'AnaNam': self.NameOfItem.Item_Model_workFlow.nameOfWorkFlow,
            'ParNum': self.NameOfItem.partNumber,
            'NameOfItem': self.NameOfItem.nameOfItem,
            'nameOfUser': self.nameOfUser.username,
            'BookedLot': self.BookedLot.Loto,
            'QTYOfItem': self.QTYOfItem,
            'StatusOfItem': self.StatusOfItem,
            'RemainingQTY': self.RemainingQTY,
        }




class QuotationStatus(models.Model):
    InvoiceNumber =  models.IntegerField(default=0,null=True)
    Status = models.CharField(max_length=50, default=None, null=True)
    def __str__(self):
        return force_str(self.Status)

class InvoiceStatus(models.Model):
    InvoiceNumber =  models.IntegerField(default=0,null=True)
    Status = models.CharField(max_length=50, default=None, null=True)
    def __str__(self):
        return force_str(self.Status)

class JobSheet(models.Model):
    
    mainUser = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    dateOfJobSheet = models.DateField(max_length=50, null=True)
    Note = models.CharField(max_length=255,null=True)
    cost = models.IntegerField(default=0,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    Item_Model_workFlow = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)
    Hospital = models.ForeignKey(HospitalsAnalyzers,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.Hospital)

class JobSheetImg(models.Model):
    images = models.ImageField(upload_to=path_and_renameListing5, null=True)
    Inpu = models.ForeignKey(JobSheet,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.Inpu)

class AssembledStore(models.Model):
    ItemId = models.CharField(max_length=255, default=None,null=True)
    ItemName = models.CharField(max_length=255, default=None,null=True)
    Dato = models.DateField(max_length=50, default=None,null=True)
    partNumber = models.CharField(max_length=255, default=None,null=True)
    QTY = models.CharField(max_length=255, default=None,null=True)
    Price = models.IntegerField(default=None,null=True)
    InvoNum = models.CharField(max_length=255, default=None,null=True)
    Cot = models.CharField(max_length=255, default=None,null=True)
    LotNum = models.ForeignKey(Lot, on_delete=models.CASCADE, default=None, null=True)
    nameOfUser = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    Item_Model_workFlow = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)
    HosName = models.ForeignKey(Hospitals,on_delete=models.CASCADE, null=True)
    Invo = models.ForeignKey(InvoiceStatus,on_delete=models.CASCADE, null=True)
    JobSheet = models.ForeignKey(JobSheet,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return force_str(self.HosName)

    def get_assem(self):
        GetSerial = HospitalsAnalyzers.objects.get(HosNam=self.HosName)
        return{   
            'id': self.id,
            'ItemName': self.ItemName,
            'Dato': self.Dato,
            'partNumber': self.partNumber,
            'QTY': self.QTY,
            'Price': self.Price,
            'InvoNum': self.InvoNum,
            'Cot': self.Cot,
            'LotNum': self.LotNum.Loto,
            'nameOfUser': self.nameOfUser.username,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
            'Item_Model_workFlow': self.Item_Model_workFlow.nameOfWorkFlow,
            'Serial':GetSerial.SerialNumber,
            # 'Serial':self.HosName.hospitalName,
            'HosName': self.HosName.hospitalName,
            'Invo': self.Invo.Status,
        }
    
    def get_spec(self):
        return{   
            'ItemName': self.ItemName,
            'Dato': self.Dato,
            'partNumber': self.partNumber,
            'Price': self.Price,
            'InvoNum': self.InvoNum,
            'LotNum': self.LotNum.Loto,
            'nameOfUser': self.nameOfUser.username,
        }

class CotNumber(models.Model):
    ItemName = models.CharField(max_length=50, default=None, null=True)
    PartNumber = models.CharField(max_length=50, default=None, null=True)
    HosName = models.CharField(max_length=50, default=None, null=True)
    CotNumber1 =  models.IntegerField(default=0,null=True)
    InvoNumber1 =  models.IntegerField(default=0,null=True)
    Datee = models.DateField(max_length=50, default=None, null=True)
    ItemLot = models.CharField(max_length=50, default=None, null=True)
    def __str__(self):
        return force_str(self.CotNumber1)

class InvoiceNumbero(models.Model):
    ItemName = models.CharField(max_length=50, default=None, null=True)
    PartNumber = models.CharField(max_length=50, default=None, null=True)
    HosName = models.CharField(max_length=50, default=None, null=True)
    CotNumber1 =  models.IntegerField(default=0,null=True)
    InvoiceNumber1 =  models.IntegerField(default=0,null=True)
    Datee = models.DateField(max_length=50, default=None, null=True)
    ItemLot = models.CharField(max_length=50, default=None, null=True)
    Price = models.CharField(max_length=50, default=None, null=True)
    def __str__(self):
        return force_str(self.InvoiceNumber1)

    def get_confirmed(self):
        return{   
            'id': self.id,
            'ItemName': self.ItemName,
            'Datee': self.Datee,
            'PartNumber': self.PartNumber,
            'HosName': self.HosName,
            'CotNumber1': self.CotNumber1,
            'InvoiceNumber1': self.InvoiceNumber1,
            'ItemLot': self.ItemLot,  
        }

class Price(models.Model):
    ItemName = models.CharField(max_length=255, default=None,null=True)
    partNumber = models.CharField(max_length=255, default=None,null=True)
    Price = models.IntegerField(default=None,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    Item_Model_workFlow = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.partNumber)
    def get_price(self):
        return{
            'id': self.id,
            'ItemName': self.ItemName,
            'partNumber': self.partNumber,
            'Price': self.Price,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
            'Item_Model_workFlow': self.Item_Model_workFlow.nameOfWorkFlow,
        }

class Undertest(models.Model):
    nameOfItem = models.CharField(max_length=255, null=True)
    mainUser = models.CharField(max_length=255,null=True)
    dateOfArrival = models.DateField(max_length=50, null=True)
    partNumber = models.CharField(max_length=255, default=None,null=True)
    LotNum = models.CharField(max_length=255, default=None,null=True)
    Status = models.CharField(max_length=255, default=None,null=True)
    Note = models.CharField(max_length=255, default=None,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    Item_Model_workFlow = models.ForeignKey(WorkFlow,on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return force_str(self.nameOfItem)
    
class WorkFlowLine(models.Model):
    date = models.DateField(max_length=50, null=True)
    UserName = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    HosName = models.ForeignKey(Hospitals,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.HosName)
    
class ParameterName(models.Model):
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    ParameterNam = models.CharField(max_length=255, default=None,null=True)

    
    def __str__(self):
        return force_str(self.ParameterNam)

class ReagentQTY(models.Model):
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    ParName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    CatNumber = models.CharField(max_length=255, default=None,null=True)
    ShippindCond = models.CharField(max_length=255, default=None,null=True)
    Cal = models.CharField(max_length=255, default=None,null=True)
    slideNumber = models.IntegerField(default=None,null=True)
    GTIN = models.CharField(max_length=255,default=None,null=True)
    Price = models.FloatField(default=None,null=True)
    
    def __str__(self):
        return force_str(self.CatNumber)
    
class Calibrator(models.Model):
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    ParName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    Cal = models.CharField(max_length=255, default=None,null=True)
    
    def __str__(self):
        return force_str(self.Cal)

class OrganizeName(models.Model):
    organizeName = models.CharField(max_length=255, default=None,null=True)
    
    def __str__(self):
        return force_str(self.organizeName)
    
class OraderCreation(models.Model):
    dat = models.DateField(max_length=10, default=None,null=True)
    Note = models.CharField(max_length=255, default=None,null=True)
    status = models.CharField(max_length=255, default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    OrganizeNam = models.ForeignKey(OrganizeName,on_delete=models.CASCADE, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return force_str(self.orderNum)
    
class ElementCreation(models.Model):
    SlidesQTY = models.IntegerField(default=None,null=True)
    QTY = models.IntegerField(default=None,null=True)
    dat = models.CharField(max_length=255, default=None,null=True)
    Note = models.CharField(max_length=255, default=None,null=True)
    status = models.CharField(max_length=255, default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    CatNumber = models.ForeignKey(ReagentQTY,on_delete=models.CASCADE, null=True)
    ElementName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return force_str(self.orderNum)
    def get_elem(self):
        return{
            'SlidesQTY': self.SlidesQTY,
            'QTY': self.QTY,
            'dat': self.dat,
            'Note': self.Note,
            'orderNum': self.orderNum,
            'CatNumber': self.CatNumber.CatNumber,
            'ElementName': self.ElementName.ParameterNam,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }
    
class ElementConfermation(models.Model):
    QTY = models.CharField(max_length=255, default=None,null=True)
    dat = models.CharField(max_length=255, default=None,null=True)
    Note = models.CharField(max_length=255, default=None,null=True)
    status = models.CharField(max_length=255, default=None,null=True)
    BatchNumber = models.CharField(max_length=255, default=None,null=True)
    SlidesQTY = models.FloatField(default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    ConfNum = models.CharField(max_length=255, default=None,null=True)
    CatNumber = models.ForeignKey(ReagentQTY,on_delete=models.CASCADE, null=True)
    ExpiryDate = models.DateField(max_length=255, default=None,null=True)
    ElementName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return force_str(self.orderNum)
    def get_conf(self):
        return{
            'ConfNum':self.ConfNum,
            'ExpiryDate': self.ExpiryDate,
            'CatNumber': self.CatNumber.CatNumber,
            'Price': self.CatNumber.Price,
            'SlidesQTY': self.SlidesQTY,
            'status': self.status,
            'QTY': self.QTY,
            'dat': self.dat,
            'BatchNumber':self.BatchNumber,
            'Note': self.Note,
            'orderNum': self.orderNum,
            'ElementName': self.ElementName.ParameterNam,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }
    
class AutoOrderInvoice(models.Model):
    QTY = models.CharField(max_length=255, default=None,null=True)
    SlidesQTY = models.FloatField(default=None,null=True)
    dat = models.CharField(max_length=255, default=None,null=True)
    Price = models.FloatField(default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    InvoiceNumber = models.CharField(max_length=255, default=None,null=True)
    CatNumber = models.ForeignKey(ReagentQTY,on_delete=models.CASCADE, null=True)
    ElementName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    orderConfermation = models.CharField(max_length=255, default=None,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.orderNum)
    def get_AutoOrderInvoice(self):
        return{
            'SlidesQTY': self.SlidesQTY,
            'QTY': self.QTY,
            'dat': self.dat,
            'Price': self.Price,
            'orderNum': self.orderNum,
            'ElementName': self.ElementName.ParameterNam,
            'CatNumber': self.CatNumber.CatNumber,
            'InvoiceNumber': self.InvoiceNumber,
            'orderConfermation': self.orderConfermation,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }

class OrderInvoice(models.Model):
    dat = models.CharField(max_length=255, default=None,null=True)
    Price = models.FloatField(default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    InvoiceNumber = models.CharField(max_length=255, default=None,null=True)
    orderConfermation = models.CharField(max_length=255, default=None,null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.InvoiceNumber)
    def get_OrderInvoice(self):
        return{
            'dat': self.dat,
            'Price': self.Price,
            'orderNum': self.orderNum,
            'InvoiceNumber': self.InvoiceNumber,
            'orderConfermation': self.orderConfermation,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }

class Shipping(models.Model):
    PO = models.CharField(max_length=255, default=None,null=True)
    ImportApproval = models.CharField(max_length=255, default=None,null=True)
    OkToShip = models.CharField(max_length=255, default=None,null=True)
    ShippingDate = models.CharField(max_length=255, default=None,null=True)
    ShippingCond = models.CharField(max_length=255, default=None,null=True)
    ArrivalDate = models.CharField(max_length=255, default=None,null=True)
    EDADate = models.CharField(max_length=255, default=None,null=True)
    TechDate = models.CharField(max_length=255, default=None,null=True)
    EDAReleaseDate = models.CharField(max_length=255, default=None,null=True)
    InvNumber = models.ForeignKey(OrderInvoice,on_delete=models.CASCADE, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.InvNumber)
    objects = models.Manager()
    def get_shipping(self):
        return{
            'id':self.id,
            'PO': self.PO,
            'ImportApproval': self.ImportApproval,
            'OkToShip': self.OkToShip,
            'ShippingDate': self.ShippingDate,
            'ShippingCond': self.ShippingCond,
            'ArrivalDate': self.ArrivalDate,
            'EDADate': self.EDADate,
            'TechDate': self.TechDate,
            'EDAReleaseDate': self.EDAReleaseDate,
            'InvNumber': self.InvNumber.InvoiceNumber,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }

class ExcelFile(models.Model):
    file = models.FileField(upload_to=path_and_renameListing)
    ordnum = models.ForeignKey(OraderCreation,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return force_str(self.file)
    
class ExcelFileOrderCrea(models.Model):
    file = models.FileField(upload_to=path_and_renameListing2)
    ordnum = models.ForeignKey(OraderCreation,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.file)

class ExcelFileInvoice(models.Model):
    file = models.FileField(upload_to=path_and_renameListing3)
    ordnum = models.ForeignKey(OraderCreation,on_delete=models.CASCADE, null=True)
    ordinv = models.ForeignKey(OrderInvoice,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return force_str(self.ordinv)

class Autoconfdata(models.Model):
    OrderNumber = models.CharField(max_length=255, default=None,null=True)
    PO = models.CharField(max_length=255, default=None,null=True)
    matrial = models.CharField(max_length=255, default=None,null=True)
    MatDesc = models.CharField(max_length=255, default=None,null=True)
    BatchNum = models.CharField(max_length=255, default=None,null=True)
    ExpiryDate = models.CharField(max_length=255, default=None,null=True)
    OrderQTY = models.CharField(max_length=255, default=None,null=True)
    CumConfQTY = models.CharField(max_length=255, default=None,null=True)
    UnitPrice = models.CharField(max_length=255, default=None,null=True)
    NetVal = models.CharField(max_length=255, default=None,null=True)
    excfile = models.ForeignKey(ExcelFile,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return force_str(self.OrderNumber)
    def get_Autoconf(self):
        return{
            'OrderNumber':self.OrderNumber,
            'PO': self.PO,
            'matrial': self.matrial,
            'MatDesc': self.MatDesc,
            'BatchNum': self.BatchNum,
            'ExpiryDate': self.ExpiryDate,
            'OrderQTY': self.OrderQTY,
            'CumConfQTY': self.CumConfQTY,
            'UnitPrice': self.UnitPrice,
            'NetVal': self.NetVal,
            
        }
    
class AutoElementCreation(models.Model):
    SlidesQTY = models.IntegerField(default=None,null=True)
    QTY = models.IntegerField(default=None,null=True)
    dat = models.CharField(max_length=255, default=None,null=True)
    status = models.CharField(max_length=255, default=None,null=True)
    orderNum = models.CharField(max_length=255, default=None,null=True)
    CatNumber = models.ForeignKey(ReagentQTY,on_delete=models.CASCADE, null=True)
    ElementName = models.ForeignKey(ParameterName,on_delete=models.CASCADE, null=True)
    Item_Model_compName = models.ForeignKey(CompanyName,on_delete=models.CASCADE, null=True)
    Item_Model_compUnit = models.ForeignKey(CompanyUnits,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return force_str(self.orderNum)
    def get_elem(self):
        return{
            'SlidesQTY': self.SlidesQTY,
            'QTY': self.QTY,
            'dat': self.dat,
            'orderNum': self.orderNum,
            'CatNumber': self.CatNumber.CatNumber,
            'ElementName': self.ElementName.ParameterNam,
            'Item_Model_compName': self.Item_Model_compName.companyName,
            'Item_Model_compUnit': self.Item_Model_compUnit.modelOfAnalyzer,
        }


