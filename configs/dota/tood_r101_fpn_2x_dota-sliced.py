_base_ = [
    './tood_r50_fpn_1x_dota-sliced.py',
]

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))

lr_config = dict(step=[16, 22])
runner = dict(type='EpochBasedRunner', max_epochs=24)

# optimizer
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)