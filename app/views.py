from django.shortcuts import render,redirect
from . models import *

# Create your views here.


# Signup page render definition
def Singup_page(request):
    return render(request,"app/signup.html")


# Signup process logic 

def Signup_logic(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']


        # first check the email is allready register in database or not 

        check = User.objects.filter(email=email)

        if check:
            sms = "User is allerady exist."
            return render(request,"app/signup.html",{'msg':sms})
        else:
            if password == cpassword:
                
                data = User.objects.create( fname = fname , lname = lname , email=email , password = password)
                return render(request,"app/login.html")
            else:
                sms = "Password and confirm password not match!"
                return render(request,"app/signup.html",{'msg':sms})
                
    return render(request,"app/signup.html")
        


# Login page render 
def Login_page(request):
    return render(request,"app/login.html")

# Login logic 

def Login_logic(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']

        # First check the email is allready include in database or not
        # whenever email is in database then get the data for particular user 
        check =  User.objects.get(email=email)

        if check:
            if check.password == password:
                request.session['fname'] = check.fname
                request.session['lname'] = check.lname
                request.session['email'] = check.email

                return redirect('user_data')  

            else:
                sms = "Invalid password! "
                return render(request,"app/login.html",{'msg':sms})
        else:
            sms = "Use does not exist ! "
            return render(request,"app/login.html",{'msg':sms})

    return render(request,"app/login.html")




# Fetch all data for user 
def User_data(request):
    data = User.objects.all()
    return render(request,"app/home.html",{'msg':data})


# let get data for particular use for edit.html page 
def get_Data(request,pk):
    data = User.objects.get(pk=pk)
    return render(request,"app/edit.html",{'msg':data})    

# Let update logic 
def Update_logic(request,pk):
    data = User.objects.get(pk=pk)

    data.fname = request.POST['fname']
    data.lname = request.POST['lname']
    data.email = request.POST['email']
    data.password = request.POST['pass']

    data.save()

    return redirect('user_data')


#  Delete the data 

def Delete_data(request,pk):
    data = User.objects.get(pk=pk)
    data.delete()
    return redirect('user_data')


