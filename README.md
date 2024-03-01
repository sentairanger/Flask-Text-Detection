# Flask-Text-Detection
A flask application that allows the user to take a picture with the Pi Camera module and then detect text within the image with OpenVINO's text detection model

## Getting Started

To get started, you will need a Camera Module (any model can suffice), an Intel NCS2 which can be found on places such as eBay, and make sure to have 64-bit Pi OS Bullseye installed on the Pi. This has been tested on the Pi 4 and will also work on the 3B+. I will test on the Pi 5 with Bookworm when I get my hands on it. A camera mount is recommended for portability. You will also need to install OpenVINO by following this [guide](https://gist.github.com/sentairanger/caf11a2432ceebd715c6b33c224f4960). Before running the app, be sure to insert the NCS2 into any USB port. Next, run the app on the terminal with `python3 app.py`. Then go to `ip-address-of-pi:5000/` and the app should appear in the browser if running remotely. Then, take a picture with the camera module, then detect text and display the result. Sample of the app shown below.

![app](https://github.com/sentairanger/Flask-Text-Detection/blob/main/text-app.png)
