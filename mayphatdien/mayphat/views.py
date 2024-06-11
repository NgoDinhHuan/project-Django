import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Slide, Post,Imageslide,Order,Order_detail
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Email,rating
from .serializer import emailSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django import template
from django.db.models import Avg
from django.shortcuts import redirect
import hashlib
register = template.Library()
@csrf_exempt

def index(request):
    new = Category.objects.all().filter(status='New')[:8]
    outstanding_old = Category.objects.all().filter(status='Old')[:4]
    outstanding = Category.objects.all()[:4]
    banner = Slide.objects.all().filter(status='Banner')[:3]
 #   del request.session['cart']
    return render(request, "index.html", {'new': new, 'outstanding': outstanding,'outstanding_old': outstanding_old, 'banner': banner})


def phatdiencu(request):
    old = Category.objects.all().filter(status='Old')
    vkey = request.GET.get('manufacturer_filter')
    from_price = request.GET.get('price1')
    to_price = request.GET.get('price2')
    print(to_price,from_price)
    if vkey is not None:
        vkey = list(vkey.split(','))
        old = Category.objects.filter(status='Old').filter(nation__in=vkey)

    if not (from_price is None or from_price==''):
       old = old.filter(price__gte=from_price)
    if not (to_price is None or to_price == ''):
       old = old.filter(price__lte=to_price)


    paginator = Paginator(old, 6)
    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, "phatdiencu.html", {'old': customers, 'page': range(1, paginator.num_pages + 1)})


def phatdienmoi(request):
    new = Category.objects.all().filter(status='New')
    vkey = request.GET.get('manufacturer_filter')
    from_price = request.GET.get('price1')
    to_price = request.GET.get('price2')
    print(to_price, from_price)
    if vkey is not None:
        vkey = list(vkey.split(','))
        new = Category.objects.filter(status='New').filter(nation__in=vkey)

    if not (from_price is None or from_price == ''):
        new = new.filter(price__gte=from_price)
    if not (to_price is None or to_price == ''):
        new = new.filter(price__lte=to_price)

    paginator = Paginator(new, 6)
    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, "phatdienmoi.html", {'new': customers, 'page': range(1, paginator.num_pages + 1)})

def phatdienthue(request):

    old = Category.objects.all().filter(status='Old')
    vkey = request.GET.get('manufacturer_filter')
    from_price = request.GET.get('price1')
    to_price = request.GET.get('price2')

    if vkey is not None:
        vkey = list(vkey.split(','))
        old = Category.objects.filter(status='Old').filter(nation__in=vkey)

    if not (from_price is None or from_price == ''):
        old =old.filter(price__gte=from_price)
    if not (to_price is None or to_price == ''):
        old =old.filter(price__lte=to_price)
       # Category.filter(status='Old').filter(price__gte=from_price).filter(price__lte=to_price)

    paginator = Paginator(old, 6)
    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, "phatdienthue.html", {'old': customers, 'page': range(1, paginator.num_pages + 1)})



def contact(request):
    return render(request, "contact.html")

def slide(request):
    return render(request, "slide.html")

def rental(request):
    pot = Post.objects.all().filter(status='rental')
    return render(request, "rental.html", {'pot': pot})


def repair(request):
    fix = Post.objects.all().filter(status='repair')
    return render(request, "repair.html", {'fix': fix})


def transport(request):
    ship = Post.objects.all().filter(status='transport')
    return render(request, "transport.html", {'ship': ship})


def service(request):
    sv = Post.objects.all().filter(status='service')
    return render(request, "service.html", {'sv': sv})


#
class Create_mail(ListCreateAPIView):
    model = Email
    serializer_class = emailSerializer
    def get_queryset(self):
        return Email.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = emailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new email successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new email unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)



