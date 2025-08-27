# Video2YOLO — Prepare YOLO Training Dataset from Video

This project provides a simple Python script to extract frames from a video and generate empty label files, preparing your dataset for training YOLO object detection models.

---

## Table of Contents

- [Overview](#overview)  
- [Requirements](#requirements)  
- [Usage](#usage)  
- [Step 1: Prepare Your Video](#step-1-prepare-your-video)  
- [Step 2: Extract Frames and Labels](#step-2-extract-frames-and-labels)  
- [Step 3: Label the Frames](#step-3-label-the-frames)  
- [Step 4: Organize the Dataset](#step-4-organize-the-dataset)  
- [Step 5: Create Data Configuration File](#step-5-create-data-configuration-file)  
- [Step 6: Train Your YOLO Model](#step-6-train-your-yolo-model)  
- [Notes](#notes)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

This script extracts frames from your video **without resizing** (assuming your video is already at the desired resolution) and creates matching empty `.txt` files for YOLO annotations.

You will label those frames with bounding boxes using tools like [LabelImg](https://github.com/tzutalin/labelImg), organize the dataset, then use YOLO training code (e.g., [YOLOv5](https://github.com/ultralytics/yolov5)) to train your model.

---

## Requirements

- Python 3.x  
- OpenCV (`pip install opencv-python`)  
- [LabelImg](https://github.com/tzutalin/labelImg) or any YOLO annotation tool  

---

## Usage

```python
from Video2Yolo import prepare_yolo_dataset_no_resize

prepare_yolo_dataset_no_resize("path/to/your_video.mp4", "output_folder", skip_frames=1)


---

## Step 1: Prepare Your Video

- Place your video file anywhere on your computer.  
- Note the full or relative path to the video file.

**Important:** The video does **not** need to be in the same directory as the script, but you must specify the correct path when calling the function.

---

## Step 2: Extract Frames and Labels

- Run the script to extract frames and create empty label files.

Example output:


Each `.txt` is an empty YOLO annotation file ready to be filled.

---

## Step 3: Label the Frames

- Use [LabelImg](https://github.com/tzutalin/labelImg) or similar tools to open the images and draw bounding boxes.  
- Save the labels in YOLO format — this populates the `.txt` files with annotations.

YOLO annotation format per line:


- Coordinates are **normalized** (0 to 1) relative to image dimensions.  
- Each line corresponds to one object instance.

---

## Step 4: Organize the Dataset

YOLO training expects a folder structure like:


- Split your extracted frames and labels into `train` and `val` folders (e.g., 80% train, 20% val).  
- Keep image and label filenames matched.

Example:


---

## Step 5: Create Data Configuration File

Create a YAML file (e.g., `data.yaml`) to describe the dataset for YOLO training.

Example:

```yaml
train: /full/path/to/dataset/images/train
val: /full/path/to/dataset/images/val

nc: 3  # number of classes

names: ['person', 'car', 'dog']  # class names
python train.py --img 416 --batch 16 --epochs 50 --data /path/to/data.yaml --weights yolov5s.pt
