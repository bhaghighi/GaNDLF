# -*- coding: utf-8 -*-
"""
Add Conv Block for MSDNet
"""
import torch.nn as nn

def add_conv_block(Conv, BatchNorm, in_ch=1, out_ch=1, kernel_size=3, dilate=1, last=False):
    """
    Helper function
    """
    pad = dilate if not last else 0
    conv_1 = Conv(in_ch, out_ch, kernel_size, padding=pad, dilation=dilate)
    bn_1 = BatchNorm(out_ch)

    return [conv_1, bn_1]
