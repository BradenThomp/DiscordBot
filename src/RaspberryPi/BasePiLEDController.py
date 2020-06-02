
class BasePiLEDController:
    def init(self):
        print('Constructing BasePiLEDController for development')

    def poweron(self):
        print('Mock LED On')

    def poweroff(self):
        print('Mock LED Off')

    def startup(self):
        print('Mock Startup')

    def cleanup(self):
        print('Mock Cleanup')