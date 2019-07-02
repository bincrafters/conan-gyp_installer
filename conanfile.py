# -*- coding: utf-8 -*-

import os
import platform
from conans import ConanFile, tools


class GypinstallerConan(ConanFile):
    name = "gyp_installer"
    version = "6.0.3"
    url = "https://github.com/bincrafters/conan-gyp_installer"
    homepage = "https://github.com/refack/GYP"
    description = "GYP is a Meta-Build system: a build system that generates other build systems"
    author = "Bincrafters <bincrafters@gmail.com>"
    topics = ("conan", "gyp", "installer", "meta-build-system", "build-system")
    license = "BSD-3-Clause"
    exports = "LICENSE"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "803d844e04b36caba83442e71ffb3775a04afbd8a75453eed439de5c92d041bb"
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        archive_name = "gyp-{}".format(self.version)
        os.rename(archive_name, self._source_subfolder)

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
