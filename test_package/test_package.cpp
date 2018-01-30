#include <ArduinoJson.h>
#include <iostream>

int main(void)
{
    char json[] = "{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";

    StaticJsonBuffer<500> jsonBuffer;

    JsonObject& root = jsonBuffer.parseObject(json);

    const char* sensor = root["sensor"].as<char*>();
    int time = root["time"].as<int>();
    double latitude = root["data"][0].as<double>();
    double longitude = root["data"][1].as<double>();

    std::cout << "sensor: " << sensor << std::endl;
    std::cout << "time: " << time << std::endl;
    std::cout << "latitude: " << latitude << std::endl;
    std::cout << "longitude: " << longitude << std::endl;

    return 0;
}