#!/usr/bin/env python

import subprocess
import os

os.environ['SETTINGS_MODE'] = prod

subprocess.call(["./manage.py", "syncdb"])
subprocess.call(["appcfg.py", "update", "."])

#let add and tag the code
APP_YAML = "app.yaml"

f = open(APP_YAML, 'r')
lines = f.readlines()
f.close()
match = re.match("version: (\d+)", lines[1])
version_number = m.group(1)
version_tag = "v{0}".format(version_number)
subprocess.call(["git", "add", APP_YAML])
subprocess.call(["git", "commit", "Update version for Release"])

subprocess.call(["git", "tag", version_tag])