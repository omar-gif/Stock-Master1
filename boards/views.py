from ast import Del, Expression
from datetime import date
import datetime
from genericpath import exists
from queue import Empty
from re import X
import select
import pandas as pd
from ssl import AlertDescription
import sys
from django.db.models.functions import Extract
from django.db.models.functions import ExtractMonth
from datetime import timedelta
from django.forms import DateField
from django.utils.timezone import now 
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *
from django.db.models import Q
from django.http import Http404, JsonResponse, HttpResponseRedirect
# Create your views here.
import boards
import json
from boards.models import Shipper, Profile, Role, ShipperList, VendorList, FollowerList ,InvoiceNumbero
import os
from django.contrib import messages

from django.forms.models import model_to_dict
from os import listdir
from os.path import isfile, join

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
# from rest_framework import serializers

import boards
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from uuid import uuid4
import os

from django.core.files import File
from django.conf import settings
import mimetypes

from django.core.files.storage import FileSystemStorage

@csrf_exempt
def getFiles2(request):
    fromId = request.GET.get('fromId')
    Inpuid = Imag.objects.filter(Inpu_id=fromId)
    # print(Inpuid)
    messagesData = []
    # print(messagesData);
    for n in list(Inpuid):
        responsee = {
            # 'acualId_id': Inpuid.id,
            'item_img': n.images.url,
            # 'item_da': item.Inpu_id,
        }
        x = messagesData.append(n.images.url)
        # print(messagesData)
    return JsonResponse(messagesData, safe=False)

@csrf_exempt
def getFiles3(request):
    fromId1 = request.GET.get('fromId1')
    Inpuid = Imag2.objects.filter(Inpu_id=fromId1)
    # print(Inpuid)
    messagesData = []
    for n in list(Inpuid):
        responsee = {
            'item_img': n.images2.url,
        }
        x = messagesData.append(n.images2.url)
        # print(messagesData)
    return JsonResponse(messagesData, safe=False)

@csrf_exempt
def uploadFiles(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = 'temporary/car/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0] + '.' + ext + '``__``' + uuid4().hex, ext)
            default_storage.save(os.path.join(upload_to, filename), f)
    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadFiles2(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = 'temporary/certificates/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0] + '.' + ext + '``__``' + uuid4().hex, ext)
            default_storage.save(os.path.join(upload_to, filename), f)
    return JsonResponse({'State': 'Success'})

def block(request):
    current_user1 = request.user
    userStaff = current_user1.is_superuser

    return render(request,'block.html',{'userStaff' : userStaff})

def getMainUser(request):
    current_user1 = request.user
    user_staff = current_user1.is_superuser
    if user_staff == True:
        current_user2 = request.user.id
        currentImage = Profile.objects.get(user_id=current_user2)
        current_position = Role.objects.get(id=current_user2)
        response ={
            'current_user12':current_user1.username,
            'current_image12':currentImage.image.url,
            'current_position12':current_position.name,
        }
        return JsonResponse(response, safe=False)
    elif user_staff == False:
        current_user = request.user
        user_prof = current_user.id
        user_staff = Profile.objects.get(user_id=user_prof)
        if user_staff.role_id == 2:
            current = current_user.username
            currentMain = TeamLeader.objects.get(profileTeamLeader_id=user_staff.id)
            currentMainUser = Profile.objects.get(id=currentMain.ProfileMainUser_id)
            current_user1 = Profile.objects.get(id=currentMainUser.id)
            current_user2 = User.objects.get(id=current_user1.user_id)
            response = {
                'current_user12': current_user2.username,
            }
            return JsonResponse(response, safe=False)
        elif user_staff.role_id == 3:
            currentMain = Engineer.objects.get(profileEngineer_id=user_staff.id)
            currentMainUser = TeamLeader.objects.get(id=currentMain.TLeaderEngineer_id)
            currentMainUserAct = Profile.objects.get(id=currentMainUser.ProfileMainUser_id)
            current_user1 = User.objects.get(id=currentMainUserAct.user_id)
            response = {
                'current_user12': current_user1.username,
            }
            return JsonResponse(response, safe=False)

def seclive(request):
    searchValue = request.GET.get('searchVal')
    print(searchValue)
    allBoard = ItemInput.objects.filter(partNumber__icontains = searchValue)
    names = ItemInput.objects.filter(Q(nameOfItem__icontains = searchValue)|Q(nameOfItem__icontains = ' '+'-'+' '+ searchValue)|Q(nameOfItem__icontains = searchValue +' '+'-'+' '))
    AllArrayOfNames = []
    ans = []
    bns = []
    if allBoard:
        for n in list(allBoard):
            print(n.partNumber)
            img = Imag3.objects.get(Inpu_id=n.id)
            
            AllArrayOfNames.append(n.partNumber)
            AllArrayOfNames.append(n.id)
            AllArrayOfNames.append(img.images.url)
            selectLot = Lot.objects.filter(JNum=n.partNumber)
            for m in list(selectLot):
                ans.append(m.LotQTY)
                bns.append(m.AllLotQTY)
            ansSum = sum(ans)
            bnsSum = sum(bns)
            AllArrayOfNames.append(ansSum)
            AllArrayOfNames.append(bnsSum)
            ans.clear()
            bns.clear()
        return JsonResponse(AllArrayOfNames, safe=False)
    if names:
        for n in list(names):
            print(n.nameOfItem)
            img = Imag3.objects.get(Inpu_id=n.id)
            
            AllArrayOfNames.append(n.nameOfItem)
            AllArrayOfNames.append(n.id)
            AllArrayOfNames.append(img.images.url)
            selectLot = Lot.objects.filter(JNum=n.partNumber)
            for m in list(selectLot):
                ans.append(m.LotQTY)
                bns.append(m.AllLotQTY)
                
            ansSum = sum(ans)
            bnsSum = sum(bns)
            AllArrayOfNames.append(ansSum)
            AllArrayOfNames.append(bnsSum)
            ans.clear()
            bns.clear()
            print(AllArrayOfNames)
        return JsonResponse(AllArrayOfNames, safe=False)
    
def lotosearch(request):
    parto = request.GET.get('lotNum')
    allBoard = OutInvoice.objects.filter(ItemPartNumber=parto)
    AllArrayOfNames = []
    for n in list(allBoard):
        response = {
            'name': n.loto,
        }
        AllArrayOfNames.append(n.loto)

    return JsonResponse(AllArrayOfNames, safe=False)

def GetUser(request):
    current_user1 = request.user
    current_user2 = request.user.id
    currentImage = Profile.objects.get(user_id=current_user2)
    current_position = Role.objects.get(id=currentImage.role_id)
    response ={
        'current_user':current_user1.username,
        'current_image':currentImage.image.url,
        'current_postistion': current_position.name,
    }
    return JsonResponse(response, safe=False)

def Geto(request):
    item = ItemInput.objects.all()
    imgo = Imag3.objects.filter(Inpu_id=item.id)
    print(imgo.url)
    arrayOfItemName=[]
    print(arrayOfItemName)
    for name in list(item):
        response = {
            'name': name.nameOfItem,
        }
        arrayOfItemName.append(name.nameOfItem)
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def QTYdataBaseQTY(request):
    fromId = request.GET.get('max')
    getlot = request.GET.get('loto')
    LotArr =[]
    selectItem = Lot.objects.filter(Q(JNum=fromId)&Q(Loto=getlot))
    for n in list(selectItem):
        LotArr.append(n.LotQTY)
    response = {
        'LotArr':LotArr,
    }
    return JsonResponse(response, safe=False)
    
def UpdateLotQTY(request):
    ReqQTY = request.GET.get('v')
    lotSelect = request.GET.get('lott')
    partnumber = request.GET.get('parto')

    x = Lot.objects.get(Q(JNum = partnumber)&Q(Loto = lotSelect ))
    Lot.objects.filter(pk=x.id).update(LotQTY=ReqQTY)
    return JsonResponse(x.id, safe=False)

def Codoimg(request):
    parto = request.GET.get('partNumber')
    selectItem = ItemInput.objects.get(partNumber=parto)
    selectURL = Imag3.objects.get(Inpu_id = selectItem.id)
    res = selectURL.images.url
    
    return JsonResponse(res, safe=False)

@login_required
def indexo(request):
    try:
        userId = request.user
        userStaff = userId.is_superuser
        if userId =="Omar":
            Item = BookStore.objects.all()
            return render(request, 'octopus-master/octopus/index.html', {'Item': Item , 'userStaff':userStaff,'userId':userId})
        if userStaff == True:
            Item = BookStore.objects.all()
            return render(request, 'octopus-master/octopus/index.html', {'Item': Item , 'userStaff':userStaff})
        else:
            Item = BookStore.objects.filter(nameOfUser_id=userId)
            return render(request, 'octopus-master/octopus/index.html', {'Item': Item})
    except:
        return render(request, 'octopus-master/octopus/pages-signin.html')

def Itemjson(request):
    usery = request.user
    userStaff = usery.is_superuser
    if userStaff == True :
        Items = BookStore.objects.all()
        data =[Item.get_data() for Item in Items]
        response = {'data':data}
        print(response)
        print(response)
        print(response)
        return JsonResponse(response,safe=False)
    else:
        print(usery)
        print(usery)
        print(usery)
        Items = BookStore.objects.filter(nameOfUser_id=usery)
        data =[Item.get_data() for Item in Items]
        print(data)
        response = {'data':data}
        return JsonResponse(response,safe=False)

def adminjson(request):
    recievedName = request.GET.get('actName')
    print(recievedName)
    print(recievedName)
    print(recievedName)
    useru = User.objects.get(username = recievedName)
    print(useru.id)
    Items = BookStore.objects.filter(nameOfUser_id=useru)
    print(Items)
    data =[Item.get_data() for Item in Items]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

def namesjson(request):
    user = request.user
    userStaff = user.is_superuser
    if userStaff == True :
        arrayOfNames=[]
        users = User.objects.all()
        for user in users:
            arrayOfNames.append(user.username)
        return JsonResponse(arrayOfNames,safe=False)

def UserBookStore(request):
    user = request.user
    userStaff = user.is_superuser
    if userStaff == True :
        user_id = user.id
        sparePart = BookStore.objects.all()
        arrayOfItemName = []
        for n in list(sparePart):
            ItemInpo = ItemInput.objects.filter(id=n.NameOfItem_id)
            Lotb = Lot.objects.get(id = n.BookedLot_id)
            usero = User.objects.get(id=n.nameOfUser_id)
            for m in list(ItemInpo):
                xName = CompanyName.objects.get(id = m.Item_Model_compName_id)
                xUnit = WorkFlow.objects.get(id = m.Item_Model_workFlow_id)
                arrayOfItemName.append(m.nameOfItem)
                arrayOfItemName.append(m.partNumber)
                arrayOfItemName.append(xName.companyName)
                arrayOfItemName.append(xUnit.nameOfWorkFlow)
            arrayOfItemName.append(n.QTYOfItem)
            arrayOfItemName.append(n.StatusOfItem)
            arrayOfItemName.append(n.RemainingQTY)
            arrayOfItemName.append(usero.username)
            arrayOfItemName.append(Lotb.Loto)
            
        print(arrayOfItemName)
        return JsonResponse(arrayOfItemName, safe=False)
    else:
        user_id = user.id
        sparePart = BookStore.objects.filter(nameOfUser_id=user_id)
        arrayOfItemName = []
        for n in list(sparePart):
            ItemInpo = ItemInput.objects.filter(id=n.NameOfItem_id)
            Lotb = Lot.objects.get(id = n.BookedLot_id)
            usero = User.objects.get(id=n.nameOfUser_id)
            for m in list(ItemInpo):
                xName = CompanyName.objects.get(id = m.Item_Model_compName_id)
                xUnit = WorkFlow.objects.get(id = m.Item_Model_workFlow_id)
                arrayOfItemName.append(m.nameOfItem)
                arrayOfItemName.append(m.partNumber)
                arrayOfItemName.append(xName.companyName)
                arrayOfItemName.append(xUnit.nameOfWorkFlow)
            arrayOfItemName.append(n.QTYOfItem)
            arrayOfItemName.append(n.StatusOfItem)
            arrayOfItemName.append(n.RemainingQTY)
            arrayOfItemName.append(usero.username)
            arrayOfItemName.append(Lotb.Loto)
        print(arrayOfItemName)
        return JsonResponse(arrayOfItemName, safe=False)

def userProfileajax(request):
    user = request.user
    selectProfile = Profile.objects.get(user_id = user.id)
    if user != "" :
        print(user)
        usery = user.username
        emaily = user.email
        mobiley = selectProfile.mobile
        imagey = selectProfile.image.url
        response = {
            'usery': usery,
            'emaily': emaily,
            'mobiley': mobiley,
            'imagey': imagey,
        }
        return JsonResponse(response, safe=False)

def updateMyProfile(request):

    requser = request.GET.get('user1')
    reqemail = request.GET.get('email1')
    reqmobile = request.GET.get('mobile1')
    reqpass = request.GET.get('pass1')
    
    userId = request.user
    selectProfile = Profile.objects.get(user_id = userId.id)
    userId.set_password(reqpass)
    userId.save()

    User.objects.filter(pk=userId.id).update(username=requser,email=reqemail)
    Profile.objects.filter(pk=selectProfile.id).update(mobile=reqmobile)
    message = "Updated Succefully"
    return JsonResponse(message, safe=False)

def UserAssem(request):
    user = request.user
    userStaff = user.is_superuser
    if userStaff == True :
        user_id = user.id
        sparePart = AssembledStore.objects.all()
        arrayOfItemName = []
        for n in list(sparePart):
            Hos = Hospitals.objects.filter(id=n.HosName_id)
            Comp = CompanyName.objects.filter(id= n.Item_Model_compName_id)
            Uni = CompanyUnits.objects.filter(id= n.Item_Model_compUnit_id)
            Work = WorkFlow.objects.filter(id= n.Item_Model_workFlow_id)
            use = User.objects.filter(id= n.nameOfUser_id)
            invo = InvoiceStatus.objects.filter(id = n.Invo_id)

            for d in list(use):
                arrayOfItemName.append(d.username)
            arrayOfItemName.append(n.ItemId)
            arrayOfItemName.append(n.ItemName)
            arrayOfItemName.append(n.partNumber)
            
            for H in list(Comp):
                arrayOfItemName.append(H.companyName)
            for j in list(Uni):
                arrayOfItemName.append(j.modelOfAnalyzer)
            for s in list(Work):
                arrayOfItemName.append(s.nameOfWorkFlow)
            for m in list(Hos):
                arrayOfItemName.append(m.hospitalName)
            for a in list(invo):
                arrayOfItemName.append(a.Status)
            arrayOfItemName.append(n.Dato)
            arrayOfItemName.append(n.Price)
            arrayOfItemName.append(n.InvoNum)
        print(arrayOfItemName)
        return JsonResponse(arrayOfItemName, safe=False)
    else:
        user_id = user.id
        sparePart = BookStore.objects.filter(nameOfUser_id=user_id)
        arrayOfItemName = []
        for n in list(sparePart):
            ItemInpo = ItemInput.objects.filter(id=n.NameOfItem_id)
            usero = User.objects.get(id=n.nameOfUser_id)
            for m in list(ItemInpo):
                arrayOfItemName.append(m.nameOfItem)
                arrayOfItemName.append(m.partNumber)
                arrayOfItemName.append(m.Item_Model_compName)
            arrayOfItemName.append(n.QTYOfItem)
            arrayOfItemName.append(n.StatusOfItem)
            arrayOfItemName.append(n.RemainingQTY)
            arrayOfItemName.append(usero.username)
        print(arrayOfItemName)
        return JsonResponse(arrayOfItemName, safe=False)

def datatabl(request):
    object_list = CompanyName.objects.all()
    return render(request, 'octopus-master/octopus/layouts-default.html',{'object_list':object_list})

@login_required
def userProfile(request):
    try:
        userId = request.user
        userStaff = userId.is_superuser

        foc = InvoiceStatus.objects.get(Status="FOC")
        ok = InvoiceStatus.objects.get(Status="OK")
        pending = InvoiceStatus.objects.get(Status="Pending")
        submitting = InvoiceStatus.objects.get(Status="Submitting")
        if userStaff == True:

            Item = AssembledStore.objects.filter(Invo = foc)
            Item1 = AssembledStore.objects.filter(Invo = ok )
            Aseem = AssembledStore.objects.filter(Invo = pending)
            Quo = AssembledStore.objects.filter(Cot = ok)
            
            return render(request, 'octopus-master/octopus/pages-user-profile.html', {'Item': Item , 'Aseem':Aseem ,'Item1':Item1 ,'Quo':Quo , 'userStaff':userStaff})
        else:
            Item = BookStore.objects.filter(Q(nameOfUser_id=userId)&Q(nameOfUser_id=userId.id))
            Item = AssembledStore.objects.filter(Q(Invo = foc)&Q(nameOfUser_id=userId.id))
            Item1 = AssembledStore.objects.filter(Q(Invo = ok)&Q(nameOfUser_id=userId.id) )
            Aseem = AssembledStore.objects.filter(Q(Invo = pending)&Q(nameOfUser_id=userId.id))
            Quo = AssembledStore.objects.filter(Q(Cot = ok)&Q(nameOfUser_id=userId.id))
            return render(request, 'octopus-master/octopus/pages-user-profile.html', {'Item': Item , 'Aseem':Aseem ,'Item1':Item1 ,'Quo':Quo , 'userStaff':userStaff})
    except:
        return render(request, 'octopus-master/octopus/pages-signin.html')

def tableRowDel(request):
    AssID = request.GET.get("idnum")
    InvID = request.GET.get("idnumm")
    OutID = request.GET.get("idnumv")
    PriceID = request.GET.get("idnumz")
    if(AssID):
        selctedAss = AssembledStore.objects.get(id=AssID)
        selctedAss.delete()
    elif(InvID):    
        selectedPending = InvoiceNumbero.objects.get(id=InvID)
        selectedPending.delete()
    elif(OutID):    
        selectedPending = OutInvoice.objects.get(id=OutID)
        selectedPending.delete()
    elif(PriceID):    
        selectedPending = Price.objects.get(id=PriceID)
        selectedPending.delete()

    return HttpResponseRedirect('')

def QuotationNum(request):
    num = request.GET.get('x')
    ida = request.GET.get('IDA')
    print(num)
    print(ida)
    zz = QuotationStatus.objects.get(id=3)
    xx = zz.id
    AssembledStore.objects.filter(pk=ida).update(Cot=num)
    return HttpResponseRedirect('')

def InvoiceNum(request):
    num = request.GET.get('x')
    ida = request.GET.get('IDA')
    print(num)
    print(ida)
    olk = InvoiceStatus.objects.get(Status="OK")
    xx = olk.id
    AssembledStore.objects.filter(pk=ida).update(Invo=xx)
    AssembledStore.objects.filter(pk=ida).update(InvoNum=num)
    return HttpResponseRedirect('/')

def Removo(request):
    myUser = request.user
    status_Item = request.GET.get('status_Item')
    note = request.GET.get('note')
    partNumber = request.GET.get('partNum')
    curdate = request.GET.get('curdate')
    Item = ItemInput.objects.get(partNumber=partNumber)
    actlot =request.GET.get('LotQTY')
    ook = request.GET.get('stat')
    itemid = request.GET.get('itemid')
    ACTRemQTY = request.GET.get('ACTRemQTY')
    ACTQTY = request.GET.get('ACTQTY')
    RemainingQTY = request.GET.get('RemainingQTY')
    SelectLot = Lot.objects.get(Q(Loto = actlot)&Q(JNum=partNumber))
    xx = SelectLot.LotQTY + 1 
    if ook == 'Pending'and RemainingQTY == "1":
        ook = "Ok"
        
        BookStore.objects.filter(pk=itemid).update(StatusOfItem=ook,RemainingQTY=ACTRemQTY,QTYOfItem=ACTQTY)
        Lot.objects.filter(pk=SelectLot.id).update(LotQTY=xx)
        return JsonResponse(ook, safe=False)

    elif ook == 'Pending'and RemainingQTY != "1":

        BookStore.objects.filter(pk=itemid).update(RemainingQTY=ACTRemQTY,QTYOfItem=ACTQTY)
        Lot.objects.filter(pk=SelectLot.id).update(LotQTY=xx)
        return JsonResponse(ook, safe=False)
    
    elif ook == 'Ok'and RemainingQTY == "0":
        alr = ("Not Enough QTY")
        return JsonResponse(alr, safe=False)
    
    elif ook == 'Undertest'and RemainingQTY == "0":
        alr = ("Not Enough QTY")
        return JsonResponse(alr, safe=False)
    
    elif ook == 'Undertest'and RemainingQTY == "1":
        Undertest.objects.create(
            nameOfItem = Item.nameOfItem,
            mainUser = myUser,
            dateOfArrival = curdate,
            partNumber = partNumber,
            LotNum = actlot,
            Note = note,
            Status=status_Item,
            Item_Model_compName = Item.Item_Model_compName,
            Item_Model_compUnit = Item.Item_Model_compUnit,
            Item_Model_workFlow = Item.Item_Model_workFlow,
        )
        BookStore.objects.get(pk=itemid).delete()
        return JsonResponse(note, safe=False)

def Hos(request):
    parto = request.GET.get('part')
    comp = ItemInput.objects.get(partNumber=parto)
    hosNam = HospitalsAnalyzers.objects.filter(compNam = comp.Item_Model_compName)
    arrayOfNames = []
    for n in list(hosNam):
        arrayOfNames.append(n.HosNam.hospitalName)

    return JsonResponse(arrayOfNames, safe=False)

def Hos1(request):
    hospitals = Hospitals.objects.all()
    
    arrayOfNames = []
    arraa = []
    for n in list(hospitals):
        
        existo = HospitalsAnalyzers.objects.filter(HosNam=n.id).exists()
        if existo == False:
            print(existo)
            arrayOfNames.append(n.hospitalName)
            print(arrayOfNames)

    return JsonResponse(arrayOfNames, safe=False)

def profileweb(request):
    profileData = Profile.objects.all()
    current_user = request.user
    current_user1 = Profile.objects.get(user_id=current_user.id)
    if current_user.is_authenticated:
        current_user_profile = Profile.objects.get(user=current_user)

        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            mobile = request.POST['mobile_shippo']
            cond = request.POST['cond_shippo']
            usernew = User.objects.create_user(username=username, email=email, password=pass1,
                                               first_name=fname, last_name=lname)
            usernew.save()
            rol_id = Role.objects.get(id=cond)
            image = request.FILES['image_shippo']
            profile = Profile.objects.create(
                user=usernew,
                mobile=mobile,
                image=image,
                role=rol_id
            )
            profile.save()
            if cond == '2':
                # allVendors = Engineer.objects.filter(Q(shippervendor__profileMainAccount__id=current_user_profile.id))
                allShippers = TeamLeader.objects.filter(Q(ProfileMainUser__id=current_user_profile.id))
                rok = TeamLeader.objects.create(
                    name=username,
                    role=rol_id.cond,
                    profileTeamLeader=profile,
                    ProfileMainUser=current_user_profile,

                )
                rok.save()
            elif cond == '3':
                allShippers = TeamLeader.objects.get( profileTeamLeader__id=current_user1.id)
                roko = Engineer.objects.create(

                    name=username,
                    role=rol_id.cond,
                    profileEngineer=profile,
                    TLeaderEngineer=allShippers,
                )
                roko.save()

            
    return render(request, 'octopus-master/octopus/pages-signup.html' ,{'profileData': profileData})

def GetTypes(request):
    namo = request.GET.get('max')
    item = CompanyUnits.objects.filter(companyName = namo)
    arrayOfItemName=[]
    for name in list(item):
        arrayOfItemName.append(name.modelOfAnalyzer)
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def GetTypeOfAnalyzer(request):
    item = CompanyName.objects.all()
    arrayOfItemName=[]
    for name in list(item):
        arrayOfItemName.append(name.companyName)
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def GetTypelikechem(request):
    maxval = request.GET.get('maxi')
    compname = CompanyName.objects.get(companyName=maxval)
    item = CompanyUnits.objects.filter(companyName1_id=compname.id)
    arrayOfItemName=[]
    for name in list(item):
        arrayOfItemName.append(name.modelOfAnalyzer)
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def OCDLinks(request):
    namo = CompanyName.objects.get(companyName = "OCD")
    getitems = CompanyUnits.objects.filter(companyName1_id=namo.id)
    arrayOfItemName = []
    for name in list(getitems):
        arrayOfItemName.append(name.modelOfAnalyzer)
        print(arrayOfItemName)
        # geto = WorkFlow.objects.filter(companyAnalyzers_id = name.id)
        # for x in list(geto):
        #     arrayOfItemName.append(x.nameOfWorkFlow)
    return JsonResponse(arrayOfItemName, safe=False)
    
def DiasysLinks(request):
    namo = CompanyName.objects.get(companyName = "Diasys")
    getitems = CompanyUnits.objects.filter(companyName1_id=namo.id)
    print(getitems)
    print(getitems)
    print(getitems)
    arrayOfItemName = []
    for name in list(getitems):
        arrayOfItemName.append(name.modelOfAnalyzer)
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def companiesName(request):
    names = CompanyName.objects.all()
    arrayOfNames = []
    for name in list(names):
        arrayOfNames.append(name.companyName)
    return JsonResponse(arrayOfNames, safe=False)

def analyzerTypes(request):
    max = request.GET.get('max')
    actmax = CompanyName.objects.get(companyName = max)
    compuni = CompanyUnits.objects.filter(companyName1_id = actmax.id)
    arrayOfNames = []
    for name in list(compuni):
        arrayOfNames.append(name.modelOfAnalyzer)
    return JsonResponse(arrayOfNames, safe=False)

def nameOfItem(request):
    max = request.GET.get('max')
    max1 = request.GET.get('max1')
    actmax1 = CompanyName.objects.get(companyName = max1)
    actmax = CompanyUnits.objects.get(Q(modelOfAnalyzer = max)&Q(companyName1_id = actmax1.id))
    compuni = WorkFlow.objects.filter(Q(companyAnalyzers_id = actmax.id)&Q(companyName_id = actmax1.id))
    arrayOfNames = []
    for name in list(compuni):
        arrayOfNames.append(name.nameOfWorkFlow)
    return JsonResponse(arrayOfNames, safe=False)

@login_required
def signup(request):

    if request.method == "POST" :
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        myuser = User.objects.create_user(username, email , pass1  )
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        messages.success(request,"Your Account has been successfully created .\n we have sent you a confermation email")


        # welcome message
        subject = "welcome to omars world"
        message = "hello"+myuser.first_name+"!\n"+"welcome to our transition company\n thank you for visiting our website \n\n thank you \n\n Omae Eldebeis"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect('/')
    return render(request,"octopus-master/octopus/pages-signup.html")

def signout1(request):
    logout(request)
    messages.success(request,"logged out successfuly")
    return redirect('/pages-signin.html')

def signinPage(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        try:
            curuser = User.objects.get(username=username)
            seluser = Profile.objects.get(user=curuser)
            user = authenticate(username=username,password=pass1)
            if user :
                login(request,user)
                if seluser.role.cond == 4 :
                    return redirect('/importsystem/')
                else:
                    return redirect('/')
            
        except:
            messages.error(request,"The Username or Password is not correct. please try again")
            return redirect('/accounts/login/?next=/')
    return render(request, 'octopus-master/octopus/pages-signin.html')

def getItemName(request):
    try:
        parto = request.GET.get('partnumber')
        getname = ItemInput.objects.get(partNumber=parto)
        getprice = Price.objects.get(partNumber=parto)
        arr=[]
        print(getname.nameOfItem)
        arr.append(getname.nameOfItem)
        arr.append(getprice.Price)
        
        return JsonResponse(arr, safe=False)
    except:
        arr=[]
        x = "there is no Item with this J Number"        
        arr.append(x)
        return JsonResponse(arr, safe=False)

@login_required
def myProfile(request):
    userId = request.user
    userStaff = userId.is_superuser   
    return render(request, 'octopus-master/octopus/pages-my-profile.html', {'userStaff':userStaff})

@login_required
def PriceList(request):
    userId = request.user
    userStaff = userId.is_superuser
    allInvo = Price.objects.all()   
    return render(request, 'octopus-master/octopus/pages-price-list.html', {'userStaff':userStaff , 'allInvo':allInvo})

def Namee(request):
    parto = request.GET.get('partnumber')

    namo = ItemInput.objects.get(partNumber=parto)
    actname = namo.nameOfItem
    return JsonResponse(actname, safe=False)

def priceJson(request):
    Items = Price.objects.all()
    print(Items)
    data =[Item.get_price() for Item in Items]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

def assemJson(request):
    Items = BookStore.objects.all()
    print(Items)
    data =[Item.get_assem() for Item in Items]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

def assemJson1(request):
    selInv = InvoiceStatus.objects.get(Status="FOC")
    Items = AssembledStore.objects.filter(Invo=selInv)

    data =[Item.get_assem() for Item in Items]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

def GetPrice(request):
    parto = request.GET.get('partnumber')
    
    namo = Price.objects.get(partNumber=parto)
    actPrice = namo.Price
    return JsonResponse(actPrice, safe=False)

def Notifactions(request):
    invid = InvoiceStatus.objects.get(Status="Pending")
    allInvo = AssembledStore.objects.filter(Invo_id=invid.id).count()
    AssemName = AssembledStore.objects.filter(Invo_id=invid.id)
    arr =[]
    for name in list(AssemName):
        arr.append(name.HosName.hospitalName)
        arr.append(name.ItemName)
        arr.append(name.Dato)
        arr.append(name.Price)
    response = {
            'allInvo': allInvo,
            'AssemName': arr,

        }
    return JsonResponse(response, safe=False)

@login_required
def OrganizationName(request):

    if request.method == "POST":
        OrganizName = request.POST['Organize_Item']
    
        newform = OrganizeName.objects.create(
            organizeName = OrganizName
        )
        newform.save()
        return HttpResponseRedirect('/Orgazine-Name.html')

    return render(request, 'octopus-master/octopus/Orgazine-Name.html')

def getOrganize(request):
    names = OrganizeName.objects.all()
    arrayOfNames = []
    for name in list(names):
        arrayOfNames.append(name.organizeName)
    return JsonResponse(arrayOfNames, safe=False)

@login_required
def ParameteName(request):

    if request.method == "POST":
        ParameteName = request.POST['Parameter_Item']
        compName = request.POST['companyName_Item']
        typeOfAna = request.POST['typeOfAnalyzer_Item']
        

        compnam = CompanyName.objects.get(companyName = compName)
        typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typeOfAna)&Q(companyName1=compnam.id))

        newform = ParameterName.objects.create(
            ParameterNam = ParameteName,
            Item_Model_compName = compnam,
            Item_Model_compUnit = typeOfana,
        )
        newform.save()
        return HttpResponseRedirect('/parameter-Name.html')

    return render(request, 'octopus-master/octopus/parameter-Name.html')

def CatNum(request):
    
    if request.method == "POST":
        ParameteName = request.POST['Parameter_Item']
        compName = request.POST['companyName_Item']
        typeOfAna = request.POST['typeOfAnalyzer_Item']
        CarNo = request.POST['catNumber_Item']
        slideNo = request.POST['slide_Item']
        Cal = request.POST['Calibrator_Item']
        prico = request.POST['Price_Item']
        shippingcond = request.POST['shipping_Item']

        compnam = CompanyName.objects.get(companyName = compName)
        typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typeOfAna)&Q(companyName1=compnam.id))
        ParName = ParameterName.objects.get(ParameterNam = ParameteName)

        newform = ReagentQTY.objects.create(
            ParName = ParName,
            Item_Model_compName = compnam,
            Item_Model_compUnit = typeOfana,
            CatNumber = CarNo,
            slideNumber = slideNo,
            Price = prico,
            ShippindCond=shippingcond,
        )
        newform.save()
        new1form = Calibrator.objects.create(
            ParName = ParName,
            Item_Model_compName = compnam,
            Item_Model_compUnit = typeOfana,
            Cal=Cal,
        )
        new1form.save()
        return HttpResponseRedirect('/parameter-cat.html')

    return render(request, 'octopus-master/octopus/parameter-cat.html')

