#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


TEST_PACKAGE_GYP = """{
    'targets': [
      {
        'target_name': 'test_package',
        'type': 'executable',
        'sources': [
          'test_package.cpp',
        ],
      },
    ],
}
"""


class TestPackage(ConanFile):

    def test(self):
        self.run("gyp --help")
        # ensure python can import gyp
        self.run('python -c "from __future__ import print_function;import gyp;print(gyp)"')
        with open('test_package.gyp', 'w') as fd:
            fd.write(TEST_PACKAGE_GYP)
        self.run("gyp  --depth=. test_package.gyp")
