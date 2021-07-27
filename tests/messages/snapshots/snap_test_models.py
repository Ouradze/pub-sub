# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_dump_message detection_vector_message'] = {
    'bounding_box': {
        'height': 6463,
        'width': 447,
        'x': 6724,
        'y': 8731
    },
    'class_prediction_vectors': [
        {
            'label': 'society',
            'prediction': 40
        },
        {
            'label': 'at',
            'prediction': 86
        }
    ],
    'frame_id': '894ade78-bdc2-4af9-b7a0-149b25d0b920',
    'timestamp': '1987-09-17T23:16:50'
}

snapshots['test_dump_message motion_vector_message'] = {
    'bounding_box': {
        'height': 4687,
        'width': 4513,
        'x': 8350,
        'y': 4501
    },
    'frame_id': 'b19182cf-2693-49eb-8f8c-801a0f7d8182',
    'timestamp': '2018-11-05T14:39:26',
    'velocity_vector': {
        'direction': {
            'x': 8458,
            'y': 3542
        },
        'speed': 4251
    }
}