def getcatNo(request):
    uni = request.GET.get('typana')
    compnam1 = request.GET.get('max')

    comp = CompanyName.objects.get(companyName = compnam1)
    print(comp.id)
    copmID = comp.id
    print(uni)
    print(uni)

    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = uni)&Q(companyName1_id=copmID))
    print(typeOfana)
    names = ParameterName.objects.filter(Q(Item_Model_compName=comp)&Q(Item_Model_compUnit=typeOfana))
    arrayOfNames = []
    for name in list(names):
        arrayOfNames.append(name.ParameterNam)
    return JsonResponse(arrayOfNames, safe=False)

def getParameter(request):
    uni = request.GET.get('unit')
    compnam = request.GET.get('compname')
    compname = CompanyName.objects.get(companyName = compnam)
    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = uni)&Q(companyName1=compname.id))
    
    names = ParameterName.objects.filter(Q(Item_Model_compName=compname)&Q(Item_Model_compUnit=typeOfana))
    print(names)
    arrayOfNames = []
    for name in list(names):
        arrayOfNames.append(name.ParameterNam)
    return JsonResponse(arrayOfNames, safe=False)

def checkDouplicatePara(request):
    orderNumber = request.GET.get('ordNum')
    ElemName = request.GET.get('ElementName')

    selectOrder = ElementCreation.objects.filter(Q(orderNum=orderNumber)&Q(ElementName__ParameterNam=ElemName)).exists()
    if selectOrder:
        message = 'This Item Is Already Exist'
        return JsonResponse(message, safe=False)

@login_required
def CreateOrder(request):
   
    return render(request, 'octopus-master/octopus/pages-create-order.html')

def SaveOrders(request):
    orgNam = request.GET.get('orgNam')
    compNam = request.GET.get('compNam')
    typAna = request.GET.get('typAna')
    ordNum = request.GET.get('ordNum')
    ordDat = request.GET.get('ordDat')
    ordNot = request.GET.get('ordNot')
    
    orgnam = OrganizeName.objects.get(organizeName=orgNam)
    compnam = CompanyName.objects.get(companyName = compNam)
    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typAna)&Q(companyName1=compnam.id))

    newform = OraderCreation.objects.create(
        OrganizeNam = orgnam,
        Item_Model_compName = compnam,
        Item_Model_compUnit = typeOfana,
        dat = ordDat,
        Note = ordNot,
        status = "Pending",
        orderNum= ordNum,
    )
    newform.save()
    return JsonResponse(ordNum, safe=False)

