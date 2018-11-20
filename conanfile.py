#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
from conans import ConanFile, tools


class GypinstallerConan(ConanFile):
    name = "gyp_installer"
    version = "20171101"
    url = "https://github.com/bincrafters/conan-gyp_installer"
    homepage = "https://chromium.googlesource.com/external/gyp"
    description = "GYP is a Meta-Build system: a build system that generates other build systems"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD-3-Clause"
    exports = "LICENSE"
    exports_sources = "gyp.patch"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("https://github.com/bincrafters/gyp/archive/{}.tar.gz".format(self.version))
        archive_name = "gyp-{}".format(self.version)
        os.rename(archive_name, self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file="gyp.patch")

    def package(self):
        self.copy(pattern="LICENSE", src=self._source_subfolder, dst="licenses")
        self.copy(pattern='*', src=self._source_subfolder, dst='bin')

    def package_info(self):
        if platform.system() in ["Linux", "Darwin"]:
            name = os.path.join('bin', 'gyp')
            os.chmod(name, os.stat(name).st_mode | 0o111)
        bin_dir = os.path.join(self.package_folder, 'bin')
        self.env_info.path.append(bin_dir)
        self.env_info.PYTHONPATH.append(os.path.join(bin_dir, 'pylib'))

    def package_id(self):
        self.info.header_only()
