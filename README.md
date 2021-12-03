# Logo Detection Project

This repository contains the final group project of the team PACO for the course 20600 DEEP LEARNING FOR COMPUTER VISION tought by Gaia Rubera and Francesco Grossetti at Bocconi University.

Team members:
- Alessandro Caruso
- Fabian Kraus
- Silvia Juzova
- Louis Lacombe
- Riccardo Tordini
- Steffen Brockmann


## Project Description

The project is to build a neural network that performs logo detection (as in object detection task) based on a large dataset of images (and noise) of 17 popular brand logos. A subset of these logos and images has been chosen and two different models, Faster R-CNN and YOLOv5 has been used to predict on a test dataset.


## Quick Start

### Set-Up
Clone the repository to your local or virtual machine. In order to run the algorithms an environment with the following settings is necessary: Python>=3.6.0 is required with all requirements.txt installed as well as PyTorch>=1.7:

`
$ git clone git@github.com:deeppaco/logo_detection_project.git
`

### YOLOv5
To predict with the YOLOv5 algorithm on our test datasets navigate into the yolov5 folder and run the following code:

`
python detect.py --source final_test/images --weights runs/exp45/weights/best.pt --img 640 --save-txt --conf-thres 0.01  --iou-thres 0.2 --save-conf
`

To predict on the additional test dataset we created run the following command:

`
python detect.py --source additional_test/images --weights runs/exp45/weights/best.pt --img 640 --save-txt --conf-thres 0.01  --iou-thres 0.2 --save-conf
`

The resulting predictions will be saved in the folder yolov5/runs/detect/.

Use the file Post_training_analysis_yolov5.ipynb in the yolov5 folder to analyze the results.

### Faster R-CNN

