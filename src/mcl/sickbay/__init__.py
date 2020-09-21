# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

This is the ``mcl.sickbay`` module.
'''

import pkg_resources


def _read_version():
    '''In Python 3.8, we should use ``importlib.metadata`` instead. But until then,
    we keep version information in a separate ``version.txt`` file. Note that this file
    cannot contain any extra comments and we assume it's text witn bytes encoded in
    utf-8.
    '''
    return pkg_resources.resource_string(__name__, 'VERSION.txt').decode('utf-8').strip()


__version__ = VERSION = _read_version()
