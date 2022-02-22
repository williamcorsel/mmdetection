# The new config inherits a base config to highlight the necessary modification
_base_ = [
    './faster_rcnn_swin-t-p4-w7_fpn_1x_dota-sliced.py',
]

pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth'

model = dict(
    backbone=dict(
        depths=[2, 2, 18, 2],
        init_cfg=dict(type='Pretrained', checkpoint=pretrained)
    )
)
