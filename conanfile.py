import os
import platform
from conans import ConanFile, tools


class GypinstallerConan(ConanFile):
    name = "gyp_installer"
    version = "20190604"
    _commit = "aca1e2c3d346d704adfa60944e6b4dd06f4728be"
    url = "https://github.com/bincrafters/conan-gyp_installer"
    homepage = "https://github.com/chromium/gyp"
    description = "GYP is a Meta-Build system: a build system that generates other build systems"
    topics = ("conan", "gyp", "installer", "meta-build-system", "build-system")
    license = "BSD-3-Clause"
    exports = "LICENSE"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "e9caff7ed8be587d8b69fe6ff31168a7da55944d3136f6a4b670d7bcddcbacdc"
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self._commit), sha256=sha256)
        archive_name = "gyp-{}".format(self._commit)
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
