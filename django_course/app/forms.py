from django import forms

class MainForm(forms.Form):


    T = forms.FloatField(label='Время, с:', initial=100*3600) #form-control
    k = forms.FloatField(label='Проницаемость, мД:', initial=20)
    por = forms.FloatField(label='Пористость, д.ед.:', initial=100*3600)
    mu = forms.FloatField(label='Вязкость, Па*с:', initial=1.5E-3)
    Ct = forms.FloatField(label='Общая сжимаемость, 1/Па:', initial=4.9E-10)
    h = forms.FloatField(label='Толщина пласта, м:', initial=100*3600)
    rw = forms.FloatField(label='Радиус скважины, м:', initial=100*3600)
    re = forms.FloatField(label='Радиус контура, м:', initial=100*3600)
    Bo = forms.FloatField(label='Объемный коэффициент, м3/м3:', initial=100*3600)
    Po = forms.FloatField(label='Пластовое давление, атм:', initial=100*3600)
    q = forms.FloatField(label='Дебит, м3/сут:', initial=100*3600)
