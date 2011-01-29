#!/usr/bin/env python3.2

import os
import genshi

loader = genshi.template.TemplateLoader('templates', variable_lookup='lenient')