#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os
import glob
import numpy as np

def get_frame_num(file_name):
    base_name = os.path.basename(file_name)
    root, _ = os.path.splitext(base_name)
    return int(root)

def get_min_max_frame_num(names):
    min_frame = get_frame_num(names[0])
    max_frame = get_frame_num(names[-1])
    return min_frame, max_frame

def main(new_result, ole_result, save_name):
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    patten = os.path.join(new_result, "*.png")
    images_new = glob.glob(patten)
    images_new.sort()

    patten = os.path.join(ole_result, "*.png")
    images_old = glob.glob(patten)
    images_old.sort()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(save_name, fourcc, 10, (1280*2, 720))

    index_new, index_old = 0, 0
    while(index_new < len(images_new) and index_old < len(images_old)):
        frame_old = get_frame_num(images_old[index_old])
        frame_new = get_frame_num(images_new[index_new])

        if(frame_old < frame_new):
            index_old = index_old+1
        elif(frame_old > frame_new):
            index_new = index_new+1
        else:
            img_old = cv2.imread(images_old[index_old])
            img_new = cv2.imread(images_new[index_new])
            cv2.putText(img_old, "V1.2.1", (50, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0))
            cv2.putText(img_new, "V2.0-beta", (50, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0))

            merged = np.hstack((img_new, img_old))

            out.write(merged)
            index_old = index_old+1
            index_new = index_new+1

            cv2.imshow('frame', merged)
        print ("old idx:%d new idx: %d" % (index_old, index_new))
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if(len(sys.argv) < 3):
       print('Please input diretory name!')
       sys.exit(0)

    abs_path1 = os.path.abspath(sys.argv[1])
    if(not os.path.exists(abs_path1) or (not os.path.isdir(abs_path1))):
       print('Input diretory 1 wrong!')
       sys.exit(0)

    abs_path2 = os.path.abspath(sys.argv[2])
    if(not os.path.exists(abs_path2) or (not os.path.isdir(abs_path2))):
       print('Input diretory 2 wrong!')
       sys.exit(0)

    if(len(sys.argv)>3):
        save_file = sys.argv[3]
        save_file = os.path.abspath(save_file)
        print(save_file)
    else:
        save_file = os.path.join(os.path.curdir, "result_compare.avi")

    main(abs_path1, abs_path2, save_file)
