# Copyright (c) 2021 NVIDIA CORPORATION. All rights reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import os
import cv2


def clip_video(input_video_path, output_path):
    cap = cv2.VideoCapture(input_video_path)
    frame_cnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("f cnt: {}".format(frame_cnt))
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    img_id = 1
    while cap.isOpened():
        ret, frame = cap.read()
        img_name = os.path.join(output_path, str(img_id).zfill(6)+".png")
        if ret:
            cv2.imwrite(img_name, frame)
        else:
            break
        img_id += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Clip video to RGB frames')
    parser.add_argument('--input_folder', type=str, help='input dataset folder')
    parser.add_argument('--output_folder', type=str, help='output images path')
    args = parser.parse_args()

    # read files
    file_list = os.listdir(args.input_folder)

    # generate output file directory
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    for class_name in file_list:
        class_path = os.path.join(args.input_folder, class_name)
        file_names = os.listdir(class_path)
        print(">> class: ", class_name)

        output_class_dir = os.path.join(args.output_folder, class_name)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)

        for video_clip in file_names:
            video_name = video_clip.split('.')
            video_dir = os.path.join(output_class_dir, video_name[0])
            if not os.path.exists(video_dir):
                os.makedirs(video_dir)
            video_dir = os.path.join(video_dir, "rgb")
            if not os.path.exists(video_dir):
                os.makedirs(video_dir)
            input_video = os.path.join(args.input_folder, class_name, video_clip)
            clip_video(input_video, video_dir)
