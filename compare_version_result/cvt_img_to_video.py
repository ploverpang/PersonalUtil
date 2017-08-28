#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os
import glob
import numpy as np

def main(dir_path, save_name):
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    patten = os.path.join(dir_path, "*.png")
    images = glob.glob(patten)
    images.sort()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(save_name, fourcc, 10, (1280, 720))
    # out = cv2.VideoWriter(save_name, fourcc, 10, (640, 480))

    for img_name in images:
        print(img_name)
        img = cv2.imread(img_name)
        out.write(img)

        cv2.imshow('frame', img)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break

    out.release()
    cv2.destoryAllWindow()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
       print('Please input diretory name!')
       sys.exit(0)

    abs_path = os.path.abspath(sys.argv[1])
    if(not os.path.exists(abs_path) or (not os.path.isdir(abs_path))):
       print('Input diretory wrong!')
       sys.exit(0)

    if(len(sys.argv)>2):
        save_file = sys.argv[2]
        save_file = os.path.abspath(save_file)
        print(save_file)
    else:
        save_file = os.path.join(os.path.curdir, "record.avi")

    main(abs_path, save_file)
