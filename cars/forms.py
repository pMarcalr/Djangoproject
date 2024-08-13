from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 100000:
            self.add_error("value", "Valor minimo do carro deve ser de R$100.000")
        return value
    def clean_factorty_year(self):
        factorty_year = self.cleaned_data.get("factorty_year")
        if factorty_year < 1950:
            self.add_error("factorty_year", "Não é possivel cadastrar carros fabricados antes de 1950")
        return factorty_year