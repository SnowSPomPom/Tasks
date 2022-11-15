# JavaScript基础学习



## <font color=#884499>学前感想:sunny:</font>：

哇库哇库（）



---------------



## <a name=t0><font color=#884499>目录:sunny:：</font></a>

<a href=#t1><font color=#8888cc>一、JavaScript简介</font></a>:book:

<a href=#t2><font color=#8888cc>二、JavaScript书写位置:book:</font></a>

<a href=#t3><font color=#8888cc>三、JavaScript输入输出语句:book:</font></a>

<a href=#t4><font color=#8888cc>四、JavaScript语法：变量:book:</font></a>

<a herf=#t5><font color=#8888cc>五、JavaScript语法：数据类型:book:</font></a>

<a href=#t6><font color=#8888cc>六、运算符</font></a>

<a href=#t7><font color=#8888cc>七、分支、循环结构语句</font></a>

<a href=#t8><font color=#8888cc>八、函数</font></a>

<a href=#t9><font color=#8888cc>九、作用域</font></a>



---------------


## <font color=#884499>学习内容:sunny::</font>

### <a name=t1><font color=#8888cc>一、JavaScript简介:book:</font></a>

<a href=#t0><font color=#8888cc>back</font></a>

* <font color=#bb6688>JavaScript是什么</font>
  
  JavaScript 是脚本语言
  JavaScript 是一种轻量级的编程语言。
  JavaScript 是可插入 HTML 页面的编程代码。
  JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。
  
*  <font color=#bb6688>JS 与HTML、CSS</font>
  
  HTML 定义了网页的内容
  CSS 描述了网页的布局
  JavaScript 控制了**网页的行为**
  
* <font color=#bb6688>浏览器执行JS过程</font>

  CSS/HTMLyou由渲染引擎（俗称内核）执行；JS 由 JS引擎（JS解释器，逐行翻译） 专门执行

* <font color=#bb6688>JS 的组成</font>![image-20221109104708228](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221109104708228.png)

  ![image-20221109105424775](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221109105424775.png)

  ![image-20221109105501343](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221109105501343.png)

  ![image-20221109105521016](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221109105521016.png)

  

  
### <a name=t2><font color=#8888cc>二、JavaScript书写位置:book:</font></a>

<a href=#t0><font color=#8888cc>back</font></a>

* <script 标签会告诉JavaScript在何处开始和结束

* <font color=#bb6688>JavaScript可存在html文件的内部和外部</font>

  * 内部：

    * 内嵌式：<head 内：在<head>内写好指令，然后在<body>需要时调用

    * 行内式：<body>内：在需要的时候<script>写指令
    
  * 外部：外部 JavaScript 文件的文件扩展名是 .js；如需使用外部文件，请在 <script> 标签的 "src" 属性中设置该 .js 文件外部脚本不能包含 <script> 标签

    

###  <a name=t3><font color=#8888cc>三、JavaScript输入输出语句:book:</font></a>

<a href=#t0><font color=#8888cc>back</font></a>

- <font color=#bb6688>使用 **alert()** 弹出警告框。</font>

- <font color=#bb6688>使用 **document.write()** 方法将内容写到 HTML 文档中。</font>
  
  - document.write() (如：document.write(Date());可以调出具体时间)（在需要的地方<sc ript>包住此指令就行了>
  
  - 使用 document.write() 仅仅向文档输出写内容。
  
    如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖。
  
- <font color=#bb6688>使用 **innerHTML** 写入到 HTML 元素。</font>

  - document.getElementById(*i d* ).innerHTML="替代文字" ;再在需要的地方应用，如：<p id=""></p>
  
- <font color=#bb6688>使用 **console.log()** 写入到浏览器的控制台。</font>

  - 可以在文档中写入 **console.log()** ，这样在F12调出开发工具，点开控制台时可以看到 js 的运行结果

- <font color=#bb6688>使用 **prompt(info)** 让用户输入。</font>

  - 让浏览器弹出输入框让用户输入(取过来的值都是字符型)



### <a name=t4><font color=#8888cc>四、JavaScript语法：变量:book:</font></a>

<a href=#t0><font color=#8888cc>back</font></a>

* <font color=#bb6688>什么是变量</font>

  * 变量时程序在内存中申请的一块用来存放数据的空间

* <font color=#bb6688>变量的使用</font>

  * 1：声明变量（**var** 声明）；2：赋值

  * 变量命名规范：

    ![image-20221109114233153](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221109114233153.png)

  

