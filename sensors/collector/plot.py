from plotly.offline import plot
from plotly.graph_objs import Scatter
from collector.models import Temperature, Humidity, Pressure


def temperature(start_time):
    data = Temperature.objects.filter(time__gt=start_time)
    x_axis = []
    y_axis = []
    for point in data:
        y_axis.append(point.value)
        x_axis.append(point.time)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines+markers', name='temperature',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div


def humidity(start_time):
    data = Humidity.objects.filter(time__gt=start_time)
    x_axis = []
    y_axis = []
    for point in data:
        y_axis.append(point.value)
        x_axis.append(point.time)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines+markers', name='humidity',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div


def pressure(start_time):
    data = Pressure.objects.filter(time__gt=start_time)
    x_axis = []
    y_axis = []
    for point in data:
        y_axis.append(point.value)
        x_axis.append(point.time)

    plot_div = plot([Scatter(x=x_axis , y=y_axis,
                             mode='lines+markers', name='pressure',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return plot_div
