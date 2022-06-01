from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from msg_and_prof.models import orders
from products.models import productstable, category
import calendar
from django.contrib.auth import get_user_model
from .models import loginstats
import datetime
from cart.models import recent, cart_id
from msg_and_prof.models import messages, users
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name ='admin/adminhome.html'

# Creating views

User = get_user_model()



class chart_data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, year=None, month=None):
        # chart1
        defaul = []
        obj = orders.objects.filter(cancel=False, ordered_date__year=year, ordered_date__month=month)

        if month is None:
            labels = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'Aug', 'sep', 'oct', 'nov', 'dec']
            for i in range(12):
                obj = orders.objects.filter(ordered_date__year=year, ordered_date__month=(i + 1))
                defaul.append(obj.count())
        else:
            labels = []
            for i in range(calendar.monthrange(year, month)[1]):
                labels.append(str(i + 1))
                obj = orders.objects.filter(ordered_date__year=year, ordered_date__month=month,
                                            ordered_date__day=(i + 1))
                defaul.append(obj.count())

        # chart2
        total = 0
        if month is not None:
            for i in obj:
                total += i.boughtprice

            cat_name = []
            cat_income = []

            cat = category.objects.all()
            for i in cat:
                cat_name.append(i.name)
                object = orders.objects.filter(prodid__categ=i, curstats=True, cancel=False, ordered_date__year=year,
                                               ordered_date__month=month)
                income = 0
                for j in object:
                    income += j.boughtprice
                cat_income.append(income)
        else:
            for i in obj:
                total += i.boughtprice

            cat_name = []
            cat_income = []

            cat = category.objects.all()
            for i in cat:
                cat_name.append(i.name)
                object = orders.objects.filter(prodid__categ=i, curstats=True, cancel=False, ordered_date__year=year)
                income = 0
                for j in object:
                    income += j.boughtprice
                cat_income.append(income)
        # chart3

        sold_items = []
        itemcount = []
        if month is not None:
            prod_table = productstable.objects.all()
            for i in prod_table:
                objects = orders.objects.filter(prodid=i, curstats=True, cancel=False, ordered_date__year=year,
                                                ordered_date__month=month)
                sold_items.append(i.name)
                if objects is not None:
                    itemcount.append(objects.count())
        else:
            prod_table = productstable.objects.all()
            for i in prod_table:
                objects = orders.objects.filter(prodid=i, curstats=True, cancel=False, ordered_date__year=year)
                sold_items.append(i.name)
                if objects is not None:
                    itemcount.append(objects.count())

        # chart 4

        user_joind = []
        if month is not None:
            for i in range(calendar.monthrange(year, month)[1]):
                user = User.objects.filter(date_joined__year=year, date_joined__month=month, date_joined__day=(i + 1))
                user_joind.append(user.count())
        else:
            for i in range(12):
                obj = User.objects.filter(date_joined__year=year, date_joined__month=(i + 1))
                user_joind.append(obj.count())

        # chart5
        views = []
        if month is not None:
            for i in range(calendar.monthrange(year, month)[1]):
                home_views = loginstats.objects.filter(date__year=year, date__month=month, date__day=(i + 1))
                if home_views.exists():
                    num = 0
                    for j in home_views:
                        num += j.home
                    views.append(num)
                else:
                    views.append(0)
        else:
            for i in range(12):
                home_views = loginstats.objects.filter(date__year=year, date__month=(i + 1))
                if home_views.exists():
                    num = 0
                    for j in home_views:
                        num += j.home
                    views.append(num)
                else:
                    views.append(0)

        # chart6
        cancel = []
        if month is None:
            for i in range(12):
                s = orders.objects.filter(cancel=True, ordered_date__month=(i + 1))
                cancel.append(s.count())

        data = {
            "label": labels,
            "defaul": defaul,
            "total": total,
            "cat_name": cat_name,
            "cat_income": cat_income,
            "sold_items": sold_items,
            "itemcount": itemcount,
            "user_joind": user_joind,
            "views": views,
            "cancel_frequency": cancel,

        }
        return Response(data)

@login_required(login_url='/')


def admin_home(request):
    if request.user.is_superuser:

        months = [{'month': 'january', 'num': 1},
                  {'month': 'february', 'num': 2},
                  {'month': 'march', 'num': 3},
                  {'month': 'april', 'num': 4},
                  {'month': 'may', 'num': 5},
                  {'month': 'june', 'num': 6},
                  {'month': 'july', 'num': 7},
                  {'month': 'August', 'num': 8},
                  {'month': 'september', 'num': 9},
                  {'month': 'october', 'num': 10},
                  {'month': 'november', 'num': 11},
                  {'month': 'december', 'num': 12}]

        date = str(datetime.date.today())
        date_find = datetime.datetime.strptime(date, "%Y-%m-%d")
        year = date_find.year
        list_year = []
        for i in range(10):
            list_year.append(year - i)
        active_orders = []
        user = recent.objects.filter(stats=True)  # recent orders true means still pending order
        for i in user:
            cartid = cart_id.objects.get(id=i.userid.id)
            if User.objects.filter(id=i.userid.userid).exists():
                userid = User.objects.get(id=i.userid.userid)
                le = {"cartid": cartid, "userid": userid}
                if not le in active_orders:
                    active_orders.append(le)
            else:
                le = {"cartid": cartid, "userid": 0}
                if not le in active_orders:
                    active_orders.append(le)
        try:
            user_ids = users.objects.filter(seen=False)
        except:
            user_ids = None
            pass
        ord_users = []
        today = datetime.date.today()
        year=datetime.datetime.strptime(str(today),'%Y-%m-%d')

        i = 0
        last_msg = []
        while i < 8:
            eachday = today - datetime.timedelta(i)
            orderes = recent.objects.filter(date=eachday)
            msg_users = messages.objects.filter(time__year =year.year ,time__month =year.month ,time__day =(year.day-i))
            for k in msg_users:
                last_msg.append(k)
            for j in orderes:
                if j.userid.userid:
                    ord_users.append(User.objects.get(id=j.userid.userid))
            i+=1
        post_user_msg = []
        for i in last_msg:
            g=User.objects.get(id=i.user.userid)
            if g not in post_user_msg:
                post_user_msg.append(g)

        return render(request, 'admin/adminhome.html',
                      {'year': year, 'months': months, 'list_year': list_year, 'act_ord': active_orders, 'users': user_ids,
                      'ord_users': ord_users,'post_user_msg':post_user_msg})
    else:
        return redirect('/')


