from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps

import json
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import json
import time
import glob

from io import StringIO
from PIL import Image

import matplotlib.pyplot as plt

# from utils import visualization_utils as vis_util
import label_map_util

from multiprocessing.dummy import Pool as ThreadPool

MAX_NUMBER_OF_BOXES = 10
MINIMUM_CONFIDENCE = 0.9

PATH_TO_LABELS = 'object/label_map.pbtxt'
PATH_TO_TEST_IMAGES_DIR = 'test_images'

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=sys.maxsize, use_display_name=True)
CATEGORY_INDEX = label_map_util.create_category_index(categories)

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'object/output_inference_graph'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

def detect_objects(image_path):
    image = Image.open(image_path)
    image_np = load_image_into_numpy_array(image)
    image_np_expanded = np.expand_dims(image_np, axis=0)

    (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, detection_classes, num_detections], feed_dict={image_tensor: image_np_expanded})

    # vis_util.visualize_boxes_and_labels_on_image_array(
    #     image_np,
    #     np.squeeze(boxes),
    #     np.squeeze(classes).astype(np.int32),
    #     np.squeeze(scores),
    #     CATEGORY_INDEX,
    #     min_score_thresh=MINIMUM_CONFIDENCE,
    #     use_normalized_coordinates=True,
    #     line_thickness=8)
    fig = plt.figure()
    fig.set_size_inches(16, 9)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.imshow(image_np, aspect = 'auto')
    plt.savefig('output/{}'.format(image_path), dpi = 62)
    plt.close(fig)

    return {
      'class': [CATEGORY_INDEX.get(i) for i in classes[0]][0]['name'],
      'box': boxes[0][0],
      'score': scores[0][0],
    }

@csrf_exempt
def index(request):
  if request.method == 'POST':
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image-{}.jpg'.format(i)) for i in range(1, 4) ]
    TEST_IMAGE_PATHS = glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.jpg'))

    # Load model into memory
    print('Loading model...')
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    print('detecting...')
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            print(detection_classes)

            for image_path in TEST_IMAGE_PATHS:
                data = detect_objects(image_path)

                api = API(
                    api_root_url='http://localhost:8000',
                    json_encode_body=True,
                    append_slash=True,
                )

                Metadata = apps.get_model('pipeline', 'Metadata')

                data = Metadata.objects.filter(body['image_name']).get()

                print(data)

            # api.add_resource(resource_name='object')

            # api.object.update(
            #     body = {
            #         'image_path': event.src_path,
            #     }
            # )

    return HttpResponse("Hello, world.")

# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
  if request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    print(body)

    Metadata = apps.get_model('pipeline', 'Metadata')

    data = Metadata.objects.filter(image_name=body['image_name']).get()
    
    return HttpResponse("Hello, world.")
