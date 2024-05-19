# Sonder

### Version: 1.0.0 | Author: H3CATE

## Description

Sonder is a Python script to test various RTSP stream paths for a given IP address and port. It uses `ffmpeg` to check the validity of the streams and `ffplay` to play valid streams.

The name is inspired by the word "Sonder":

_"n. the realization that each random passerby is living a life as vivid and complex as your own—populated with their own ambitions, friends, routines, worries and inherited craziness—an epic story that continues invisibly around you like an anthill sprawling deep underground, with elaborate passageways to thousands of other lives that you’ll never know existed, in which you might appear only once, as an extra sipping coffee in the background, as a blur of traffic passing on the highway, as a lighted window at dusk."_

-The Disctionary of Obscure Sorrows.

## Requirements

- Python 3.x
- termcolor
- ffmpeg

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/H3CATE/Sonder
    cd Sonder
    ```
    
2. **Install the dependencies**:
    ```bash
    pip install -r termcolor
    ```

## Usage

Run the script with the IP address and optional port as command-line arguments:
```bash
python sonder.py <ip> [port]
```

## Recommendation 

Use it alongside Shodan Image with search filter "rtsp". 

# This script is provided for educational purpose.
