#!/usr/env/bin python3

import os
import subprocess

# See parse_args for supported arguments
configs = [
    dict(tag='test1',
         num_img=50,
         img_width=150,
         fonts_by_image=True,
         corpus_dir='./data/corpus_line',
         corpus_mode='list',
         fonts_list='./data/fonts_list/img_font.txt',
         strict=True),
    dict(tag='test2',
         num_img=50,
         strict=True)
]


def dict_to_args(config: dict):
    args = []
    for k, v in config.items():
        if v is False:
            continue
        args.append('--%s' % k)
        args.append('%s' % v)

    return args


if __name__ == "__main__":
    main_func = './main.py'

    for config in configs:
        args = dict_to_args(config)
        print("Run with args: %s" % args)
        subprocess.run(['python3', main_func] + args)
