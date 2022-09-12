from car import Car
from datetime import datetime
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from tires.octoprime_tire import OctoprimeTire


class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)
        rorschach_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(rorschach_engine, rorschach_battery, rorschach_tire)

        self.engine = rorschach_engine
        self.battery = rorschach_battery
        self.tire = rorschach_tire

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
