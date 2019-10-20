from django.shortcuts import render
from . import plot
from . import collector

def index_view(request):
    collector.values_to_db()
    plot_temp = plot.temperature()
    plot_humidity = plot.humidity()
    plot_pressure = plot.pressure()
    return render(request, "collector/index.html",
                  context={'plot_temp': plot_temp,
                           'plot_humidity': plot_humidity,
                           'plot_pressure': plot_pressure})
