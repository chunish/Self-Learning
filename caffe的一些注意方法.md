# caffe的一些注意方法
@[caffe | 深度学习] 

## 基本项目
### MNIST手写字符识别
> 采用`LeNet5`结构

主要配置方法如下：
1. 生成**MNIST**数据对应的`lmdb`文件夹两个，在`examples\mnist\train_lmdb,examples\mnist\test_lmdb`，其中，`lmdb`与`leveldb`数据：提高磁盘IO利用率


2. 修改`lenet_solver.prototxt`,运行方式改为CPU
3. 修改`lenet_train_test.prototxt`路径
4. 开始训练
	```basic
	Build\x64\Release\caffe.exe train --solver=examples/mnist/lenet_solver.prototxt
	```

5. 生成均值文件
	```basic
	Build\x64\Release\compute_image_mean.exe examples\mnist\mnist_train_lmdb mean.binaryproto --backend=lmdb
	```
6. 在`lenet_train_test.prototxt`中，`transform_param`前，添加 `mean_file:"mean.binaryproto"`(共2处)
7. 建立标签文件`synset_words.txt`
8. 自己手写训练，24*24
	```basic
	Build\x64\Release\classification.exe examples\mnist\lenet.prototxt examples\mnist\lenet_iter_10000.caffemodel mean.binaryproto examples\mnist\synset_words.txt examples\mnist\0.bmp
	```


	
	

	

## 数据结构
### Blob：
> - 连续的N(一般为4)维数组 ，**Blob** 是caffe中实际处理和传递数据的数据封装包，并且在CPU和GPU之间有数据同步能力， 
- `blob.hpp`文件位于`../libcaffe/include.hpp`下 

### lmdb与leveldb数据：
> 提高磁盘IO利用率


### Layers：
1. Layer是caffe模型的【本质内容】和【执行计算】的基本单元。 
2. Layer可以进行很多运算，如:convolve(卷积)、pool(池化)、inner product(内积)、sigmod等非线性运算，元素级别的数 
             据变换，normalize(归一化)、load data(数据加载)、softmax和loss 
3. 一个Layer通过底部bottom(底部)连接层接收数据，通过top(顶部)连接层输出数据 
4. 每一个Layer层都定义了3中重要的运算: 
	-  setup(初始化设置):在模型初始化时，重置Layers及其相互之间的连接 
	- forward(前向传播):从bottom层中接收数据，进行计算后，将输出送入到top层中 
	- backforward(反向传播):给定相对于top层输出的梯度，计算其相对于输入的梯度，并传递到bottom层。一个有 
                      参数的layer需要计算相对各个参数的梯度值，并存储在内部。 
5. 需要特别指出的，Forward和Backward函数分别有CPU和GPU两种实现方式。如果没有GPU版本，那么layer将转向作为备用选 
             型的CPU方式。尽管这样会增加额外的数据传递成本(输入数据由GPU上复制到CPU，之后输出数据从CPU又复制回到GPU)，但是 
             对于做一些快速实验，这样的操作还是很方便的。 
6. 总的来说，layer承担了网络的【两个核心操作】: 
	- forward pass(前向传播):接收输入，并计算输出。 
	- backward pass(反向传播):接收关于输出的梯度，计算相对于参数和输入的梯度并反向传播给在它前面的层。由此 
                      组成每个layer的前向和反向通道 
7.  由于caffe网络的组合性和其代码的模块化，自定义layer是很容易的。只要定义好layer的: 
	- setup 
	- forward 
	- backward 
      就可以将layer纳入到网络。


### 关于参数命名的一些事项
```python
name:				#表示该层的名称，可以随意命名
type:				#层类型，主要有：Convolution, Data, pooling
bottom/top:			#输入/输出
data/label: 		#data层中，双输出
inclulde：			#指定属训练阶段or测试阶段
Transformations:	#数据的预处理，scale为0.00390625，即是1/255, 即将输入数据由0-255归一化到0-1之间


```
**卷积层**
```protobuf
layer
{
	name: "conv2"
    type: "Convolution"
    bottom: "norm1"
    top: "conv2"
    convolution_param 
    {
      num_output: 256
      pad: 2
      kernel_size: 5
      group: 2
    }
}
```
**池化层**
```protobuf
@ poollayer
layer 
    {
	      name: "pool5"
	      type: "Pooling"
	      bottom: "conv5"
	      top: "pool5"
	      pooling_param 
      {
	        pool: MAX
	        kernel_size: 3
	        stride: 2
      }
    }
```
**激活层**
```protobuf
layer 
    {
      name: "relu1"
      type: "ReLU"
      bottom: "conv1"
      top: "conv1"
    }
```
**LRN**
```protobuf
layer 
    {
      name: "norm1"
      type: "LRN"
      bottom: "pool1"
      top: "norm1"
      lrn_param 
      {
        local_size: 5
        alpha: 0.0001
        beta: 0.75
      }
    }
```
**Full Connect**
```protobuf
layer 
    {
      name: "fc6"
      type: "InnerProduct"
      bottom: "pool5"
      top: "fc6"
      inner_product_param 
      {
        num_output: 4096
      }
    }
```
**DropOut**
```protobuf
layer 
{
  name: "drop6"
  type: "Dropout"
  bottom: "fc6"
  top: "fc6"
  dropout_param 
  {
    dropout_ratio: 0.5
  }
}
```
**SoftMax**
```protobuf
layer 
    {
      name: "prob"
      type: "Softmax"
      bottom: "fc8"
      top: "prob"
    }
```
**Accuracy**
```protobuf
layer 
    {
      name: "accuracy"
      type: "Accuracy"
      bottom: "prob"
      bottom: "label"
      top: "accuracy"
    }
```
**Loss**
```protobuf
layer 
    {
	name: "loss"
      type: "SoftmaxWithLoss"
      bottom: "fc8"
      bottom: "label"
      top: "loss"
    }
```
  
    
