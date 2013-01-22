#!/usr/bin/env python

import subprocess
import os
import re 

print "Changing SETTINGS_MODE changed in prod."
os.environ['SETTINGS_MODE'] = "prod"

print "Performing remote syncdb"

subprocess.call(["./manage.py", "syncdb"])


## We get the version from the APP_YAML and increase the version automatically.
APP_YAML = "app.yaml"

f = open(APP_YAML, 'r+')
lines = f.readlines()

match = re.match("version: (\d+)", lines[1])
version_number = int(match.group(1))
version_number += 1
lines[1] = "version: {0}\n".format(version_number)
f.seek(0) # rewind
f.writelines(lines)
f.close()

version_tag = "v{0}".format(version_number)

print "Releasing with appcfg"
subprocess.call(["appcfg.py", "update", "."])

#let add and tag the code

print "Committing the changed app.yaml"
subprocess.call(["git", "add", APP_YAML])
subprocess.call(["git", "commit", "-m", "Update version for Release"])

subprocess.call(["git", "tag", version_tag])
print "Code tagged with: {0}".format(version_tag)