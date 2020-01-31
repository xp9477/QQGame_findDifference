# QQGame_findDifference

### 1.截取全屏，找出两幅图片

### 2.对比两幅图片，框出区别之处

##### img.shape 取图像的垂直尺寸（高度）、水平尺寸（宽度）、通道数  image。

> shape[0]、shape[1]、shape[2]

##### numpy.zeros(shape, dtype=float, order=‘C’)   返回一个0数组 

> shape —— 整型或者整数序列，新数组的大小，比如 (2, 3) 或者 2
> dtype —— 数据类型，可选参数，默认float 
> order —— 是否在内存中以 C- 或 Fortran-contiguous（行或列）顺序存储多维数据。可选参数 

##### cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst.表示将两个图像进行重叠操作

> alpha 为 src1 透明度;
> beta 为 src2 透明度;
> gamma – scalar added to each sum
> 此函数可以用一下矩阵表达式来代替： dst = src1 * alpha + src2 * beta + gamma;
> **被叠加的两幅图像必须是尺寸相同、类型相同的**

##### 几种形态学运算

> **开运算(open)**：先腐蚀后膨胀的过程。开运算可以用来消除小黑点，在纤细点处分离物体、平滑较大物体的边界的同时并不明显改变其面积。
> **闭运算(close)**：先膨胀后腐蚀的过程。闭运算可以用来排除小黑洞。
> **形态学梯度(morph-grad)**：可以突出团块(blob)的边缘，保留物体的边缘轮廓。
> **顶帽(top-hat)**：将突出比原轮廓亮的部分。
> **黑帽(black-hat)**：将突出比原轮廓暗的部分。

##### getStructuringElement函数会返回指定形状和尺寸的结构元素。

> 这个函数的第一个参数表示内核的形状，有三种形状可以选择:
> 矩形：MORPH_RECT; 交叉形：MORPH_CROSS; 椭圆形：MORPH_ELLIPSE;
> 第二和第三个参数分别是内核的尺寸以及锚点的位置。对于锚点的位置，有默认值Point（-1,-1），表示锚点位于中心点

##### cv2.morphologyEx(src, op, kernel) 进行各类形态学的变化

> src - 传入的图片
> op - 进行变化的方式
> kernel - 核心

##### cv2.imread()接口读图像，读进来直接是BGR 格式数据格式在 0~255.

> **需要特别注意的是图片读出来的格式是BGR，不是我们最常见的RGB格式**

##### cv2.cvtColor(p1,p2) 是颜色空间转换函数

> p1是需要转换的图片，p2是转换成何种格式。

##### cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst  作用是将一幅灰度图二值化。

> src：图片源
> thresh：阈值
> maxval：表示的是最大值
> type：表示的是这里划分的时候使用的是什么类型的算法，常用值为0（cv2.THRESH_BINARY）
> 
> retval与参数thresh一致表示阈值
> dst：结果图像

##### cv2.findContours(image, mode, method, contours=None, hierarchy=None, offset=None)

> image 代表输入的图片。**注意输入的图片必须为二值图片。若输入的图片为彩色图片，必须先进行 <u>灰度化</u> 和 <u>二值化</u> 。**
> mode  表示轮廓的检索模式，有4种：
> - cv2.RETR_EXTERNAL  表示只检测外轮廓。
> - cv2.RETR_LIST  检测的轮廓不建立等级关系。
> - cv2.RETR_CCOMP  建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
> - cv2.RETR_TREE  建立一个等级树结构的轮廓。
> 
> method  为轮廓的近似办法，有4种：
> - cv2.CHAIN_APPROX_NONE  存储所有的轮廓点，相邻的两个点的像素位置差不超过1
> - cv2.CHAIN_APPROX_SIMPLE  压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息。
> - cv2.CHAIN_APPROX_TC89_L1 和 cv2.CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法。 
> cv2.findContours()函数返回两个值，一个是轮廓本身contours，还有一个是每条轮廓对应的属性hierarchy。

##### cv2.boundingRect(img)  用一个最小的矩形，把找到的形状包起来.
>img是一个二值图，也就是它的参数；返回四个值，分别是x，y，w，h；
x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
然后利用cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)画出矩行.

##### cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) 画出矩形
> 第一个参数：img是原图
> 第二个参数：（x，y）是矩阵的左上点坐标
> 第三个参数：（x+w，y+h）是矩阵的右下点坐标
> 第四个参数：（0,255,0）是画线对应的rgb颜色
> 第五个参数：2是所画的线的宽度
