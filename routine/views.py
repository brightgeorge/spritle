from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from routine.models import *
import datetime


def index(request):
    context={

    }
    return render(request,'index.html',context)

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if login.objects.filter(username=username,password=password).exists():
            loginobj=login.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Admin':
                tusers=login.objects.all()
                tu=len(tusers)

                tstu = login.objects.all().filter(role='Student')
                ts = len(tstu)

                total_task=task.objects.all().filter(task_status=1)
                ltotal_task=len(total_task)

                tp=task.objects.all().filter(task_type='plus',task_status=1)
                tpl=len(tp)
                tm = task.objects.all().filter(task_type='minus',task_status=1)
                tml = len(tm)
                tt = task.objects.all().filter(task_type='times',task_status=1)
                ttl = len(tt)
                tdb = task.objects.all().filter(task_type='divided_by',task_status=1)
                tdbl = len(tdb)
                ll=0

                yl=[]
                yl.append(tpl)
                yl.append(tml)
                yl.append(ttl)
                yl.append(tdbl)
                yl.append(ll)

                ul=[]
                teul=login.objects.all().filter(user_flage=1)
                ltuel=len(teul)

                tdul = login.objects.all().filter(user_flage=0)
                ltudl = len(tdul)

                ul.append(ltuel)
                ul.append(ltudl)


                request.session['username'] = username
                us = request.session['username']

                context={
                   'user':loginobj,
                    'tus':tu,
                    'tos': ts,
                    'ltotal_tasks':ltotal_task,
                    'y':yl,
                    'yy':ul,
                    'active_user':ltuel,
                    'total_disableusers':ltudl,
                }
                return render(request,'admindashboard/index.html',context)
            if role=='Student':
                print(datetime.datetime.now())
                x=datetime.datetime.now()
                print(x.strftime("%x"))
                print(datetime.date.today())
                request.session['username'] = username
                us = request.session['username']

                tp = task.objects.all().filter(task_type='plus', task_status=1,task_assigned_to=us)
                tpl = len(tp)
                tm = task.objects.all().filter(task_type='minus', task_status=1,task_assigned_to=us)
                tml = len(tm)
                tt = task.objects.all().filter(task_type='times', task_status=1,task_assigned_to=us)
                ttl = len(tt)
                tdb = task.objects.all().filter(task_type='divided_by', task_status=1,task_assigned_to=us)
                tdbl = len(tdb)
                ll = 0

                yl = []
                yl.append(tpl)
                yl.append(tml)
                yl.append(ttl)
                yl.append(tdbl)
                yl.append(ll)
                context={
                    'user': loginobj,
                    'y':yl
                }

                return render(request, 'studentsdashboard/students_dashboard.html', context)
            if role=='Employer':
                return render(request, 'kalyan.html', context={'user': loginobj})
            if role=='staff':
                return render(request, 'kalyan.html', context={'user': loginobj})
            else:
                return render(request,'index.html',context={'user':loginobj})

        else:

            return render(request,'index.html',context={'msg':'User Name or Password Incorrect'})
    else:
        return render(request,'index.html')

def admin_dashboard(request):
    tusers = login.objects.all()
    tu = len(tusers)

    tstu = login.objects.all().filter(role='Student')
    ts = len(tstu)

    total_task = task.objects.all().filter(task_status=1)
    ltotal_task = len(total_task)

    tp = task.objects.all().filter(task_type='plus', task_status=1)
    tpl = len(tp)
    tm = task.objects.all().filter(task_type='minus', task_status=1)
    tml = len(tm)
    tt = task.objects.all().filter(task_type='times', task_status=1)
    ttl = len(tt)
    tdb = task.objects.all().filter(task_type='divided_by', task_status=1)
    tdbl = len(tdb)
    ll = 0

    yl = []
    yl.append(tpl)
    yl.append(tml)
    yl.append(ttl)
    yl.append(tdbl)
    yl.append(ll)

    ul = []
    teul = login.objects.all().filter(user_flage=1)
    ltuel = len(teul)

    tdul = login.objects.all().filter(user_flage=0)
    ltudl = len(tdul)

    ul.append(ltuel)
    ul.append(ltudl)

    context = {
        'tus': tu,
        'tos': ts,
        'ltotal_tasks': ltotal_task,
        'y': yl,
        'yy': ul,
        'active_user': ltuel,
        'total_disableusers': ltudl,
    }
    return render (request,'admindashboard/index.html',context)

