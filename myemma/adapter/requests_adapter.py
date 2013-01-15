import json
import requests
import requests.auth
from myemma.adapter import AbstractAdapter, ApiRequestFailed

class RequestsAdapter(AbstractAdapter):
    """
    Emma API Adapter for the `Requests Library
    <http://docs.python-requests.org/>`_

    :param auth: A dictionary with keys for your account id and public/private
                 keys
    :type auth: :class:`dict`

    Example auth :class:`dict`::

        {"account_id": "1234",
         "public_key": "08192a3b4c5d6e7f",
         "private_key": "f7e6d5c4b3a29180"}

    """
    def __init__(self, auth):
        self.auth = requests.auth.HTTPBasicAuth(
            auth['public_key'],
            auth['private_key'])
        self.url = "https://api.e2ma.net/%s" % auth['account_id']

    def _process_response(self, response):
        if response.status_code == 404:
            return None
        elif response.status_code > 200:
            raise ApiRequestFailed(response)

        return response.json

    def post(self, path, data=None):
        """
        Takes an effective path (portion after https://api.e2ma.net/:account_id)
        and a parameter dictionary, then passes these to :func:`requests.post`

        :param path: The path portion of a URL
        :type path: :class:`str`
        :param data: The content to encode
        :type data: :class:`object`
        :rtype: JSON-encoded value or None (if 404)
        """
        return self._process_response(
            requests.post(
                self.url + "%s" % path,
                data=json.dumps(data),
                auth=self.auth))

    def get(self, path, params={}):
        """
        Takes an effective path (portion after https://api.e2ma.net/:account_id)
        and a parameter dictionary, then passes these to :func:`requests.get`

        :param path: The path portion of a URL
        :type path: :class:`str`
        :param params: The dictionary of HTTP parameters to encode
        :type params: :class:`dict`
        :rtype: JSON-encoded value or None (if 404)
        """
        return self._process_response(
            requests.get(
                self.url + "%s" % path,
                params=params,
                auth=self.auth))

    def put(self, path, params={}):
        """
        Takes an effective path (portion after https://api.e2ma.net/:account_id)
        and a parameter dictionary, then passes these to :func:`requests.put`

        :param path: The path portion of a URL
        :type path: :class:`str`
        :param params: The dictionary of HTTP parameters to encode
        :type params: :class:`dict`
        :rtype: JSON-encoded value or None (if 404)
        """
        return self._process_response(
            requests.put(
                self.url + "%s" % path,
                params=params,
                auth=self.auth))

    def delete(self, path, params={}):
        """
        Takes an effective path (portion after https://api.e2ma.net/:account_id)
        and a parameter dictionary, then passes these to :func:`requests.delete`

        :param path: The path portion of a URL
        :type path: :class:`str`
        :param params: The dictionary of HTTP parameters to encode
        :type params: :class:`dict`
        :rtype: JSON-encoded value or None (if 404)
        """
        return self._process_response(
            requests.delete(
                self.url + "%s" % path,
                params=params,
                auth=self.auth))