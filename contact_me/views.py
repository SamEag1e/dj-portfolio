from django.shortcuts import render, redirect
from django.core.mail import send_mail


def contact_me(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Send email
        send_mail(
            subject=subject,
            message=f"Message:\n\t{message}\n\nEmail:\n\t{email}\n\nPhone:\n\t{phone}\n",
            from_email="HelloWorld@sameagle.ir",
            recipient_list=["samadtnd@gmail.com"],
            fail_silently=False,
        )
        return redirect("contact_success")
    return render(request, "contact_me/contact.html")


def contact_success(request):
    return render(request, "contact_me/contact_success.html")
