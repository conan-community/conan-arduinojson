# conan-arduinojson

![conan-arduinojson image](/images/conan-arduinojson.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/arduinojson%3Aconan/images/download.svg?version=5.13.0%3Astable)](https://bintray.com/conan-community/conan/arduinojson%3Aconan/5.13.0%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-arduinojson.svg?branch=stable%2F5.13.0)](https://travis-ci.org/conan-community/conan-arduinojson)

[Conan.io](https://conan.io) package for [ArduinoJson](https://github.com/bblanchon/ArduinoJson) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/arduinojson%3Aconan).

## Basic setup

    $ conan install arduinojson/5.13.0@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    arduinojson/5.13.0@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)