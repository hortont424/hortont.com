#!/usr/bin/env python3.2

import os
import json
import config

from datetime import datetime

class InvalidAttributeError(Exception):
    def __init__(self, filename, attrname):
        super(InvalidAttributeError, self).__init__()

        self.filename = filename
        self.attrname = attrname

    def __str__(self):
        return repr("Invalid attribute '{0}' in control file {1}".format(self.attrname, self.filename))

class MissingAttributeError(Exception):
    def __init__(self, filename, attrname):
        super(MissingAttributeError, self).__init__()

        self.filename = filename
        self.attrname = attrname

    def __str__(self):
        return repr("Missing required attribute '{0}' in control file {1}".format(self.attrname, self.filename))

class Page(object):
    def __init__(self, filename):
        super(Page, self).__init__()

        # Figure out whether we were given the control file or the data file
        if filename.endswith(".control"):
            self.controlPath = filename
            self.filePath = filename.replace(".control", "")
        else:
            self.controlPath = filename + ".control"
            self.filePath = filename

        # Make sure the files both actually exist
        for file in (self.controlPath, self.filePath):
            if not os.path.exists(file):
                raise IOError("File not found: {0}".format(file))

        self.parse_metadata(json.load(open(self.controlPath)))

        self.data = open(self.filePath).read()

    def parse_metadata(self, control):
        def copy_attribute(name, attrname=None, required=False, default=None, valid=None, convert=None):
            # If no destination attribute name is specified, use the source name
            if not attrname:
                attrname = name

            if name in control:
                # The control file includes the attribute we're going to copy
                value = control[name]

                # Convert the value with the given function if necessary
                if convert:
                    value = convert(value)

                if valid == None or valid(value):
                    # There was no validator specified, or the value passes validation
                    setattr(self, attrname, value)
                else:
                    # The value failed validation
                    raise InvalidAttributeError(self.controlPath, attrname)
            else:
                # The control file doesn't include the attribute we're going to copy
                if required:
                    # If it's a required attribute, alert the user
                    raise MissingAttributeError(self.controlPath, attrname)
                else:
                    # If it's optional, use the default instead
                    setattr(self, attrname, default)

        copy_attribute("title", required=True, valid=lambda x: x != "")
        copy_attribute("date", default=datetime.now(), convert=lambda x: datetime.strptime(x, config.date_format))
        copy_attribute("author", default=config.default_author)
