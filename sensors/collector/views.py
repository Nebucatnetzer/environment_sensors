from datetime import datetime, timedelta
from django.shortcuts import render
from . import plot

def index_view(request):
    start_time = datetime.now() - timedelta(hours=24)
    plot_temp = plot.temperature(start_time)
    plot_humidity = plot.humidity(start_time)
    plot_pressure = plot.pressure(start_time)
    return render(request, "collector/index.html",
                  context={'plot_temp': plot_temp,
                           'plot_humidity': plot_humidity,
                           'plot_pressure': plot_pressure})
