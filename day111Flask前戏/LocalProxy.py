DATA = {
    'request': {
        'method': "GET",
        'form': {}
    },
    'session': {
        'name': 'xiaoli',
        'age': '19'
    }
}


class LocalProxy(object):
    def __init__(self, key):
        self.key = key

    def get_dict(self):
        return DATA[self.key]

    def __str__(self):
        return 'aa'

    def __getattr__(self, item):
        data_dict = self.get_dict()
        return data_dict[item]

    def __getitem__(self, item):
        data_dict = self.get_dict()
        return data_dict[item]


request = LocalProxy('request')
session = LocalProxy('session')

