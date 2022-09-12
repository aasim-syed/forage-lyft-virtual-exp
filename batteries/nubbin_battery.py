from datetime import datetime
from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
