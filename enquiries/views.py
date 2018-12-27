from django.shortcuts import render, redirect
from .models import Enquiry
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives

# # Create your views here.
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing_name = request.POST['listing_name']
    name = request.POST['user']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    seller_id = request.POST['seller_id']
    enquirer_id = request.POST['enquirer_id']
    seller_email = request.POST['seller_email']
#
    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      has_contacted = Enquiry.objects.all().filter(listing_id=listing_id, enquirer_id=enquirer_id)
      print(has_contacted)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listing/'+str(listing_id))

    contact = Enquiry(listing_name=listing_name, listing_id=listing_id, name=name, email=email, phone=phone, message=message, seller_id=seller_id, enquirer_id=enquirer_id )
#
    contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    # email = form1.cleaned_data['email']
    # password = form1.cleaned_data['password']
    # subject = 'Confirmation Mail'
    # msg = 'u are confirm'
    # send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])


    subject, from_email, to = 'ENQUIRY LISTED', 'shubhambabu0001@gmail.com', 'shubham24006@gmail.com'
    text_content = 'There has been an inquiry for your posted property.'
    html_content = '<p>This is an <strong>important</strong> message.</p><br><p>There has been an inquiry for your posted property.</p> <br><a href={% url "listing" pk %}>Click</a>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    messages.success(request, 'Your request has been submitted, the seller will get back to you shortly.')

  return redirect('/')


def enquiries(request):
  enquiries = Enquiry.objects.order_by('-contact_date').filter(seller_id=request.user.id)
  print(enquiries)
  return render(request,'enquries.html', {'enquries':enquiries})