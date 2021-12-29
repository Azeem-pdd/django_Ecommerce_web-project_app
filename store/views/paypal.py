from django.http import request
from django.http.response import HttpResponse
from django.views import View
from django.shortcuts import render,redirect, reverse
from ..models.order import Order
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt

def process_payment(request):
    order_id=request.session.get('order_id')
    if order_id:
        order_obj=Order.objects.get(id=order_id)
    price=order_obj.price
    paypal_dict={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % price,
        'item_name': 'Order {}'.format(order_id),
        'invoice': str(order_id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format('127.0.0.1:8000',
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format('127.0.0.1:8000',
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format('127.0.0.1:8000',
                                              reverse('payment_cancelled')),
    }
    form=PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'process_payment.html', {'form':form})
@csrf_exempt
def payment_done(request):
    request.session['cart']={}
    order_id = request.session.get('order_id')
    if order_id:
        order_obj=Order.objects.get(id=order_id)
        order_obj.order_status='paid'
        order_obj.save()
    return render(request, 'payment_done.html')
@csrf_exempt
def payment_cancelled(request):
    
    return render(request, 'payment_cancelled.html')