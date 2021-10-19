from django import forms

class NameForm(forms.Form):
    T = forms.FloatField(label='Время, с:', initial=100*3600)
    k = forms.FloatField(label='Проницаемость, мД:', initial=20)
    por = forms.FloatField(label='Пористость, д.ед.:', initial=0.3)
    mu = forms.FloatField(label='Вязкость, Па*с:', initial=1.5E-3)
    Ct = forms.FloatField(label='Общая сжимаемость, 1/Па:', initial=4.9E-10)
    h = forms.FloatField(label='Толщина пласта, м:', initial=20)
    rw = forms.FloatField(label='Радиус скважины, м:', initial=0.1)
    re = forms.FloatField(label='Радиус контура, м:', initial=250)
    Bo = forms.FloatField(label='Объемный коэффициент, м3/м3:', initial=1)
    Po = forms.FloatField(label='Пластовое давление, атм:', initial=250)
    q = forms.FloatField(label='Дебит, м3/сут:', initial=50)
