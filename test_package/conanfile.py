#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import ConanFile


TEST_PACKAGE_GYP = """{
    "targets": [
      {
        "target_name": "test_package",
        "type": "executable",
        "sources": [
          "test_package.cpp"
        ]
      }
    ]
}
"""

class TestPackage(ConanFile):

    def test(self):
        self.run("gyp --help")
        # ensure python can import gyp
        self.run('python -c "from __future__ import print_function;import gyp;print(gyp)"')
        with open("test_package.gyp", "w") as fd:
            fd.write(TEST_PACKAGE_GYP)
        shutil.copyfile(os.path.join(self.source_folder, "test_package.cpp"), os.path.join(os.getcwd(), "test_package.cpp"))
        self.run("gyp test_package.gyp --depth=. -f make --generator-output=%s" % os.path.join("build", "makefiles"))
        self.run("gyp test_package.gyp --depth=. -f xcode --generator-output=%s" % os.path.join("build", "xcodefiles"))
        self.run("gyp test_package.gyp --depth=. -f msvs -G msvs_version=2015")
