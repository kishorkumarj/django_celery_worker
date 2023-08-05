import logging
from user.models import User
from celery import shared_task, Task
from kombu.exceptions import OperationalError

logger = logging.getLogger(__name__)

class BaseErrorHandlerMixin(Task):
    def delay(self, *args, **kwargs):
        try:
            super(BaseErrorHandlerMixin, self).delay(*args, **kwargs)
        except OperationalError:
            print('error')

@shared_task(base=BaseErrorHandlerMixin)
def send_email(to, subject="", message="", cc="", from_address=""):
    pass

@shared_task(base=BaseErrorHandlerMixin)
def sample_task(message):
    logger.info(f"Message is {message}")

@shared_task(base=BaseErrorHandlerMixin)
def user_registration_email(user_id):
    user = User.objects.get(pk=user_id)
    logger.info(f"sending welcome email to user {user}")
    send_email(user.email,  subject="welcome", message="Welcome")