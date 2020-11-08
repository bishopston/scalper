from django import forms
from . models import Option

import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import FormActions, InlineRadios

EXP_YEAR_CHOICES = [('', 'Choose...'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'),]
EXP_MONTH_CHOICES = [
    ('', 'Choose...'),
    ('1', 'JAN'),
    ('2', 'FEB'),
    ('3', 'MAR'),
    ('4', 'APR'),
    ('5', 'MAY'),
    ('6', 'JUN'),
    ('7', 'JUL'),
    ('8', 'AUG'),
    ('9', 'SEP'),
    ('10', 'OCT'),
    ('11', 'NOV'),
    ('12', 'DEC'),
]

ASSETS = [
    ('', 'Choose...'),
    ('FTSE', 'FTSE'),
    ('ALPHA', 'ALPHA'),
    ('HTO', 'HTO'),
    ('ETE', 'ETE'),
    ('OPAP', 'OPAP'),
    ('PPC', 'PPC'),
    ('TPEIR', 'TPEIR'),
]

OPTION_TYPE = [
    ('c', 'Call'),
    ('p', 'Put'),
]

class OptionSelectionForm(forms.Form):
    asset = forms.CharField(
        label="Underlying Asset",
        widget=forms.Select(
        choices=ASSETS,
    ))

    option_type = forms.ChoiceField(
        label="Option Type",
        widget=forms.RadioSelect,
        choices=OPTION_TYPE,
        initial = 'call',
    )
    exp_month = forms.CharField(
        label="Expiration Month",
        widget=forms.Select(
        choices=EXP_MONTH_CHOICES,
    ))
    exp_year = forms.CharField(
        label="Expiration Year",
        widget=forms.Select(
        choices=EXP_YEAR_CHOICES,
    ))


    # Uni-form
    helper = FormHelper()
    helper.form_method = 'GET'
    #helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    #helper.form_tag = False
    #helper.add_input(Submit('submit', 'Submit', css_class='btn_primary'))
    helper.layout = Layout(
        Field('asset', css_class='form-group col-md-4 mb-0', style="font-size: 0.8rem;"),
        InlineRadios('option_type', style="font-size: 0.8rem;"),
        Field('exp_month', style="font-size: 0.8rem;"),
        Field('exp_year', style="font-size: 0.8rem;"),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )



class OptionSelectionFormInit(forms.Form):
    asset = forms.CharField(
        label="Underlying Asset",
        widget=forms.Select(attrs={'class': 'myfieldclass'},
        choices=ASSETS
    ))

    option_type = forms.ChoiceField(
        label="Option Type",
        widget=forms.RadioSelect,
        choices=OPTION_TYPE,
        initial = 'c',
    )
    exp_month = forms.CharField(
        label="Expiration Month",
        widget=forms.Select(
        choices=EXP_MONTH_CHOICES,
    ))
    exp_year = forms.CharField(
        label="Expiration Year",
        widget=forms.Select(
        choices=EXP_YEAR_CHOICES,
    ))

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.label_class = 'col-lg-2'
    self.helper.field_class = 'col-lg-2'
    self.helper.layout = Layout(
        Row(
            Column('asset', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('option_type', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('exp_month', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('exp_year', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Submit('submit', 'Submit')
    )

class OptionScreenerForm(forms.Form):
    asset = forms.CharField(
        label="Underlying Asset",
        widget=forms.Select(
        choices=ASSETS,
        attrs={
            'class': 'form-control form-control-sm',
        }
    ))

    option_type = forms.ChoiceField(
        label="Option Type",
        widget=forms.RadioSelect(attrs={
        'class': 'form-check-label'
        }),
        choices=OPTION_TYPE,
        initial = 'c'

    )

    exp_month = forms.CharField(
        label="Expiration Month",
        widget=forms.Select(
        choices=EXP_MONTH_CHOICES,
        attrs={
        'class': 'form-control form-control-sm'
    }
    ))

    exp_year = forms.CharField(
        label="Expiration Year",
        widget=forms.Select(
        choices=EXP_YEAR_CHOICES,
        attrs={
        'class': 'form-control form-control-sm'
    }
    ))