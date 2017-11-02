#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class TestPackage(ConanFile):

    def test(self):
        self.run("gyp --help")
        # ensure python can import gyp
        self.run('python -c "from __future__ import print_function;import gyp;print(gyp)"')
