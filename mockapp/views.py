from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from utils.common import *
from django.views.decorators.http import *
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger("mockapp.views")



def loginmsg(request):
    return fail_jsonresponse("-1","登入信息已过期，请先登入")

@require_POST
def register(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    if username and password and email:
        if User.objects.filter(username=username).count()>0:
            logger.info("该账号已被注册")
            return fail_jsonresponse("该账号已被注册",-4)
        else:
            try:
                user = User.objects.create_user(username,password=password,email=email)
                user.save()
                logger.info("注册成功")
                return success_jsonresponse("注册成功",100000)
            except Exception as e:
                logger.error(e)
                logger.error("系统错误")
                return fail_jsonresponse("系统错误",999999)
    elif  username == "" or username == None:
        logger.info("账号不能为空")
        return fail_jsonresponse("账号不能为空",-1)
    elif password == "" or password == None:
        logger.info("密码不能为空")
        return fail_jsonresponse("密码不能为空",-2)
    else:
        logger.info("邮箱不能为空")
        return fail_jsonresponse("邮箱不能为空",-3)


@require_POST
def login(request):

    usr = json.loads(request.body)
    username = usr.get("username")
    password = usr.get("password")
    if username and password:
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            logger.info("登入成功")
            return success_jsonresponse("登入成功",100000,data={"username":user.username,"email":user.email})
        else:
            logger.info("登入失败,请检查账号密码是否正确")
            return fail_jsonresponse("登入失败,请检查账号密码是否正确",-1)
    else:
        logger.info("账号密码不允许为空！")
        return fail_jsonresponse("账号密码不允许为空！",-2)

def logout(request):
    try:
        auth.logout(request)
        return success_jsonresponse("注销成功", 100000)
    except Exception as e:
        return fail_jsonresponse("你已经注销了哦",100000)


@require_GET
@login_required
def query_all_user(request):

    users = User.objects.all()
    logger.info("查询成功")
    return success_jsonresponse("查询成功",100000,data=users)

@require_POST
@login_required
def query_by_name(request):
    username = json.loads(request.body).get("username")
    user = User.objects.get(username=username)
    return success_jsonresponse("查询成功",100000,data=user)





