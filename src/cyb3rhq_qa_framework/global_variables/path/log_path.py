"""
Module to build the Cyb3rhq log paths according to the selected operating system.

This modules contains the following:

- LogPath(Cyb3rhqPath):
    - get_ossec_log_path
    - get_active_responses_log_path
    - get_cluster_log_path
    - get_api_log_path
    - get_integrations_log_path
"""

import sys
import os

from cyb3rhq_qa_framework.global_variables.path.cyb3rhq_path import Cyb3rhqPath
from cyb3rhq_qa_framework.global_variables.platform import WINDOWS


class LogPath(Cyb3rhqPath):
    """Class to build the cyb3rhq log paths according to the selected OS.

    Args:
        os_system (str): Operating system.

    Attributes:
        os_system (str): Operating system.
        logs_path (str): Cyb3rhq logs path.
    """
    def __init__(self, os_system=sys.platform):
        super().__init__(os_system)
        self.logs_path = os.path.join(self.get_cyb3rhq_path()) if os_system == WINDOWS else \
            os.path.join(self.get_cyb3rhq_path, 'logs')

    def get_ossec_log_path(self):
        return os.path.join(self.logs_path, 'ossec.log')

    def get_active_responses_log_path(self):
        return os.path.join(self.logs_path, 'active-response', 'active-responses.log') if self.os_system == WINDOWS \
            else os.path.join(self.logs_path, 'active-responses.log')

    def get_cluster_log_path(self):
        return os.path.join(self.logs_path, 'cluster.log')

    def get_api_log_path(self):
        return os.path.join(self.logs_path, 'api.log')

    def get_integrations_log_path(self):
        return os.path.join(self.logs_path, 'integrations.log')

    def get_alerts_log_path(self):
        return os.path.join(self.logs_path, 'alerts', 'alerts.log')

    def get_alerts_json_path(self):
        return os.path.join(self.logs_path, 'alerts', 'alerts.json')

    def get_archives_log_path(self):
        return os.path.join(self.logs_path, 'archives', 'archives.log')

    def get_archives_json_path(self):
        return os.path.join(self.logs_path, 'archives', 'archives.json')