def SavelementOrder(request):
    eleNam = request.GET.get('eleNam')
    compNam = request.GET.get('compNam')
    typAna = request.GET.get('typAna')
    ordNum = request.GET.get('ordNum')
    ordDat = request.GET.get('ordDat')
    ordNot = request.GET.get('ordNot')
    ordqty = request.GET.get('ordqty')
    catno = request.GET.get('CatNum')
    SlidesQTY = request.GET.get('SlidesQTY')
    
    cat = ReagentQTY.objects.get(CatNumber = catno)
    ele = ParameterName.objects.get(ParameterNam = eleNam)
    compnam = CompanyName.objects.get(companyName = compNam)
    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typAna)&Q(companyName1=compnam.id))

    newform = ElementCreation.objects.create(
        QTY=ordqty,
        ElementName = ele,
        Item_Model_compName = compnam,
        Item_Model_compUnit = typeOfana,
        dat = ordDat,
        Note = ordNot,
        status = "Pending",
        orderNum= ordNum,
        CatNumber=cat,
        SlidesQTY = SlidesQTY,
    )
    newform.save()
    return JsonResponse(ordNum, safe=False)

def ShowOrder(request):
    
    return render(request, 'octopus-master/octopus/pages-show-order.html')

def getOreders(request):
    allOrders = OraderCreation.objects.all()

    arrayOfNames = []
    for name in list(allOrders):
        arrayOfNames.append(name.OrganizeNam.organizeName)
        arrayOfNames.append(name.orderNum)
        arrayOfNames.append(name.Item_Model_compName.companyName)
        arrayOfNames.append(name.Item_Model_compUnit.modelOfAnalyzer)
        
        arrayOfNames.append(name.dat)
        arrayOfNames.append(name.Note)
        arrayOfNames.append(name.status)

    return JsonResponse(arrayOfNames, safe=False)

def CheckOrderNum(request):
    searchval = request.GET.get('searchVal')
    print(searchval)
    arwa = OraderCreation.objects.filter(orderNum__iexact=searchval).exists()
    if arwa:
        message = "this is aleardy taken"
        print(message)
        return JsonResponse(message, safe=False)

def getOrderElements(request):
    ordernum = request.GET.get('itemId')

    getOrders = ElementCreation.objects.filter(orderNum=ordernum)
    print(getOrders)
    arr =[]
    for order in list(getOrders):
        arr.append(order.ElementName.ParameterNam)
        arr.append(order.Item_Model_compName.companyName)
        arr.append(order.Item_Model_compUnit.modelOfAnalyzer)
        arr.append(order.orderNum)
        arr.append(order.dat)
        arr.append(order.QTY)
        arr.append(order.status)
        arr.append(order.Note)
        arr.append(order.ElementName.id)

    return JsonResponse(arr, safe=False)

def SavconnfOrder1(request):
    eleNam = request.GET.get('eleNam')
    compNam = request.GET.get('compNam')
    typAna = request.GET.get('typAna')
    ordNum = request.GET.get('ordNum')
    ordDat = request.GET.get('ordDat')
    ordNot = request.GET.get('ordNot')
    ordqty = request.GET.get('ordqty')
    catNumslide = request.GET.get('result')
    expdate = request.GET.get('expdate')
    slideqty = request.GET.get('slideqty')
    statusval = request.GET.get('statu')
    confnum = request.GET.get('confnum')
 
    ele = ParameterName.objects.get(ParameterNam = eleNam)
    cat = ReagentQTY.objects.get(Q(ParName=ele)&Q(slideNumber=catNumslide))


    compnam = CompanyName.objects.get(companyName = compNam)
    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typAna)&Q(companyName1=compnam.id))
    newform = ElementConfermation.objects.create(
        QTY=ordqty,
        ElementName = ele,
        Item_Model_compName = compnam,
        Item_Model_compUnit = typeOfana,
        dat = ordDat,
        Note = ordNot,
        status = statusval,
        orderNum= ordNum,
        CatNumber= cat,
        ExpiryDate= expdate,
        SlidesQTY= slideqty,
        ConfNum=confnum,
    )
    
    return JsonResponse(ordNum, safe=False)

def CheckOrderNum2(request):
    searchval = request.GET.get('searchVal')
    selectOptions = ElementCreation.objects.filter(orderNum=searchval)
    arr =[]
    for option in list(selectOptions):
        if option.QTY != 0:
            arr.append(option.ElementName.ParameterNam)
    print(arr)
    return JsonResponse(arr, safe=False)

def getcatnum(request):
    eleNam = request.GET.get('eleNam')
    ordNum = request.GET.get('ordNum')
    ele = ParameterName.objects.get(ParameterNam = eleNam)
    selectOptions = ElementCreation.objects.filter(Q(orderNum=ordNum)&Q(ElementName=ele))
    arr = []
    for n in list(selectOptions):
        arr.append(n.CatNumber.CatNumber)
    
    return JsonResponse(arr, safe=False)

def CheckelementNum2(request):
    eleNam = request.GET.get('eleNam')
    ordNum = request.GET.get('ordNum')
    eleNum = request.GET.get('eleNum')
    eleNumbers = ReagentQTY.objects.get(CatNumber = eleNum)
    ele = ParameterName.objects.get(ParameterNam = eleNam)
    selectOptions = ElementCreation.objects.get(Q(orderNum=ordNum)&Q(ElementName=ele)&Q(CatNumber=eleNumbers))
    number = selectOptions.QTY
    number1 = selectOptions.SlidesQTY
    response = {
        'number':number,
        'number1':number1,
    }
    return JsonResponse(response, safe=False)

def UpdateOrderQTy(request):
    requestedQTY = request.GET.get('searchVal')
    ordNum = request.GET.get('ordNum')
    eleNum = request.GET.get('eleNum')
    slidesnum = request.GET.get('slidesnum')
    sta = request.GET.get('statusacpt')

    if sta == "Accepted" :
        actname = ParameterName.objects.get(ParameterNam=eleNum)
        selectOptions = ElementCreation.objects.get(Q(orderNum=ordNum)&Q(ElementName=actname.id))
        newval = int(selectOptions.QTY) - int(requestedQTY)
        slidesval = int(selectOptions.SlidesQTY) - int(slidesnum)    
        
        if newval == 0:
            ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval)
            ElementCreation.objects.filter(pk=selectOptions.id).update(status="OK")
        elif newval != 0:
            ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval)
        
        is_taken = ElementCreation.objects.filter(Q(orderNum=ordNum)&Q(status__iexact="Pending")).exists()
        data = {'is_taken': is_taken}
        if is_taken == False:
            actname = OraderCreation.objects.get(orderNum=ordNum)
            OraderCreation.objects.filter(pk=actname.id).update(status="OK")
        return JsonResponse(newval, safe=False)
    else:
        return JsonResponse(sta, safe=False)
    
def confJson(request):
    elementName  = request.GET.get('val')
    ordNum = request.GET.get('val1')

    actname = ParameterName.objects.get(id=elementName)
    selectOptions = ElementConfermation.objects.filter(Q(orderNum=ordNum)&Q(ElementName=actname))
    print("MOHA")
    print("MOHA")
    print("MOHA")
    print("MOHA")
    data =[Item.get_conf() for Item in selectOptions]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

@login_required
def homeReagent(request):
    userOmar = request.user
    userStaff = userOmar.is_superuser
    if userStaff:
        return render(request, 'secproj/index.html',{'userStaff':userStaff})
    else:
        return render(request, 'secproj/index.html')


def pardata(request):
    itemName = request.GET.get('itemName')
    print(itemName)
    itname = ParameterName.objects.get(ParameterNam=itemName)
    print(itname)
    orders = ElementCreation.objects.filter(ElementName=itname)

    data =[Item.get_elem() for Item in orders]

    response = {'data':data}
    return JsonResponse(response,safe=False)

def confdata(request):
    itemName = request.GET.get('itemName')
    print(itemName)
    itname = ParameterName.objects.get(ParameterNam=itemName)
    print(itname)
    orders = ElementConfermation.objects.filter(ElementName=itname)

    data =[Item.get_conf() for Item in orders]

    response = {'data':data}
    return JsonResponse(response,safe=False)

def checkcat(request):

    compn = request.GET.get('compNam')
    itemname = request.GET.get('eleNam')

    itname = ParameterName.objects.get(ParameterNam=itemname)
    coname = CompanyName.objects.get(companyName=compn)

    datas = ReagentQTY.objects.filter(Q(Item_Model_compName=coname)&Q(ParName=itname))
    
    arr =[]
    for data in list(datas):
        arr.append(data.CatNumber)
        arr.append(data.slideNumber)

    return JsonResponse(arr,safe=False)

def checkcatQty(request):

    compn = request.GET.get('catval')

    catalog = ReagentQTY.objects.get(CatNumber=compn)
    num = catalog.slideNumber

    return JsonResponse(num,safe=False)

def getcompanies(request):
    ord = request.GET.get('ordernum')
    selectord = OraderCreation.objects.filter(orderNum=ord)
    arr = []
    for option in list(selectord):
        arr.append(option.Item_Model_compName.companyName)
        arr.append(option.Item_Model_compUnit.modelOfAnalyzer)

    return JsonResponse(arr,safe=False)

def checkOrderNumdate(request):
    curYear = request.GET.get('yyyy')
    curMonth = request.GET.get('mm')
    xc = OraderCreation.objects.filter(Q(dat__month =curMonth)&Q(dat__year = curYear) )
    
    if xc :
        arr = []
        j = 0
        for x in list(xc):
            if str(x.dat.month).zfill(2) == curMonth:
                arr.append(x.orderNum)
                j=j+1
            arr.sort()
            newOrderNum = int(arr[j-1]) + 1
            print(newOrderNum)
        else:
            newOrderNum = str(curYear) + str(curMonth) + str(1).zfill(2)
        

        return JsonResponse(newOrderNum,safe=False)
    else:
        newOrderNum = str(curYear)+ str(curMonth)+str(1).zfill(2)
        return JsonResponse(newOrderNum,safe=False)

def CreateConNum(request):
    ordNumber = request.GET.get('ordNum')
    actorders = ElementConfermation.objects.filter(orderNum=ordNumber)
    if actorders :
        arr=[]
        j=0
        for n in list(actorders):
            arr.append(n.ConfNum)
            j=j+1

        arr.sort()
        newConfNum = int(arr[j-1])+1 
        return JsonResponse(newConfNum,safe=False)
    else:
        newConfNum = str(ordNumber)+str(1).zfill(2)
        print(newConfNum)
        return JsonResponse(newConfNum,safe=False)

def SavInvoOrder(request):
    compNam = request.GET.get('compNam')
    typAna = request.GET.get('typAna')
    ordNum = request.GET.get('ordNum')
    ordDat = request.GET.get('ordDat')
    InvNum = request.GET.get('InvNum')
    InvPrice = request.GET.get('Price')
    confNumber = request.GET.get('confNumber')
    catalogNum = request.GET.get('catalogNum')
    ItemNameItem = request.GET.get('ItemNameItem')
    CatNumberItem = request.GET.get('CatNumberItem')
    QTYItem = request.GET.get('QTYItem')
    QTYSlidesItem = request.GET.get('QTYSlidesItem')

    ord1 = OrderInvoice.objects.filter(InvoiceNumber=InvNum).exists() 
    
    cat = ReagentQTY.objects.get(CatNumber=catalogNum)
    compnam = CompanyName.objects.get(companyName = compNam)
    confNumber1 = ElementConfermation.objects.get(ConfNum = confNumber)

    ele = ParameterName.objects.get(ParameterNam = confNumber1.ElementName)
    # cal = Calibrator.objects.get(ParName = ele)

    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typAna)&Q(companyName1=compnam.id))

    newform = OrderInvoice.objects.create(
        Item_Model_compName = compnam,
        Item_Model_compUnit = typeOfana,
        dat = ordDat,
        orderNum= ordNum,
        Price=InvPrice,
        orderConfermation=confNumber,
        InvoiceNumber=InvNum,

    )
    newform.save()
    autoinvo = AutoOrderInvoice.objects.get(orderConfermation = confNumber)
    autoinvo.delete()
      
    if ord1 == True:
        
        return JsonResponse(ordNum, safe=False)
    else:
        ord = OrderInvoice.objects.get(InvoiceNumber=InvNum)
        new1form = Shipping.objects.create(
            PO=ordNum,
            InvNumber = ord,
            Item_Model_compName = compnam,
            Item_Model_compUnit = typeOfana,
            ShippingCond=cat.ShippindCond,
        )
        new1form.save()
        return JsonResponse(ordNum, safe=False)

def SavconnfOrder(request):
    compNam = request.GET.get('compNam')
    typAna = request.GET.get('typAna')
    ordNum = request.GET.get('ordNum')
    ordDat = request.GET.get('ordDat')
    InvNum = request.GET.get('InvNum')
    InvPrice = request.GET.get('Price')
    confNumber = request.GET.get('confNumber')

    ItemNameItem = request.GET.get('ItemNameItem')
    CatNumberItem = request.GET.get('CatNumberItem')
    QTYItem = request.GET.get('QTYItem')
    QTYSlidesItem = request.GET.get('QTYSlidesItem')

    ord1 = OrderInvoice.objects.filter(InvoiceNumber=InvNum).exists()
    

    compnam = CompanyName.objects.get(companyName = compNam)
    confNumber1 = ElementConfermation.objects.get(ConfNum = confNumber)

    ele = ParameterName.objects.get(ParameterNam = confNumber1.ElementName)
    cat = ReagentQTY.objects.get(Q(ParName=ele)&Q(CatNumber=confNumber1.CatNumber))
    cal = Calibrator.objects.get(ParName = ele)

    typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = typAna)&Q(companyName1=compnam.id))

    newform = AutoOrderInvoice.objects.create(
        QTY=QTYItem,
        SlidesQTY=QTYSlidesItem,
        CatNumber=CatNumberItem,
        ElementName=ItemNameItem,
        Item_Model_compName = compnam,
        Item_Model_compUnit = typeOfana,
        dat = ordDat,
        orderNum= ordNum,
        Price=InvPrice,
        orderConfermation=confNumber,
        InvoiceNumber=InvNum,

    )
    newform.save()
    #                      omar mn hena elmoshkla f elshipping condition 

    if ord1 == True:
        return JsonResponse(ordNum, safe=False)
    else:
        ord = OrderInvoice.objects.get(InvoiceNumber=InvNum)
        new1form = Shipping.objects.create(
            PO=ordNum,
            InvNumber = ord,
            Item_Model_compName = compnam,
            Item_Model_compUnit = typeOfana,
            ShippingCond = cat.ShippindCond ,
        )
        new1form.save()
    return JsonResponse(ordNum, safe=False)

def getAllConf(request):
    orders = request.GET.get('itemId')
    confs = ElementConfermation.objects.filter(Q(orderNum=orders)&Q(status="Accepted"))
    arr = []
    data2 = []
    for conf in list(confs):
        reagent = ReagentQTY.objects.get(CatNumber=conf.CatNumber)
        arr.append(conf.SlidesQTY)
        data2.append(float(conf.QTY)*float(reagent.Price))
    sumOfArr = sum(arr)
    sumOfData = sum(data2)
    empty = {'dat':'','orderNum': '','ConfNum':'' ,'Item_Model_compName': '','ElementName': '','CatNumber': '','BatchNumber': '', 'ExpiryDate': '','QTY': '','SlidesQTY':''}
    addition = {'dat':'','orderNum': '' ,'ConfNum':'','Item_Model_compName': '','ElementName': '','CatNumber': '','BatchNumber': '', 'ExpiryDate': 'Total No. Of Tests','QTY': '','SlidesQTY':sumOfArr}
    multi1 = {'dat':'','orderNum': '','ConfNum':'' ,'Item_Model_compName': '','ElementName': '','CatNumber': '','BatchNumber': '', 'ExpiryDate': 'Total Price','QTY': '','SlidesQTY':sumOfData}

   
    data1 =[Item.get_conf() for Item in confs]
    data1.append(empty)
    data1.append(addition)
    data1.append(multi1)
    response1 = {'data1':data1}
    return JsonResponse(response1,safe=False)

def getdates(request):
    dato = request.GET.get('dateval')
    ElementNumber =request.GET.get('ElementNumber2')
    getCat = ReagentQTY.objects.get(CatNumber=ElementNumber)
    experiment = ElementConfermation.objects.filter(Q(ExpiryDate__gte=dato)&Q(CatNumber=getCat))
    print(experiment)
    arr=[]
    if experiment:
        for n in list(experiment):
            arr.append(n.orderNum)
            arr.append(n.ExpiryDate)
        return JsonResponse(arr,safe=False)
    else:
        return JsonResponse(arr,safe=False)

def showPrices(request):
    confNumber = request.GET.get('confNum')

    selectOrderConf = ElementConfermation.objects.get(ConfNum=confNumber)
    selectReagent = ReagentQTY.objects.get(CatNumber=selectOrderConf.CatNumber)

    curPrice = float(selectReagent.Price) * float(selectOrderConf.QTY)

    return JsonResponse(curPrice,safe=False)

@login_required
def ConfInvoice(request):
    

    return render(request, 'octopus-master/octopus/pages-show-invoices.html')

