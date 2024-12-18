from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm,PaymentForm
from payment.models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from picproject.models import Product,Profile
import datetime
# import paypal stuff
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid # unique user id for duplicate orders
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def orders(request,pk):
    if request.user.is_authenticated and request.user.is_superuser:
        # Get the order
        order = Order.objects.get(id=pk)
        # Get the order items
        items = OrderItem.objects.filter(order=pk)

        if request.POST:
            status = request.POST['shipping_status']
            # check if true or false
            if status == "true":
                # Get the order
                order = Order.objects.filter(id=pk)
                # update the status
                now = datetime.datetime.now()
                order.update(shipped=True,date_shipped=now)
            else:
                # Get the order
                order = Order.objects.filter(id=pk)
                # update the status
                order.update(shipped=False)
            messages.success(request,"Shipping status updated") 
            return redirect('home')   


        return render(request,"payment/orders.html",{"order":order,"items":items})
    else:
        messages.success(request,"Access Denied")
        return redirect('home')    


def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            # Grab the order
            order = Order.objects.filter(id=num)
            # Grab date and time
            
            now = datetime.datetime.now()

            # update order
            order.update(shipped=False)
            messages.success(request,"Shipping status updated") 
            return redirect('home') 
        return render(request,"payment/shipped_dash.html",{"orders":orders})
    else:
        messages.success(request,"Access Denied")
        return redirect('home') 

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)

        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            # Grab the order
            order = Order.objects.filter(id=num)
            # Grab date and time
            
            now = datetime.datetime.now()

            # update order
            order.update(shipped=True,date_shipped=now)
            messages.success(request,"Shipping status updated") 
            return redirect('home') 

        return render(request,"payment/not_shipped_dash.html",{"orders":orders})
    else:
        messages.success(request,"Access Denied")
        return redirect('home') 


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        # Get billing info from the last page
        payment_form = PaymentForm(request.POST or None)
        # Get shipping session data
        my_shipping = request.session.get('my_shipping')

        # Gather order info
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        # create shipping address from session info
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_paid = totals

        # create an order

        
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user,full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
            create_order.save()
           
            
            
            #Add order items
            #Get the order ID
            order_id = create_order.pk
            # Get Product info
            for product in cart_products():
                # Get product ID
                product_id = product.id
                #Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # create order item
                        create_order_item = OrderItem(order_id=order_id,product_id=product_id,user=user,quantity=value,price=price)
                        create_order_item.save() 
            #Delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]

            # delete cart from database (old_cart field)
            current_user = Profile.objects.filter(user__id=request.user.id)
            # delete shopping cart in database (old_cart field)
            current_user.update(old_cart="")                           


            messages.success(request,"Order has been placed!")
            return redirect('home') 
        else:
            # not logged in
            # create order
            create_order = Order(full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
            create_order.save()

            #Add order items
            #Get the order ID
            order_id = create_order.pk
            # Get Product info
            for product in cart_products():
                # Get product ID
                product_id = product.id
                #Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # create order item
                        create_order_item = OrderItem(order_id=order_id,product_id=product_id,quantity=value,price=price)
                        create_order_item.save()

            #Delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]            

            messages.success(request,"Order has been placed!")
            return redirect('home')   



    else:
         messages.success(request,"Access Denied")
         return redirect('home')   


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # create a session with shipping info
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        # Gather order info
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        # create shipping address from session info
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_paid = totals




        my_payment_id = str(uuid.uuid4())
        client = razorpay.Client(auth=("rzp_live_50JrmHESiXLiZJ", "VhVL08D59BJQbhOdDuBXlqw0"))
        amount = int(totals*100)
        currency = 'INR'
        
        payment = client.order.create(dict(amount=amount , currency=currency, payment_capture=1))
        #payment_order_id = payment['id']
        #print(payment)

        #Check to see ifthe user is logged in
        if request.user.is_authenticated:
           # Get the billing form
           #billing_form = PaymentForm()

           user = request.user
           create_order = Order(user=user,full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid,payment_id=payment['id'])
           create_order.save()
           
            
            
            #Add order items
            #Get the order ID
           order_id = create_order.pk
            # Get Product info
           for product in cart_products():
                # Get product ID
                product_id = product.id
                #Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # create order item
                        create_order_item = OrderItem(order_id=order_id,product_id=product_id,user=user,quantity=value,price=price)
                        create_order_item.save() 
            

            # delete cart from database (old_cart field)
           current_user = Profile.objects.filter(user__id=request.user.id)
            # delete shopping cart in database (old_cart field)
           current_user.update(old_cart="")                           


           return render(request,"payment/billing_info.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals,"shipping_info":request.POST,"payment":payment}) 
        else:
            # not logged in
            # create order
            create_order = Order(full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid,payment_id=payment['id'])
            create_order.save()

            #Add order items
            #Get the order ID
            order_id = create_order.pk
            # Get Product info
            for product in cart_products():
                # Get product ID
                product_id = product.id
                #Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # create order item
                        create_order_item = OrderItem(order_id=order_id,product_id=product_id,quantity=value,price=price)
                        create_order_item.save()

             
            #billing_form = PaymentForm()
            return render(request,"payment/billing_info.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals,"shipping_info":request.POST,"payment":payment})



           

        
    else:
        messages.success(request,"Access Denied")
        return redirect('home')



def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None , instance=shipping_user)
        return render(request,"payment/checkout.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals,"shipping_form":shipping_form})

    else:
        # checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request,"payment/checkout.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals,"shipping_form":shipping_form})

#@login_required(login_url='home')
@csrf_exempt
def payment_success(request):
        
    if request.method == 'POST':
        a = request.POST
        order_id = ''
        data = {}
        for key , val in a.items():
            if key == 'razorpay_order_id' :
                data['razorpay_order_id'] = val
                order_id = val

            elif key == 'razorpay_payment_id' :
                 data['razorpay_payment_id'] = val

            elif key == 'razorpay_signature' :
                 data['razorpay_signature'] = val        
        user = Order.objects.filter(payment_id = order_id).first() 
        #user1 = OrderItem.objects.filter(user=user)
        #client = razorpay.Client(auth=("rzp_live_50JrmHESiXLiZJ", "VhVL08D59BJQbhOdDuBXlqw0"))
        #check = client.utility.verify_payment_signature(data)
        #print (check)
        #if check:
            #return render(request, "payment/payment_failed.html", {})

        user.paid = True
        user.save()
        context= {
                    'Name': user.full_name,
                    'Amount': user.amount_paid,
                    'Orderdate' : user.date_ordered,
                    'Address' : user.shipping_address,
                    'OrderNo' : user.payment_id,
                    

        }
        msg_plain = render_to_string('payment/email.txt')
        msg_html = render_to_string('payment/email.html',context=context)
        send_mail("Greetings from Holystore",msg_plain, settings.EMAIL_HOST_USER , [user.email], html_message=msg_html)             

        for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]

        # delete cart from database (old_cart field)
        current_user = Profile.objects.filter(user__id=request.user.id)
            # delete shopping cart in database (old_cart field)
        current_user.update(old_cart="")

    
    return render(request, "payment/payment_success.html", {})

def payment_failed(request):
    return render(request, "payment/payment_failed.html", {})

def paid_details(request):
    if request.user.is_authenticated and request.user.is_superuser:
        paymentinfo = Order.objects.all()
        return render(request,"payment/paid_details.html",{'paymentinfo': paymentinfo})
    else:
        
        messages.success(request,"Access Denied")
        return redirect('home')