# environment_sensors

A project to read temperature, humidity and pressure from a Raspberry Pi Sense
Hat and display the corresponding graphs on a simple website.

## Installation

Make sure that you have the following libraries installed on your system.

python-cairo
pygobject

On Arch Linux you can do this with:

``` shell
sudo pacman -S python-cairo python-gobject
```

## Running

Afterwards you can run the application with:

``` shell
make
```

## Development and Testing

If you want to create a development environment simply run:

``` shell
make test
```

This will create a virtual environment which includes some useful dependencies
for development including the SenseHat emulator. In addition it will run all
tests. If all tests finish correctly you know that the environment is setup
correctly.