def invTable(request):
    ordnum = request.GET.get('ordnumber')
    print(ordnum)
    confs = OrderInvoice.objects.filter(orderNum=ordnum)

    for n in list(confs):
        data =[Item.get_OrderInvoice() for Item in confs]

        response1 = {'data':data}
    return JsonResponse(response1,safe=False)

def progressTable(request):

    confs = Shipping.objects.all()

    data =[Item.get_shipping() for Item in confs]

    response = {'data':data}
    return JsonResponse(response,safe=False)

def iteminInvoice(request):
    ordNumber = request.GET.get('da')
    invoiceNumber = request.GET.get('invda')
    arr=[]
    selparameter = OrderInvoice.objects.filter(Q(orderNum=ordNumber)&Q(InvoiceNumber=invoiceNumber))
    arr.clear()
    for n in list(selparameter):
        selitem = ElementConfermation.objects.get(ConfNum=n.orderConfermation)
        arr.append(selitem.ElementName.ParameterNam)
    return JsonResponse(arr,safe=False)

def editship(request):
    ship_id = request.GET.get('da_id')
    ordNumber = request.GET.get('da')
    importval = request.GET.get('importval')
    print(importval)
    print(importval)
    if importval == "":
        importval = ""

    OkToShipval = request.GET.get('OkToShipval')

    if OkToShipval == "":
        OkToShipval = ""

    shipval = request.GET.get('shipval')

    if shipval == "":
        shipval = ""

    shipcondval = request.GET.get('shipcondval')

    if shipcondval == "":
        shipcondval = ""

    arrivdateval = request.GET.get('arrivdateval')
    if arrivdateval == "":
        arrivdateval = ""

    EDAdatval = request.GET.get('EDAdatval')
    if EDAdatval == "":
        EDAdatval = ""

    techval = request.GET.get('techval')
    if techval == "":
        techval = ""

    edareleaseval = request.GET.get('edareleaseval')
    if edareleaseval == "":
        edareleaseval = ""

    Shipping.objects.filter(id=ship_id).update(ImportApproval= importval,OkToShip=OkToShipval ,ShippingDate= shipval,ShippingCond=shipcondval ,
                                                 ArrivalDate= arrivdateval,EDADate=EDAdatval ,TechDate=techval ,EDAReleaseDate= edareleaseval)

    
    return JsonResponse(ordNumber,safe=False)

def orderExcels(request):
    GetOrder = OraderCreation.objects.all()
    arr=[]
    for n in list(GetOrder):
        arr.append(n.orderNum)
    
    return JsonResponse(arr,safe=False)

def excelbtns(request):
    orderNumber = request.GET.get('excOrdNum')
    selOrder = OraderCreation.objects.get(orderNum=orderNumber)
    excels = ExcelFile.objects.filter(ordnum=selOrder)
    
    exc = []
    for m in list(excels):
        exc.append(m.file.url)
        exc.append(m.pk)
        print(exc)

    response = {'exc':exc }
    return JsonResponse(response,safe=False)

def exceldatatable(request):
    excelpk = request.GET.get('excpk')
    confs = Autoconfdata.objects.filter(excfile=excelpk)
    
    
    for n in list(confs):
        data =[Item.get_Autoconf() for Item in confs]

        response = {'data':data}
    return JsonResponse(response,safe=False)

def collectinfo(request):
    ordnum = request.GET.get('ordNumber') 
    catnumber = request.GET.get('matrial')
    confqty = request.GET.get('confqty')

    try:
        selcetReagent = ReagentQTY.objects.get(CatNumber=catnumber)
        itemConf = ElementCreation.objects.get(Q(orderNum=ordnum)&Q(CatNumber=selcetReagent))

        remainingqty = (itemConf.QTY) - float(confqty)
        respone={
            'remainingqty':remainingqty
        }
        return JsonResponse(respone,safe=False)
    except:
        messa = "Fas"
        respone={
            'messa':messa
        }
        return JsonResponse(respone,safe=False)

def saveExcelToConf(request):
    selectedQTY = request.GET.get('selectedQTY')
    orderNumber = request.GET.get('ordNumber')
    matrial = request.GET.get('matrial')
    batchnumber = request.GET.get('batchnumber')
    expirydate = request.GET.get('expirydate')
    confqty = request.GET.get('confqty')
    price = request.GET.get('price')
    netval = request.GET.get('netval')
    status = "Accepted"

    matrialNumber = ReagentQTY.objects.get(CatNumber=matrial)
    elementName = ParameterName.objects.get(id=matrialNumber.ParName_id)
    actorders = ElementConfermation.objects.filter(orderNum=orderNumber)
    selCompany = CompanyName.objects.get(companyName=matrialNumber.Item_Model_compName)
    seluni = CompanyUnits.objects.get(Q(modelOfAnalyzer=matrialNumber.Item_Model_compUnit)&Q(companyName1=selCompany))

    if actorders :
        arr=[]
        j=0
        for n in list(actorders):
            arr.append(n.ConfNum)
            j=j+1

        arr.sort()
        newConfNum = int(arr[j-1])+1 
    else:
        newConfNum = str(orderNumber)+str(1).zfill(2)
    if selectedQTY == "":
        QTYInSlides = int(matrialNumber.slideNumber) * float(confqty)

        if status == "Accepted" :
            actname = ParameterName.objects.get(id=matrialNumber.ParName_id)
            selectOptions = ElementCreation.objects.get(Q(orderNum=orderNumber)&Q(ElementName=actname.id))
            newval = int(selectOptions.QTY) - float(confqty)
            slidesval = int(selectOptions.SlidesQTY) - int(QTYInSlides)    
            if newval < 0 :
                message = ("Not Enough QTY")
                return JsonResponse(message, safe=False)
            if newval == 0:
                ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval,status="OK")

                obj = ElementConfermation.objects.create(
                    QTY=confqty,
                    dat=date.today(),
                    status="Accepted",
                    BatchNumber=batchnumber,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ConfNum=newConfNum,
                    CatNumber=matrialNumber,
                    ExpiryDate=expirydate,
                    ElementName=elementName,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                )
                
                obj.save()


                obj1 = AutoOrderInvoice.objects.create(
                    dat=date.today(),
                    QTY=confqty,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ElementName=elementName,
                    orderConfermation=newConfNum,
                    CatNumber=matrialNumber,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                    Price=netval,
                )
                
                obj1.save()
            elif newval > 0:
                ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval)

                obj = ElementConfermation.objects.create(
                    QTY=confqty,
                    dat=date.today(),
                    status="Accepted",
                    BatchNumber=batchnumber,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ConfNum=newConfNum,
                    CatNumber=matrialNumber,
                    ExpiryDate=expirydate,
                    ElementName=elementName,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                )
                
                obj.save()


                obj2 = AutoOrderInvoice.objects.create(
                    dat=date.today(),
                    QTY=confqty,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ElementName=elementName,
                    orderConfermation=newConfNum,
                    CatNumber=matrialNumber,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                    Price=netval,
                )
                
                obj2.save()
            is_taken = ElementCreation.objects.filter(Q(orderNum=orderNumber)&Q(status__iexact="Pending")).exists()

            if is_taken == False:
                actname = OraderCreation.objects.get(orderNum=orderNumber)
                OraderCreation.objects.filter(pk=actname.id).update(status="OK")

            seldeleted = Autoconfdata.objects.get(BatchNum=batchnumber)
            seldeleted.delete()    
    
    
    if selectedQTY != "":
        QTYInSlides = int(matrialNumber.slideNumber) * float(confqty)

        if status == "Accepted" :
            actname = ParameterName.objects.get(id=matrialNumber.ParName_id)
            selectOptions = ElementCreation.objects.get(Q(orderNum=orderNumber)&Q(ElementName=actname.id))
            newval = int(selectOptions.QTY) - int(selectedQTY)
            slidesval = int(selectOptions.SlidesQTY) - int(QTYInSlides)    
            if newval < 0 :
                message = ("Not Enough QTY")
                return JsonResponse(message, safe=False)
            if newval == 0:
                ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval,status="OK")

                obj = ElementConfermation.objects.create(
                    QTY=selectedQTY,
                    dat=date.today(),
                    status="Accepted",
                    BatchNumber=batchnumber,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ConfNum=newConfNum,
                    CatNumber=matrialNumber,
                    ExpiryDate=expirydate,
                    ElementName=elementName,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                )
                
                obj.save()


                obj1 = AutoOrderInvoice.objects.create(
                    dat=date.today(),
                    QTY=selectedQTY,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ElementName=elementName,
                    orderConfermation=newConfNum,
                    CatNumber=matrialNumber,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                    Price=netval,
                )
                
                obj1.save()
            elif newval > 0:
                ElementCreation.objects.filter(pk=selectOptions.id).update(QTY=newval,SlidesQTY=slidesval)

                obj = ElementConfermation.objects.create(
                    QTY=selectedQTY,
                    dat=date.today(),
                    status="Accepted",
                    BatchNumber=batchnumber,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ConfNum=newConfNum,
                    CatNumber=matrialNumber,
                    ExpiryDate=expirydate,
                    ElementName=elementName,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                )
                
                obj.save()


                obj2 = AutoOrderInvoice.objects.create(
                    dat=date.today(),
                    QTY=selectedQTY,
                    SlidesQTY=QTYInSlides,
                    orderNum=orderNumber,
                    ElementName=elementName,
                    orderConfermation=newConfNum,
                    CatNumber=matrialNumber,
                    Item_Model_compName=selCompany,
                    Item_Model_compUnit=seluni,
                    Price=netval,
                )
                
                obj2.save()
            is_taken = ElementCreation.objects.filter(Q(orderNum=orderNumber)&Q(status__iexact="Pending")).exists()

            if is_taken == False:
                actname = OraderCreation.objects.get(orderNum=orderNumber)
                OraderCreation.objects.filter(pk=actname.id).update(status="OK")

            seldeleted = Autoconfdata.objects.get(BatchNum=batchnumber)
            seldeleted.delete()   
  
def cancelExcelToConf(request):
    orderNumber = request.GET.get('ordNumber')
    # po = request.GET.get('po')
    matrial = request.GET.get('matrial')
    batchnumber = request.GET.get('batchnumber')
    expirydate = request.GET.get('expirydate')
    confqty = request.GET.get('confqty')
    price = request.GET.get('price')
    netval = request.GET.get('netval')
    status = "Rejected"

    matrialNumber = ReagentQTY.objects.get(CatNumber=matrial)
    elementName = ParameterName.objects.get(ParameterNam=matrialNumber.ParName)
    actorders = ElementConfermation.objects.filter(orderNum=orderNumber)
    selCompany = CompanyName.objects.get(companyName=matrialNumber.Item_Model_compName)
    seluni = CompanyUnits.objects.get(Q(modelOfAnalyzer=matrialNumber.Item_Model_compUnit)&Q(companyName1=selCompany))

    if actorders :
        arr=[]
        j=0
        for n in list(actorders):
            arr.append(n.ConfNum)
            j=j+1

        arr.sort()
        print(arr[j-1])
        newConfNum = int(arr[j-1])+1 
        print(newConfNum)
    else:
        newConfNum = str(orderNumber)+str(1).zfill(2)
        print(newConfNum)


    obj = ElementConfermation.objects.create(
        QTY=confqty,
        dat=date.today(),
        status="Rejected",
        SlidesQTY=confqty,
        orderNum=orderNumber,
        ConfNum=newConfNum,
        CatNumber=matrialNumber,
        ExpiryDate=expirydate,
        ElementName=elementName,
        Item_Model_compName=selCompany,
        Item_Model_compUnit=seluni,
    )
    obj.save()
    
    seldeleted = Autoconfdata.objects.get(BatchNum=batchnumber)
    seldeleted.delete()
    return JsonResponse(status, safe=False)

def checkShippingCond(request):
    ordNumber = request.GET.get('ordNum')

    selectConfermations = ElementConfermation.objects.filter(Q(orderNum=ordNumber)& Q(status="Accepted"))
    refri = []
    freez = []
    normalTemp = []
    for n in list(selectConfermations):
        is_taken = OrderInvoice.objects.filter(orderConfermation=n.ConfNum).exists()
        if is_taken == False:
            cond = ReagentQTY.objects.filter(CatNumber = n.CatNumber)        
            for m in list(cond):
                print(m.ShippindCond)
                if m.ShippindCond == "Refrigrated":
                    refri.append(n.ConfNum)
                elif m.ShippindCond == "Frozen":
                    freez.append(n.ConfNum)
                elif m.ShippindCond == "Normal Temperture":
                    normalTemp.append(n.ConfNum)

    response = {
        'refri':refri,
        'freez':freez,
        'normalTemp':normalTemp,
    }
    print(response)
    return JsonResponse(response, safe=False)

def InvoiceData(request):
    orderNumber = request.GET.get('ordernum')
    confNumber = request.GET.get('confNum')
    arr =[]
    selcof = ElementConfermation.objects.get(Q(orderNum=orderNumber)& Q(ConfNum=confNumber))
    # for n in list(selcof):
    arr.append(selcof.ElementName.ParameterNam)
    arr.append(selcof.CatNumber.CatNumber)
    arr.append(selcof.QTY)
    arr.append(selcof.SlidesQTY)
    return JsonResponse(arr, safe=False)

def getAutoconf(request):
    getAllAutoConf = Autoconfdata.objects.all()
    arr=[]
    for n in list(getAllAutoConf):
        arr.append(n.OrderNumber)
        arr.append(n.matrial)
        arr.append(n.MatDesc)
        arr.append(n.BatchNum)
        arr.append(n.ExpiryDate)
        arr.append(n.OrderQTY)
        arr.append(n.CumConfQTY)
        arr.append(n.id)

    return JsonResponse(arr, safe=False)   

def delAutoconf(request):
    val = request.GET.get('vala')

    selAutoConf = Autoconfdata.objects.get(id=val)

    selAutoConf.delete()
    return JsonResponse(val, safe=False) 

def backOrder(request):

    pendingConf = ElementCreation.objects.filter(status="Pending")
    print(pendingConf)
    data =[Item.get_elem() for Item in pendingConf]
    
    response = {'data':data}
    return JsonResponse(response, safe=False)

def AutoInvOrder(request):
    condo = request.GET.get("vals")
    orderNumbero = request.GET.get('numord')
    print(orderNumbero)
    if condo == "1" :
        if orderNumbero != "1":
            pendingConf = AutoOrderInvoice.objects.filter(Q(orderNum = orderNumbero)&Q(InvoiceNumber = None)&Q(CatNumber__ShippindCond="Normal Temperture"))
            # pendingConf = AutoOrderInvoice.objects.all()
            
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]
            
            response = {'data':data}
            return JsonResponse(response, safe=False)
        else:
            pendingConf = AutoOrderInvoice.objects.filter(Q(InvoiceNumber = None)&Q(CatNumber__ShippindCond="Normal Temperture"))
            print(pendingConf)
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]
            
            response = {'data':data}
            return JsonResponse(response, safe=False)
    if condo == "2" :
        if orderNumbero != "1":
            pendingConf = AutoOrderInvoice.objects.filter(Q(orderNum = orderNumbero)&Q(InvoiceNumber = None) & Q(CatNumber__ShippindCond="Refrigrated"))
            print(pendingConf)
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]
            response = {'data':data}
            return JsonResponse(response, safe=False)
        else:
            pendingConf = AutoOrderInvoice.objects.filter(Q(InvoiceNumber = None) & Q(CatNumber__ShippindCond="Refrigrated"))
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]
            
            response = {'data':data}
            return JsonResponse(response, safe=False)
    if condo == "3" :
        if orderNumbero != "1":
            pendingConf = AutoOrderInvoice.objects.filter(Q(orderNum = orderNumbero)&Q(InvoiceNumber = None)&Q(CatNumber__ShippindCond="Frozen"))
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]            
            response = {'data':data}
            print(response)
            return JsonResponse(response, safe=False)
        else:
            pendingConf = AutoOrderInvoice.objects.filter(Q(InvoiceNumber = None)&Q(CatNumber__ShippindCond="Frozen"))
            print(pendingConf)
            data =[Item.get_AutoOrderInvoice() for Item in pendingConf]
            
            response = {'data':data}
            return JsonResponse(response, safe=False)
    
def showinginvoices(request):
    allinvoices = OrderInvoice.objects.all()

    data =[Item.get_OrderInvoice() for Item in allinvoices]
    
    response = {'data':data}
    return JsonResponse(response, safe=False)

