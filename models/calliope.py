from datetime import datetime
from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire
#from engines.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = SpindlerBattery(last_service_date)
        calliope_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(calliope_engine, calliope_battery, calliope_tire)

        self.engine = calliope_engine
        self.battery = calliope_battery
        self.tire = calliope_tire   



    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
