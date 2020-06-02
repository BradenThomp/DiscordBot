

class BaseCollection:
    def __init__(self):
        print('Constructing base collection for developement...')

    def save(self, bson):
        print('Mock saving: {0}'.format(bson))