class UpdateDeleteemail(RetrieveUpdateDestroyAPIView):
    model = Email
    serializer_class = emailSerializer

    def put(self, request, *args, **kwargs):
        email = get_object_or_404(Email, mail_name=kwargs.get('pk'))
        serializer = emailSerializer(Post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update email successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update email  unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        email = get_object_or_404(Email, mail_name=kwargs.get('pk'))
        email.delete()

        return JsonResponse({
            'message': 'Delete email successful!'
        }, status=status.HTTP_200_OK)

def post_danhgia(request):
    print (request.body)
    id_para = request.GET.get('id')
    if request.method == 'POST':
        params = request.POST
        vname = params['name']
        vtext = params['text']
        vrating = params['rating']
 #       print (vtext,vrating,id_para,vname)
    p = rating(id_category_id=id_para,name=vname,text=vtext,rating=vrating)
    p.save()
    return JsonResponse({'message': 'Create successful!'},status=status.HTTP_200_OK)

def postgiohang(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    if request.user.is_authenticated:
        cart = (request.session['cart'])
        if request.method == "POST":
                data = json.loads(request.body)
                if data==0:
                    return HttpResponse(len(cart))
                else:
                    cart.append(int(data))
                    request.session['cart']=cart
                #catalog is the name of the main pagedata

        return HttpResponse(len(cart))
    else:

        return HttpResponse('0')
@login_required(login_url='/login/')
def updategiohang(request):
    cart = (request.session['cart'])
    if request.method == "POST":
            data = json.loads(request.body)
            print(data)
           # while  data in cart:
           #     cart.remove(data)
            for key, value in data.items():
                if key=='remove': #xoa all cart
                    while int(value) in cart:
                        cart.remove(int(value))

                if key=='desc': #desc cart
                   cart.remove(int(value))
                   request.session['cart'] = cart
                   return HttpResponse(cart.count(int(value)))
                if key=='inc':
                   cart.append(int(value))
                   request.session['cart'] = cart
                   return HttpResponse(cart.count(int(value)))
            request.session['cart'] = cart
            giohang = Category.objects.all().filter(id__in=list(cart))
            sum_price = 0
            for p in giohang:
                p.total = cart.count(p.id)
                p.total_price = cart.count(p.id) * p.price
                sum_price = sum_price + p.total_price

    return HttpResponse(sum_price)
def sanpham(request, query):
    if not query:
        query = request.GET.get('query', '')
    sanpham = Category.objects.all().filter(slug=query)


    id_sp = sanpham.values('id')[0].get("id")
    sp_name = sanpham.values('category_name')[0].get("category_name")
    mota = sanpham.values('description')[0].get("description")
    detail = sanpham.values('detail')[0].get("detail")
    price = sanpham.values('price')[0].get("price")
    image = Imageslide.objects.all().filter(category_name=id_sp)
    i=0
    for p in image:
        p.counter=i
        i=i+1
    danhgia = rating.objects.all().filter(id_category=id_sp)
    stars_average = danhgia.aggregate(Avg('rating')).get("rating__avg")
    print(stars_average)
    return render(request, "product1.html",{'sanpham':sanpham,'image':image,'tieude':sp_name,'id':id_sp,'mota':mota,'detail':detail,'danhgia':danhgia,'countstart':len(danhgia),'star_avg':stars_average,'price':"{:0,.2f}".format(float(price))})
@login_required(login_url='/login/')
def giohang(request):
    #if current_user.is_authenticated():
    user = request.user
    print(user)
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = (request.session['cart'])
    if len(cart)<=0:
        return  redirect('index')
    giohang=Category.objects.all().filter(id__in=list(cart))
    sum_price=0
    for p in giohang:
        p.total=cart.count(p.id)
        p.total_price = cart.count(p.id) * p.price
        sum_price=sum_price+p.total_price

    return render(request, "giohang.html",{'giohang':giohang,'sum_price':sum_price})
@login_required(login_url='/login/')
def dathang(request):
    cart = (request.session['cart'])
    giohang = Category.objects.all().filter(id__in=list(cart))
    sum_price = 0
    for p in giohang:
        p.total = cart.count(p.id)
        p.total_price = cart.count(p.id) * p.price
        sum_price = sum_price + p.total_price

    return render(request, "dathang.html",{'giohang':giohang,'sum_price':sum_price,'sum_product':len(set(cart))})
@login_required(login_url='/login/')
def update_order(request):
    if request.method == 'POST':
        vname = request.POST['firstname']
        vemail = request.POST['email']
        vphone =request.POST['telephone']
        vcountry = request.POST['country_id']
        vzone_id = request.POST['zone_id']
        vward_id = request.POST['ward_id']
        vaddress_1 = request.POST['address_1']
        vcomment = request.POST['comment']
        vtax_code= request.POST['tax_code']
        vcompany = request.POST['company']
        vcompany_address = request.POST['company_address']
        vpayment_method = request.POST['payment_method']
        vuser = request.user.username
        p = Order(full_name=vname,user_update=vuser,email=vemail,number_phone=vphone,country=vcountry,payment_methosd=vpayment_method,
                 city=vzone_id,province=vward_id,address=vaddress_1,tax_data=vtax_code,company_name=vcompany,company_adress=vcompany_address,comment=vcomment,fulfilled=False)
        p.save()
    #   print(p.id)
        cart = (request.session['cart'])
        giohang = Category.objects.all().filter(id__in=list(cart))
        sumpride=0
        sumqty=0
        for od in giohang:
            PP=Order_detail.objects.create(id_order=Order.objects.get(id = p.id),id_category=Category.objects.get(id = od.id),qty=cart.count(od.id),price=od.price,amount=cart.count(od.id) * od.price)
            PP.save
            sumpride=sumpride + cart.count(od.id) * od.price
            sumqty=sumqty + cart.count(od.id)
        del request.session['cart']
   #     print(vpayment_method)
        if vpayment_method=='2':
            text = 'ĐẶT HÀNG THÀNH CÔNG<br>MÃ DƠN ĐẶT HÀNG LÀ: '+ str(p.payment_code)
            text = '<b>' + text + '</b>' + '<br>' + '<a href="/dathang/' + str(p.payment_code) + '/">XEM LẠI ĐƠN HÀNG</a>'
            return HttpResponseRedirect('/notice?text_status='+text)
        else:
            buyer_info=vname+'*|*'+vemail+'*|*'+vphone+'*|*'+vaddress_1
            verify_secure_code = '36680' + ' ' + 'http://localhost:8000/ktthanhtoan' + ' ' + 'vantt4@yopmail.com' + ' ' + str(p.payment_code) + ' ' + str(p.payment_code) + ' ' + str(sumpride) + ' ' + 'vnd' + ' ' + str(sumqty) + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + 'thanhtoandonhang' + ' ' + buyer_info + ' ' + '' + ' ' + 'matkhauketnoi'
            md5 = hashlib.md5(verify_secure_code.encode()).hexdigest()  # returns a str
            linkthanhtoan='''https://sandbox.nganluong.vn/nl35/checkout.php?merchant_site_code=36680&return_url=http://localhost:8000/ktthanhtoan&receiver=vantt4@yopmail.com&transaction_info='''+str(p.payment_code)+'''&order_code='''+str(p.payment_code)+'''&price='''+str(sumpride)+'''&currency=vnd&quantity='''+str(sumqty)+'''&tax=0&discount=0&fee_cal=0&fee_shipping=0&order_description=thanhtoandonhang&buyer_info='''+buyer_info+'''&affiliate_code=&lang=vi&secure_code='''+md5+'''&cancel_url=http://localhost:8000/dathang/'''+str(p.payment_code)+'''/'''
            print(linkthanhtoan)
    return redirect(linkthanhtoan)
@login_required(login_url='/login/')
def don_dathang(request,query):
    if not query:
        query = request.GET.get('query', '')
    don = Order.objects.all().filter(payment_code=query).filter(user_update=request.user.username)
    if don :
        giohang = Order_detail.objects.all().filter(id_order=don[0])
        sum_price = 0
        for p in giohang:
            p.total = p.qty
            p.total_price = p.qty * p.price
            p.category_image=Category.objects.all().filter(id=p.id_category_id).values('category_image')[0].get("category_image")
            sum_price = sum_price + p.amount

        return render(request, "donhang.html",{'don':don,'giohang':giohang,'sum_price':sum_price,'sum_product':len(giohang)})
    else:
        text = 'KHÔNG TỒN TẠI ĐƠN HÀNG NÀY'
        text = '<b>' + text + '</b>' + '<br>' + '<a href="/timkiem/">Quay Lại</a>'
    #  return render(request, "notice.html",{'text':text})
        return HttpResponseRedirect('/notice?text_status=' + text)
@login_required(login_url='/login/')
def thanhtoan(request,query):
    if not query:
        query = request.GET.get('query', '')
    #don = Order.objects.all().filter(payment_code=query)
    don = Order.objects.all().filter(payment_code=query).filter(user_update=request.user.username)
    if don:
        giohang = Order_detail.objects.all().filter(id_order=don[0])
        sum_price = 0
        sumqty=0
        for p in giohang:
            p.total = p.qty
            sumqty = sumqty + p.qty
            sum_price = sum_price + p.amount
        vname = don.values('full_name')[0].get("full_name")
        vemail = don.values('email')[0].get("email")
        vphone = don.values('number_phone')[0].get("number_phone")
        vaddress_1 = don.values('address')[0].get("address")
        buyer_info = vname + '*|*' + vemail + '*|*' + vphone + '*|*' + vaddress_1

        verify_secure_code = '36680' + ' ' + 'http://localhost:8000/ktthanhtoan' + ' ' + 'vantt4@yopmail.com' + ' ' + str(
            query) + ' ' + str(query) + ' ' + str(sum_price) + ' ' + 'vnd' + ' ' + str(
            sumqty) + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + 'thanhtoandonhang' + ' ' + buyer_info + ' ' + '' + ' ' + 'matkhauketnoi'
        md5 = hashlib.md5(verify_secure_code.encode()).hexdigest()  # returns a str
        linkthanhtoan = '''https://sandbox.nganluong.vn/nl35/checkout.php?merchant_site_code=36680&return_url=http://localhost:8000/ktthanhtoan&receiver=vantt4@yopmail.com&transaction_info=''' + str(query) + '''&order_code=''' + str(query) + '''&affiliate_code=&price=''' + str(sum_price) + '''&currency=vnd&quantity=''' + str(sumqty) + '''&tax=0&discount=0&fee_cal=0&fee_shipping=0&order_description=thanhtoandonhang&buyer_info=''' + buyer_info + '''&lang=vi&secure_code=''' + md5 + '''&cancel_url=http://localhost:8000/dathang/''' + str(query) + '''/'''

        #print(linkthanhtoan)
        return redirect(linkthanhtoan)
    else:
        text = 'KHÔNG TỒN TẠI ĐƠN HÀNG NÀY'
        text = '<b>' + text + '</b>' + '<br>' + '<a href="/timkiem/">Quay Lại</a>'
        #  return render(request, "notice.html",{'text':text})
        return HttpResponseRedirect('/notice?text_status=' + text)
def check_pay(request):
    # vpayment_id = request.GET.get('payment_id')
    # vtransaction_info= request.GET.get('transaction_info')
    vorder_code= request.GET.get('order_code')
    # vpayment_type = request.GET.get('payment_type')
    verror_text = request.GET.get('error_text')
    print(vorder_code,verror_text)
    text = 'THANH TOÁN THẤT BẠI, LỖI THANH TOÁN LÀ: ' + verror_text
    text = '<b>' + text + '</b>' + '<br>' + '<a href="/dathang/'+vorder_code+'/">QUAY LẠI ĐƠN HÀNG</a>'
    if verror_text is None or verror_text =='':
       t = Order.objects.get(payment_code=vorder_code)
       t.fulfilled = True
       t.save(update_fields=['fulfilled'])
#       return HttpResponse('thanh toan thanh công')
       text='THANH TOÁN THÀNH CÔNG'
       text='<b>'+text+'</b>'+'<br>'+'<a href="/">Về Trang Chủ</a>'
  #  return render(request, "notice.html",{'text':text})
    return HttpResponseRedirect('/notice?text_status='+text)
def check_pay_status(request):
    import requests
    from requests.structures import CaseInsensitiveDict
    url = "https://sandbox.nganluong.vn/nl35/service/order/checkV2"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    verify_secure_code = '100014' + '|' + 'matkhauketnoi'
    checksum = hashlib.md5(verify_secure_code.encode()).hexdigest()
    data = "merchant_id=36680&order_code=100009&checksum="+checksum
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)
    return HttpResponseRedirect('/notice?textstatus=')
def notice(request):
    vpayment_id = request.GET.get('text_status')
    #return HttpResponse(vpayment_id)
    return render(request, "notice_alert.html",{'payment_id':vpayment_id})
def timkiem(request):
    don = Order.objects.all().filter(user_update=request.user.username)
    #vorder_code = don.values('payment_code').get("payment_code")
    #print(vorder_code)
    return render(request, "timkiem.html",{'order_code':don})