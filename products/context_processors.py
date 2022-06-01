from cart.views import tot_itm


def tot(request):
    if request.user.is_authenticated:
        tot = tot_itm(request)
    else :
        tot = tot_itm(request)
    return dict(totl=tot)