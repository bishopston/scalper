from django.urls import path
from . import views
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('options/', views.OptionView, name='option'),
    path('options/<str:optionsymbol>/', views.OptionScreenerDetail, name='option_screener_detail'),
    path('options_multiple/<str:optionsymbol>/', views.OptionScreenerMultipleDetail, name='option_screener_multiple_detail'),
    path('options/chart/<str:tradesymbol>/', views.OptionJSChartView, name="option_jschart"),
    path('options/chart_multiple/<str:tradesymbol>/', views.OptionJSChartMultipleView, name="option_jschart_multiple"),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)