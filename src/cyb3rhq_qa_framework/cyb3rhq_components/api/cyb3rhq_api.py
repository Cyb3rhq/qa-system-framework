"""
Module to wrapp the main Cyb3rhq API calls. This module contains the following:

- Cyb3rhqAPI:
    - get_token
    - set_token_expiration
    - get_api_info
    - list_agents
    - restart_agent
"""
from base64 import b64encode
from http import HTTPStatus
import requests

from cyb3rhq_qa_framework.cyb3rhq_components.api.cyb3rhq_api_request import Cyb3rhqAPIRequest
from cyb3rhq_qa_framework.generic_modules.request.request import GetRequest
from cyb3rhq_qa_framework.generic_modules.exceptions.exceptions import ConnectionError, RuntimeError


DEFAULT_USER = 'cyb3rhq'
DEFAULT_PASSOWRD = 'cyb3rhq'
DEFAULT_PORT = 55000
DEFAULT_ADDRESS = 'localhost'
DEFAULT_PROTOCOL = 'https'
DEFAULT_TOKEN_EXPIRATION = 900


class Cyb3rhqAPI:
    """Class to manage the Cyb3rhq API via requests.

    Args:
        user (str): Cyb3rhq API user.
        password (str): Cyb3rhq API password.
        port (int): Cyb3rhq API port connection.
        address (str): Cyb3rhq API address.
        protocol (str): Cyb3rhq API protocol.
        auto_auth (boolean): True for getting the API auth token automatically, False otherwise.
        token_expiration (int): Number of seconds to set to the token expiration.

    Attributes:
        user (str): Cyb3rhq API user.
        password (str): Cyb3rhq API password.
        port (int): Cyb3rhq API port connection.
        address (str): Cyb3rhq API address.
        protocol (str): Cyb3rhq API protocol.
        token (str): Cyb3rhq API auth token.
        token_expiration (int): Number of seconds to set to the token expiration.
    """
    def __init__(self, user=DEFAULT_USER, password=DEFAULT_PASSOWRD, port=DEFAULT_PORT, address=DEFAULT_ADDRESS,
                 protocol=DEFAULT_PROTOCOL, auto_auth=True, token_expiration=DEFAULT_TOKEN_EXPIRATION):
        self.user = user
        self.password = password
        self.port = port
        self.address = address
        self.protocol = protocol
        self.url = f"{protocol}://{address}:{port}"
        self.token_expiration = token_expiration
        self.token = self.get_token() if auto_auth else None

        if token_expiration != DEFAULT_TOKEN_EXPIRATION:
            self.set_token_expiration(token_expiration)
            self.token = self.get_token()

    def get_token(self):
        """Get the auth API token.

        Returns:
            str: API auth token.

        Raises:
            exceptions.RuntimeError: If there are any error when obtaining the login token.
            exceptions.RuntimeError: Cannot establish connection with API.
        """
        basic_auth = f"{self.user}:{self.password}".encode()
        auth_header = {'Content-Type': 'application/json', 'Authorization': f'Basic {b64encode(basic_auth).decode()}'}

        try:
            response = GetRequest(f"{self.url}/security/user/authenticate?raw=true", headers=auth_header).send()

            if response.status_code == HTTPStatus.OK:
                return response.text

            raise RuntimeError(f"Error obtaining login token: {response.json()}")

        except requests.exceptions.ConnectionError as exception:
            raise ConnectionError(f"Cannot establish connection with {self.url}") from exception

    def set_token_expiration(self, num_seconds):
        """Set the Cyb3rhq API token expiration.

        Returns:
            Cyb3rhqAPIResponse: Operation result (response).
        """
        response = Cyb3rhqAPIRequest(method='PUT', endpoint='/security/config',
                                   payload={'auth_token_exp_timeout': num_seconds}).send(self)
        return response

    @Cyb3rhqAPIRequest(method='GET', endpoint='/')
    def get_api_info(self, response):
        """Get the Cyb3rhq API info.

        Returns:
            dict: Cyb3rhq API info.
        """
        return response.data

    @Cyb3rhqAPIRequest(method='GET', endpoint='/agents')
    def list_agents(self, response):
        """List the cyb3rhq agents.

        Returns:
            dict: Cyb3rhq API info.
        """
        return response.data

    def restart_agent(self, agent_id):
        """Restart a cyb3rhq-agent.

        Returns:
            dict: Cyb3rhq API info.
        """
        response = Cyb3rhqAPIRequest(method='PUT', endpoint=f"/agents/{agent_id}/restart").send(self)

        return response
