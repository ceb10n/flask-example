from .account import Account
from .api_resource import APIResource


class DigitalOcean(object):

    def __init__(self, token):
        self.token = token
        self._account = None

    def account(self):
        if not self._account:
            resource = APIResource('account', self.token)
            account = Account()
            self._account = resource.get(account)

        return self._account
