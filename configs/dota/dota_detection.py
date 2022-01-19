dataset_type = 'CocoDataset'
data_root = 'data/dota1-5h/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
	dict(type='RandomCrop', crop_size=(1024, 1024)),
    # dict(type='Resize', img_scale=(1000, 600), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
classes = ('airplane', 'bridge', 'storage-tank', 'ship', 'swimming-pool', 'vehicle', 'person', 'wind-mill')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
		type=dataset_type,
        img_prefix=data_root + 'train/images/',
        classes=classes,
        ann_file=data_root + 'train/DOTA1_5_train.json',
		pipeline=train_pipeline),
    val=dict(
		type=dataset_type,
        img_prefix=data_root + 'val/images',
        classes=classes,
        ann_file=data_root + 'val/DOTA1_5_val.json',
		pipeline=test_pipeline),
    test=dict(
		type=dataset_type,
        img_prefix=data_root + 'test/images',
        classes=classes,
        ann_file=data_root + 'test/DOTA1_5_test.json'),
		pipeline=test_pipeline)
evaluation = dict(interval=1, metric='bbox')