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

import os
import shutil
import argparse

def generate_test_folder(output_folder, split_file_path, input_folder, cls_list):
    # generate class dirs
    for class_name in cls_list:
        output_class_dir = os.path.join(output_folder, class_name)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)    

    with open(split_file_path, "r") as f:
        split_list = f.readlines()
    
    for line in split_list:
        cls_name, video_clip = line.split('/')
        video_name, _ = video_clip.split('.')

        cur_path = os.path.join(input_folder, cls_name, video_name)
        des_path = os.path.join(output_folder, cls_name, video_name)
        
        shutil.move(cur_path, des_path)

def generate_train_folder(output_folder, split_file_path, input_folder, cls_list):
    # generate class dirs
    for class_name in cls_list:
        output_class_dir = os.path.join(output_folder, class_name)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)    

    with open(split_file_path, "r") as f:
        split_list = f.readlines()
    
    for line in split_list:
        datafile, idx = line.split(' ')
        cls_name, video_clip = datafile.split('/')
        video_name, _ = video_clip.split('.')

        cur_path = os.path.join(input_folder, cls_name, video_name)
        des_path = os.path.join(output_folder, cls_name, video_name)
        
        shutil.move(cur_path, des_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Clip video to RGB frames')
    parser.add_argument('--input_folder', type=str, help='input dataset folder')
    parser.add_argument('--output_folder', type=str, help='splited output images path')
    parser.add_argument('--annotation_folder', type=str, help='split .txt file')
    args = parser.parse_args()

    # annotation files
    train_list_path = os.path.join(args.annotation_folder, 'trainlist01.txt')
    test_list_path = os.path.join(args.annotation_folder, 'testlist01.txt')

    # read class list
    cls_list = os.listdir(args.input_folder)

    # generate output file directory
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    target_train_path = os.path.join(args.output_folder, 'train')
    if not os.path.exists(target_train_path):
        os.makedirs(target_train_path)

    target_test_path = os.path.join(args.output_folder, 'test')
    if not os.path.exists(target_test_path):
        os.makedirs(target_test_path)
    
    generate_train_folder(target_train_path, train_list_path, args.input_folder, cls_list)
    generate_test_folder(target_test_path, test_list_path, args.input_folder, cls_list)