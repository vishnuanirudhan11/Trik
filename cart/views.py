from django.shortcuts import render,redirect
from .models import cartlist,cart_id
from django.core.exceptions import ObjectDoesNotExist
from products.models import productstable
from cart.models import recent
from msg_and_prof.models import orders
from django.core.exceptions import MultipleObjectsReturned


# Create your views here.


def s_id(request):
    id=request.session.session_key
    if id is None:
        id=request.session.create()
    return id

def tot_itm(request):
    make_key=s_id(request)
    make_key = s_id(request)
    num_of_items=0
    if request.user.is_authenticated:
        userid= cart_id.objects.get(userid=request.user.id)
        obj=cartlist.objects.filter(user=userid)
        num_of_items =0
        for i in obj:
            num_of_items += i.quantity
    else:
        try:
            try:
                user = cart_id.objects.get(session=request.session.session_key)
            except MultipleObjectsReturned:
                u = cart_id.objects.filter(session=request.session.session_key)
                print()
                h=0
                for i in u:
                    if h != 0:
                        i.delete()
                        h=2
            user = cart_id.objects.get(session=request.session.session_key)
            objct=cartlist.objects.filter(user=user)
            num_of_items = 0
            for i in objct:
                num_of_items += i.quantity
        except ObjectDoesNotExist:
            pass
    return num_of_items

def cart(request):
    if request.user.is_authenticated:
        cartid=cart_id.objects.get(userid=request.user.id)
        ct_list=cartlist.objects.filter(user=cartid)
        total=0
        num=0
        realtot=0
        for i in ct_list:
            realtot += i.productid.price * i.quantity
            if i.productid.offers:
                total=(i.productid.offerprice * i.quantity) + total
            else:
                total = (i.productid.price * i.quantity) + total
            num = num + i.quantity
        savedmoney = realtot - total
    else:
        cartid=cart_id.objects.get(session=request.session.session_key)
        ct_list=cartlist.objects.filter(user=cartid)
        total = 0
        num = 0
        realtot=0
        for i in ct_list:
            realtot += i.productid.price * i.quantity
            if i.productid.offers:
                total = (i.productid.offerprice * i.quantity) + total
            else:
                total = (i.productid.price * i.quantity) + total
            num = num + i.quantity
        savedmoney = realtot - total
                                                                #num=total Quantity
    return render(request,'cart.html',{'ct':ct_list,'tot':total,'num':num,'save':savedmoney})

def add(request,prod_id):
    if request.user.is_authenticated:
        cartid = cart_id.objects.get(userid=request.user.id)
        try:
            item=cartlist.objects.get(user=cartid,productid__id=prod_id)
            item.quantity=item.quantity+1
            item.save()
        except ObjectDoesNotExist:
            pr=productstable.objects.get(id=prod_id)
            s=cartlist(user=cartid,productid=pr,quantity=1)
            s.save()
    else:
        cartid = cart_id.objects.get(session=request.session.session_key)
        try:
            pr = productstable.objects.get(id=prod_id)
            item = cartlist.objects.get(user=cartid, productid=pr)
            item.quantity = item.quantity + 1
            item.save()
        except ObjectDoesNotExist:
            prod=productstable.objects.get(id=prod_id)
            s = cartlist(user=cartid, productid=prod, quantity=1)
            s.save()
    return redirect('cart')

def minus(request,prod_id):
    if request.user.is_authenticated:
        cartid = cart_id.objects.get(userid=request.user.id)
        item=cartlist.objects.get(user=cartid,productid__id=prod_id)
        if item and item.quantity>1:
            item.quantity=item.quantity-1
            item.save()
        elif item:
            s=cartlist.object.get(user=cartid,productid__id=prod_id)
            s.delete()
    else:
        cartid = cart_id.objects.get(session=request.session.session_key)
        item=cartlist.objects.get(user=cartid,productid__id=prod_id)
        if item and item.quantity > 1:
            item.quantity = item.quantity - 1
            item.save()
        elif item:
            item.delete()
    return redirect('cart')

def delete(request,prod_id):
    if request.user.is_authenticated:
        cartid = cart_id.objects.get(userid=request.user.id)
        dele=cartlist.objects.get(user=cartid,productid__id=prod_id)
        dele.delete()
    else:
        cartid = cart_id.objects.get(session=request.session.session_key)
        dele = cartlist.objects.get(user=cartid, productid__id=prod_id)
        dele.delete()
    return redirect('cart')

def checkout(request):
    if request.user.is_authenticated:
        obj=cartlist.objects.filter(user__userid=request.user.id)
        cartid = cart_id.objects.get(userid=request.user.id)
        for i in obj:
            ord_check = orders.objects.filter(userid=request.user.id, prodid=i.productid, curstats=False, cancel=False)
            if ord_check.exists():
                ord = orders.objects.get(userid=request.user.id, prodid=i.productid, curstats=False, cancel=False)
                if i.productid.offers:
                    money=i.productid.offerprice
                else:
                    money=i.productid.price
                if ord.boughtprice == money:
                    ord.quan = ord.quan + i.quantity
                    ord.save()
                else:
                    s = orders(userid=request.user.id, prodid=i.productid, boughtprice=money,
                               quan=i.quantity, phone=request.user.phone)
                    s.save()


            else:
                if i.productid.offers:
                    price=i.productid.offerprice
                else:
                    price=i.productid.price
                s=orders(userid=request.user.id, prodid=i.productid, boughtprice=price,
                         quan=i.quantity,phone=request.user.phone)
                s.save()
        save=recent(userid=cartid,stats=True)
        save.save()
        obj.delete()
    else:
        phone=request.POST.get('phone')
        obj = cartlist.objects.filter(user__session=request.session.session_key)
        cartid = cart_id.objects.get(session=request.session.session_key)
        for i in obj:
            ord_chek = orders.objects.filter(prodid=i.productid, session=request.session.session_key, curstats=False, cancel=False, )
            if ord_chek.exists():
                ord = orders.objects.get(prodid=i.productid, session=request.session.session_key, curstats=False,
                                         cancel=False, )
                if i.productid.offers:
                    money = i.productid.offerprice
                else:
                    money = i.productid.price
                if ord.boughtprice == money:
                    ord.quan = ord.quan + i.quantity
                    ord.save()
                else:
                    s = orders( prodid=i.productid, session=request.session.session_key, boughtprice=money,
                               quan=i.quantity, phone=phone)

            else:
                if i.productid.offers:
                    price = i.productid.offerprice
                else:
                    price = i.productid.price
                s = orders(prodid=i.productid, session=request.session.session_key, boughtprice=price,
                           quan=i.quantity, phone=phone)
                s.save()
        save = recent(userid=cartid,stats=True)
        save.save()
        obj.delete()
    return redirect('home')
