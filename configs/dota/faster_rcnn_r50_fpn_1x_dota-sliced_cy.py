# The new config inherits a base config to highlight the necessary modification
_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    './dota-sliced_detection.py',
    '../_base_/schedules/schedule_1x.py', 
    '../_base_/default_runtime.py'
]

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=16)
    ),
    train_cfg=dict(
        rpn=dict(
            assigner=dict(
                type='MaxIoUAssignerCy',
            )
        ),
        rcnn=dict(
            assigner=dict(
                type='MaxIoUAssignerCy',
            )
        )
    )
)

optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)


