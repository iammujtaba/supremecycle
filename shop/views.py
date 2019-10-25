from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerQueries,Product,CustomerOrder,order_update
import math
import json
from django.views.decorators.csrf import csrf_exempt
from payTm import checkSum
# Create your views here.
MERCHANT_KEY = 'wkvh!Yoq3EUqN0oE'
def index(request):
    allProd=[]
    prod_catogery=Product.objects.all()
    allProd=list(prod_catogery)
    allProd1=[]
    #product_catogery=['Cycle','Tricycle','BikeTyre']
    product_catogery=['Cycle','Tricycle']
    for cat in product_catogery:
        prod=Product.objects.filter(product_type=cat)
        n=len(prod)
        nSlides=n//4+math.ceil(n/4-n//4)
        allProd1.append([prod,range(1,nSlides),nSlides])

    print(allProd1)

    params={"allProd":allProd,"range":range(1,len(allProd)),"allprod1":allProd1}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if(request.method=='POST'):
        name=request.POST.get("name")
        email=request.POST.get("email")
        query=request.POST.get("query")
        phone=request.POST.get("phone")
        customer=CustomerQueries(name=name,phone=phone,email=email,query=query)
        customer.save()
    return render(request,'shop/contact.html')
def productView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        itemJson=request.POST.get("itemJson",default="")
        name=request.POST.get("name",default="")
        amount=request.POST.get("amount",default=0)
        address=request.POST.get("address1",default="") +" "+ request.POST.get("address2",default="")
        phone=request.POST.get('phone',default="")
        email=request.POST.get('email',default="")
        zip_code=request.POST.get('zip_code',default="")
        city=request.POST.get('city',default="")
        state=request.POST.get('state',default="")
        custOrder=CustomerOrder(itemJson=itemJson,order_name=name,order_address=address,order_phone=phone,order_email=email,order_zip=zip_code,order_city=city,order_state=state,amount=amount)
        custOrder.save()
        id=custOrder.order_id
        orderUpdation=order_update(update_order_id=custOrder.order_id,update_desc="Order Has been Placed...")
        orderUpdation.save()
        checkOk=True
        param_dic={
            'MID':'eABIcv17661333413077',
            'ORDER_ID':str(custOrder.order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dic['CHECKSUMHASH'] = checkSum.generate_checksum(param_dic, MERCHANT_KEY)
        return render(request,'shop/paytm.html',{"param_dict":param_dic})
    return render(request,'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = checkSum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})
    # Python Will handle post Request Sent by Paytm here.........

