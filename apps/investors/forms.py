from django.forms import ModelForm

from .models import Info


class ChooseBroker(ModelForm):
    class Meta:
        model = Info
        fields = ('chosen_broker',)

    def __init__(self, *args, **kwargs):
        super(ChooseBroker, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[
                'chosen_broker'].help_text = '*Select the broker you wish to signup and click continue, a sign up window will pop up'
            self.fields['chosen_broker'].label = 'Choose your broker'


class VerifyAmountInvested(ModelForm):
    class Meta:
        model = Info
        fields = ('invest_amount',)

    def __init__(self, *args, **kwargs):
        super(VerifyAmountInvested, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['invest_amount'].help_text = '*It must match the amount you\'ve invested with the broker'
            self.fields['invest_amount'].label = 'Please verify your investment amount (In dollar amount)'