#************USER SECTION STARTED HERE ***************

def view_all_users(requst):
    vu=login.objects.filter(user_flage=1)
    context={
        'users':vu
    }
    return render(requst,'admindashboard/users/view_all_users.html',context)

def create_user(request):
    return render(request,'admindashboard/users/user_creation.html')

def user_regi(request):
    itname = request.POST.get('username')
    chkitemname = login.objects.filter(username=itname).exists()
    print('this is m y test uname',chkitemname)
    empcod= request.POST.get('code')
    chkemcod= login.objects.filter(student_id=empcod).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'User name and Employee Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Employee Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'admindashboard/users/user_creation.html', )
    else:
        if request.method == 'POST':
            ucode=request.POST.get('code')
            empname = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            urole = request.POST.get('role')

            udes = request.POST.get('description')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=login()
            uc.student_id = ucode
            uc.student_name = empname
            uc.username = uname
            uc.password = upass
            uc.role = urole

            uc.student_description=udes
            uc.user_flage = chk
            uc.save()

    messages.info(request,'user created sucessfully')
    context = {
        'users': login.objects.filter(user_flage=1),
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def delete_user(request,id):
    de=login.objects.get(id=id)
    de.delete()
    messages.info(request, 'user deleted sucessfully')
    vu = login.objects.all()
    context = {
        'users': login.objects.filter(user_flage=1),
        'users': vu
    }
    return render(request, 'admindashboard/users/view_all_users.html', context)

def user_update(request,id):
    if request.method == 'POST':
        ucode = request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')

        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc = login.objects.get(id=id)
        uc.emp_code = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole

        uc.emp_description = udes
        uc.user_flage = chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_users(request)

    context = {
        'users': login.objects.filter(user_flage=1),
        'sd': login.objects.get(id=id),
    }
    return render(request,'admindashboard/users/update_user.html',context)

#************USER SECTION END HERE ***************

def student_dashboard(request):
    us = request.session['username']
    tp = task.objects.all().filter(task_type='plus', task_status=1, task_assigned_to=us)
    tpl = len(tp)
    tm = task.objects.all().filter(task_type='minus', task_status=1, task_assigned_to=us)
    tml = len(tm)
    tt = task.objects.all().filter(task_type='times', task_status=1, task_assigned_to=us)
    ttl = len(tt)
    tdb = task.objects.all().filter(task_type='divided_by', task_status=1, task_assigned_to=us)
    tdbl = len(tdb)
    ll = 0

    yl = []
    yl.append(tpl)
    yl.append(tml)
    yl.append(ttl)
    yl.append(tdbl)
    yl.append(ll)
    context = {

        'y': yl
    }
    return render(request, 'studentsdashboard/students_dashboard.html', context)

def create_task(request):
    context = {
        'users': login.objects.filter(user_flage=1),

    }
    return render(request,'admindashboard/task/create_task.html',context)


def task_regi(request):
    itname = request.POST.get('code')
    chkitemname = task.objects.filter(task_code=itname).exists()

    if chkitemname == True:
        messages.info(request, 'Task name already exists!. please try another one')
        name = request.session['username']
        context = {
            'users': login.objects.filter(user_flage=1),
            'tc': task.objects.filter(task_status=1, task_assigned_by=name),

        }
        return render(request, 'admindashboard/task/create_task.html',context)
    else:
        if request.method == 'POST':
            tcode = request.POST.get('code')
            tname = request.POST.get('name')
            urole = request.POST.get('role')
            udes = request.POST.get('description')
            ttype = request.POST.get('type')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=task()
            uc.task_code = tcode
            uc.task = tname
            uc.task_assigned_to = urole
            uc.task_description=udes
            uc.task_assigned_by=request.session['username']
            uc.task_type = ttype
            uc.task_status = chk
            uc.save()

    messages.info(request,'task created sucessfully')
    name=request.session['username']
    context = {
        'users': login.objects.filter(user_flage=1),
        'tc': task.objects.filter(task_status=1,task_assigned_by=name),

    }
    return render(request,'admindashboard/task/view_all_task.html',context)

def view_all_task(request):
    name=request.session['username']

    context = {
        'tc': task.objects.filter(task_status=1,task_assigned_by=name),
    }
    return render(request,'admindashboard/task/view_all_task.html',context)

#************ADMIN REPORT START HERE ***************

def detailed_individual_report(request):
    name = request.session['username']
    context = {
        'vt': task.objects.all().filter(task_status=2,task_assigned_by=name).order_by('task_assigned_to')
    }
    return render(request,'admindashboard/reports/detailed_individual_report.html',context)


#************ADMIN REPORT END HERE ***************


#************STUDENTS SECTION START HERE ***************

#****************************STUDENT TASK START HERE****************************

def view_all_student_task(request):
    name = request.session['username']
    context={
        'vt':task.objects.all().filter(task_assigned_to=name).order_by('task_status')
    }
    return render(request,'studentsdashboard/studenttask/view_all_student_task.html',context)


def create_studenttask(request,id):
    if request.method == 'POST':
        def zero(f=None):
            if f is None:
                return 0
            else:
                int(f(0))

        def one(f=None):
            return 1 if f is None else int(f(1))

        def two(f=None):
            return 2 if f is None else int(f(2))

        def three(f=None):
            return 3 if f is None else int(f(3))

        def four(f=None):
            return 4 if f is None else int(f(4))

        def five(f=None):
            return 5 if f is None else int(f(5))

        def six(f=None):
            return 6 if f is None else int(f(6))

        def seven(f=None):
            return 7 if f is None else int(f(7))

        def eight(f=None):
            return 8 if f is None else int(f(8))

        def nine(f=None):
            return 9 if f is None else int(f(9))

        def plus(y):
            return lambda x: x + y

        def minus(y):
            return lambda x: x - y

        def times(y):
            return lambda x: x * y

        def divided_by(y):
            return lambda x: x // y

        def pwr(x, y):
            return x ** y

        def add(x, y):
            return x + y

        dispatcher = {'pwr': pwr, 'add': add}
        fv = {'zero': zero, 'one': one, 'two': two, 'three': three, 'four': four, 'five': five, 'six': six,'seven': seven,'eight': eight, 'nine': nine}
        sv = {'zero': zero, 'one': one, 'two': two, 'three': three, 'four': four, 'five': five, 'six': six,'seven': seven,'eight': eight, 'nine': nine}
        ac = {'plus': plus, 'minus': minus, 'times': times, 'divided_by': divided_by}

        #x = input('enter fvalue')
        #y = input('enter second value')
        #z = input('enter action')

        #print(fv[x](ac[z](sv[y]())))
        #p = fv[x](ac[z](sv[y]()))

        x=request.POST.get('fnum')
        y=request.POST.get('snum')
        z=request.POST.get('act')

        res = fv[x](ac[z](sv[y]()))

        #tc=task.objects.get(id=id)
        tc = task.objects.get(id=id)
        tc.task_answer = res
        tc.task_status = 2

        tc.save()
        return view_all_student_task(request)

    context = {
        'tc': task.objects.all().filter(task_status=1),
        'sd' : task.objects.get(id=id)
    }
    return render(request,'studentsdashboard/studenttask/create_studenttask.html',context)

def student_task_submitting_page(request):
    return render(request,'studentsdashboard/studenttask/create_studenttask.html')



#****************************STUDENT TASK START HERE****************************


#************STUDENTS DASHBOARD END HERE ***************

def students_dashboard(request):

    dt = datetime.datetime.today()
    ddt = dt.date()
    #udt=prayer.objects.all().filter(prayer_date=ddt)
    context={
        'da': ddt,
        'cd':dt,
        #'usdt':udt,

    }

    return render(request,'studentsdashboard/students_dashboard.html',context)

#************STUDENTS DASHBOARD END HERE ***************

#************STUDENTS daily routine START HERE ***************


#************STUDENTS daily routine END HERE ***************

#************STUDENTS PROFILE START HERE ***************

def students_profile(request):
    return render(request,'studentsdashboard/profile/profile.html')

#************STUDENTS PROFILE END HERE ***************

#************STUDENTS SECTION END HERE ***************

def aboutus(request):
    return render(request,'admindashboard/aboutus.html')

def test(request):
    if request.method=='POST':
        da=request.POST.get('d')
        dal=request.POST.get('dl')
        print('this is my da',da)
        print('this is my dal',dal)
    context={
        'pl':1,
    }
    return students_dashboard(request,context)
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request,'index.html')