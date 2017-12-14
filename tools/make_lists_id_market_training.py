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

def main(args):
    # all the filenames
    images_train = glob(osp.join(args.input_dir, 'bounding_box_train', '*.jpg'))
    images_query = glob(osp.join(args.input_dir, 'query', '*.jpg'))
    images_test = glob(osp.join(args.input_dir, 'bounding_box_test', '*.jpg'))
    print(len(images_train))
    # train
    trainval = _get_list(images_train)
    np.random.shuffle(trainval)
    # num_val = int(len(trainval) * args.val_ratio)
    # train = trainval[num_val:]
    # val = trainval[:num_val]
    # test
    test_probe = _get_list(images_query)
    test_gallery = _get_list(images_test)
    # Save to files
    mkdir_if_missing(args.output_dir)
    # _save(train, osp.join(args.output_dir, 'train.txt'))
    # _save(val, osp.join(args.output_dir, 'val.txt'))
    _save(trainval, osp.join(args.output_dir, 'trainval.txt'))
    _save(test_probe, osp.join(args.output_dir, 'test_probe.txt'))
    _save(test_gallery, osp.join(args.output_dir, 'test_gallery.txt'))


if __name__ == '__main__':
    parser = ArgumentParser(
        description="Create lists of image file and label for making lmdbs")
    parser.add_argument('input_dir',
                        help="Root directory of the market dataset containing "
                             " bounding_box_train/" "bounding_box_test/" "query/")
    parser.add_argument('output_dir',
                        help="Output directory for the lists")
    parser.add_argument(
        '--val-ratio',
        type=float,
        default=0.1,
        help="Ratio between validation and trainval data. Default 0.1.")
    args = parser.parse_args()
    main(args)

        
