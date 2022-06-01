from django.shortcuts import render,redirect
from.models import *
from django.db.models import Q
from msg_and_prof.views import msgfun,cmtfun,order
from msg_and_prof.models import orders
from cart.models import cart_id
from cart.views import s_id
from statistic.models import loginstats
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.


def home(request,ct_slug=None):
    ord_recent=[]
    orderes=''
    msg=''
    ct=ct_slug
    ctg=category.objects.all()
    obj=productstable.objects.all().filter(offers=True)
    if not cart_id.objects.filter(userid=request.user.id).exists():
        s=cart_id(userid=request.user.id)
        s.save()
    if request.user.is_authenticated:
        recent = orders.objects.filter(userid=request.user.id)
        date=[]
        for i in recent:
            if i.done_date not in date:
                date.append(i.done_date)
                itms = orders.objects.filter(userid=request.user.id,done_date=i.done_date)
                items={'date':i.done_date,'items':itms}
                ord_recent.append(items)
        orderes = order(request)
        msg = msgfun(request)
        userid = cart_id.objects.get(userid=request.user.id)
        try:
            num = loginstats.objects.get(user=userid,date=datetime.date.today())
            num.home=num.home + 1
            num.save()
        except ObjectDoesNotExist:
            s=loginstats(user=userid,date=datetime.date.today(),home=1)
            s.save()
    else:
        key = s_id(request)

        key = s_id(request)

        if not cart_id.objects.filter(session=key).exists():
            if key is not None:
                s = cart_id(session=key)
                s.save()
        userid=cart_id.objects.get(session=key)
        try:
            num = loginstats.objects.get(user=userid,date=datetime.date.today())
            num.home=num.home + 1
            num.save()
        except ObjectDoesNotExist:
            s=loginstats(user=userid,date=datetime.date.today(),home=1)
            s.save()

    if ct_slug is not None:
        obj=productstable.objects.all().filter(categ__slug=ct_slug)
        return render(request, 'base.html', {'obj': obj, 'ctg': ctg,'ct':ct,'msg':msg,'ord':orderes,'ord_recent':ord_recent})

    return render(request,'home.html',{'obj':obj,'ctg':ctg,'ct':ct,'msg':msg,'ord':orderes,'ord_recent':ord_recent})

def details(request,id):
    obj=productstable.objects.get(id=id)
    cmt=cmtfun(id)
    return render(request,'detail.html',{'obj':obj,'cmt':cmt})

def search(request):

    search=request.GET.get('search')
    obj=productstable.objects.filter(Q(name__contains=search) | Q(desc__contains=search))
    return render(request, 'search.html', {'obj': obj})

def catg(request,ct_slug):
    msg=''
    ct=ct_slug
    if request.user.is_authenticated:
        msg = msgfun(request)
    ctg=category.objects.all()
    obj=productstable.objects.all().filter(categ__slug=ct_slug)
    return render(request, 'home.html', {'obj': obj, 'ctg': ctg,'ct':ct,'msg':msg})

def details_ord(request,date):
    itms = orders.objects.filter(userid=request.user.id, done_date=date)
    return render(request,'ord.html',{'items':itms})