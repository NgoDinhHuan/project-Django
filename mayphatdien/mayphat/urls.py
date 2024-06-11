from idlelib.multicall import r

from django.urls import path
import os

from . import views
from .views import index, phatdiencu,phatdienmoi, contact, rental,  repair, transport,\
                   service, sanpham, slide,phatdienthue,post_danhgia,postgiohang,giohang,updategiohang,dathang,update_order,don_dathang,thanhtoan,check_pay,notice,timkiem
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path(r'',index, name='index'),
    path(r'slide/',slide, name='slide'),
    path(r'phatdiencu/', phatdiencu, name='phatdiencu'),
    path(r'phatdienmoi/', phatdienmoi, name='phatdienmoi'),
    path(r'phatdienthue/', phatdienthue, name='phatdienthue'),
    path(r'contact/', contact, name='contact'),
    path(r'rental/', rental, name='rental'),
    path(r'repair/', repair, name='repair'),
    path(r'transport/', transport, name='transport'),
    path('email', views.Create_mail.as_view()),
    path(r"sanpham/<str:query>/", sanpham, name="sanpham"),
    path('email/<str:pk>', views.UpdateDeleteemail.as_view()),
    path('danhgia/', post_danhgia),
    path('postgiohang/', postgiohang, name="postgiohang"),
    path(r"giohang/", giohang, name="giohang"),
    path(r"updategiohang/", updategiohang, name="updategiohang"),
    path(r"dathang/", dathang, name="dathang"),
    path(r"updatedathang/", update_order, name="updatedathang"),
    path(r"dathang/<str:query>/", don_dathang, name="don_dathang"),
    path(r"thanhtoan/<str:query>/", thanhtoan, name="thanhtoan"),
    path(r"ktthanhtoan", check_pay, name="check_pay"),
    path(r"notice", notice, name="notice"),
    path(r"timkiem/", timkiem, name="timkiem"),
]