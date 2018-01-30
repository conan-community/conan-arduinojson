from conans import ConanFile, CMake, tools
import os


class ArduinojsonConan(ConanFile):
    name = "arduinojson"
    version = "5.13.0"
    license = "The MIT License (MIT)"
    homepage = "https://arduinojson.org"
    url = "https://github.com/bblanchon/ArduinoJson"
    description = "C++ JSON library for IoT. Simple and efficient."
    no_copy_source = True

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.url, self.version))
        tools.get(source_url)
        os.rename("ArduinoJson-%s" % self.version, "sources")

    def package(self):
        self.copy("*.h", dst="include", src="sources")
        self.copy("*.hpp", dst="include", src="sources")