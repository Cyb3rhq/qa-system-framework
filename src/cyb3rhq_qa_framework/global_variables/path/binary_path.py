"""
Module to build the Cyb3rhq binary paths according to the selected operating system.

This modules contains the following:

- BinaryPath(Cyb3rhqPath):
    - get_binary_path
    - get_agent_control_path
    - get_agent_groups_path
    - get_agent_upgrade_path
    - get_clear_stats_path
    - get_cluster_control_path
    - get_manage_agents_path
    - get_cyb3rhq_control_path
    - get_cyb3rhq_agentlessd_path
    - get_cyb3rhq_analysisd_path
    - get_cyb3rhq_apid_path
    - get_cyb3rhq_authd_path
    - get_cyb3rhq_clusterd_path
    - get_cyb3rhq_csyslogd_path
    - get_cyb3rhq_db_path
    - get_cyb3rhq_dbd_path
    - get_cyb3rhq_execd_path
    - get_cyb3rhq_integratord_path
    - get_cyb3rhq_logcollector_path
    - get_cyb3rhq_logtest_path
    - get_cyb3rhq_maild_path
    - get_cyb3rhq_modulesd_path
    - get_cyb3rhq_monitord_path
    - get_cyb3rhq_regex_path
    - get_cyb3rhq_remoted_path
    - get_cyb3rhq_reportd_path
    - get_cyb3rhq_syscheckd_path
    - get_agent_auth_path
    - get_cyb3rhq_agentd_path
"""

import sys
import os

from cyb3rhq_qa_framework.global_variables.path.cyb3rhq_path import Cyb3rhqPath
from cyb3rhq_qa_framework.global_variables.platform import WINDOWS


class BinaryPath(Cyb3rhqPath):
    """Class to build the cyb3rhq binary paths according to the selected OS.

    Args:
        os_system (str): Operating system.

    Attributes:
        os_system (str): Operating system.
        binary_path (str): Cyb3rhq binary paths.
    """
    def __init__(self, os_system=sys.platform):
        super().__init__(os_system=os_system)
        self.binary_path = os.path.join(self.get_cyb3rhq_path()) if os_system == WINDOWS else \
            os.path.join(self.get_cyb3rhq_path, 'bin')

    def get_binary_path(self):
        return self.binary_path

    def get_agent_control_path(self):
        return os.path.join(self.binary_path, 'agent_control')

    def get_agent_groups_path(self):
        return os.path.join(self.binary_path, 'agent_groups')

    def get_agent_upgrade_path(self):
        return os.path.join(self.binary_path, 'agent_upgrade')

    def get_clear_stats_path(self):
        return os.path.join(self.binary_path, 'clear_stats')

    def get_cluster_control_path(self):
        return os.path.join(self.binary_path, 'cluster_control')

    def get_manage_agents_path(self):
        return os.path.join(self.binary_path, 'manage_agents')

    def get_cyb3rhq_control_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq_control')

    def get_cyb3rhq_agentlessd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-agentlessd')

    def get_cyb3rhq_analysisd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-analysisd')

    def get_cyb3rhq_apid_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-apid')

    def get_cyb3rhq_authd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-authd')

    def get_cyb3rhq_clusterd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-clusterd')

    def get_cyb3rhq_csyslogd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-csyslogd')

    def get_cyb3rhq_db_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-db')

    def get_cyb3rhq_dbd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-dbd')

    def get_cyb3rhq_execd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-execd')

    def get_cyb3rhq_integratord_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-integratord')

    def get_cyb3rhq_logcollector_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-logcollector')

    def get_cyb3rhq_logtest_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-logtest')

    def get_cyb3rhq_maild_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-maild')

    def get_cyb3rhq_modulesd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-modulesd')

    def get_cyb3rhq_monitord_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-monitord')

    def get_cyb3rhq_regex_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-regex')

    def get_cyb3rhq_remoted_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-remoted')

    def get_cyb3rhq_reportd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-reportd')

    def get_cyb3rhq_syscheckd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-syscheckd')

    def get_agent_auth_path(self):
        return os.path.join(self.binary_path, 'agent-auth')

    def get_cyb3rhq_agentd_path(self):
        return os.path.join(self.binary_path, 'cyb3rhq-agentd')
