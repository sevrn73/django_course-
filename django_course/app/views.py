from django.shortcuts import render
from django.http import HttpResponse
from app.forms import MainForm
from app.stable_rate import *
from plotly.offline import plot
from plotly.graph_objects import Scattergl, Layout, Figure

def index(request):
    main_form = MainForm()
    context = {'main_form': main_form}
    # try:
    main_form = MainForm(request.POST)
    T = main_form["T"].value()
    k = main_form["k"].value()
    por = main_form["por"].value()
    mu = main_form["mu"].value()
    Ct = main_form["Ct"].value()
    h = main_form["h"].value()
    rw = main_form["rw"].value()
    re = main_form["re"].value()
    Bo = main_form["Bo"].value()
    Po = main_form["Po"].value()
    q = main_form["q"].value()
    N = 12 # точность
    if request.method == "POST":
        x_data, y_data = [_ for _ in range(1, int(T), 1000)], []
        for t in x_data:
            y_data.append((float(Po)*101325 + Pt11(int(N), float(t), float(k)*10**-14, float(por), float(mu), float(Ct), float(Bo), float(rw), float(re), float(h), float(Po)*101325, float(q)/86400))/101325)

        print(x_data, y_data)
        plot = create_nodal_func_plot(x_data, y_data,  f'Динамика добычи', 'Время', 'Дебит, м3/сут')
        context['plot'] = plot
    # except:
        # pass

    return render(request, 'app/index.html', context)

def create_nodal_func_plot(x_list: list, y_list: list, name: str, xaxis: str, yaxis: str):
    """
    ## Функция построения графика динамики параметров стоимости электричества
    Parameters
    ----------
    :param x_list: список с данными по x
    :param y_list: список с данными по y
    :param name: анотация к trace
    :param xaxis: подпись оси y
    :param yaxis: подпись оси y
    :return: plot_fig: график
    ----------
    """
    data = []
    data.append(Scattergl(y=y_list, x=x_list, mode='lines',
                          line={'dash': 'solid', 'color': '#AF479D'},
                          name=name))
    layout = Layout(
        xaxis={'title': xaxis},
        yaxis={'title': yaxis}, width=800, height=600, legend=dict(orientation="h", y=1.1),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', )
    figure = Figure(data=data, layout=layout)
    figure.update_xaxes(linewidth=2, linecolor='#A6A8AB', gridcolor='#A6A8AB')
    figure.update_yaxes(linewidth=2, linecolor='#A6A8AB', gridcolor='#A6A8AB')
    plot_fig = plot(figure, auto_open=False, output_type='div')

    return plot_fig