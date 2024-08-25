"""
Module to build the Cyb3rhq path according to the selected operating system.

This modules contains the following:

- Cyb3rhqPath:
    - get_cyb3rhq_path
"""

import sys
import os

from cyb3rhq_qa_framework.global_variables.platform import WINDOWS, MACOS


class Cyb3rhqPath:
    """Class to build the cyb3rhq paths according to the selected OS.

    Args:
        os_system (str): Operating system.

    Attributes:
        os_system (str): Operating system.
    """
    def __init__(self, os_system=sys.platform):
        self.os_system = os_system

    def get_cyb3rhq_path(self):
        """Get the cyb3rhq path.

        Returns:
            str: Cyb3rhq path.
        """
        if self.os_system == WINDOWS:
            return os.path.join('C:', os.sep, 'Program Files (x86)', 'ossec-agent')
        elif self.os_system == MACOS:
            return os.path.join('/', 'Library', 'Ossec')
        else:
            return os.path.join('/var', 'ossec')
