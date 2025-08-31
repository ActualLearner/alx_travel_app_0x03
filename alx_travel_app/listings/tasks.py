from celery import shared_task
from django.core.mail import send_mail
from .models import Booking


@shared_task
def send_booking_confirmation_email(booking_id):
    """
    A Celery task to send a booking confirmation email.
    """
    try:
        # Best Practice: Always fetch the fresh object from the DB inside the task.
        booking = Booking.objects.get(pk=booking_id)

        subject = f"Your Booking Confirmation for {booking.listing.title}"
        message = f"""
        Hello {booking.user.username},

        Thank you for your booking!

        Here are your details:
        - Property: {booking.listing.title}
        - Check-in: {booking.check_in_date}
        - Check-out: {booking.check_out_date}

        We look forward to hosting you!
        """
        from_email = "noreply@travelapp.com"
        recipient_list = [booking.user.email]

        send_mail(subject, message, from_email, recipient_list)

        return f"Email sent successfully for booking {booking_id}"
    except Booking.DoesNotExist:
        return f"Booking with id {booking_id} does not exist. Could not send email."