def updateInvNumber(request):
    confirmationNumber = request.GET.get('conNum')
    invNumber = request.GET.get('invnum')
    OrderNumber = request.GET.get('orderNumber')
    cond = request.GET.get('vals')
    if cond == "1":
        ordersInvoice = AutoOrderInvoice.objects.filter(Q(orderNum=OrderNumber)&Q(CatNumber__ShippindCond="Normal Temperture"))
        print(ordersInvoice)
        for order in list(ordersInvoice):
            AutoOrderInvoice.objects.filter(id = order.id).update(InvoiceNumber=invNumber)

            sel = AutoOrderInvoice.objects.get(orderConfermation=order.orderConfermation)
            compnam = CompanyName.objects.get(companyName = sel.Item_Model_compName)
            typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = sel.Item_Model_compUnit)&Q(companyName1=compnam.id))

            newform = OrderInvoice.objects.create(
                Item_Model_compName = compnam,
                Item_Model_compUnit = typeOfana,
                dat = sel.dat,
                orderNum= sel.orderNum,
                orderConfermation=order.orderConfermation,
                InvoiceNumber=invNumber,
                Price = sel.Price

            )
            newform.save()
            sel.delete()

            ord1 = OrderInvoice.objects.filter(InvoiceNumber=invNumber).count()
            
            if ord1 == 1:
                ord = OrderInvoice.objects.get(InvoiceNumber=invNumber)
                new1form = Shipping.objects.create(
                    PO=sel.orderNum,
                    InvNumber = ord,
                    Item_Model_compName = compnam,
                    Item_Model_compUnit = typeOfana,
                    ShippingCond = "Normal Temperture",
                )
                new1form.save()
        return JsonResponse(invNumber, safe=False)
    if cond == "2":
        orderssInvoice = AutoOrderInvoice.objects.filter(Q(orderNum=OrderNumber)&Q(CatNumber__ShippindCond="Refrigrated"))

        for order in list(orderssInvoice):
            AutoOrderInvoice.objects.filter(id = order.id).update(InvoiceNumber=invNumber)
            
            sel = AutoOrderInvoice.objects.get(orderConfermation=order.orderConfermation)
            compnam = CompanyName.objects.get(companyName = sel.Item_Model_compName)
            typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = sel.Item_Model_compUnit)&Q(companyName1=compnam.id))

            newform = OrderInvoice.objects.create(
                Item_Model_compName = compnam,
                Item_Model_compUnit = typeOfana,
                dat = sel.dat,
                orderNum= sel.orderNum,
                orderConfermation=order.orderConfermation,
                InvoiceNumber=invNumber,
                Price = sel.Price

            )
            newform.save()
            sel.delete()

            ord1 = OrderInvoice.objects.filter(InvoiceNumber=invNumber).count()
        
            if ord1 == 1:
                ord = OrderInvoice.objects.get(InvoiceNumber=invNumber)
                new1form = Shipping.objects.create(
                    PO=sel.orderNum,
                    InvNumber = ord,
                    Item_Model_compName = compnam,
                    Item_Model_compUnit = typeOfana,
                    ShippingCond = "Refrigrated",
                )
                new1form.save()
        return JsonResponse(invNumber, safe=False)
        
    if cond == "3":
        ordersInvoicelist = AutoOrderInvoice.objects.filter(Q(orderNum=OrderNumber)&Q(CatNumber__ShippindCond="Frozen"))
        print(ordersInvoicelist)
        for order in list(ordersInvoicelist):
            AutoOrderInvoice.objects.filter(id = order.id).update(InvoiceNumber=invNumber)

            sel = AutoOrderInvoice.objects.get(orderConfermation=order.orderConfermation)
            compnam = CompanyName.objects.get(companyName = sel.Item_Model_compName)
            typeOfana = CompanyUnits.objects.get(Q(modelOfAnalyzer = sel.Item_Model_compUnit)&Q(companyName1=compnam.id))

            newform = OrderInvoice.objects.create(
                Item_Model_compName = compnam,
                Item_Model_compUnit = typeOfana,
                dat = sel.dat,
                orderNum= sel.orderNum,
                orderConfermation=order.orderConfermation,
                InvoiceNumber=invNumber,
                Price = sel.Price

            )
            newform.save()
            sel.delete()

            ord1 = OrderInvoice.objects.filter(InvoiceNumber=invNumber).count()
            
            if ord1 == 1:
                ord = OrderInvoice.objects.get(InvoiceNumber=invNumber)
                new1form = Shipping.objects.create(
                    PO=sel.orderNum,
                    InvNumber = ord,
                    Item_Model_compName = compnam,
                    Item_Model_compUnit = typeOfana,
                    ShippingCond = "Frozen",
                )
                new1form.save()
        return JsonResponse(invNumber, safe=False)

def Import_Excel_pandas(request):
    if request.method == 'POST':     
        file = request.FILES['Orderfiles']

        return HttpResponseRedirect('/Import_Excel_pandas')
    return render(request, 'octopus-master/octopus/pages-show-invoices1.html')

def base(request):
    return render(request, 'secproj/base.html')

def uploadexcelname(request):
    invNum =request.GET.get('searchVal')
    innumber = request.GET.get('innumber')
    request.session['invNum'] = invNum
    request.session['innumber'] = innumber 
    path = str(invNum)
    return JsonResponse(path, safe=False)

def uploadexcelnamechick(request):
    try:
        invNum =request.GET.get('searchVal')
        print(invNum)
        print(invNum)
        innumber = request.GET.get('innumber')
        request.session['invNum'] = invNum
        request.session['innumber'] = innumber
        chickNumber = OraderCreation.objects.get(orderNum=invNum)
        print(chickNumber) 
        return JsonResponse(True, safe=False)
    except:
        return JsonResponse(False, safe=False)

@csrf_exempt
def uploadexcel(request):
    path = request.session.get('invNum')
    ordnum1 = OraderCreation.objects.get(orderNum=path)
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Orders/{path}/OC'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            

            # validation
            new13 = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'
            df = pd.read_excel(new13)
            
            for d in df.values:
                
                nym = str(d[2])
                catnum = d[4]
                if nym[4:] == path :
                    try:
                        selCat = OraderCreation.objects.get(orderNum=nym[4:])
                        chickReagent = ReagentQTY.objects.get(CatNumber=catnum)
                    
                    except:
                        default_storage.delete(new13)
                        message = "There is an error in this Catalog Number "+str(d[4])
                        response = {
                            'message':message
                        }
                        return JsonResponse(response, safe=False)
                else:
                    default_storage.delete(new13)
                    message = "This File is Not Compatable OR the order Number is Wrong"
                    response = {
                        'message':message
                    }
                    return JsonResponse(response, safe=False)
                
            # end validation


            obj = ExcelFile.objects.create(
                file = f,
                ordnum=ordnum1,
            )
            path2 = str(obj.file)
            new = f'{settings.MEDIA_ROOT}/{path2}'
            df = pd.read_excel(new)
            for d in df.values:
                obm = Autoconfdata.objects.create(
                    OrderNumber=d[0],
                    PO=d[2],
                    matrial = d[4],
                    MatDesc=d[5],
                    BatchNum=d[6],
                    ExpiryDate=d[7],
                    OrderQTY=d[8],
                    CumConfQTY=d[9],
                    UnitPrice=d[10],
                    NetVal=d[11],
                    # ProdDate=d[12]
                    excfile=obj
                )
                obm.save()
        response = {'State': 'Success'}


    return JsonResponse(response,safe=False)

@csrf_exempt
def uploadItems(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Companies_Data/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            

            # validation
            new13 = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'
            df = pd.read_excel(new13)
            try:
                print("MOH")
                print("MOH")
                for d in df.values:
                    print("MOH")
                    print("MOH")
                    
                    catnum = d[0]
                    desc = d[2]
                    compName = d[5]
                    print(compName)
                    GTIN = d[6]
                    unit = d[8]
                    print(unit)
                    getCompName = CompanyName.objects.get(companyName=compName)
                    print("DIa")
                    getCompunit = CompanyUnits.objects.get(Q(modelOfAnalyzer=unit)&Q(companyName1=getCompName))
                    

                    
            except:
                default_storage.delete(new13)
                message = "This File is Not Compatable"
                return JsonResponse(message, safe=False)
            # end validation

            for d in df.values:
                catnum = d[0]
                desc = d[2]
                compName = d[5]
                GTIN = d[6]
                unit = d[8]               
                getCompName = CompanyName.objects.get(companyName=compName)
                getCompunit = CompanyUnits.objects.get(Q(modelOfAnalyzer=unit)&Q(companyName1=getCompName))
                selpar = ParameterName.objects.create(Item_Model_compName=getCompName,Item_Model_compUnit=getCompunit,
                                                        ParameterNam=desc)
                # for d in df.values:
                chickReagent = ReagentQTY.objects.create(Item_Model_compName= getCompName,Item_Model_compUnit= getCompunit,
                                                            GTIN=GTIN, ParName=selpar ,CatNumber=catnum)
            
    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadItems8(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Companies_Data/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            

            # validation
            new13 = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'
            df = pd.read_excel(new13)
            try:
                for d in df.values:
                    catnum = d[0]
                    print(catnum)
                    packSize = d[2]
                    catNum = d[0]

                    getCat = ReagentQTY.objects.filter(CatNumber=catNum)
                    for chickReagent in getCat:
                            ReagentQTY.objects.filter(pk=chickReagent.id).update(slideNumber=packSize)
            except:
                default_storage.delete(new13)
                message = "This File is Not Compatable"
                return JsonResponse(message, safe=False)
            # end validation

            # for d in df.values:
            #     catnum1 = d[0]
            #     desc = d[2]
            #     print(desc)
            #     print(catnum1)
            #     compName = d[5]
            #     GTIN = d[6]
            #     unit = d[8]               
            #     getCompName = CompanyName.objects.get(companyName=compName)
            #     getCompunit = CompanyUnits.objects.get(modelOfAnalyzer=unit)
            #     selpar = ParameterName.objects.filter(ParameterNam=desc)
            #     chickReagent = ReagentQTY.objects.create(Item_Model_compName= getCompName,Item_Model_compUnit= getCompunit,
            #                                                 GTIN=GTIN, ParName=selpar[0] ,CatNumber=catnum1)

    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadItems7(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Companies_Data/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            

            # validation
            new13 = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'
            df = pd.read_excel(new13)
            try:
                arr=[]
                for d in df.values:
                    
                    catnum = d[0]
                    print(catnum)
                    unit = d[2]
                    print(unit)
                    getit = ReagentQTY.objects.filter(CatNumber=catnum)
                    if getit:
                        if unit == "2 to 8 °C":
                            print("2 to 8 °C")
                            # for chickReagent in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="Refrigrated")

                        if unit == "-18 °C":
                            print("-18")
                            # for chickReagentz in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="Frozen")

                        if unit == "2 to 25 °C":
                            print("2 to 25 °C")
                            # for chickReagentb in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="Normal Temperture")
                        if unit == "frozen":
                            print("frozen")
                            # for chickReagentb in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="frozen")
                        if unit == "15 to 25 °C":
                            print("15 to 25 °C")
                            # for chickReagentq in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="Normal Temperture")
                        if unit == "2 to 25 °C":
                            print("2 to 25 °C")
                            # for chickReagentd in chickReagents:
                            ReagentQTY.objects.filter(CatNumber=catnum).update(ShippindCond="Normal Temperture")
                # default_storage.delete(new13)
            except:
                # print(catnum)
                default_storage.delete(new13)
                message = "This File is Not Compatable"
                return JsonResponse(message, safe=False)
            # end validation

            # for d in df.values:
            #     catnum1 = d[0]
            #     desc = d[2]
                # print(desc)
                # print(catnum1)
                # compName = d[5]
                # GTIN = d[6]
                # unit = d[8]               
                # getCompName = CompanyName.objects.get(companyName=compName)
                # getCompunit = CompanyUnits.objects.get(modelOfAnalyzer=unit)
                # selpar = ParameterName.objects.filter(ParameterNam=desc)
                # ReagentQTY.objects.filter(CatNumber=catnum1).update(ShippindCond=desc)
                # chickReagent = ReagentQTY.objects.create(Item_Model_compName= getCompName,Item_Model_compUnit= getCompunit,
                #                                             GTIN=GTIN, ParName=selpar[0] ,CatNumber=catnum1)

    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadItems6(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Companies_Data/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            

            # validation
            new13 = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'
            df = pd.read_excel(new13)
            try:
                for d in df.values:
                    catnum = d[0]
                    print(catnum)
                    desc = d[2]
                    compName = d[5]
                    GTIN = d[6]
                    unit = d[8]
                    getCompName = CompanyName.objects.get(companyName=compName)
                    getCompunit = CompanyUnits.objects.get(modelOfAnalyzer=unit)
                    getCat = ParameterName.objects.filter(ParameterNam=desc)
                    
            except:
                print(desc)
                default_storage.delete(new13)
                message = "This File is Not Compatable"
                return JsonResponse(message, safe=False)
            # end validation

            for d in df.values:
                catnum1 = d[0]
                desc = d[2]
                print(desc)
                print(catnum1)
                compName = d[5]
                GTIN = d[6]
                unit = d[8]               
                getCompName = CompanyName.objects.get(companyName=compName)
                getCompunit = CompanyUnits.objects.get(modelOfAnalyzer=unit)
                selpar = ParameterName.objects.filter(ParameterNam=desc)
                chickReagent = ReagentQTY.objects.create(Item_Model_compName= getCompName,Item_Model_compUnit= getCompunit,
                                                            GTIN=GTIN, ParName=selpar[0] ,CatNumber=catnum1)

    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadInvoices(request):
    path = request.session.get('invNum')
    pathinv = request.session.get('innumber')
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            xc = OraderCreation.objects.get(orderNum=path)
            invo = OrderInvoice.objects.filter(InvoiceNumber=pathinv)
            print(invo)
            obj = ExcelFileInvoice.objects.create(
                file = f,
                ordnum=xc,
                ordinv=invo[0],
            )
            upload_to = f'Orders/{path}/Invoices/{pathinv}'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            
    return JsonResponse({'State': 'Success'})

@csrf_exempt
def uploadOrder(request):
    path = request.session.get('invNum')
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = f'Orders/{path}'
            
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0], ext)
            default_storage.save(os.path.join(upload_to, filename), f)
            new = f'{settings.MEDIA_ROOT}/{upload_to}/{filename}'   
            df = pd.read_excel(new)

            # Validate order excel 

            
            for d in df.values:
                try:
                    selCat = ReagentQTY.objects.get(CatNumber=d[0])
                    selcomp = CompanyName.objects.get(companyName=selCat.Item_Model_compName)
                    selunit = CompanyUnits.objects.get(Q(modelOfAnalyzer=selCat.Item_Model_compUnit)&Q(companyName1=selCat.Item_Model_compName))
                except:
                    default_storage.delete(new)
                    fo = d[0]
                    return JsonResponse(fo, safe=False)

            ordnumber = OraderCreation.objects.get(orderNum=path)
            obj = ExcelFileOrderCrea.objects.create(
            file = f,
            ordnum=ordnumber,
            )
            path1 = str(obj.file)
            new12 = f'{settings.MEDIA_ROOT}/{path1}'
            df = pd.read_excel(new12)
        
            for d in df.values:
                selCat = ReagentQTY.objects.get(CatNumber=d[0])
                selcomp = CompanyName.objects.get(companyName=selCat.Item_Model_compName)
                selunit = CompanyUnits.objects.get(Q(modelOfAnalyzer=selCat.Item_Model_compUnit)&Q(companyName1=selCat.Item_Model_compName))
                obm = ElementCreation.objects.create(
                    SlidesQTY=d[4],
                    QTY=d[3],
                    dat = date.today(),
                    orderNum=path,
                    status="Pending",
                    CatNumber=selCat,
                    ElementName=selCat.ParName,
                    Item_Model_compName=selcomp,
                    Item_Model_compUnit=selunit,
                )
                obm.save()
        

        mess = "OK",      

    return JsonResponse(mess,safe=False)

def getAllOrders(request):
    allorders = OraderCreation.objects.all()
    arr = []
    for n in list(allorders):
        arr.append(n.orderNum)
    return JsonResponse(arr, safe=False)

def OrdersFiles(request):
    ordernum = request.GET.get('valu')
    selord = OraderCreation.objects.filter(orderNum=ordernum)
    is_taken = ExcelFileInvoice.objects.filter(ordnum=selord[0])
    arra = []
    for n in list(is_taken):
        if n.ordinv.InvoiceNumber not in list(arra):
            arra.append(n.ordinv.InvoiceNumber)
    print(arra)
    return JsonResponse(arra, safe=False)

def Ordersinvoices(request):
    orderinv = request.GET.get('valas')
    selord = OrderInvoice.objects.filter(InvoiceNumber=orderinv)
    invNumbers = ExcelFileInvoice.objects.filter(ordinv=selord[0])
    arra = []
    for n in list(invNumbers):
        arra.append(n.file.url)
    print(arra)
    return JsonResponse(arra, safe=False)

def getconfirmations(request):
    ordernum = request.GET.get('valu')
    path = request.session.get('invNum')
    getorder = OraderCreation.objects.get(orderNum=ordernum)    
    selconf = ExcelFile.objects.filter(ordnum=getorder)
    arra = []
    for n in list(selconf):
        arra.append(n.file.url)
    print(arra)
    return JsonResponse(arra, safe=False)

def ckeckInvo(request):
    invoNumber = request.GET.get('innumber')
    is_taken = OrderInvoice.objects.filter(InvoiceNumber=invoNumber).exists()
    if is_taken:
        return JsonResponse(invoNumber, safe=False)
    else:
        return JsonResponse(is_taken, safe=False)

def getOrders(request):
    ordernum = request.GET.get('valu')
    path = request.session.get('invNum')
    getorder = OraderCreation.objects.get(orderNum=ordernum)    
    selconf = ExcelFileOrderCrea.objects.filter(ordnum=getorder)
    arra = []
    for n in list(selconf):
        arra.append(n.file.url)
    print(arra)
    return JsonResponse(arra, safe=False)

def checkForOrder(request):
    ordernumber = request.GET.get('searchVal')
    is_taken = OraderCreation.objects.filter(orderNum=ordernumber).exists()
    try:
        if (is_taken == True):
            return JsonResponse(is_taken, safe=False)
        if(ordernumber == "1"):  
            is_taken = True
            return JsonResponse(is_taken, safe=False)
        if(is_taken == False):
            return JsonResponse(is_taken, safe=False)
    except:
        return JsonResponse(is_taken, safe=False)
@login_required
def secProHomePage(request):

    return render(request, 'secproj/indexo.html')

def itemsnumbers(request):
    allItems = ParameterName.objects.count()

    allOrderCreations = OraderCreation.objects.count()
    allOrderCreationsSta = OraderCreation.objects.all()
    cnt = OraderCreation.objects.filter(status = "OK").count()
    perc = cnt * 100 / allOrderCreations
    arr_ok=[]
    arr_pending=[]
    for n in list(allOrderCreationsSta):
        if n.status == "OK":
            arr_ok.append(n.orderNum)
        if n.status == "Pending":
            arr_pending.append(n.orderNum)
    Response = {
        'perc':perc,
        'arr_ok':arr_ok,
        'arr_pending':arr_pending,
        'allItems':allItems
    }
    print(Response)
    return JsonResponse(Response, safe=False)


## Third Project 
@login_required
def mainPage(request):  
    current_user1 = request.user
    userStaff = current_user1.is_superuser

    return render(request, 'thirdPro/index.html',{'userStaff':userStaff})

@login_required
def InvoicePage(request):

    return render(request, 'thirdPro/testimonial.html')

@login_required
def InputPage(request):

    return render(request, 'thirdPro/courses.html')

@login_required
def InventoryPage(request):

    return render(request, 'thirdPro/about.html')

@login_required
def setupPage(request):

    return render(request, 'thirdPro/setup.html')

@login_required
def HospitalsPage(request):
    
    return render(request, 'thirdPro/Hospitals.html')

def ItemPriceFunc(request):
    companyNan = request.GET.get('companyNan')
    typeOfAnaly = request.GET.get('typeOfAnaly')
    analyzerNam = request.GET.get('analyzerNam')
    PartNum = request.GET.get('PartNum')
    ItemNam = request.GET.get('ItemNam')
    ItemPrice = request.GET.get('ItemPrice')

    compName = CompanyName.objects.get(companyName = companyNan )
    compuni = CompanyUnits.objects.get(Q(companyName1_id = compName.id )& Q(modelOfAnalyzer = typeOfAnaly) )
    compwork = WorkFlow.objects.get(nameOfWorkFlow = analyzerNam )

    try:
        searchPartnum =  Price.objects.get(partNumber=PartNum)
        Price.objects.filter(pk=searchPartnum.id).update(Price=ItemPrice)

        Response = {'state':'success'}
        return JsonResponse(Response, safe=False)
    except:
        cartable = Price.objects.create(
            Item_Model_compName = compName ,
            Item_Model_compUnit = compuni ,
            Item_Model_workFlow = compwork ,
            ItemName=ItemNam,
            partNumber=PartNum,
            Price=ItemPrice,

        )
        Response = {'state':'success'}
        return JsonResponse(Response, safe=False)

@csrf_exempt
def uploadFiles3(request):

    mypath3 = os.path.join(settings.MEDIA_ROOT, 'temporary','Item')
        
    onlyfiles = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]
    for item_att in onlyfiles:
        item_att =  'temporary/'+'Item/'+item_att
        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
        fi = open(file_path, 'rb')
        local_file = File(fi)
        local_file.close()
        default_storage.delete(item_att)


    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = 'temporary/Item/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0] + '.' + ext + '``__``' + uuid4().hex, ext)
            default_storage.save(os.path.join(upload_to, filename), f)
    return JsonResponse({'State': 'Success'})

def CheckItemName(request):
    partNum = request.GET.get('partNumVal')
    try:
        getName = Price.objects.get(partNumber=partNum)
        Response = {
            'getName':getName.ItemName
        }
        return JsonResponse(Response, safe=False)
    except:
        mess = "There is no Item with this part number"
        Response = {
            'mess':mess
        }
        return JsonResponse(Response, safe=False)

def ItemInput3(request):

    userId = request.user
    partNumber_Item = request.GET.get('PartNum')
    dateOfArrival_Item = request.GET.get('itemDate')
    
    selItemPrice = Price.objects.get(partNumber=partNumber_Item)
    compName = CompanyName.objects.get(companyName = selItemPrice.Item_Model_compName )
    compuni = CompanyUnits.objects.get(Q(companyName1_id = compName.id )& Q(modelOfAnalyzer = selItemPrice.Item_Model_compUnit) )
    compwork = WorkFlow.objects.get(nameOfWorkFlow = selItemPrice.Item_Model_workFlow )

    cartable = ItemInput.objects.create(
        Item_Model_compName = compName ,
        Item_Model_compUnit = compuni ,
        Item_Model_workFlow = compwork ,
        nameOfItem=selItemPrice.ItemName,
        mainUser=userId,
        dateOfArrival=dateOfArrival_Item,
        partNumber=partNumber_Item,
        cost=selItemPrice.Price,

    )

    mypath3 = os.path.join(settings.MEDIA_ROOT, 'temporary','Item')
    onlyfiles = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]
    for item_att in onlyfiles:
        # print(item_att)
        item_att =  'temporary/'+'Item/'+item_att
        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
        file_type, file_encoding = mimetypes.guess_type(file_path)
        fi = open(file_path, 'rb')
        local_file = File(fi)
        fileName = os.path.basename(local_file.name).split('``__``')[0]

        attachmetToAdd = Imag3.objects.create(images=local_file,Inpu=cartable)
        attachmetToAdd.save()
    
        local_file.close()
        default_storage.delete(item_att)

    return JsonResponse({'State': 'Success'})

