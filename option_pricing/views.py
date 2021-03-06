from django.shortcuts import render
from django.db.models import Max, Min
from django.core.paginator import Paginator
from django.http import JsonResponse

from datetime import datetime
import json

from .models import Option
from .forms import OptionScreenerForm

# Create your views here.
def home(request):
    return render(request, 'option_pricing/home.html')

def OptionView(request):
    #max_date = Option.objects.all().aggregate(Max('date'))
    #latest_option = Option.objects.filter(date=max_date['date__max']) 
    option = Option.objects.all()
    
    asset_query = request.GET.get('asset')
    callputflag_query = request.GET.get('option_type')
    exp_month_query = request.GET.get('exp_month')
    exp_year_query = request.GET.get('exp_year')

    if asset_query != '' and asset_query is not None:
        option = option.filter(asset__iexact=asset_query)

    if callputflag_query != '' and callputflag_query is not None:
        option = option.filter(optiontype__iexact=callputflag_query)

    if exp_month_query != '' and exp_month_query is not None:
        option = option.filter(expmonthdate__month=exp_month_query)

    if exp_year_query != '' and exp_year_query is not None:
        option = option.filter(expmonthdate__year=exp_year_query)

    max_date = option.aggregate(Max('date'))
    queryset = option.filter(date=max_date['date__max']).order_by('strike')
    #queryset = latest_option.distinct('strike').order_by('strike')

    queryset_num = queryset.count()

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'queryset' : queryset,
        'max_date' : max_date,
        'asset_query': asset_query,
        'callputflag_query': callputflag_query,
        'exp_month_query' : exp_month_query,
        'exp_year_query' : exp_year_query,
        'optionscreenerform' : OptionScreenerForm(),
        'queryset_num' : queryset_num,
        'page_obj': page_obj
    }
    return render(request, 'option_pricing/option.html', context)

def OptionScreenerDetail(request, optionsymbol):
    option_strikespan = Option.objects.filter(optionsymbol=optionsymbol).order_by('-date')
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 
    closing_price = option_strikespan[0].closing_price
    change = option_strikespan[0].change
    asset = option_strikespan[0].asset
    optiontype = option_strikespan[0].optiontype
    if optiontype == 'c': 
        optiontype = 'Call'
    else:
        optiontype = 'Put'
    expmonth = option_strikespan[0].expmonthdate.strftime("%B")
    expyear = option_strikespan[0].expmonthdate.strftime("%Y")
    expdate = option_strikespan[0].expmonthdate.strftime("%#d-%#m-%Y")
    strike = option_strikespan[0].strike
    latest_trad_date = option_strikespan[0].date.strftime("%#d-%#m-%Y")
    volume = option_strikespan[0].volume
    trades = option_strikespan[0].trades
    open_interest = option_strikespan[0].open_interest
    imp_vol = "{:.2%}".format(option_strikespan[0].imp_vol)
    stock = option_strikespan[0].stock
    moneyness = 'moneyness'

    if optiontype == 'c' and stock > strike: 
        moneyness = 'ITM'
    elif optiontype == 'c' and stock < strike:
        moneyness = 'OTM'
    elif optiontype == 'p' and stock > strike: 
        moneyness = 'OTM'
    elif optiontype == 'c' and stock < strike:
        moneyness = 'ITM'
    else:
        moneyness = 'ATM'

    lifetime_high = option_strikespan.aggregate(Max('closing_price'))
    lifetime_low = option_strikespan.aggregate(Min('closing_price'))

    context = {
        'option_strikespan' : option_strikespan,
        'trade_symbol' : trade_symbol,
        'closing_price' : round(closing_price,3),
        'change' : change,
        'asset' : asset,
        'optiontype' : optiontype,
        'expmonth' : expmonth,
        'expyear' : expyear,
        'expdate' : expdate,
        'strike' : strike,
        'latest_trad_date' : latest_trad_date,
        'volume' : volume,
        'trades' : trades,
        'open_interest' : open_interest,
        'imp_vol' : imp_vol,
        'moneyness' : moneyness,
        'lifetime_high' : lifetime_high['closing_price__max'],
        'lifetime_low' : lifetime_low['closing_price__min'],
    }

    return render(request, 'option_pricing/option_screener_div_table.html', context)
"""
def OptionScreenerMultipleDetail(request, optionsymbol):
    option_strikespan = Option.objects.filter(optionsymbol=optionsymbol).order_by('-date')
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 

    context = {
        'option_strikespan' : option_strikespan,
        'trade_symbol' : trade_symbol,
    }

    return render(request, 'option_pricing/option_screener_multiple.html', context)
"""

def OptionJSChartView(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    #opt = option.all()

    for i in option:
        optiondata.append({json.dumps(i.date.strftime("%#d-%#m-%Y")):i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)
"""
def OptionJSChartMultipleView(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    #opt = option.all()

    for i in option:
        optiondata.append({json.dumps(i.date.strftime("%#d-%#m-%Y")):i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)
"""
def OptionJSChartVolView(request, tradesymbol):
    voldata = []

    vol = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    #opt = option.all()

    for i in vol:
        voldata.append({json.dumps(i.date.strftime("%#d-%#m-%Y")):i.volume})
    
    #print(voldata)
    return JsonResponse(voldata, safe=False)