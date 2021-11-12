# -*- coding: utf-8 -*-
from datetime import datetime
import pytz


def time_zone(continente,ciudad):
    my_city_timezone = pytz.timezone(continente+'/'+ciudad)
    my_city_time = datetime.now(my_city_timezone)
    print(ciudad,':', my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

time_zone('America','Bogota')
time_zone('America','Mexico_City')
time_zone('America','Caracas')
time_zone('America','Lima')
time_zone('Europe','Madrid')
time_zone('Europe','Lisbon')
time_zone('Europe','Paris')