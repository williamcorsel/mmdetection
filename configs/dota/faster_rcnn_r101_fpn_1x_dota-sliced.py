# The new config inherits a base config to highlight the necessary modification
_base_ = [
    './faster_rcnn_r50_fpn_1x_dota-sliced.py',
]

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
