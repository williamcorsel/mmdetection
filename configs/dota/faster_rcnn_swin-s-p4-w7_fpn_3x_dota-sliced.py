# The new config inherits a base config to highlight the necessary modification
_base_ = [
    './faster_rcnn_swin-s-p4-w7_fpn_1x_dota-sliced.py',
]

lr_config = dict(step=[27, 33])
runner = dict(max_epochs=36)
