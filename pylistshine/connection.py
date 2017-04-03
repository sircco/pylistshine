from abc import ABCMeta
from builtins import object
from functools import partial

import requests
from future.utils import with_metaclass

from .constants import LISTSHINE_API_BASE
from .contactlist import LSContact, LSContactList


class LSConnection(with_metaclass(ABCMeta, object)):
    ''' connection class, used for connecting to ListShine API'''

    def __init__(self, api_key, api_base=LISTSHINE_API_BASE):
        headers = {'Authorization': 'Token %s' % api_key}
        self.api_base = api_base
        self.connection_post = partial(requests.post, headers=headers)
        self.connection_get = partial(requests.get, headers=headers)

    def contact(self, list_id):
        ''' initialize lscontact class
        Args:
            list_id (str): contactlist_uuid from listhine application
        Returns:
            LSContact instance
	'''
        return LSContact(connection=self, list_id=list_id)

    def contactlist(self):
        return LSContactList(connection=self)
