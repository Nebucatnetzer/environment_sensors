from plotly.offline import plot
from plotly.graph_objs import Scatter
from collector.models import Time, Temperature, Humidity, Pressure


def temperature():
    data = Temperature.objects.all()[30:]
    x_axis = []
    y_axis = []
    for point in data:
        print(point.value)
        x_axis.append(point.value)
        y_axis.append(point.time.value)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines', name='temperature',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div


def humidity():
    data = Humidity.objects.all()[30:]
    x_axis = []
    y_axis = []
    for point in data:
        x_axis.append(point.value)
        y_axis.append(point.time.value)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines', name='humidity',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div


def pressure():
    data = Pressure.objects.all()[30:]
    x_axis = []
    y_axis = []
    for point in data:
        x_axis.append(point.value)
        y_axis.append(point.time.value)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines', name='pressure',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div
