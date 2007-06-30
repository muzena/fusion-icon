#!/usr/bin/python
# Author(s): crdlb
from distutils.core import setup

# Default installation prefix
INSTALL_PREFIX = '/usr'

# Setup function from distutils
setup(
	name = 'compiz-fusion-icon',
	version = '0.1',
	author = 'crdlb (Christopher Williams)',
	author_email = 'christopherw@verizon.net',
	url = 'http://www.opencompositing.org/',
	license = 'GPL',
	description = 'Compiz Fusion Icon is a simple tray icon for starting Compiz Fusion, providing easy access to CCSM and using CompizConfig to switch decorators',
	# Files that needs to be installed
	data_files = [
		(INSTALL_PREFIX + '/bin',
			['src/fusion-icon']),
		(INSTALL_PREFIX + '/share/pixmaps',
			['fusion-icon.svg']),
		     ]
)
