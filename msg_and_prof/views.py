from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from products.models import productstable
from cart.models import cart_id
from django.core.exceptions import ObjectDoesNotExist
import datetime
import copy

# Create your views here.



def msgfun(request):
    if messages.objects.filter(user__userid=request.user.id).exists():
        obj = messages.objects.filter(user__userid=request.user.id)
    else:
        obj = ''
    return obj


def cmtfun(ids):
    try:
        obj = comment.objects.filter(productid=ids)
    except ObjectDoesNotExist:
        obj = None
        pass
    return obj


def order(request):
    try:
        if request.user.is_authenticated:
            obj = orders.objects.filter(userid=request.user.id,curstats=False,cancel=False)
    except ObjectDoesNotExist:
        obj = None
    return obj


def cmmt(request, ids):
    cmt = request.POST['cmmt']
    userid = User.objects.get(id=request.user.id)
    if request.user.is_authenticated:
        s = comment(productid=ids, cmt=cmt, user=userid)
        s.save()
    return redirect('details', ids)


def msg(request):
    mssg = request.POST['message']
    userid = cart_id.objects.get(userid=request.user.id)
    if not users.objects.filter(userid__id=request.user.id).exists():
        U=User.objects.get(id=request.user.id)
        users.objects.create(userid=U)
    seen=users.objects.get(userid__id=request.user.id)
    s = messages(msgtxt=mssg, user=userid, trikmsg=False,seen=seen)
    s.save()
    ids = User.objects.get(id=request.user.id)
    if users.objects.filter(userid=ids).exists():
        msgs = users.objects.get(userid=ids)
        if msgs.seen == True:
            msgs.seen = False
            msgs.save()

    else:
        users(userid=ids).save()
    return redirect('home')

def msgtrik(request,id):
    mssg = request.POST['msgtxt']
    seen=users.objects.get(userid__id=id)
    userid = cart_id.objects.get(userid=id)
    s = messages(msgtxt=mssg, user=userid, trikmsg=True,seen=seen)
    s.save()
    return redirect('admin_home')

def deletemsg(request):
    todaymsg=messages.objects.all()
    todaymsg.delete()
    # copytoday = copy.deepcopy(todaymsg)
    # d=messages.objects.all()
    # d.delete()
    # for i in copytoday:
    #     s=messages(msgtxt=i.msgtxt,user=i.user,trikmsg=i.trikmsg,time=i.time,seen=i.seen)
    #     s.save()
    return redirect('home')