from ast import Return
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from Project_App.forms import *
from Project_App import models

# Create your views here.
def Home(request):
    if request.method=="POST":
        form=MyForm(request.POST)
        if form.is_valid():
            print("Success")
        else:
            print("Fail")
        
        Admin_Form=AdminForm(request.POST)
        if Admin_Form.is_valid():
            print("Congrats")
        else:
            print("Sorry! try again")

    form=MyForm()
    Admin_Form=AdminForm()
    return render(request,'home.html',{'form':form,'Admin_Form':Admin_Form})

def Registration_Successful(request):
    if request.method=='POST':
        F_name=request.POST.get('First_Name')
        L_name=request.POST.get('Last_Name')
        Name=F_name+" "+L_name

        Registered_Users_Obj= models.Registered_Users()
        Registered_Users_Obj.Username=request.POST.get('Username')
        Registered_Users_Obj.First_Name=F_name
        Registered_Users_Obj.Last_Name=L_name
        Registered_Users_Obj.Email=request.POST.get('Email')
        Registered_Users_Obj.Password=request.POST.get('Password')
        Registered_Users_Obj.save()

        return render(request,'user_profile.html',{'name':Name})


def Login(request):

    return render(request,'login.html')


def Verification(request):
    if request.method=='POST':
        Registered_Users_UName=models.Registered_Users.objects.values_list('Username')
        Registered_Users_Email=models.Registered_Users.objects.values_list('Email')
        Registered_Users_PWord=models.Registered_Users.objects.values_list('Password')

        Form_Input=request.POST.get('Username/Email')
        Form_PWord=request.POST.get('Password')

        for val in range(len(Registered_Users_UName)):
            if (Registered_Users_UName[val][0]==Form_Input or Registered_Users_Email[val][0]==Form_Input) and Registered_Users_PWord[val][0]==Form_PWord:
                F_Name=models.Registered_Users.objects.get(Password=Form_PWord).First_Name
                L_Name=models.Registered_Users.objects.get(Password=Form_PWord).Last_Name
                Name=F_Name+" "+L_Name
                return render(request,'user_profile.html',{'name':Name})
        else:
            return HttpResponse("OOPS! Something Is Wrong")



def Admin_Registration(request):
    if request.method=='POST':
        Form_UName=request.POST.get('Username')
        Form_PWord=request.POST.get('Password')

        Admin_Objects=models.Admin.objects.all()
        for val in range(len(Admin_Objects)):
            if Admin_Objects[val].Username==Form_UName:
                return HttpResponse("This Username is already taken")
        
        else:
            New_Admin=models.Admin()
            New_Admin.Username=Form_UName
            New_Admin.Password=Form_PWord
            New_Admin.save()

            User_Obj=models.Registered_Users.objects.all()
            No_Of_Users=len(User_Obj)

            return render(request,'Welcome_Admin.html',{'name':New_Admin.Username,'No_Of_Users':No_Of_Users})



def Admin_Login(request):
    Admin_Form=AdminForm()
    return render(request,'Admin_Login.html',{'Admin':Admin_Form})


def Admin_Login_Verification(request):
    if request.method=='POST':
        Form_UName=request.POST.get('Username')
        Form_Pword=request.POST.get('Password')
        Admin_Objects=models.Admin.objects.all()
        for data in range(len(Admin_Objects)):
            if Admin_Objects[data].Username==Form_UName:
                if Admin_Objects[data].Password==Form_Pword:
                    User_Obj=models.Registered_Users.objects.all()
                    No_Of_Users=len(User_Obj)

                    New_User=MyForm()
                    return render(request,'Welcome_Admin.html',{'name':Admin_Objects[data].Username,'No_Of_Users':No_Of_Users,'New_User':New_User})
                
                else:
                    return HttpResponse("Invalid Admin Password")
        else:
            return HttpResponse("Invalid Admin Username")

def Add_New_User(request):
    New_User_Obj=models.Registered_Users()
    New_User_Obj.Username=request.POST.get('Username')
    New_User_Obj.First_Name=request.POST.get('First_Name')
    New_User_Obj.Last_Name=request.POST.get('Last_Name')
    New_User_Obj.Password=request.POST.get('Password')
    New_User_Obj.Email=request.POST.get('Email')
    
    New_User_Obj.save()
    return HttpResponse("New User Saved with Username "+New_User_Obj.Username)

def User_Listing(request):
    listed_users=models.Registered_Users.objects.all()
    List_Of_Attributes=['ID','Name','Email','Action']
    List_Of_Id=list()
    List_Of_Name=list()
    List_Of_Email=list()
    Listed_Users_ID=list()
    Listed_Users_Name=list()
    List_Of_ID_And_User_First_Name=list()

    for users in range(len(listed_users)):
        f_name=listed_users[users].First_Name
        l_name=listed_users[users].Last_Name
        name=f_name+" "+l_name
        List_Of_Name.append(name)

        id=listed_users[users].id
        List_Of_Id.append(id)

        email=listed_users[users].Email
        List_Of_Email.append(email)

    combined_list=list()
    for user_id in range(len(List_Of_Id)):
        li=list()
        li.append(List_Of_Id[user_id])
        li.append(List_Of_Name[user_id])
        li.append(List_Of_Email[user_id])
        combined_list.append(li)

    for users in range(len(listed_users)):
        Listed_Users_ID.append(listed_users[users].id)
        Listed_Users_Name.append(listed_users[users].First_Name)
    
    for val in range(len(Listed_Users_ID)):
        li=list()
        li.append(Listed_Users_ID[val])
        li.append(Listed_Users_Name[val])
        List_Of_ID_And_User_First_Name.append(li)

    return render(request,'User_Listing.html',{'Combined_List':combined_list,'listed_users':List_Of_ID_And_User_First_Name})
    
    
    


def Edit_User(request,i):
    User_Obj=models.Registered_Users.objects.get(id=i)
    # return HttpResponse(User_Obj.id)
    EditUser=Edit_User_Form()
    return render(request,'Edit_User.html',{'EditUser':EditUser,'ID_Of_Changed_User':i})

def Delete_User(request,i):
    User_Obj=models.Registered_Users.objects.get(id=i)
    User_Obj.delete()
    return HttpResponse("You deleted the user with user ID="+str(i))

def User_Credentials_Changed(request,i):
    User_Obj=models.Registered_Users.objects.get(id=i)
    User_Obj.Username=request.POST.get('Username')
    User_Obj.First_Name=request.POST.get('First_Name')
    User_Obj.Last_Name=request.POST.get('Last_Name')
    User_Obj.Email=request.POST.get('Email')
    User_Obj.Password=request.POST.get('Password')
    User_Obj.save()
    return HttpResponse("You changed the user with Username= "+ str(User_Obj.Username)+" ID= "+str(User_Obj.id))


def Selected_User_Details(request):
    if request.method=='POST':
        User_Obj=models.Registered_Users.objects.get(id=int(request.POST.get('Users')))
    return render(request,'User_Details.html',{'Username':User_Obj.Username,'First_Name':User_Obj.First_Name,'Last_Name':User_Obj.Last_Name,'Password':User_Obj.Password,'Email':User_Obj.Email,'ID':User_Obj.id})