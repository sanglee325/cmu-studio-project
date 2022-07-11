import numpy as np
import argparse
import imutils
import sys
import cv2
import matplotlib.pyplot as plt
import os

import datetime
import time
import json

names = "action_recognition_kinetics.txt"
model = "resnet-34_kinetics.onnx"
video = "example_activities.mp4"

SAMPLE_DURATION = 16 
SAMPLE_SIZE = 112

with open(names) as l:
    CLASSES = l.read().strip().split("\n")

# load the human activity recognition model
print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet(model)

# grab a pointer to the input video stream
print("[INFO] accessing video stream...")

vs = cv2.VideoCapture(video)

# initialize the list / dictionaries to captured classified frames
classifiedFrames = []
dictKey = {}
n = 0

# Run the model
# loop until we explicitly break from it
FLAG_EXIT = False
while True:
    # initialize the batch of frames that will be passed through the model
    frames = []

    n += 1

    # loop over the number of required sample frames
    for i in range(0, SAMPLE_DURATION):
        # read a frame from the video stream
        (grabbed, frame) = vs.read()

        #Identiy the frame number
        pos_frame = vs.get(cv2.CAP_PROP_POS_FRAMES)

        # if the frame was not grabbed then we've reached the end of
        # the video stream so exit the script
        if not grabbed:
            print("[INFO] no frame read from stream - exiting")
            FLAG_EXIT = True
            break
        # otherwise, the frame was read so resize it and add it to
        # our frames list
        frame = imutils.resize(frame, width=400)
        frames.append(frame)

    if FLAG_EXIT is True:
        break
    # now that our frames array is filled we can construct our blob
    blob = cv2.dnn.blobFromImages(frames, 1.0, (SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750), 
                                swapRB=True, crop=True)
    blob = np.transpose(blob, (1, 0, 2, 3))
    blob = np.expand_dims(blob, axis=0)

    # pass the blob through the network to obtain our human activity
    # recognition predictions
    net.setInput(blob)
    outputs = net.forward()
    label = CLASSES[np.argmax(outputs)]


    #capture the frames and labels for future database search engine 
    classifiedFrames.append([pos_frame, label])
    live_datetime = datetime.datetime.now().isoformat()

    dictKey = json.dumps({"index": {"_index" : "test-live", "_id" : n}})
    value = json.dumps({"datetime" : live_datetime, "activity" : label})

    #import pdb; pdb.set_trace()

    data = str(dictKey) + '\n' + str(value) + '\n'

    with open("bulk_action.json", "w") as outfile:
        outfile.write(data)
    
    opensearch_cmd = "curl -XPOST -u 'team3:Vsateam3!' 'https://search-vsa-team3-ei4mkk647obgdhz6qcohcaitxu.us-east-1.es.amazonaws.com/_bulk' --data-binary @bulk_action.json -H 'Content-Type: application/json'"
    os.system(opensearch_cmd)
    print()