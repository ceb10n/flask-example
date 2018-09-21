import requests
from urllib.parse import urljoin

class APIResource(object):
    """ 
    Digital Ocean api class
    """ 

    base_endpoint = 'https://api.digitalocean.com/v2/'

    def __init__(self, name, token):
        self.name = name
        self.headers = {'Authorization': f'Bearer {token}'}
        self.endpoint = urljoin(self.base_endpoint, name)
        self.loaded_data = None


    def get(self, target):
        r =  requests.get(self.endpoint, headers=self.headers)
        self.json_data = r.json()
        
        for attr in self.json_data[self.name].keys():
            setattr(target, attr, self.json_data[self.name][attr])

        return target

    def as_dict(self):
        return self.json_data