def subIntrInvoice(request):

    compNam = request.GET.get('compNam')
    partNam = request.GET.get('partNam')
    ItemNam = request.GET.get('ItemNam')
    ItemDate = request.GET.get('ItemDate')
    ItemInv = request.GET.get('ItemInv')
    ItemQTY = request.GET.get('ItemQTY')
    ItemLot = request.GET.get('ItemLot')
    
    newOne = OutInvoice.objects.create(
        outInvoiceNumber = ItemInv,
        Datao = ItemDate,
        CompaniesNAme = compNam,
        ItemName = ItemNam,
        ItemPartNumber=partNam,
        LtQTY = ItemQTY,
        Lots = ItemLot,
        
        )
    newOne.save()

    Hoso = OutInvoice.objects.get(Q(outInvoiceNumber=ItemInv)&Q(ItemPartNumber=partNam)&Q(Lots=ItemLot))
    newLot = Lot.objects.create(
        Loto = ItemLot,
        LotQTY = ItemQTY, 
        AllLotQTY = ItemQTY,
        JNum = partNam,
        Lot_outInvoice=Hoso,
    )
    newLot.save()

    return JsonResponse({'State': 'Success'})

def subUnderTest(request):
    selUser = request.user
    compNam = request.GET.get('compNam')
    typeOfAna = request.GET.get('typeOfAna')
    analyzerNam = request.GET.get('analyzerNam')
    PartNum = request.GET.get('PartNum')
    ItemNam = request.GET.get('ItemNam')
    ItemStatus = request.GET.get('ItemStatus')
    ItemDate = request.GET.get('ItemDate')
    ItemNote = request.GET.get('ItemNote')

    SelLot = Lot.objects.filter(JNum=PartNum)

    compName = CompanyName.objects.get(companyName = compNam )
    compuni = CompanyUnits.objects.get(Q(companyName1_id = compName.id )& Q(modelOfAnalyzer = typeOfAna) )
    compwork = WorkFlow.objects.get(nameOfWorkFlow = analyzerNam )
    cartable = Undertest.objects.create(
        Item_Model_compName = compName ,
        Item_Model_compUnit = compuni ,
        Item_Model_workFlow = compwork ,
        nameOfItem=ItemNam,
        partNumber=PartNum,
        dateOfArrival=ItemDate,
        mainUser=selUser.username,
        Note = ItemNote,
        Status = ItemStatus ,
        LotNum=SelLot[0].Loto,

    )
    cartable.save()

    return JsonResponse({'State': 'Success'})

## Invoice Page 
def assemJsonPending(request):
    selInv = InvoiceStatus.objects.get(Status="Pending")
    Items = AssembledStore.objects.filter(Invo=selInv)
    print(Items)
    data =[Item.get_assem() for Item in Items]
    
    response = {'data':data}
    return JsonResponse(response,safe=False)

def HospitalsInvoices(request):
    allInvo = InvoiceNumbero.objects.all()
    data =[Item.get_confirmed() for Item in allInvo]
    response = {'data':data}
    return JsonResponse(response,safe=False)

def InternationalInvoices(request):

    allInvo = OutInvoice.objects.all()
    data =[Item.get_International() for Item in allInvo]
    response = {'data':data}
    return JsonResponse(response,safe=False)

def sendingQuotNum(request):

    QuotNumber = request.GET.get('QuotNumber')
    ItemName = request.GET.get('ItemName')
    HosName = request.GET.get('HosName')
    LotNum = request.GET.get('LotNum')
    ItemDate = request.GET.get('ItemDate')
    PartNum = request.GET.get('PartNum')
    itemId = request.GET.get('itemId')
    cartable3 = CotNumber.objects.create (
            ItemName=ItemName,
            PartNumber=PartNum,
            HosName=HosName,
            ItemLot = LotNum,
            CotNumber1 = QuotNumber,
            Datee=ItemDate

        )
    cartable3.save()

    AssembledStore.objects.filter(pk=itemId).update(Cot=QuotNumber)
    return JsonResponse(True,safe=False)

def sendingInvoiceNum(request):

    QuotNumber = request.GET.get('QuotNumber')
    ItemName = request.GET.get('ItemName')
    HosName = request.GET.get('HosName')
    LotNum = request.GET.get('LotNum')
    ItemDate = request.GET.get('ItemDate')
    PartNum = request.GET.get('PartNum')
    itemId = request.GET.get('itemId')
    CotNum = request.GET.get('CotNumber')
    
    # SelPrice = Price.objects.get(partNumber=PartNum)
    SelItem = AssembledStore.objects.get(pk=itemId)
    SelFoc = InvoiceStatus.objects.get(Status="OK")
    cartable3 = InvoiceNumbero.objects.create (
            ItemName=ItemName,
            PartNumber=PartNum,
            HosName=HosName,
            ItemLot = LotNum,
            CotNumber1 = SelItem.Cot,
            Datee=ItemDate,
            InvoiceNumber1=QuotNumber,
            Price=SelItem.Price,
        )
    cartable3.save()

    AssembledStore.objects.filter(pk=itemId).update(InvoNum=QuotNumber,Invo=SelFoc)
    return JsonResponse(True,safe=False)

## Stock Page

def GetVitros350(request):
    namo = CompanyName.objects.get(companyName = "OCD")
    namouni = CompanyUnits.objects.get(Q(companyName1_id=namo.id)& Q( modelOfAnalyzer = "Chimestry" ))

    getitems = ItemInput.objects.filter(Q(Item_Model_compName_id = namo.id)& Q(Item_Model_compUnit_id = namouni.id ))

    
    arrayOfItemName = []
    sumarray = []
    sumAllarray = []
    for name in list(getitems):
        undertestItem = Undertest.objects.filter(partNumber=name.partNumber)
        getimg = Imag3.objects.get(Inpu_id=name.id)
        getlot = Lot.objects.filter(JNum=name.partNumber)

        for n in list(getlot):
            sumarray.append(n.LotQTY)
            sumAllarray.append(n.AllLotQTY)
            
        ans = sum(sumarray)
        Allans = sum(sumAllarray)

        arrayOfItemName.append(name.nameOfItem)
        arrayOfItemName.append(getimg.images.url)
        arrayOfItemName.append(ans)
        sumarray.clear()
        arrayOfItemName.append(name.partNumber)
        arrayOfItemName.append(name.id)
        arrayOfItemName.append(Allans)
        arrayOfItemName.append(undertestItem.count())
        sumAllarray.clear()

        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def GetItemR940(request):
    namo = CompanyName.objects.get(companyName = "Diasys")
    typo = WorkFlow.objects.get(nameOfWorkFlow="R940")

    item = ItemInput.objects.filter(Q(Item_Model_compName_id=namo.id)&Q(Item_Model_workFlow=typo))
    arrayOfItemName=[]
    sumarray = []
    sumAllarray = []

    for name in list(item):
        undertestItem = Undertest.objects.filter(partNumber=name.partNumber)
        getimg = Imag3.objects.get(Inpu_id=name.id)
        getlot = Lot.objects.filter(JNum=name.partNumber)
        for n in list(getlot):
            sumarray.append(n.LotQTY)
            sumAllarray.append(n.AllLotQTY)
        ans = sum(sumarray)
        Allans = sum(sumAllarray)

        arrayOfItemName.append(name.nameOfItem)
        arrayOfItemName.append(getimg.images.url)
        arrayOfItemName.append(ans)
        sumarray.clear()
        arrayOfItemName.append(name.partNumber)
        arrayOfItemName.append(name.id)
        arrayOfItemName.append(Allans)
        arrayOfItemName.append(undertestItem.count())
        sumAllarray.clear()
        
    return JsonResponse(arrayOfItemName, safe=False)

def GetItem(request):
    namo = CompanyName.objects.get(companyName = "Diasys")
    typo = WorkFlow.objects.get(nameOfWorkFlow="R920")

    item = ItemInput.objects.filter(Q(Item_Model_compName_id=namo.id)&Q(Item_Model_workFlow=typo))
    arrayOfItemName=[]
    sumarray = []
    sumAllarray = []

    for name in list(item):
        undertestItem = Undertest.objects.filter(partNumber=name.partNumber)
        getimg = Imag3.objects.get(Inpu_id=name.id)
        getlot = Lot.objects.filter(JNum=name.partNumber)
        for n in list(getlot):
            sumarray.append(n.LotQTY)
            sumAllarray.append(n.AllLotQTY)
        ans = sum(sumarray)
        Allans = sum(sumAllarray)

        arrayOfItemName.append(name.nameOfItem)
        arrayOfItemName.append(getimg.images.url)
        arrayOfItemName.append(ans)
        sumarray.clear()
        arrayOfItemName.append(name.partNumber)
        arrayOfItemName.append(name.id)
        arrayOfItemName.append(Allans)
        arrayOfItemName.append(undertestItem.count())
        sumAllarray.clear()
        
    return JsonResponse(arrayOfItemName, safe=False)

def GetItemr910(request):
    namo = CompanyName.objects.get(companyName = "Diasys")
    typo = WorkFlow.objects.get(nameOfWorkFlow="R910")
    item = ItemInput.objects.filter(Q(Item_Model_compName_id=namo.id)&Q(Item_Model_workFlow=typo))
    arrayOfItemName=[]
    sumarray = []
    sumAllarray = []
    for name in list(item):
        undertestItem = Undertest.objects.filter(partNumber=name.partNumber)
        getimg = Imag3.objects.get(Inpu_id=name.id)
        getlot = Lot.objects.filter(JNum=name.partNumber)
        for n in list(getlot):
            sumarray.append(n.LotQTY)
            sumAllarray.append(n.AllLotQTY)
        ans = sum(sumarray)
        Allans = sum(sumAllarray)

        arrayOfItemName.append(name.nameOfItem)
        arrayOfItemName.append(getimg.images.url)
        arrayOfItemName.append(ans)
        sumarray.clear()
        arrayOfItemName.append(name.partNumber)
        arrayOfItemName.append(name.id)
        arrayOfItemName.append(Allans)
        arrayOfItemName.append(undertestItem.count())
        sumAllarray.clear()
        print(arrayOfItemName)
    return JsonResponse(arrayOfItemName, safe=False)

def GetItemmc15(request):
    namo = CompanyName.objects.get(companyName = "Diasys")
    typo = WorkFlow.objects.get(nameOfWorkFlow="MC15")
    item = ItemInput.objects.filter(Q(Item_Model_compName_id=namo.id)&Q(Item_Model_workFlow=typo))
    arrayOfItemName=[]
    sumarray = []
    sumAllarray = []
    for name in list(item):
        undertestItem = Undertest.objects.filter(partNumber=name.partNumber)
        getimg = Imag3.objects.get(Inpu_id=name.id)
        getlot = Lot.objects.filter(JNum=name.partNumber)
        for n in list(getlot):
            sumarray.append(n.LotQTY)
            sumAllarray.append(n.AllLotQTY)
        ans = sum(sumarray)
        Allans = sum(sumAllarray)

        arrayOfItemName.append(name.nameOfItem)
        arrayOfItemName.append(getimg.images.url)
        arrayOfItemName.append(ans)
        sumarray.clear()
        arrayOfItemName.append(name.partNumber)
        arrayOfItemName.append(name.id)
        arrayOfItemName.append(Allans)
        arrayOfItemName.append(undertestItem.count())
        sumAllarray.clear()

    return JsonResponse(arrayOfItemName, safe=False)

def QTYdataBase(request):
    ItemId = request.GET.get('itemId')
    sumarray =[]
    LotArr =[]
    selItem = ItemInput.objects.get(id=ItemId)
    selectItem = Lot.objects.filter(JNum=selItem.partNumber)
    for n in list(selectItem):
        sumarray.append(n.LotQTY)
        LotArr.append(n.Loto)
        LotArr.append(n.LotQTY)
        print(sumarray)
    ans = sum(sumarray)
    response = {
        'ans': ans,
        'LotArr':LotArr,
    }
    return JsonResponse(response, safe=False)

