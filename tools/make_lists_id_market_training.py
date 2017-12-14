import numpy as np
from argparse import ArgumentParser
from glob import glob
import math
import sys
import os
import os.path as osp

def _get_list(filename_list):
    ret = []
    for filename in filename_list:
        # file = osp.basename(filename)
        if int(osp.basename(filename)[:2]) == -1:
            label = -1
        else:
            label = int(osp.basename(filename)[:4])
        ret.append((filename, label))
    return np.asarray(ret)

def write_list(arr, file_path, coding=None):
    if coding is None:
        arr = ['{}'.format(item) for item in arr]
        with open(file_path, 'w') as f:
            f.write('\n'.join(arr))
    else:
        with codecs.open(file_path, 'w', coding) as f:
            f.write(u'\n'.join(arr))

def _save(file_label_list, file_path):
    content = ['{} {}'.format(x, y) for x, y in file_label_list]
    write_list(content, file_path)

def mkdir_if_missing(d):
    if not osp.isdir(d):
        os.makedirs(d)
