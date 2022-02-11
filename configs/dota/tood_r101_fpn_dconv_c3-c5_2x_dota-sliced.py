_base_ = './tood_r101_fpn_2x_dota-sliced.py'

model = dict(
    backbone=dict(
        dcn=dict(type='DCNv2', deformable_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)),
    bbox_head=dict(num_dcn=2))

# optimizer
optimizer = dict(type='SGD', lr=0.001875, momentum=0.9, weight_decay=0.0001)

data = dict(
    samples_per_gpu=6,
    workers_per_gpu=4,
)