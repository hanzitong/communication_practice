
// #include <stdio.h>
// #include <unistd.h>
#include <iostream>
#include <gpiod.h>
#include <chrono>
#include <thread>


int main (void){
    struct gpiod_chip *chip;
    struct gpiod_line *line;
    int ret;
    auto interval = std::chrono::milliseconds(100);

    chip = gpiod_chip_open("/dev/gpiochip0");
    if (!chip) {
        std::cout << "error: open chip" << std::endl;
        return -1;
    }

    // follow raspberry pi pin number, not bcm pin number
    line = gpiod_chip_get_line(chip, 4);    // GPIO4
    if (!line) {
        std::cout << "error: get line" << std::endl;
        return -1;
    }

    ret = gpiod_line_request_output(line, "example", 0);
    if (ret < 0) {
        std::cout << "error: request output" << std::endl;
        gpiod_chip_close(chip);
        return -1;
    }

    for (int i = 0; i < 20; i++){
        std::cout << "blinking led" << std::endl;
        gpiod_line_set_value(line, 1);
        std::this_thread::sleep_for(interval);
        gpiod_line_set_value(line, 0);
        std::this_thread::sleep_for(interval);
    }

    gpiod_line_release(line);
    gpiod_chip_close(chip);


    return 0;
}


