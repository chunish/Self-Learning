# _*_ coding: utf-8 _*_
import os
import time
import numpy as np
import tensorflow as tf

class loader(object):
    def __init__(self, batch_size=1, img_width=0, img_height=0):
        self.batch_size = batch_size
        self.img_w = img_width
        self.img_h = img_height
        self.batch_total = 0

    def load_csv(self, csv_path):
        paths = []
        labels = []
        only_path = True
        with open(csv_path, 'rb') as ff:
            for i,d in enumerate(ff):
                if only_path:
                    path = d[:-1]
                    label = i
                else:
                    path, label = d.split(',')
                    path = path[:-1]
                paths.append(path)
                labels.append(label)
        self.batch_total = len(labels) // self.batch_size + 1
        return paths, labels


    def run(self, csv_path):
        paths_list, labels_list = self.load_csv(csv_path)

        img_queue, label_queue = tf.train.slice_input_producer([paths_list, labels_list], shuffle=True)

        img_content = tf.read_file(img_queue)
        img_data = tf.image.decode_jpeg(img_content, channels=3)
        img_resize = tf.image.resize_images(img_data, [self.img_w, self.img_h])
        img_standard = tf.image.per_image_standardization(img_resize)
        img_batch, label_batch = tf.train.batch([img_standard, label_queue], batch_size=self.batch_size)

        return img_batch, label_batch


if __name__ == '__main__':
    IMG_WIDTH = 1200
    IMG_HEIGHT = 1600
    MAX_EPOCH = 1000
    img_path = '/home/kcadmin/datasets/img_list.csv'
    data = loader(batch_size=90, img_width=IMG_WIDTH, img_height=IMG_HEIGHT)
    ibatch, lbatch = data.run(csv_path=img_path)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        thread = tf.train.start_queue_runners(sess=sess, coord=coord)

        for epoch in range(MAX_EPOCH):
            for batch in range(data.batch_total):
                i, l = sess.run([ibatch, lbatch])
                print '{}/{}, {}/{}: {},{}'.format(batch, data.batch_total, epoch, MAX_EPOCH, len(l), i.shape)

        coord.request_stop()
        coord.join(thread)

