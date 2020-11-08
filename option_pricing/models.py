from django.db import models

class Option(models.Model):
    FTSE = 'FTSE'
    ALPHA = 'ALPHA'
    HTO = 'HTO'
    ETE = 'ETE'
    OPAP = 'OPAP'
    PPC = 'PPC'
    TPEIR = 'TPEIR'
    C = 'c'
    P = 'p'
    
    ASSETS = [
        (FTSE, 'FTSE'),
        (ALPHA, 'ALPHA'),
        (HTO, 'HTO'),
        (ETE, 'ETE'),
        (OPAP, 'OPAP'),
        (PPC, 'PPC'),
        (TPEIR, 'TPEIR'),
    ]

    OPTIONTYPES = [
        (C, 'Call'),    
        (P, 'Put')
    ]

    optionsymbol = models.CharField(max_length=15)
    date = models.DateTimeField()
    asset = models.CharField(max_length=10)
    optiontype = models.CharField(max_length=4)
    strike = models.FloatField()
    expmonthdate = models.DateField()
    closing_price = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    max = models.FloatField()
    min = models.FloatField()
    trades = models.IntegerField()
    fixing_price = models.FloatField()
    open_interest = models.IntegerField()
    stock = models.FloatField()
    imp_vol = models.FloatField()
    atm_strike = models.FloatField()
    frontexpdate = models.DateField()
    expmonth_atm_impvol = models.FloatField()

    def __str__(self):
	    return self.optionsymbol

class Future(models.Model):
    futuresymbol = models.CharField(max_length=15)
    date = models.DateTimeField()
    asset = models.CharField(max_length=10)
    expmonthyear = models.DateField()
    closing_price = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    max = models.FloatField()
    min = models.FloatField()
    trades = models.IntegerField()
    fixing_price = models.FloatField()
    open_interest = models.IntegerField()

    def __str__(self):
	    return self.futuresymbol

class Stock(models.Model):
    symbol = models.CharField(max_length=15)
    date = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
	    return self.symbol