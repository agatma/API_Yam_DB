import random
import string

from django.core.mail import send_mail
from django.http import Http404
from rest_framework.views import exception_handler


def email_code() -> int:
    code = ''.join(random.choice(string.digits) for _ in range(6))
    return int(code)


def custom_exception_handler(exc, context):
    """Changing exception handler from rest framework version to django.

    Returns: response object
    """
    response = exception_handler(exc, context)
    if response is not None and isinstance(exc, Http404):
        response.data['detail'] = exc.args[0]
    return response


def send_email(email: str, code: int) -> None:
    """Create email verification message with email and code.
    Args:
        email: user email for getting code
        code: int number for email verification message

    Returns: None
    """
    mail_subject = 'Код подтверждения для сайта YAMDB'
    message = (f'Ваш код подтверждения: {code} . '
               f'Используйте код для активации токена '
               f'по адресу /api/v1/auth/token/')
    send_mail(mail_subject, message, 'madikhanagatanov@gmail.com',
              [email], fail_silently=False)
