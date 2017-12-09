#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GypinstallerConan(ConanFile):
    name = "gyp_installer"
    version = "20171101"
    url = "https://github.com/bincrafters/conan-gyp_installer"
    description = "GYP is a Meta-Build system: a build system that generates other build systems"
    license = "https://chromium.googlesource.com/external/gyp/+/master/LICENSE"
    no_copy_source = True

    # def system_requirements(self):
        # if tools.os_info.is_linux:
            # if tools.os_info.with_apt:
                # installer = tools.SystemPackageTool()
                # installer.install('ca-certificates')

    def build(self):
        #self.run('git clone --depth 1 https://github.com/SSE4/gyp')
        tools.get("https://github.com/SSE4/gyp/archive/master.zip")
        os.rename("gyp-master", "sources")
    
    def package(self):
        self.copy(pattern='*', src='sources', dst='bin')

    def package_info(self):
        # ensure gyp is executable
        if os.name == 'posix':
            name = os.path.join('bin', 'gyp')
            os.chmod(name, os.stat(name).st_mode | 0o111)
        bin_dir = os.path.join(self.package_folder, 'bin')
        self.env_info.path.append(bin_dir)
        self.env_info.PYTHONPATH.append(os.path.join(bin_dir, 'pylib'))
