#!/usr/bin/python3
#
# Copyright 2022 Signal Messenger, LLC
# SPDX-License-Identifier: AGPL-3.0-only
#

prefix = r'''
// Copyright 2022 Signal Messenger, LLC
// SPDX-License-Identifier: AGPL-3.0-only
// GENERATED BY sandbox.py, DO NOT EDIT MANUALLY
const char* sandbox_code =
'''

suffix = r'''
    "";
'''

with open("sandbox.lua", "r") as infile:
  with open("sandbox.c", "w") as outfile:
    outfile.write(prefix)
    for line in infile:
      outfile.write('    "%s\\n"\n' % line.rstrip())
    outfile.write(suffix)
