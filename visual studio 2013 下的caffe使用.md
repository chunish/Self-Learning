# visual studio 2013 下的caffe使用

---

### debug模式
1. 关于include路径问题
```cpp
//预加载项目录
E:\caffe\include;  
E:\NugetPackages\glog.0.3.3.0\build\native\include;
E:\NugetPackages\OpenBLAS.0.2.14.1\lib\native\include;
E:\NugetPackages\OpenCV.2.4.10\build\native\include;
E:\NugetPackages\boost.1.59.0.0\lib\native\include;
E:\NugetPackages\gflags.2.1.2.1\build\native\include;
E:\NugetPackages\hdf5-v120-complete.1.8.15.2\lib\native\include;
E:\NugetPackages\LevelDB-vc120.1.2.0.0\build\native\include;
E:\NugetPackages\lmdb-v120-clean.0.9.14.0\lib\native\include;
E:\NugetPackages\protobuf-v120.2.6.1\build\native\include;
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v7.5\include //使用GPU额外附加
```
2. lib目录
```cpp
//lib目录
E:\caffe\Build\x64\Debug;  
E:\NugetPackages\OpenCV.2.4.10\build\native\lib\x64\v120\Debug;  
E:\NugetPackages\boost_chrono-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_date_time-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_filesystem-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_system-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_thread-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\gflags.2.1.2.1\build\native\x64\v120\dynamic\Lib;  
E:\NugetPackages\glog.0.3.3.0\build\native\lib\x64\v120\Debug\dynamic;  
E:\NugetPackages\hdf5-v120-complete.1.8.15.2\lib\native\lib\x64;  
E:\NugetPackages\LevelDB-vc120.1.2.0.0\build\native\lib\x64\v120\Debug;  
E:\NugetPackages\lmdb-v120-clean.0.9.14.0\lib\native\lib\x64;  
E:\NugetPackages\OpenBLAS.0.2.14.1\lib\native\lib\x64;  
E:\NugetPackages\protobuf-v120.2.6.1\build\native\lib\x64\v120\Debug;  
E:\NugetPackages\boost_date_time-vc120.1.59.0.0\lib; 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v7.5\lib\x64  //使用GPU附加
```
3. 连接器
```cpp
//linker
caffe.lib;  
compute_image_mean.lib;  
convert_imageset.lib;  
convert_mnist_data.lib;  
libcaffe.lib;  
opencv_highgui2410d.lib;  
opencv_imgproc2410d.lib;  
opencv_objdetect2410d.lib;  
opencv_core2410d.lib;  
opencv_ml2410d.lib;  
libboost_date_time-vc120-mt-gd-1_59.lib;  
libboost_filesystem-vc120-mt-gd-1_59.lib;  
libboost_system-vc120-mt-gd-1_59.lib;  
libglogD.lib;  
hdf5.lib;  
hdf5_cpp.lib;  
hdf5_f90cstub.lib;  
hdf5_fortran.lib;  
hdf5_hl.lib;  
hdf5_hl_cpp.lib;  
hdf5_hl_f90cstub.lib;  
hdf5_hl_fortran.lib;  
hdf5_tools.lib;  
szip.lib;  
zlib.lib;  
LevelDbD.lib;  
lmdbD.lib;  
libprotobufD.lib;  
libopenblas.dll.a;  
gflags_nothreadsd.lib;  
gflagsd.lib;  
//连接器附加
cublas.lib  
cuda.lib  
cublas_device.lib  
cudnn.lib  
cudadevrt.lib  
cudart.lib  
cudart_static.lib  
cudnn_static.lib  
cufft.lib  
cufftw.lib  
curand.lib  
cusolver.lib  
cusparse.lib  
nppc.lib  
nppi.lib  
npps.lib  
nvblas.lib  
nvcuvid.lib  
nvrtc.lib 
```

### release模式

1. lib目录
```cpp
E:\caffe\Build\x64\Release;  
E:\NugetPackages\boost_chrono-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_date_time-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_filesystem-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_system-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\boost_thread-vc120.1.59.0.0\lib\native\address-model-64\lib;  
E:\NugetPackages\gflags.2.1.2.1\build\native\x64\v120\dynamic\Lib;  
E:\NugetPackages\glog.0.3.3.0\build\native\lib\x64\v120\Release\dynamic;  
E:\NugetPackages\hdf5-v120-complete.1.8.15.2\lib\native\lib\x64;  
E:\NugetPackages\LevelDB-vc120.1.2.0.0\build\native\lib\x64\v120\Release;  
E:\NugetPackages\lmdb-v120-clean.0.9.14.0\lib\native\lib\x64;  
E:\NugetPackages\OpenBLAS.0.2.14.1\lib\native\lib\x64;  
E:\NugetPackages\OpenCV.2.4.10\build\native\lib\x64\v120\Release;  
E:\NugetPackages\protobuf-v120.2.6.1\build\native\lib\x64\v120\Release; 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v7.5\lib\x64  //gpu附加
```
2. 链接器
```cpp
opencv_core2410.lib;  
opencv_highgui2410.lib;  
opencv_imgproc2410.lib;  
caffe.lib;  
libcaffe.lib;  
gflags.lib;  
libglog.lib;  
libopenblas.dll.a;  
libprotobuf.lib;  
leveldb.lib;  
lmdb.lib;  
hdf5.lib;  
hdf5_hl.lib;  
libboost_date_time-vc120-mt-s-1_59.lib;  
libboost_filesystem-vc120-mt-s-1_59.lib;
//GPU附加
cublas.lib  
cuda.lib  
cublas_device.lib  
cudnn.lib  
cudadevrt.lib  
cudart.lib  
cudart_static.lib  
cudnn_static.lib  
cufft.lib  
cufftw.lib  
curand.lib  
cusolver.lib  
cusparse.lib  
nppc.lib  
nppi.lib  
npps.lib  
nvblas.lib  
nvcuvid.lib  
nvrtc.lib
```