def SaveBookStore(request):
    user1 = request.user
    GetId = request.GET.get('itemId')
    loto = request.GET.get('loto')
    InptQTY = request.GET.get('InptQTY')

    selectItem = ItemInput.objects.get(id=GetId)

    try:
        Lot_entry = Lot.objects.get(Q(Loto=loto)&Q(JNum=selectItem.partNumber))
        cartable3 = BookStore.objects.create(
            QTYOfItem=InptQTY,
            StatusOfItem="Pending",
            nameOfUser=user1,
            NameOfItem=selectItem,
            RemainingQTY=InptQTY,
            BookedLot = Lot_entry,
        )
        cartable3.save()
        
        actualLotQTY = Lot_entry.LotQTY
        finalQty = int(actualLotQTY) - int(InptQTY)
        if(finalQty >= 0):
            Lot.objects.filter(pk=Lot_entry.id).update(LotQTY=finalQty)
            return JsonResponse(actualLotQTY, safe=False)
    except:
            message = "Error 404"
            
            return JsonResponse(message, safe=False) 
        
def QTYdataBaseQTY(request):
    itemId = request.GET.get('itemId')
    getlot = request.GET.get('loto')
    SelItemInput = ItemInput.objects.get(id=itemId)
    LotArr =[]
    selectItem = Lot.objects.filter(Q(JNum=SelItemInput.partNumber)&Q(Loto=getlot))
    print(selectItem)
    for n in list(selectItem):
        LotArr.append(n.LotQTY)
    response = {
        'LotArr':LotArr,
    }
    return JsonResponse(response, safe=False)

def codevalid(request):
    actLot = request.GET.get('ItemLot')
    
    if(actLot != "--Please choose an option--" ):
        response = actLot
        return JsonResponse(response, safe=False)

def foriphone(request):
    reqQty = request.GET.get('reqQty')
    lotSelect = request.GET.get('lott')
    itemId = request.GET.get('itemId')
    selItem = ItemInput.objects.get(id=itemId)
    actualLot = Lot.objects.get(Q(Loto=lotSelect)&Q(JNum=selItem.partNumber))
    print(actualLot)
    actualLotQTY = actualLot.LotQTY
    finalQty = int(actualLotQTY) - int(reqQty)

    
    response={
            'finalQty':finalQty
    }
    return JsonResponse(response, safe=False)

def ItemHopitals(request):
    itemId = request.GET.get('itemId')
    selItem = ItemInput.objects.get(id=itemId)
    allInvo = OutInvoice.objects.filter(ItemPartNumber = selItem.partNumber)
    data =[Item.get_International() for Item in allInvo]
    response = {'data':data}

    return JsonResponse(response,safe=False)

def GetUnderTest(request):
    itemId = request.GET.get('itemId')
    selItem = ItemInput.objects.get(id=itemId)
    allInvo = OutInvoice.objects.filter(ItemPartNumber = selItem.partNumber)
    data =[Item.get_International() for Item in allInvo]
    response = {'data':data}

    return JsonResponse(response,safe=False)

def ShowUndertest(request):
    itemId = request.GET.get('itemId')
    arrayOfItems = []
    arr =[]
    hosarray = []
    selItem = ItemInput.objects.get(id=itemId)
    Items = Undertest.objects.filter(partNumber=selItem.partNumber)
    print(Items)
    print(Items)
    print(Items)
    for item in list(Items):
        if item.Status == "Undertest":
            arr.append(item.id)
            arr.append(item.nameOfItem)
            arr.append(item.Item_Model_compName.companyName)
            arr.append(item.Item_Model_compUnit.modelOfAnalyzer)
            arr.append(item.Item_Model_workFlow.nameOfWorkFlow)
            arr.append(item.partNumber)
            arr.append(item.mainUser)
            arr.append(item.Note)
            arr.append(item.Status)
        else:
            arrayOfItems.append(item.id)
            arrayOfItems.append(item.nameOfItem)
            arrayOfItems.append(item.Item_Model_compName.companyName)
            arrayOfItems.append(item.Item_Model_compUnit.modelOfAnalyzer)
            arrayOfItems.append(item.Item_Model_workFlow.nameOfWorkFlow)
            arrayOfItems.append(item.partNumber)
            arrayOfItems.append(item.mainUser)
            arrayOfItems.append(item.Note)
            arrayOfItems.append(item.Status)
    
    response = {
        'arrayOfItems':arrayOfItems,
        'arr':arr,
    }
    return JsonResponse(response, safe=False)

def BookUndertest(request):
    itemid = request.GET.get('itemId')
    selectedItem = Undertest.objects.get(id=itemid)
    name = selectedItem.nameOfItem
    selname = ItemInput.objects.get(nameOfItem=name)
    myuser = request.user
    mypart = selectedItem.partNumber
    # lotq = selectedItem.LotNum
    zz = Lot.objects.get(Loto="Null")

    cartable3 = BookStore.objects.create(
        QTYOfItem=1,
        StatusOfItem="Undertest",
        nameOfUser=myuser,
        NameOfItem=selname,
        RemainingQTY=1,
        BookedLot = zz,
    )
    cartable3.save()
    selectedItem.delete()
    return JsonResponse(itemid, safe=False)


## Setup Page
def GetHosName(request):
    HosName = request.GET.get('HosName')
    compName = request.GET.get('compName')
    compMudules = request.GET.get('compMudules')
    compAnalyzers = request.GET.get('compAnalyzers')
    Serial_Number = request.GET.get('Serial_Number')
    try:
        comp = CompanyName.objects.get(companyName=compName)
        typo = CompanyUnits.objects.get(Q( companyName1 = comp)& Q(modelOfAnalyzer=compMudules))
        namo = WorkFlow.objects.get(nameOfWorkFlow=compAnalyzers)

        HosptialName = Hospitals.objects.create(
                hospitalName=HosName,
            )
        
        cartable3 = HospitalsAnalyzers.objects.create(
                HosNam=HosptialName,
                compNam=comp,
                compUni=typo,
                WorFlo=namo,
                SerialNumber=Serial_Number,
            )
        cartable3.save()
        return JsonResponse({'State': 'Success'})
    except:
        return JsonResponse({'State': 'Failed'})

def ValHosName(request):
    HosNam = request.GET.get('HosNam')
    try:
        tryHosName = Hospitals.objects.get(hospitalName=HosNam)
        response = tryHosName.hospitalName
        return JsonResponse(response, safe=False)
    except:
        return JsonResponse(tryHosName, safe=False)
    
def ValSerialNum(request):
    serialNum = request.GET.get('serialNum')
    try:
        tryHosName = HospitalsAnalyzers.objects.get(SerialNumber=serialNum)
        response = tryHosName.SerialNumber
        return JsonResponse(response, safe=False)
    except:
        return JsonResponse(tryHosName, safe=False)

def SubCompForm(request):
    CompName = request.GET.get('CompName')
    typeOfANa = request.GET.get('typeOfANa')
    AnalyzerName = request.GET.get('AnalyzerName')
    try:
        CompanyNam = CompanyName.objects.create(
            companyName=CompName,
        )
        CompanyNam.save()   

        CompModules = CompanyUnits.objects.create(
            companyName1=CompanyNam,
            modelOfAnalyzer=typeOfANa,
        )
        CompModules.save() 

        AnalyzerName = WorkFlow.objects.create(
            nameOfWorkFlow=AnalyzerName,
            companyAnalyzers=CompModules,
            companyName=CompanyNam,
        )
        AnalyzerName.save()


        return JsonResponse({'State': 'Success'})
    except:
        return JsonResponse({'State': 'Failed'})

def uservald(requset):
    takenuser = requset.GET.get('takenusername')
    is_taken = User.objects.filter(username__iexact=takenuser).exists()
    data = {'is_taken': is_taken}
    return JsonResponse(data)

@csrf_exempt
def uploadFilesSignup(request):
    if request.method=='POST':
        for f in request.FILES.getlist('file'):
            upload_to = 'temporary/SignUp/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0] + '.' + ext + '``__``' + uuid4().hex, ext)
            default_storage.save(os.path.join(upload_to, filename), f)
    return JsonResponse({'State': 'Success'}) 

def SubUserForm(request):
    current_user = request.user
    current_user1 = Profile.objects.get(user_id=current_user.id)

    if current_user.is_authenticated:
        current_user_profile = Profile.objects.get(user=current_user)

        UsrName = request.GET.get('UsrName')
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        email = request.GET.get('email')
        cond_shippo = request.GET.get('cond_shippo')
        monileNum = request.GET.get('monileNum')
        pass1 = request.GET.get('pass1')
        pass2 = request.GET.get('pass2')
        
        usernew = User.objects.create_user(username=UsrName, email=email, password=pass1,
                                                first_name=fname, last_name=lname)
        usernew.save()
        rol_id = Role.objects.get(id=cond_shippo)

        mypath3 = os.path.join(settings.MEDIA_ROOT, 'temporary','SignUp')
        onlyfiles = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]
        # for item_att in onlyfiles:
            # print(item_att)
        item_att =  'temporary/'+'SignUp/'+onlyfiles[0]
        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
        file_type, file_encoding = mimetypes.guess_type(file_path)
        fi = open(file_path, 'rb')
        local_file = File(fi)
        fileName = os.path.basename(local_file.name).split('``__``')[0]

        attachmetToAdd = Profile.objects.create(
            image=local_file,
            user=usernew,
            mobile=monileNum,
            role=rol_id
            )

        attachmetToAdd.save()
    
        local_file.close()
        default_storage.delete(item_att)

        if cond_shippo == '2':
            # allVendors = Engineer.objects.filter(Q(shippervendor__profileMainAccount__id=current_user_profile.id))
            allShippers = TeamLeader.objects.filter(Q(ProfileMainUser__id=current_user_profile.id))
            rok = TeamLeader.objects.create(
                name=UsrName,
                role=rol_id.cond,
                profileTeamLeader=attachmetToAdd,
                ProfileMainUser=current_user_profile,

            )
            rok.save()
        elif cond_shippo == '3':
            allShippers = TeamLeader.objects.get( profileTeamLeader__id=current_user1.id)
            roko = Engineer.objects.create(

                name=UsrName,
                role=rol_id.cond,
                profileEngineer=attachmetToAdd,
                TLeaderEngineer=allShippers,
            )
            roko.save()

    return JsonResponse({'State': 'Success'}) 


## Hospital Page

def GetAllGovern(request):
    AllGovern = Governorate.objects.all()

    arr=[]
    for n in list(AllGovern):
        arr.append(n.GovernorateName)
    
    return JsonResponse(arr , safe=False)

def GetFilterHos(request):
    GovernValue = request.GET.get('GovernValue')
    SelCompany = CompanyName.objects.get(companyName="OCD")
    SelGovern = Governorate.objects.get(GovernorateName=GovernValue)
    GetHos = HospitalsAnalyzers.objects.filter(Q(compNam=SelCompany)&Q(Govern=SelGovern))
    print(GetHos)
    arr=[]

    for n in list(GetHos):
        arr.append(n.SerialNumber)
        arr.append(n.HosNam.hospitalName)
        arr.append(n.WorFlo.nameOfWorkFlow)
        arr.append(n.id)
        arr.append(n.Counter)
        arr.append(n.PM)
        arr.append(n.Software)



    return JsonResponse(arr, safe=False)

def GetDiaHos(request):
    GovernValue = request.GET.get('GovernValue')
    SelCompany = CompanyName.objects.get(companyName="Diasys")
    SelGovern = Governorate.objects.get(GovernorateName=GovernValue)
    GetHos = HospitalsAnalyzers.objects.filter(Q(compNam=SelCompany)&Q(Govern=SelGovern))
    arr=[]

    for n in list(GetHos):
        arr.append(n.SerialNumber)
        arr.append(n.HosNam.hospitalName)
        arr.append(n.WorFlo.nameOfWorkFlow)
        arr.append(n.id)
        arr.append(n.Counter)
        arr.append(n.PM)
        arr.append(n.Software)



    return JsonResponse(arr, safe=False)

def GetHosJob(request):
    SerialNo = request.GET.get('HosId')

    GetHosAnalyzer = HospitalsAnalyzers.objects.get(SerialNumber=SerialNo)
    GetJobSheets = JobSheet.objects.filter(Hospital=GetHosAnalyzer.id)
    arr=[]
    arrAssem=[]
    arrsum =[]
    arrPri = []
    arrl=[]
    arrItems=[]
    for n in list(GetJobSheets):
        l=0
        arrsum.clear()
        arr.append(n.mainUser.username)
        arr.append(n.dateOfJobSheet)
        arr.append(n.Note)
        selImg = JobSheetImg.objects.get(Inpu=n.id)
        arr.append(selImg.images.url)
        
        selAssem = AssembledStore.objects.filter(JobSheet=n.id)
        for m in list(selAssem):
            print(m.ItemName)
            arrAssem.append(m.ItemName)
            arrsum.append(m.Price)
            l=l+1
        ans = sum(arrsum)
        arrl.append(l)
        arrPri.append(ans)
    arrItems.append(arrAssem)
    
    

    response={
        'arr':arr,
        'arrAssem':arrAssem,
        'arrPri':arrPri,
        'arrl':arrl,
        'arrItems':arrItems
    }
        

    return JsonResponse(response, safe=False)       

def GetHosSpare(request):
    SerialNum = request.GET.get('HosId')
    selHoasAna = HospitalsAnalyzers.objects.get(SerialNumber=SerialNum)

    GetSpares = AssembledStore.objects.filter(HosName=selHoasAna.HosNam)

    data =[Item.get_spec() for Item in GetSpares]
    response = {'data':data}

    return JsonResponse(response,safe=False)

def OpenHos(request):
    GetSerial = request.GET.get('HosId')
   
    selHos = HospitalsAnalyzers.objects.get(SerialNumber=GetSerial)
    arr=[]
    arrpart=[]
    arrPrice=[]
    arrpend=[]
    arrPic=[]
    allnames=[]
    arrInvo=[]
    arrTDS=[]

    arr.append(selHos.HosNam.hospitalName)
    arr.append(selHos.WorFlo.nameOfWorkFlow)
    arr.append(selHos.SerialNumber)
    arr.append(selHos.PM)
    arr.append(selHos.Counter)
    arr.append(selHos.Software)
    arr.append(selHos.Ups)
    arr.append(selHos.Stab)
    arr.append(selHos.Earth)

    SelAssem = AssembledStore.objects.filter(HosName=selHos.HosNam)

    for n in list(SelAssem):
        arrpart.append(n.ItemName)
        arrpart.append(n.Dato)

    today = date.today()
    m=1
    while m <13:
        arrpend.clear()
        SelAssemDate = AssembledStore.objects.filter(Q(Dato__year = today.year)&Q(Dato__month=m)&Q(HosName=selHos.HosNam))
        m = m+1
        for k in list(SelAssemDate):
            arrpend.append(k.Price)
        
        # num = SelAssemDate.count()
        arrPrice.append(sum(arrpend))

    selJob = JobSheet.objects.filter(Hospital=selHos)
    for l in list(selJob):
        allnames.append(l.mainUser.username)
        selJobImage = JobSheetImg.objects.get(Inpu=l)
        arrPic.append(selJobImage.images.url)
    arr.append(allnames[-1])

    SelInv = InvoiceNumbero.objects.filter(HosName=selHos.HosNam.hospitalName)

    for i in list(SelInv):
        arrInvo.append(i.InvoiceNumber1)
        arrInvo.append(i.ItemName)
        arrInvo.append(i.PartNumber)
        arrInvo.append(i.Datee)
        arrInvo.append(i.ItemLot)
        arrInvo.append(i.CotNumber1)
        arrInvo.append(i.Price)
        
    FilterTDS = TDS.objects.filter(HosNam=selHos)

    for k in list(FilterTDS):
        arrTDS.append(k.TDS)
        arrTDS.append(k.Datao)

    response={
        'arr':arr,
        'arrpart':arrpart,
        'arrPrice':arrPrice,
        'arrPic':arrPic,
        'arrInvo':arrInvo,
        'arrTDS':arrTDS,
    }

    return JsonResponse(response,safe=False)

def SearchOCDHosp(request):
    searchVal = request.GET.get('searchVal')
    selHos = Hospitals.objects.filter(hospitalName__icontains = searchVal)
    SelComp = CompanyName.objects.get(companyName="OCD")
    arr=[]
    for m in list(selHos):
        GetHos = HospitalsAnalyzers.objects.filter(Q(HosNam=m)&Q(compNam=SelComp))
        for n in list(GetHos):
            arr.append(n.SerialNumber)
            arr.append(n.HosNam.hospitalName)
            arr.append(n.WorFlo.nameOfWorkFlow)
            arr.append(n.id)
            arr.append(n.Counter)
            arr.append(n.PM)
            arr.append(n.Software)
        
    return JsonResponse(arr, safe=False)

def SearchDiaHosp(request):
    searchVal = request.GET.get('searchVal')
    selHos = Hospitals.objects.filter(hospitalName__icontains = searchVal)
    SelComp = CompanyName.objects.get(companyName="Diasys")
    arr=[]
    for m in list(selHos):
        GetHos = HospitalsAnalyzers.objects.filter(Q(HosNam=m)&Q(compNam=SelComp))
        for n in list(GetHos):
            arr.append(n.SerialNumber)
            arr.append(n.HosNam.hospitalName)
            arr.append(n.WorFlo.nameOfWorkFlow)
            arr.append(n.id)
            arr.append(n.Counter)
            arr.append(n.PM)
            arr.append(n.Software)
        
    return JsonResponse(arr, safe=False)
