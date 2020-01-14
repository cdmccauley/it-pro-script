# http://kazuar.github.io/scraping-tutorial/

import os
import sys

pkgPath = '{}{}packages{}'.format(os.getcwd(), os.path.sep, os.path.sep)

sys.path.insert(0, pkgPath)

import requests

sessionRequests = requests.session()

