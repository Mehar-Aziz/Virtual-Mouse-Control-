# Virtual Mouse Control Using Hand Gestures

This project implements virtual mouse control using hand gestures. The code is written in Python and integrated with MATLAB.

## Overview

The Python code accesses hand points and logic to move the cursor virtually. MATLAB integration code is provided for using the virtual mouse control within MATLAB environment.

## Requirements

Before running the code, ensure you have the following:

1. **Python (3.11)**: Supported by MATLAB versions R2022a-R2024.
2. **Python Libraries**:
   - OpenCV (opencv-python)
   - MediaPipe
   - PyAutoGUI
3. **MATLAB**: Versions R2022a-R2024a.
4. **MATLAB Support Package for USB Webcams**.

## Functionalities

The virtual mouse control supports the following functionalities:
- Left click
- Right click
- Scroll up
- Scroll down

## Setup and Usage

1. Install Python and required libraries.
2. Install MATLAB and the MATLAB Support Package for USB Webcams.
3. Run the Python code for hand gesture recognition.
4. Integrate the provided MATLAB code to use virtual mouse control within MATLAB.

## Usage Example

1. Run the Python script to initialize the virtual mouse control (i.e 'python mouse-control.py').
2. Perform hand gestures to move the cursor and trigger left, right clicks and scroll.

## Files

- `mouse-control.py`: Python script for hand gesture recognition and virtual mouse control.
- `matlabConnection.m`: MATLAB script for integrating virtual mouse control.

## Acknowledgements

The project utilizes the following technologies and libraries:
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [MATLAB](https://www.mathworks.com/products/matlab.html)

## License

This project is licensed under the [MIT License](LICENSE).
