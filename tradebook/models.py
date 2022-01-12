from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


INDEX = (
        ('Nifty', 'NIFTY'),
        ('Banknifty', 'BANKNIFTY'),
)
POSITION = (
    ('BUY', 'Buy'),
    ('SELL', 'Sell'),
)
CALL_TYPE = (
    ('CE', 'CE'),
    ('PE', 'PE'),
)
QUANTITIES = [(i,i) for i in range(11)]

class Note(models.Model):
    # serial_id = models.IntegerField(default=lambda: Note.objects.latest('id').serial + 1)
    # serial_id = models.AutoField(primary_key=True, null=False)
    
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    index = models.CharField(max_length=10, choices=INDEX, default='Nifty')
    strike_price = models.IntegerField(default=0)
    call_type = models.CharField(
        max_length=10, choices=CALL_TYPE, default='CE')
    position = models.CharField(max_length=10, choices=POSITION, default='BUY')
    lot = models.CharField(max_length=9, choices=QUANTITIES, default='1')

    avg_price = models.IntegerField(default=0)
    sqo_price = models.IntegerField(default=0)
    sqo_price2 = models.IntegerField(default=0, null=True, blank=True)
    swing_high = models.IntegerField(default=0, null=True, blank=True)
    swing_low = models.IntegerField(default=0, null=True, blank=True)
    profit_loss = models.IntegerField(default=0)

    upload = models.ImageField(upload_to='static-coll/charts/', null=True, blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- ' + self.index + ' -- ' + str(self.strike_price) + ' -- ' + self.call_type
       
