def OptionJSChartMultipleView(request, tradesymbol):
    #number_days_query = request.GET.get('number_days')
    optiondata = [[] for i in range(15)]
    #vol = []

    option1 = Option.objects.filter(optionsymbol=tradesymbol).order_by('-date')[:15]
    _option1 = list(reversed(option1))
    #_option1_ = serializers.serialize("json", _option1)
    option2 = Option.objects.filter(optionsymbol=tradesymbol).order_by('-date')[:30]
    _option2 = list(reversed(option2))
    option3 = Option.objects.filter(optionsymbol=tradesymbol).order_by('-date')[:90]
    _option3 = list(reversed(option3))
    option4 = Option.objects.filter(optionsymbol=tradesymbol).order_by('-date')[:180]
    _option4 = list(reversed(option4))
    option5 = Option.objects.filter(optionsymbol=tradesymbol).order_by('-date')
    _option5 = list(reversed(option5))

    for i in _option1:
        optiondata[0].append({json.dumps(i.date.strftime("%#d/%m/%Y")):i.closing_price})
    for i in _option2:
        optiondata[1].append({json.dumps(i.date.strftime("%#d/%m/%Y")):i.closing_price})
    for i in _option3:
        optiondata[2].append({json.dumps(i.date.strftime("%#d/%m/%Y")):i.closing_price})
    for i in _option4:
        optiondata[3].append({json.dumps(i.date.strftime("%#d/%m/%Y")):i.closing_price})
    for i in _option5:
        optiondata[4].append({json.dumps(i.date.strftime("%#d/%m/%Y")):i.closing_price})


    print(optiondata[0])
    #optiondata = serializers.serialize("json", optiondata)
    return JsonResponse(optiondata, safe=False)