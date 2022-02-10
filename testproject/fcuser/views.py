from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm
import pandas as pd
from pandas import DataFrame
import datetime
import cx_Oracle
import os
# Create your views here.
LOCATION = r"C:\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

connection = cx_Oracle.connect("system", "oracle", "192.168.1.210:1521/kcluster")
cursor = connection.cursor()

def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    form = LoginForm()
    return render(request,'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('name',None)
        phonenumber = request.POST.get('phonenumber',None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        duplicate_check = False
        cursor.execute("SELECT PHONENUMBER FROM KCLUSTER.TBUSER")

        x = cursor.fetchall()
        df_oracle = pd.DataFrame(x)
        if not (name and password and re_password and phonenumber):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 서로 다릅니다.'
        else:
            for i in df_oracle[0]:
                if int(phonenumber) == i:
                    res_data['error'] = '이미 가입된 번호입니다.'
                    duplicate_check = True

            if duplicate_check == False:
                now = datetime.datetime.now()
                fcuser = Fcuser(
                    name = name,
                    phonenumber = phonenumber,
                    password = make_password(password),
                    re_password = make_password(re_password),
                    created_at = now
                )
                cursor.execute("INSERT INTO KCLUSTER.TBUSER (NAME, PHONENUMBER, PASSWORD, PASSWORD_CHECK, CREATED_AT) VALUES (:1,:2,:3,:4,:5)", [fcuser.name, fcuser.phonenumber, fcuser.password, fcuser.re_password, fcuser.created_at])
                connection.commit()

        return render(request, 'register.html', res_data)
