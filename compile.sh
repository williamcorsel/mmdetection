#!/usr/bin/env bash

PYTHON=${PYTHON:-"python"}

echo "Building cpu_nms..."
cd mmdet/core/bbox/iou_calculators
$PYTHON setup_linux.py build_ext --inplace