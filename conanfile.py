from conans import ConanFile, tools
import os


class ArduinojsonConan(ConanFile):
    name = "arduinojson"
    version = "5.13.0"
    license = "The MIT License (MIT)"
    description = "C++ JSON library for IoT. Simple and efficient."
    homepage = "https://github.com/bblanchon/ArduinoJson"
    url = "https://github.com/conan-community/conan-arduinojson"
    no_copy_source = True
    exports_sources = ["LICENSE"]

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.homepage, self.version))
        tools.get(source_url)
        os.rename("ArduinoJson-%s" % self.version, "sources")

    def package(self):
        self.copy("*LICENSE*", dst="licenses", src="sources")
        self.copy("*.h", dst="include", src="sources")
        self.copy("*.hpp", dst="include", src="sources")
