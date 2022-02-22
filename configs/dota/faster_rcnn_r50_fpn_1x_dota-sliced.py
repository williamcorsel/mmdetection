# The new config inherits a base config to highlight the necessary modification
_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    './dota-sliced_detection.py',
    '../_base_/schedules/schedule_1x.py', 
    '../_base_/default_runtime.py'
]

# Change bbox head to classify 16 classes
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=16
        )
    )
)

# Increase batchsize for RTX 3090
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)

# LR for 1 GPU = (0.02 / 8) * (batchsize / 2)
# Default is 8 GPUs with batchsize 2
optimizer = dict(
    lr=0.005,
)