def htmlfile(request):
    return render(request, 'admin/charts.html')


def detail(request, id):
    phone = None
    cartid = cart_id.objects.get(id=id)
    if request.user.is_authenticated:

        order_placed = orders.objects.filter(curstats=False, cancel=False, userid=cartid.userid)
        user_obj = User.objects.get(id=cartid.userid)
        realtot = 0
        total = 0
        num = 0
        for i in order_placed:
            realtot += i.prodid.price * i.quan
            if i.prodid.offers:
                total = (i.prodid.offerprice * i.quan) + total
            else:
                total = (i.prodid.price * i.quan) + total
            num = num + i.quan
        savedmoney = realtot - total

        money = {'num': num, 'realtot': realtot, 'total': total, 'savedmoney': savedmoney}
    else:
        order_placed = orders.objects.filter(curstats=False, cancel=False, session=cartid.session)
        try:
            one_obj = order_placed[0]
            phone = one_obj.phone
        except:
            one_obj = ''
            pass
        user_obj = cartid
        realtot = 0
        total = 0
        num = 0
        for i in order_placed:
            realtot += i.prodid.price * i.quan
            if i.prodid.offers:
                total = (i.prodid.offerprice * i.quan) + total
            else:
                total = (i.prodid.price * i.quan) + total
            num = num + i.quan
        savedmoney = realtot - total
        money = {'num': num, 'realtot': realtot, 'total': total, 'savedmoney': savedmoney}
    return render(request, 'admin/client_detail.html',
                  {'ord': order_placed, 'user': user_obj, 'phone': phone, 'money': money, 'id': id})


def ord_process(request, id, comd):
    cartid = cart_id.objects.get(id=id)
    if cartid.userid is not None:
        order_placed = orders.objects.filter(curstats=False, cancel=False, userid=cartid.userid)
        if comd == 'cancel':
            for i in order_placed:
                i.cancel = True
                i.done_date = datetime.date.today()
                i.save()
            try:
                s = recent.objects.get(userid=cartid)
            except MultipleObjectsReturned:
                l = recent.objects.filter(userid=cartid)
                h = 0
                for i in l:
                    if not h == 0:
                        l[h].delete()
                    h += 1

            s = recent.objects.get(userid=cartid)
            tdy=datetime.date.today()
            s.stats=False
            s.date=tdy
            s.save()
        else:
            for i in order_placed:
                i.curstats = True
                i.done_date = datetime.date.today()
                i.save()
            try:
                s = recent.objects.get(userid=cartid)
            except MultipleObjectsReturned:
                l = recent.objects.filter(userid=cartid)
                h = 0
                for i in l:
                    if not h == 0:
                        l[h].delete()
                    h += 1
            s = recent.objects.get(userid=cartid)
            s.stats = False
            s.date = datetime.date.today()
            s.save()
    else:
        order_placed = orders.objects.filter(curstats=False, cancel=False, session=cartid.session)
        if comd == 'cancel':
            for i in order_placed:
                i.cancel = True
                i.save()
            s = recent.objects.get(userid=cartid)
            s.stats = False
            s.save()
        else:
            for i in order_placed:
                i.curstats = True
                i.save()
            s = recent.objects.get(userid=cartid)
            s.stats = False
            s.date = datetime.date.today()
            s.save()
    return redirect('ord_detail', id)


def msg_view(request, id):
    if request.method == 'POST':
        msgtxt = request.POST.get('msgtxt')

        if not users.objects.filter(userid=request.user).exists():
            s = users(userid=request.user)
            s.save()
        seen = users.objects.get(userid=request.user)
        user = cart_id.objects.get(userid=id)  # call msg receiving client
        s = messages(msgtxt=msgtxt, user=user, trikmsg=True, seen=seen)
        s.save()

    ids = User.objects.get(id=id)
    if not users.objects.filter(userid=ids).exists():
        users.objects.create(userid=ids).save()
    obj = users.objects.get(userid=ids)
    msg = messages.objects.filter(seen=obj)
    return render(request, 'admin/msg_detail.html', {'msg': msg, 'id': ids})

def post_detail(request,id):
    order_place1 = orders.objects.filter(userid=id,cancel=True)
    order_place2 = orders.objects.filter(userid=id,curstats=True)
    order_placed = []
    for i in order_place1:
        order_placed.append(i)
    for i in order_place2:
        order_placed.append(i)

    user_obj = User.objects.get(id=id)
    return render(request, 'admin/client_detail.html',
                  {'ord': order_placed, 'user': user_obj,'post':'post','id': id})