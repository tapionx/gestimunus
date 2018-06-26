from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.utils.translation import gettext as _
from tinymce import HTMLField
from gestimunus import settings
from recurrence.fields import RecurrenceField
from settings.models import CashDesk, MovementsCausal, Customer, Profile

# Create your models here.

def protocolgen():
	return 201803001 + CashMovements.objects.count()


class Diary(models.Model):
	class Meta:
		verbose_name_plural = _("Diaries")
		verbose_name = _("Diary")

	diaryType = models.ForeignKey('settings.DiariesType', on_delete=models.CASCADE)
	customer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=200)
	# text = models.TextField()
	text = HTMLField('Content')
	upload = models.FileField(upload_to=settings.STATIC_UPLOAD, null=True)
	sign = models.ForeignKey('settings.Operator', on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s' % (self.diary_id)
		return u'%s %s' % (self.created_date.strftime("%Y-%m-%d"), self.title, )

class Agenda(models.Model):

	class Meta:
		verbose_name_plural = _("Events")
		verbose_name = _("Event")

	eventTitle = models.CharField(max_length=200)
	eventCustomer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
	eventDescription = models.TextField(null=True)
	eventStart = models.DateTimeField()
	eventEnd = models.DateTimeField()
	recurrence = RecurrenceField(null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.eventTitle)
	    # return u'%s %s' % (self.title, self.created_date)

class Planner(Agenda):
    class Meta:
        proxy = True
    	verbose_name_plural = _("Events Planner")
        verbose_name = _("Agenda")

class CashMovements(models.Model):

    class Meta:
        verbose_name_plural = "Cash Movements"

    author = models.ForeignKey(
        User,
        null=True,
        editable=False
        )

    annulled = models.BooleanField(default=True, help_text='[Deselect for cancel entry]', verbose_name="Validation")
    recived = models.BooleanField(default=False, verbose_name="Recived")
    operation_date = models.DateField(verbose_name="Operation Date", default=timezone.now)
    document_date =  models.DateField(blank=True, null=True, verbose_name="Document Date")
    cashdesk = models.ForeignKey('settings.CashDesk', verbose_name="Cash Service")
    causal = models.ForeignKey('settings.MovementsCausal', verbose_name="Causal")
    supplier = models.CharField(max_length=200, verbose_name="Supplier", null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    customer = models.ForeignKey('settings.Customer', null=True, blank=True, editable=False, verbose_name="Service Customer")
    note = models.CharField(max_length=200, blank=True, verbose_name="Note")
    sign = models.ForeignKey('settings.Operator', on_delete=models.CASCADE, verbose_name="Sign")
    protocol = models.IntegerField(unique=True, editable=False, default=protocolgen)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # return u'%s %s %s %s' % (self.operation_date, self.amount, self.causal, self.cashdesk)
        return u'%s' % (self.protocol)

class CashMovementsCustomerDetails(models.Model):

	class Meta:
		verbose_name_plural = "Cash Movements Customer Details"

	prot = models.ForeignKey('CashMovements')
	operation_date = models.DateField(default=timezone.now, editable=False) # models.DateField(verbose_name="Operation Date")
	customer = models.ForeignKey('settings.Customer', null=True, blank=True, verbose_name="Service Customer")
	supplier = models.CharField(max_length=200, verbose_name="Supplier", null=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount", blank=True)
	note = models.CharField(max_length=200, blank=True, verbose_name="Note")

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s %s %s %s' % (self.operation_date, self.amount, self.causal, self.cashdesk)
		return u'%s' % (self.prot)

class PharmaceuticalInventoryMovements(models.Model):

	class Meta:
		verbose_name_plural = "Pharmaceutical Inventory Movements"
	IN = 1
	OUT = 2
	IN_OUT = (
		(IN, 'LOAD'),
		(OUT, 'UNLOAD'),
	)


	author = models.ForeignKey(
			User,
			null=True,
			editable=False,
	)

	load_discharge = models.PositiveSmallIntegerField(choices=IN_OUT, null=True, verbose_name="Load / Discharge")
	annulled = models.BooleanField(default=True, help_text='[Deselect for cancel entry]', verbose_name="Validation")
	operation_date = models.DateField(verbose_name="Operation Date", default=timezone.now)
	cashdesk = models.ForeignKey('settings.CashDesk', verbose_name="Cash Service")
	customer = models.ForeignKey('settings.Customer', null=True, verbose_name="Service Customer")
	# drug = models.ForeignKey('settings.Customer', verbose_name="Generic Drug")
	drug = models.CharField(max_length=200, blank=True, verbose_name="Generic Drug")
	quantity = models.IntegerField()
	note = models.CharField(max_length=200, blank=True, verbose_name="Note")
	sign = models.ForeignKey('settings.Operator', on_delete=models.CASCADE, verbose_name="Sign")

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s %s %s %s' % (self.operation_date, self.amount, self.causal, self.cashdesk)
		return u'%s' % (self.id)
