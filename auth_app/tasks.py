
from django.core.mail import send_mail

def send_activation_email(email, activation_link):
    send_mail(
        'Activate your account.',
        f'Anyone who asks you for the link is a scammer.\n\n{activation_link}\n\n',
        None,
        recipient_list=[email],
        fail_silently=False
    )


def send_passwordreset_email(email, passwordreset_link):
    send_mail(
        'Reset password.',
        f'Anyone who asks you for the link is a scammer.\n\n{passwordreset_link}\n\n',
        None,
        recipient_list=[email],
        fail_silently=False
    )