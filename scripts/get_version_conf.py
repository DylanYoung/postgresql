#!/usr/bin/env python

from subprocess import Popen
from sys import argv, exit
import os


version = len(argv) > 1 and argv[1]
if not version:
    print "A version is required"
    exit(1)


BASE_URL = 'https://raw.githubusercontent.com/postgres/postgres/'
SAMPLE_CONF_PATH = 'src/backend/utils/misc/postgresql.conf.sample'
TEMPLATE_PATH = 'templates/'
if int(version.split('.')[0]) > 9: 
    REPO_FORMAT = 'REL_{version}_STABLE'
else:
    REPO_FORMAT = 'REL{version}_STABLE'
DELIMITER = '_'
FILE_FORMAT = 'postgresql.conf-{version}.orig'


url = os.path.join(BASE_URL, 
                   REPO_FORMAT.format(version=version.replace('.', DELIMITER)),
                   SAMPLE_CONF_PATH)
outfile = os.path.join(TEMPLATE_PATH, FILE_FORMAT.format(version=version))

Popen(['wget', url, '-O', outfile]) 
