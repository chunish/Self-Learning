## Tensorflow 数据加载方法
---
#### 1. 加载txt，csv
一般不直接加载txt，而是选择csv， 若是txt则先将其转换成csv再读取，可使用多进程

```python
file_queue = tf.train.string_input_producer([img_path], shuffle=False)
txt_reader = tf.TextLineReader()
key, value = txt_reader.read(file_queue)
paths = tf.decode_csv(value, record_defaults=[['null']])
path_batch = tf.train.batch(paths, batch_size=10)  # path_batch = tf.train.shuffle_batch(paths, batch_size=10)
# both train.batch and train.shuffle_batch can be used as multi-threads

with tf.Session() as sess:
    co = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=co)
    for i in range(5):
        p_evl = sess.run(path_batch)
        print i, p_evl
    co.request_stop()
    co.join(threads)
```

---
#### 2. 加载图片
##### a. 加载单张图
```python
path = './*.png'
img_raw = tf.gfile.FastGFile(path, 'r').read()
with tf.Session() as sess:
    img_data = tf.image.decode_jpeg()
    img_data = tf.image.convert_image_dtype(img_data, tf.int8)
    plt.imshow(img_data.eval())
```

##### b. 加载batch
方法一，imgs without labels,  `tf.WholeFileReader`:
```python
# multi-imgs without labels: WholeFileReader
path = ['0.jpg', '1.jpg', '...']
file_queue = tf.train.string_input_producer(path, shuffle=False, num_epochs=1)
img_reader = tf.WholeFileReader()

with tf.Session() as sess:
    key, imgs = img_reader.read(file_queue)
    img = tf.image.decode_jpeg(imgs)
    threads = tf.train.batch(img, batch_size=100)
    tf.train.start_queue_runners(sess=sess)
    img_eval = sess.run()
    # imshow(img_eval[i] for i in range(batch)    
```


方法二， imgs with labels, `tf.train.slice_input_producer`:
```python
# imgs with labels
path = ['0.jpg', '1.jpg', '...']
label = [0, 1, 2, ]

with tf.Session() as sess:
    file_queue = tf.train.slice_input_producer([path, label], shuffle=True, num_epochs=5)
    img_content = tf.read_file(file_queue[0])
    img_data = tf.image.decode_jpeg(img_content, channels=3)
    label_data = file_queue[1]
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(batch_size):
        img, label_evl = sess.run([img_data, label_data])
        # imshow('label_eval[i]', img[i])
    coord.request_stop()
    coord.join()
```


方法三, `tf.'TFRecordReader`:

