from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class Faq1(models.Model):
    question = models.CharField(max_length=150)
    Ans = models.TextField(max_length=2500)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Faq'


class ContactUs(models.Model):
    Reason_for_request = 'RR'
    Account_Opening = 'AC'
    With_drawal = 'WD'
    Deposit_Issue = 'DP'
    General = 'GR'
    Reason_CHOICES = (
        (Reason_for_request, 'Reason of Request'),
        (Account_Opening, 'Account Opening'),
        (With_drawal, 'Withdrawal Issue'),
        (Deposit_Issue, 'Deposit Issue'),
        (General, 'General Issue')

    )
    reason = models.CharField(
        max_length=2,
        choices=Reason_CHOICES,
        default=Reason_for_request,
    )
    First_name = models.CharField(max_length=80, default=None)
    Last_name = models.CharField(max_length=50, default=None)
    Email = models.CharField(max_length=150, validators=[validate_email], default=None)
    phone_number = models.CharField(max_length=10, default=None)
    subject = models.CharField(max_length=140, default=None)
    request = models.CharField(max_length=1500, default=None)

    def __str__(self):
        return ' {} Email: {} '.format(self.First_name, self.Email)


# class User(AbstractUser):
#     pass
    # USERNAME_FIELD = 'email'
    # email = models.EmailField('email address', unique=True)  # changes email to unique and blank to false
    # REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

class EmailAuthBackend():
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None