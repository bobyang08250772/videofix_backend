from django.core.mail import send_mail
from django.utils.html import strip_tags

def send_activation_email(email, activation_link):
    """
    Send email to activate account.
    """
    subject = 'Activate your VideoFlix account'
    html_message = f"""
        <p>Dear User,</p>
        <p>Thank you for registering with <strong>VideoFlix</strong>!</p>
        <p>To complete your registration, please click the button below to activate your account:</p>
        <p><a href="{activation_link}" style="padding: 10px 15px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 5px;">Activate Account</a></p>
        <p>If the button above doesn't work, you can also copy and paste this link into your browser:</p>
        <p>{activation_link}</p>
        <hr>
        <p>If you did not create an account, please disregard this email.</p>
        <p>Best regards,<br>VideoFlix Team</p>
    """
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        None,
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False
    )


def send_passwordreset_email(email, passwordreset_link):
    """
    Send email to reset password.
    """
    subject = 'Reset your VideoFlix password'
    html_message = f"""
        <p>Dear User,</p>
        <p>We received a request to reset your password for your <strong>VideoFlix</strong> account.</p>
        <p>You can reset your password by clicking the button below:</p>
        <p><a href="{passwordreset_link}" style="padding: 10px 15px; background-color: #DC3545; color: white; text-decoration: none; border-radius: 5px;">Reset Password</a></p>
        <p>If the button above doesn't work, you can also copy and paste this link into your browser:</p>
        <p>{passwordreset_link}</p>
        <hr>
        <p>If you did not request a password reset, you can safely ignore this email.</p>
        <p>Best regards,<br>VideoFlix Team</p>
    """
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        None,
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False
    )
