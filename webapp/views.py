from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import teacher
from .models import timetable
from .models import student,student_marks
from django.shortcuts import redirect
import random
from . import viewextension
# Create your views here.
def home(request):
    if request.session.session_key is None :#or request.session['e_id']:
        return render(request,'login.html')
    #request.session.flush()
    #emp_id=active.objects.get(id=1).e_id
    emp_id=request.session.get('e_id')
    teacherlist = teacher.objects.filter(e_id=emp_id)
    tclass,tname='',''
    for i in teacherlist:
        tclass=i.class_teacher_of
        tname = i.first_name +' '+ i.last_name
        tid= i.id
    topper=viewextension.classTopper(tclass)
    studentlist= student.objects.filter(class_in=tclass)
    stucount= student.objects.filter(class_in=tclass).count()
    malestu=studentlist.filter(gender='male').count()
    femalestu = studentlist.filter(gender='female').count()
    data={'male':malestu,'female':femalestu,'totstu':stucount}
    Timetable= timetable.objects.filter(e_id=tid)
    return render(request,'index.html',{'teacher':teacherlist,'class':tclass,'name':tname,'student':studentlist,'data':data,'timetable':Timetable,'tname':topper[0],'marks':topper[1]})

def login(request):
    #print(request.session)
    #print(dir(request.session))
    #request.session.set_expiry(300)
    #print(request.session.session_key)
    #request.session['itech'] = 'divyanshu'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = teacher.objects.get(email=username,password=password)
        except:
            user = 'None'
        print(user)
        if str(user) != '<QuerySet []>' and user != 'None':
            #active_usr = active.objects.filter(id=1)
            #active_usr.update(e_id=user.e_id)
            request.session['e_id']=user.e_id
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    request.session.flush()
    return render(request,'login.html')

def profile(request):
    if request.session.session_key is None :#or request.session['e_id']:
        return render(request,'login.html')
    emp_id=request.session.get('e_id')
    teacherlist = teacher.objects.filter(e_id=emp_id)
    cover=['a','b']
    return render(request,'profile.html',{'teacher':teacherlist,'cover':random.choice(cover)})

def report(request):
    if request.session.session_key is None :#or request.session['e_id']:
        return render(request,'login.html')
    emp_id=request.session.get('e_id')
    teacherlist = teacher.objects.filter(e_id=emp_id)
    tclass,tname='',''
    for i in teacherlist:
        tclass=i.class_teacher_of
        tname = i.first_name +' '+ i.last_name
        tid= i.id
    studentlist= student.objects.filter(class_in=tclass)
    return render(request,'report.html',{'student':studentlist})
def report_final(request):
    if request.session.session_key is None :#or request.session['e_id']:
        return render(request,'login.html')
    if request.method == 'POST':
        studname = request.POST['name']
        remarks = request.POST['remarks']
        height = request.POST['Height']
        weight = request.POST['weight']
        ped = request.POST['ped']
        wed = request.POST['wed']
        aed = request.POST['aed']
    stuobj = student.objects.filter(adm_no=studname)
    value=stuobj.values()
    value = list(value)
    value = value[0]
    dictadditional={'remark':remarks,'height':height,'weight':weight,'ped':ped,'wed':wed,'aed':aed}
    value.update(dictadditional)
    marks=student_marks.objects.filter(adm_no=studname)
    return render(request,'finalcard.html',{'value':value,'marks':marks})
def updateorcreate(request):
    if request.session.session_key is None :#or request.session['e_id']:
        return render(request,'login.html')
    if request.method == 'POST':
        adm = request.POST['adm']
        sub = request.POST['sub']
        pra = request.POST['pra']
        the = request.POST['the']
    
    print(student_marks.objects.filter(adm_no=adm,subject=sub))
    try:
        marks=student_marks.objects.filter(adm_no=adm,subject=sub)
    except:
        marks = 'None'
    if str(marks) == '<QuerySet []>' or marks == 'None':
        p=student_marks()
        s=student()
        s.adm_no=adm
        p=student_marks()
        p.adm_no=s
        p.subject=sub
        p.marks_in_theory=the
        p.marks_in_practical=pra
        p.save()
        return HttpResponse("Marks added to database!")
    else:
        marks.update(marks_in_theory=the,marks_in_practical=pra)
        return HttpResponse("Marks updated to database!")

def attendance(request):
    return render(request,'attendance.html')

def error_404(request,exception):
    return render(exception,'error404.html')
