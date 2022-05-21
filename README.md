
# ML CV based Smart Signal Lights

Traffic congestion is becoming one of the critical issues with the increasing population and automobiles in cities. Traffic jams not
only cause extra delay and stress for the drivers but also increase fuel consumption and air pollution.
According to the TomTom Traffic Index, 3 of the top 10 countries facing the most traffic congestion are in India viz. Mumbai, Bengaluru, and New Delhi. People are compelled to spend hours stuck in traffic jams, wasting away their precious time commuting. 

Current traffic light controllers use a fixed timer and do not adapt according to the real-time traffic on the road.In an attempt to reduce traffic congestion, I am developing an improved traffic management system in the form of a Computer
Vision-based traffic light controller that can autonomously adapt to the traffic situation at the traffic signal. The proposed system sets the green signal time adaptively according to the traffic density at the signal and ensures that the direction with more traffic is allotted a green signal for a longer duration of time as compared to the direction with lesser traffic.


## Basic work flow 
- Most of the busy junctions already have a camera system to catch defaulters. Using the same cameras we can run an image detection code in the control room that detects the cars waiting at each junction and then notes it down in a file.

- The file created by the image detection code will be read in a sketch code in Arduino IDE

- A c++ function would then write the time at which the signal has to change

- This Data will be uploaded to thinkspeak channel

- This data will then be accessed by a node MCU in the traffic light
## Stage 1: Implementing for a T junction

- In stage 1 of this project I have focussed only on one aspect of this smart signal management system, and the algorithm has been implemented on a T junction . Following is the explanation of the algorithm

- In a T junction, usually there is heavier traffic on one road than the other, because of this the conventional systems have different timers for different crossings.

- For the stage 1 implementation I have kept the upper limit of the timer same, and my system kicks in only when it detects that all the traffic from one crossing has cleared and there the lights are still green. This is a problem in conventional systems because after all the traffic has cleared from one road, the other road users have to wait for no reason till the light turns green. This is a very common problem as traffic is mostly unpredictable. To help with this problem my program detects the number of cars waiting at a junction at any second, If it detects that there are zero cars waiting at the junction, and the light is still green, it changes the light to red so that the other road users can use the junction without wasting any time.
## Version 1

This version includes the machine learning code that is used to detect the number of vehicles waiting at the junction at any given time
## Dependencies

This project requires numpy, openCV and a pre-trained DNN model. Use the following commands to donwload numpy and openCV

```bash
  pip3 install opencv-python
  pip install numpy
```

It also requires an DNN (Deep Neural Network) model that can be downloaded from 
```bash
  https://drive.google.com/drive/folders/1IXAVyhUQuOWFB0FfIWhfyHGQBxtHxA1x?usp=sharing
```

Place this model in the project directory
    
## Running Locally

- clone the repository using 
```bash
  git clone https://github.com/aditya-gitte/ML-CV-based-Smart-Signal-Lights.git
```

- Place the downloaded DNN model in the same directory

- Place all the images from which you want to detect vehicles in the `images` folder( this folder will already be present in the cloned repository with sample images)

- Run the `vehicle_counting.py` file 

- Each image will be shown on screen for 10 seconds with red boxes showing all the detected vehicles after running the `vehicle_counting.py` file. The final result will be stored in the `vehicle_count.txt` file( this file will already be present in the cloned repository ) The contents of this file will be updated as and when the program is run

- For video detection store the video from which you want to detect vehicles with name as `cars.mp4` in the project repository and run `videoDetection.py`
## Demo

video link for the demonstration of image detection
```bash
  https://drive.google.com/file/d/1-9FuNtxolJkYcqJRkga-2Yey_QUoK3fE/view?usp=sharing
```
video link for the demonstration of video detection
```bash
  https://drive.google.com/file/d/1-FNdDbASN_aapSRKooB0LKTmjjwQatpA/view?usp=sharing
```


