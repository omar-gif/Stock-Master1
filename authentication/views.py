# from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from  django.contrib.auth.models import User
# from django.contrib import messages

# # Create your views here.
# from discussion_board import settings


# def home(request):
#     return render(request,"authentication/index.html")

# def signup(request):

#     if request.method == "POST" :
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']


#         myuser = User.objects.create_user(username, email , pass1  )
#         myuser.first_name = fname
#         myuser.last_name = lname

#         myuser.save()
        
#         messages.success(request,"Your Account has been successfully created .\n we have sent you a confermation email")


#         # welcome message
#         subject = "welcome to omars world"
#         message = "hello"+myuser.first_name+"!\n"+"welcome to our transition company\n thank you for visiting our website \n\n thank you \n\n Omae Eldebeis"
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [myuser.email]
#         send_mail(subject,message,from_email,to_list,fail_silently=True)
#         return redirect('signin')
#     return render(request,"octopus-master/octopus/pages-signup.html")

# def signin(request):

#     if request.method == "POST":
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username,password=pass1)

#         if user is not None:
#             login(request,user)
#             fname = user.first_name
#             return render(request,"authentication/index.html",{'fname':fname})
#         else:
#             messages.error(request,"Bad credentials")
#             return redirect('home')
#     return render(request,"octopus-master/octopus/pages-signin.html")

# def signout(request):
#     logout(request)
#     messages.success(request,"logged out successfuly")
#     return redirect('pages-signin.html')

# def signinPage(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username,password=pass1)

#         if user is not None:
#             login(request,user)
#             fname = user.first_name
#             print("iam signed in")
#             print(fname)
#             return redirect('/')
#         else:
#             messages.error(request,"Bad credentials")
#             return redirect('home')
#     return render(request, 'octopus-master/octopus/pages-signin.html')