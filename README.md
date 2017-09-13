# CNN-Tracker-v1
### This project is not actively maintained and has not been brought to a usable state so far
Convolutional Neural Network Tracker v1 - Using YOLO and Correlation Tracker to track objects

## Contributors & Implemented Code from others
#### / Dependencies
This project heavily relies on the work that has already been done by others. Other Open-Source Projects that are essential to this project are:

1. [OpenCV](https://github.com/opencv/opencv "OpenCV by opencv")
2. [Dlib](https://github.com/davisking/dlib "Dlib by davisking")
3. [YOLO](https://github.com/pjreddie/darknet "YOLO by pjreddie")
4. [object-tracker](https://github.com/bikz05/object-tracker "object-tracker by bikz05")

Repo's do not stand in a particular order of importance.
Thank you to everyone who (generally) contributes to this project, or has open-sourced their projects to enable us to build this software!


## Known Problems / Why?
I'm planning on building a 2nd version of this CNN that combines the power of LSTM with YOLO, instead of simply using a correlational tracker. Correlational trackers struggle with occlusion and lags of the input. Since my own usage of this tracker will most likely include **both** of these scenarios at some point, I'll work on using LSTM with YOLO at some point. And I know that [ROLO](https://github.com/Guanghan/ROLO "Recurrent YOLO") seems to have done a pretty amazing job at that. But since ROLO has not been updated since 1 Nov 2016 (about 10 months ago at the point of writing this), I can't get any of the tests or training that ROLO offers to run. That's why I decided to build the CNN-Tracker-v1 (& later v2 as well).


## Usage
- As soon as this project is somewhat usable, I'll write this part out :)
- But generally, simply try to get all the linked dependecies running and you should be able to run my code as well

## What I learned through this
- Python Wrappers for YOLO are often not well maintained (as well as ROLO) and I will simply use the ´shell_exec´ command to communicate with darknet
