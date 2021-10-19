from django.shortcuts import render
from django.http import HttpResponse
from app.forms import NameForm
from plotly.offline import plot
from plotly.graph_objects import Scattergl, Layout, Figure
from app.stable_rate import *
from app.models import StableRate

def index(request):
    context = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        context['form'] = form

        k = float(form['k'].value())*10**-15 #2.0E-14 # проницаемость, Д (20 мД)
        por = float(form['por'].value()) #0.3 # пористость д.ед.
        mu = float(form['mu'].value()) #1.5E-3 # взякость, Па*с
        Ct = float(form['Ct'].value()) #4.9E-10 # сжимаемость, 1/Па
        h = float(form['h'].value()) #20 # толщина пласта, м
        rw = float(form['rw'].value()) #0.1 # радиус скважины, м
        re = float(form['re'].value()) #250 # радиус контура, м
        Bo = float(form['Bo'].value()) #1 # объемный коэффициент м3/м3
        Po = float(form['Po'].value())*101325 # пластовое давление, Па
        q = float(form['q'].value())/86400 # дебит, м3/с
        
        N = 12 # точность
        T = int(form['T'].value())
        x_list = [_ for _ in range(100, T, 10000)]
        y_list = []
        for t in x_list:
            stable_rate = StableRate()
            y_list.append((Po + Pt11(N, t, k, por, mu, Ct, Bo, rw, re, h, Po, q))/101325)
            stable_rate.x = t
            stable_rate.y = y_list[-1]
            stable_rate.save()

        # построение графика
        print(x_list, y_list)
        data = []
        data.append(Scattergl(y=y_list, x=x_list, mode='lines',
                            line={'dash': 'solid', 'color': '#AF479D'}))
        layout = Layout(width=800, height=600, legend=dict(orientation="h", y=1.1),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', )
        figure = Figure(data=data, layout=layout)
        figure.update_xaxes(linewidth=2, linecolor='#A6A8AB', gridcolor='#A6A8AB')
        figure.update_yaxes(linewidth=2, linecolor='#A6A8AB', gridcolor='#A6A8AB')
        plot_fig = plot(figure, auto_open=False, output_type='div')
        context['plot'] = plot_fig
    else:
        form = NameForm()
        context['form'] = form

    return render(request, 'app/index.html', context)