## Index Page

def returnFun(request):

    myUser = request.user

    itemid = request.GET.get('ItemId')
    RemainingQTY = request.GET.get('RemainingQTY')
    AllQty = request.GET.get('AllQty')
    partnum = request.GET.get('parto')
    actlot = request.GET.get('loto')
    ook = request.GET.get('stat')
    status_Item = request.GET.get('undro')
    note = request.GET.get('InputNote')
    ACTRemQTY = int(RemainingQTY) -1
    ACToQTY = int(AllQty)-1

    Item = ItemInput.objects.get(partNumber=partnum)
    # SelectLot = Lot.objects.get(Q(Loto = actlot)&Q(JNum=partnum))
    if actlot != "Null":
        SelectLot = Lot.objects.get(Q(Loto = actlot)&Q(JNum=partnum))
        xx = SelectLot.LotQTY + 1
    else:
        if ook == 'Undertest'and RemainingQTY == "1":
            Undertest.objects.create(
                nameOfItem = Item.nameOfItem,
                mainUser = myUser,
                dateOfArrival = date.today(),
                partNumber = Item.partNumber,
                # LotNum = actlot,
                Note = note,
                Status=status_Item,
                Item_Model_compName = Item.Item_Model_compName,
                Item_Model_compUnit = Item.Item_Model_compUnit,
                Item_Model_workFlow = Item.Item_Model_workFlow,
            )
            BookStore.objects.get(pk=itemid).delete()
            return JsonResponse(note, safe=False)

    
    if ook == 'Pending'and RemainingQTY == "1":
        ook = "Ok"
        
        BookStore.objects.filter(pk=itemid).update(StatusOfItem=ook,RemainingQTY=ACTRemQTY,QTYOfItem=ACToQTY)
        Lot.objects.filter(pk=SelectLot.id).update(LotQTY=xx)
        return JsonResponse(ook, safe=False)

    elif ook == 'Pending'and RemainingQTY != "1":

        BookStore.objects.filter(pk=itemid).update(RemainingQTY=ACTRemQTY,QTYOfItem=ACToQTY)
        Lot.objects.filter(pk=SelectLot.id).update(LotQTY=xx)
        return JsonResponse(ook, safe=False)
    
    elif ook == 'Ok'and RemainingQTY == "0":
        alr = ("Not Enough QTY")
        return JsonResponse(alr, safe=False)
    
    elif ook == 'Undertest'and RemainingQTY == "0":
        alr = ("Not Enough QTY")
        return JsonResponse(alr, safe=False)
    
def searchSN(request):
    SN = request.GET.get('SN')
    arr=[]
    try:
        searchHos = HospitalsAnalyzers.objects.get(SerialNumber=SN)
        arr=[]
        arrDates=[]
        arr.append(searchHos.PM)
        SelHos = Hospitals.objects.get(id = searchHos.HosNam.id)
        try:
            selLamp = AssembledStore.objects.filter(Q(partNumber="356666")&Q(HosName=SelHos.id)&Q(Dato__lte=date.today()))
            for n in list(selLamp):
                arrDates.append(n.Dato)
            arrDates.sort()
            arr.append(arrDates[-1])
        except:
            try:
                    selLamp = AssembledStore.objects.filter(Q(partNumber="960115")&Q(HosName=SelHos.id)&Q(Dato__lte=date.today()))
                    for n in list(selLamp):
                        arrDates.append(n.Dato)
                    arrDates.sort()
                    arr.append(arrDates[-1])
            except:
                try:
                        selLamp = AssembledStore.objects.filter(Q(partNumber="910553")&Q(HosName=SelHos.id)&Q(Dato__lte=date.today()))
                        for n in list(selLamp):
                            arrDates.append(n.Dato)
                        arrDates.sort()
                        arr.append(arrDates[-1])
                except:
                        selLamp = AssembledStore.objects.filter(Q(partNumber="960505")&Q(HosName=SelHos.id)&Q(Dato__lte=date.today()))
                        for n in list(selLamp):
                            arrDates.append(n.Dato)
                        arrDates.sort()
                        arr.append(arrDates[-1])

        return JsonResponse(arr , safe=False)
    except:

    
        return JsonResponse(arr , safe=False)
    
def GetWorkFlowUsers(request):
    current_user1 = request.user
    user_staff = current_user1.is_superuser
    arr=[]
    if user_staff == True:
        GetAllUser = User.objects.all()
        for n in list(GetAllUser):
            arr.append(n.id)
            arr.append(n.username)
        
        return JsonResponse(arr , safe=False)
    else:
        arr.append(current_user1.id)
        arr.append(current_user1.username)
        return JsonResponse(arr , safe=False)

def GetWorkFlow(request):
    # getUser = request.user
    er=[]
    UserId = request.GET.get('UserId')
    selUser = User.objects.get(id=UserId)
    er.append(selUser)

    BtnVal = request.GET.get('BtnVal')
    arr=[]
    i = 1
    arr.clear()
    while i < 31:
        currentDate = str(date.today().year) +'-'+ str(BtnVal) +'-'+ str(i)
        selWork = WorkFlowLine.objects.filter(Q(UserName=er[0])&Q(date=currentDate))
        
        if selWork :
            for n in list(selWork):
                arr.append(n.date)
                arr.append(n.HosName.hospitalName)
        i = i +1
    print(arr)
    er.clear()
    return JsonResponse(arr,safe=False)

def GetAllInvoices(request):
    arr=[]
    arrHos=[]
    arrNam=[]
    arrlen=[]

    GetPending = InvoiceStatus.objects.get(Status="Pending")
    GetAllHos = Hospitals.objects.all()
    for n in list(GetAllHos):
        GetAllInvo = AssembledStore.objects.filter(Q(HosName=n.id)&Q(InvoNum="Pending")&~Q(Cot="Submitting"))
        
        if GetAllInvo:
            arrNam.append(n.hospitalName)
            arr.clear()
            l = 0
            for m in list(GetAllInvo):
                getJobSheet = JobSheet.objects.get(id=m.JobSheet.id)
                SelJobImg = JobSheetImg.objects.get(Inpu=getJobSheet)
                arr.append(m.Dato)
                arr.append(SelJobImg.images.url)
                arr.append(m.ItemName)
                arr.append(m.partNumber)
                arr.append(m.Price)
                arr.append(m.nameOfUser.username)
                arr.append(m.Item_Model_workFlow.nameOfWorkFlow)
                arr.append(m.id)
                arr.append(m.Cot)
                arr.append(m.InvoNum)
                l=l+1
            arrlen.append(l)
            arrHos +=(arr)
            

    response={
        'arrNam':arrNam,
        'arrlen':arrlen,
        'arrHos':arrHos
    }
    return JsonResponse(response , safe=False)

def GetItems(request):

    selUser = request.user

    GetItems = BookStore.objects.filter(nameOfUser=selUser.id)
    arr=[]

    for n in list(GetItems):
        if n.RemainingQTY > 0: 
            selItem = ItemInput.objects.get(id=n.NameOfItem.id)
            getImage = Imag3.objects.get(Inpu=selItem)
            arr.append(selItem.id)
            arr.append(selItem.nameOfItem)
            arr.append(getImage.images.url)
    
    return JsonResponse(arr , safe=False)

def GetAllHos(request):
    GetHos = HospitalsAnalyzers.objects.all()
    arr=[]

    for n in list(GetHos):
        arr.append(n.SerialNumber)
        arr.append(n.HosNam.hospitalName)
        arr.append(n.WorFlo.nameOfWorkFlow)
        arr.append(n.id)
        arr.append(n.Counter)
        arr.append(n.PM)
        arr.append(n.Software)


    return JsonResponse(arr, safe=False)

def GethosName(request):
    Hoss = Hospitals.objects.all()
    arr=[]
    for n in list(Hoss):
        arr.append(n.hospitalName)

    return JsonResponse(arr, safe=False)

def hosSearch(request):
    searchVal = request.GET.get('searchVal')
    arrayOfNames = []

    allBoard = Hospitals.objects.filter(hospitalName__icontains = searchVal)
    for n in list(allBoard):
       arrayOfNames.append(n.hospitalName)
    return JsonResponse(arrayOfNames, safe=False)

def GetMySpareParts(request):
    SelUser = request.user

    selSpare = BookStore.objects.filter(nameOfUser=SelUser.id)
    arr=[]
    for n in list(selSpare):
        if n.RemainingQTY > 0:
            arr.append(n.id)
            arr.append(n.NameOfItem.nameOfItem)
            arr.append(n.BookedLot.Loto)
            arr.append(n.RemainingQTY)
            selImg = Imag3.objects.get(Inpu=n.NameOfItem.id)
            arr.append(selImg.images.url)
            arr.append(n.NameOfItem.partNumber)
    return JsonResponse(arr, safe=False)

def GetPartNumber(request):
    ItemId = request.GET.get('GetId')

    selBooked = BookStore.objects.get(id=ItemId)

    selItem = ItemInput.objects.get(id=selBooked.NameOfItem.id)
    partNum = selItem.partNumber
    return JsonResponse(partNum, safe=False)

@csrf_exempt
def SendSubmitForm(request):
    
    user = request.user

    Hospital_name = request.POST.get('HosName')
    tds = request.POST.get('tds')
    Dato_item = request.POST.get('BookDate')
    Note = request.POST.get('note')
    checkVal = request.POST.get('checkVal')
    checkValUps = request.POST.get('checkValUps')
    checkValStab = request.POST.get('checkValStab')
    checkValEarth = request.POST.get('checkValEarth')
    counte = request.POST.get('counter')
    Softwar = request.POST.get('Software')


    
   

    HosName = Hospitals.objects.get(hospitalName = Hospital_name)
    

    ## To get Hospital Company
    SelHospital = Hospitals.objects.get(hospitalName = Hospital_name)
    SelSerial = HospitalsAnalyzers.objects.get(HosNam=SelHospital.id)

    # to create TDS
    if tds !="":
        form = TDS.objects.create(
            TDS = tds,
            HosNam = SelSerial,
            Datao = Dato_item,
        )

    ## To Update Hospitals Analyzers
    HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(Ups=checkValUps)
    HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(Stab=checkValStab)
    HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(Earth=checkValEarth)

    if checkVal == "Yes":
        checkVal = date.today()
        HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(PM=checkVal)
        
    if counte != "":
        HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(Counter=counte)

    if Softwar != "":
        HospitalsAnalyzers.objects.filter(HosNam=SelHospital.id).update(Software=Softwar)


    SelCompany = CompanyName.objects.get(id=SelSerial.compNam.id)
    typo = CompanyUnits.objects.get(id = SelSerial.compUni.id)
    worknamo = WorkFlow.objects.get(id = SelSerial.WorFlo.id)

    ## Create Job Sheet
    NewJobSheet = JobSheet.objects.create(
        mainUser = user,
        dateOfJobSheet = Dato_item,
        Note = Note,
        Item_Model_compName = SelCompany,
        Item_Model_compUnit = typo,
        Item_Model_workFlow = worknamo,
        Hospital = SelSerial,
    )

    ## Create Assembeled Store
    arrPart = []
    arrInv=[]
    for f in request.POST.getlist('partNumber[]'):
        arrPart.append(f)
      
    for k in request.POST.getlist('InvData[]'):
        arrInv.append(k)

    j=0 
    if len(arrPart) > 0:
        for m in request.POST.getlist('IdArr[]'):
            f = arrPart[j]
            InvSta = arrInv[j]
            selectItem = BookStore.objects.get(id=m)
            ook = selectItem.StatusOfItem
            ido = selectItem.id
            cerQTY = selectItem.RemainingQTY

             ## Invoice Conditions
            if InvSta == "Pending":
                Quo = "Submitting"
            else:
                Quo = "None"

            Status = InvoiceStatus.objects.get(Status = InvSta)
            QuoStatus = QuotationStatus.objects.get(Status = Quo)

            Item = ItemInput.objects.get(id=selectItem.NameOfItem_id)
            ACTa = int (cerQTY) - 1

            Lotselection = Lot.objects.get(Q(JNum=f)&Q(Loto=selectItem.BookedLot.Loto))
            inpId = Lotselection.id
            actnum = int(Lotselection.AllLotQTY) - int(1)

            ido = selectItem.id
            namo = Item.nameOfItem
            parto = Item.partNumber
            qtyo = selectItem.QTYOfItem
            CompName = Item.Item_Model_compName
            compUni = Item.Item_Model_compUnit
            compwork = Item.Item_Model_workFlow

            prico = Price.objects.get(partNumber=parto)
            costo = prico.Price

            
            ItemID = BookStore.objects.get(id = ido)

            if ook == 'Undertest'and cerQTY == "1":
                    BookStore.objects.filter(pk=ido).update(StatusOfItem="Used")
                    BookStore.objects.filter(pk=ido).update(RemainingQTY=0)
            if ook == 'Pending'and cerQTY == "1":
                ook = "Ok"
                BookStore.objects.filter(pk=ido).update(StatusOfItem="Ok")
                BookStore.objects.filter(pk=ido).update(RemainingQTY=ACTa)
                Lot.objects.filter(pk=inpId).update(AllLotQTY=actnum)
            if ook == 'Pending'and cerQTY != "1":

                BookStore.objects.filter(pk=ido).update(RemainingQTY=ACTa)
                Lot.objects.filter(pk=inpId).update(AllLotQTY=actnum)

            if ook == 'Ok'and cerQTY == "0":
                alr = ("Not Enough QTY")
                return JsonResponse(alr, safe=False)
            
            Assembled = AssembledStore.objects.create(
                ItemId = ido,
                ItemName = namo,
                Dato = Dato_item,
                QTY = qtyo,
                Price = costo,
                partNumber = f,
                nameOfUser = user,
                Item_Model_compName = CompName,
                Item_Model_compUnit = compUni,
                Item_Model_workFlow = compwork,
                HosName = HosName,
                Invo=Status,
                Cot=QuoStatus.Status,
                LotNum=Lotselection,
                InvoNum=Status.Status,
                JobSheet = NewJobSheet,

            )
            Assembled.save()
        
            if(QuoStatus =="Submitting"):
                QuoNumbero = CotNumber.objects.create(
                    Status = Status,
                    Itemo = ItemID,
                ) 
                QuoNumbero.save()
            
            if(Status =="Pending"):
                InvoiceNumbero = CotNumber.objects.create(
                    Status = Status,
                    Itemo = ItemID,
                ) 
                InvoiceNumbero.save()
            j = j+1

    
    ## Upload Images 
    
    mypath3 = os.path.join(settings.MEDIA_ROOT, 'temporary','JobSheets')
    onlyfiles = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]
    for item_att in onlyfiles:
        item_att =  'temporary/'+'JobSheets/'+item_att
        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
        file_type, file_encoding = mimetypes.guess_type(file_path)
        fi = open(file_path, 'rb')
        local_file = File(fi)
        fileName = os.path.basename(local_file.name).split('``__``')[0]

        attachmetToAdd = JobSheetImg.objects.create(images=local_file,Inpu=NewJobSheet)
        attachmetToAdd.save()
    
        local_file.close()
        default_storage.delete(item_att)

    
    ## WORK FLOW Line
    SelUser = User.objects.get(username=user)
    
    CreateWorkFlow = WorkFlowLine.objects.create(
        date = Dato_item,
        UserName = SelUser,
        HosName = HosName,
    )
    CreateWorkFlow.save()
    return JsonResponse(Hospital_name, safe=False)

@csrf_exempt
def uploadFiles8(request):
    
    mypath3 = os.path.join(settings.MEDIA_ROOT, 'temporary','JobSheets')
    onlyfiles = [f for f in listdir(mypath3)]
    for item_att in onlyfiles:
        item_att =  'temporary/'+'JobSheets/'+item_att
        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
        fi = open(file_path, 'rb')
        local_file = File(fi)
        local_file.close()
        default_storage.delete(item_att)

    if request.method=='POST':
        
        for f in request.FILES.getlist('file'):
            upload_to = 'temporary/JobSheets/'
            ext = f.name.split('.')[-1]
            filename = '{}.{}'.format(f.name.split('.')[0] + '.' + ext + '``__``' + uuid4().hex, ext)
            default_storage.save(os.path.join(upload_to, filename), f)
    return JsonResponse({'State': 'Success'})

def AddPendingInvo(request):
    ItemId = request.GET.get('ItemId')
    invNum = request.GET.get('IvnNumbro')
    SelFoc = InvoiceStatus.objects.get(Status="OK")
    SelItem = AssembledStore.objects.get(pk=ItemId)
    cartable3 = InvoiceNumbero.objects.create (
            ItemName=SelItem.ItemName,
            PartNumber=SelItem.partNumber,
            HosName=SelItem.HosName.hospitalName,
            ItemLot = SelItem.LotNum.Loto,
            CotNumber1 = SelItem.Cot,
            Datee=date.today(),
            InvoiceNumber1=invNum,
            Price=SelItem.Price,
        )
    cartable3.save()
    AssembledStore.objects.filter(pk=ItemId).update(InvoNum=invNum,Invo=SelFoc)
    

    return JsonResponse({'state':'response'})