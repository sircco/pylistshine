import json
import logging
from abc import ABCMeta
from builtins import object
from functools import partial

import requests
from future.utils import with_metaclass

from .constants import LISTSHINE_API_BASE

logger = logging.getLogger(__name__)


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


class LSContact(object):
    ''' get information about single contact i.e. blah@blah.com'''

    def __init__(self, connection, list_id):
        self.connection = connection
        self.list_id = list_id
        self.url_base = connection.api_base + 'escontact'

    def subscribe(self, email, **kwargs):
        ''' subscribe email to contactlist '''
        api_url = self.url_base + '/contactlist/subscribe/{list_id}/'.format(list_id=self.list_id)
        kwargs.update({'email': email})
        response = self.connection.connection_post(url=api_url, json=kwargs)
        logger.warning('posting to url %s', api_url)
        response.raise_for_status()
        return response

    def list(self, email=None):
        ''' retrieve contacts from contactlist ''

        Args:
            email (str, optional): filter list by this email, if none show paged contacts in list

        Returns:
            http json encoded response object, use .json() if you need dictionary
        '''

        api_url = self.url_base + '/contactlist/{list_id}/'.format(list_id=self.list_id)
        jsonfilter = {'filters': [{'filter_type': 'equal',
                                   'filter_field': 'contactlist_uuid',
                                   'filter_value': self.list_id}]}
        if email:
            jsonfilter['filters'].append({'filter_type': 'equal',
                                          'filter_field': 'email',
                                          'filter_value': email})
        params = {'jsonfilter': json.dumps(jsonfilter)}
        response = self.connection.connection_get(url=api_url, params=params)
        logger.warning('getting from url %s', api_url)
        response.raise_for_status()
        return response

    def unsubscribe(self, email):
        ''' unsubscribe email from contactlist

        Args:
            email (str):

        Returns:
            generator for json encoded response objects, use .json() on each result if you
            need dictionary.
        '''
        api_url = self.url_base + '/contactlist/{list_id}/contact/{id}/unsubscribe/'
        contacts = self.list(email)
        for contact in contacts.json()['results']:
            api_url = api_url.format(list_id=self.list_id, id=contact['id'])
            response = self.connection.connection_post(api_url)
            response.raise_for_status()
            logger.warning('posting to url %s', api_url)
            yield response


class LSContactList(object):
    ''' get information about contactlist '''

    def __init__(self, connection):
        self.connection = connection
        self.url_base = connection.api_base + 'contactlist'

    def list(self):
        ''' list all contactlists '''
        return self.connection.connection_get(url=self.url_base)

    def retrieve(self, list_id):
        ''' contactlist details '''
        api_url = self.url_base + '/{list_id}/'.format(list_id=list_id)
        return self.connection.connection_get(url=api_url)

# class LSSegment:
#     def all_segments(self):
#         pass

#     def get_segment_by_id(self, segment_id):
#         pass
