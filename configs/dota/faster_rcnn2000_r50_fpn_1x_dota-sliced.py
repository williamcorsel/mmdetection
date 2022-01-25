# The new config inherits a base config to highlight the necessary modification
_base_ = [
    './faster_rcnn_r50_fpn_1x_dota-sliced.py'
]

model = dict(
    train_cfg = dict(
        rpn_proposal = dict(
            max_per_img=2000
        )
    ),
    test_cfg = dict(
        rpn = dict(
            nms_pre=2000,
            max_per_img=2000 
        ),
        rcnn = dict(
            max_per_img=2000
        )
    )
)
