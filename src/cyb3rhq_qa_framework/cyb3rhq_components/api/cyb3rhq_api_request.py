"""
Module to wrapp the Cyb3rhq API requests. Normally, the developers should not use this class but Cyb3rhqAPI one. This class
is used by Cyb3rhqAPI to make and send the API requests.

This module contains the following:

- Cyb3rhqAPIRequest:
    - send
"""
import json
import requests

from cyb3rhq_qa_framework.generic_modules.request.request import Request
from cyb3rhq_qa_framework.generic_modules.exceptions.exceptions import ConnectionError
from cyb3rhq_qa_framework.cyb3rhq_components.api.cyb3rhq_api_response import Cyb3rhqAPIResponse


class Cyb3rhqAPIRequest:
    """Wrapper class to manage requests to the Cyb3rhq API.

    Args:
        endpoint (str): Target API endpoint.
        method (str): Request method (GET, POST, PUT, DELETE).
        payload (dict): Request data.
        headers (dict): Request headers.
        verify (boolean): False for ignore making insecure requests, False otherwise.

    Attributes:
        endpoint (str): Target API endpoint.
        method (str): Request method (GET, POST, PUT, DELETE).
        payload (dict): Request data.
        headers (dict): Request headers.
        verify (boolean): False for ignore making insecure requests, False otherwise.
    """
    def __init__(self, endpoint, method, payload=None, headers=None, verify=False):
        self.endpoint = endpoint
        self.method = method.upper()
        self.payload = payload
        self.headers = headers
        self.verify = verify

    def __get_request_parameters(self, cyb3rhq_api_object):
        """Build the request parameters.

        Args:
            cyb3rhq_api_object (Cyb3rhqAPI): Cyb3rhq API object.
        """
        # Get the token if we have not got it before.
        if cyb3rhq_api_object.token is None:
            cyb3rhq_api_object.token = cyb3rhq_api_object.get_token()

        self.headers = {} if self.headers is None else self.headers
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {cyb3rhq_api_object.token}'
        })

        request_args = {
            'method': self.method,
            'url': f"{cyb3rhq_api_object.url}{self.endpoint}",
            'headers': self.headers,
            'verify': self.verify
        }

        if self.payload is not None:
            request_args['payload'] = self.payload

        return request_args

    def __call__(self, func):
        """Perform directly the Cyb3rhq API call and add the response object to the function parameters. Useful to run
        the request using only a python decorator.

        Args:
            func (function): Function object.
        """
        def wrapper(obj, *args, **kwargs):
            kwargs['response'] = self.send(obj)

            return func(obj, *args, **kwargs)

        return wrapper

    def __str__(self):
        """Overwrite the print object representation"""
        return json.dumps(self.__dict__)

    def send(self, cyb3rhq_api_object):
        """Send the API request.

        Args:
            cyb3rhq_api_object (Cyb3rhqAPI): Cyb3rhq API object.

        Returns:
            Cyb3rhqAPIResponse: Cyb3rhq API response object.

        Raises:
            exceptions.RuntimeError: Cannot establish connection with the API.
        """
        request_parameters = self.__get_request_parameters(cyb3rhq_api_object)

        try:
            return Cyb3rhqAPIResponse(Request(**request_parameters).send())
        except requests.exceptions.ConnectionError as exception:
            raise ConnectionError(f"Cannot establish connection with {cyb3rhq_api_object.url}") from exception
