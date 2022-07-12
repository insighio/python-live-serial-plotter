# python-live-serial-plotter
A small python script to monitor live data read from UART and show them in a plot. 

Each line is searched for an integer/float using the regex: __^.*raw:\s+(-?\d+(\.\d+)?).*$__ 

example line: ```[DEBUG] raw: 1664227.0```

# dependencies

```sh
sudo apt-get install python3-matplotlib python3-serial
```
or
```sh
pip3 install matplotlib serial
```

# Usage

```bash
#linux
python3 plotter.py /dev/ttyUSB0

#windows
python3 plotter.py COM3
```

[live view example](https://user-images.githubusercontent.com/550020/178537239-07c841b8-c08c-4dea-bcd4-cacc9a12063b.webm)