### <a name=t5><font color=#8888cc>五、JavaScript语法：数据类型:book:</font></a>

  <a href=#t0><font color=#8888cc>back</font></a>

 * ![image-20221110161645083](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221110161645083.png)
  
 * JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型
  
 * <font color=#bb6688>数据类型：</font>
   
    * *数字型*：十进制：10；八进制：010；十六进制：0x10；（蓝紫色）
    * *字符串型*：加了 ‘’ 或 ‘ 引号的，都是字符串；（黑色）
      * 字符串内不能用标签，完成换行和tab缩进可用转义字符 \n、\t；
      * 检测字符串长度 'length'（如var str=...;console.log(str.length);）
    * 字符串的拼接：（‘ ’ **+**  ‘ ’)，数值相加，字符相连，与字符相加都变成字符串型； 
    
  * *布尔型*：布尔型有两种值：ture和false，其中true表示真（1），false表示假（0）（深蓝色）
    
    * 其他：undefine（灰色）
    
  * <font color=#bb6688>可以用**typeof**检测变量数据类型，如:</font>
  
    ```
     var flag = 1;
     console.log(typeof flag);
    ```
  
  * <font color=#bb6688>数据类型转换</font>
    
    * 转换为字符串型：**1.加号拼接字符串(和字符串拼接的结果都是字符串);**	2.变量.toString();	3.String(变量)强制转换
    * **转换为数字型**：1.parselnt(变量)函数；（取整）   2.parseFloat(变量)函数；（取整）（首为数字，会自动去掉单位）  3.parseFloat(变量)函数；（可以取小数）   4.隐式转换：如 2018 - year-->变成数字型
    * 其他：编译语言与解释语言![image-20221114191033649](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114191033649.png)
    * 其他：标识符、关键字、保留字
    
  * 实操：alert()获取用户信息并展示



### <a name=t6><font color=#8888cc>六、运算符</font></a>

* 算数运算符

  * 尽量避免浮点数运算

* 递增递减运算符

  * ++i和i++（先返回值后自加）

* 比较运算符

* 逻辑运算符

* 赋值运算符

* 运算符优先级

  ![image-20221114194030025](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114194030025.png)





### <a name=t7><font color=#8888cc>七、分支、循环结构语句</font></a>

* 三元表达式

  ![image-20221114200726528](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114200726528.png)

* 数字补0

  ![image-20221114200906149](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114200906149.png)

* 断点调试

  ![image-20221114201057455](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114201057455.png)

  点击代码行数数字，即设置好了断点，断点即让程序在此停止





### <a name=t8><font color=#8888cc>八、函数</font></a>

* <font color=#bb6688>函数使用</font>

  * 函数：函数就是封装了一段代码块

  * 函数声明

    * ![image-20221114203438042](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114203438042.png)

  * 调用函数

    * 调用函数不要忘记加小括号

  * 函数参数：

    * 声明函数小括号里是形参；函数调用小括号里实参；

    * 形参的作用是接收实参（类似于帮实参占个位，形参是不需要声明的变量）；

    * 函数形参实参个数不匹配问题：

      ![image-20221114204629692](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114204629692.png)

      tip:函数只能return一个值、return后面的代码不会被执行（return终止函数并只能返回一个值）

    * arguments的使用

      ![image-20221114210341710](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114210341710.png)

      ![image-20221114210451932](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114210451932.png)

      tip:pop()方法移除数组最后一个元素；shift()移除第一个元素；push()向数组末尾添加新项目，并返回新长度；unpush()向数组开头添加新项目

      tip：const 声明一个只读的常量

      实例：利用函数求任意输入个数的最大值

      ![image-20221114211754433](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221114211754433.png)





### <a name=t9><font color=#8888cc>九、作用域</font></a>

* <font color=#bb6688>JS作用域：</font>就是代码名字（变量）在某个范围内起作用和效果 目的是为了提高程序的可靠性更重要的是减少命名冲突
  * 全局作用域：整个scri pt标签 或者是一个单独的js文件
  * 局部（函数）作用域：在函数内部，代码名字只在函数内部起作用












---------------

## <font color=#884499>参考文献:sunny:：</font>

* [JavaScript 语法 | 菜鸟教程 (runoob.com)](https://www.runoob.com/js/js-syntax.html)
* [JavaScript基础语法-dom-bom-js-es6新语法-jQuery-数据可视化echarts黑马pink老师前端入门基础视频教程(500多集)持续_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Sy4y1C7ha/?spm_id_from=333.337.search-card.all.click&vd_source=a53694399a591711b5b6fddd1ee60075)
* 



















