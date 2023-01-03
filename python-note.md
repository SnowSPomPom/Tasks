# Python笔记:book:
------
## 目录：<br>
* :sunny:VSC相关
  * 插件
  * 快捷键
* :sunny:Python
  * 动态数据类型
  * 字符串
  * 转义字符
  * 格式化字符串
  * 常用的字符串方法
  * 操作数字、代数运算法、数据转换
  * 条件语句
  * 操作符
  * 循环语句
  * 函数
  * 数据结构
------
### :sunny:VSC相关
* 打开内置编译器：ctrl+`
* 打开命令行（windows)：ctrl+shift+P
* pylint:纠错
* autopep8:排版
* code runner:ctrl+alt+N 运行
* 快捷键：
  至句尾/首 fn + end/home
一行代码移动（复制） (shift +) alt + pgup/pgdn
代码变注释 ctrl + /
批量选中相同内容 Ctrl + d

### :sunny:Python
* **动态数据类型：**
  * 是动态语言，在定义时不用声明类型;
  * 若想知道变量类型，将鼠标移到变量上就会出现变量类型的提醒;
  * type()可以传入一个变量或对象;如print(type(变量/数据))会输出相应数据的类型
  * id()可以调出数据存储的地址
* **字符串**
  * len()计算字符串长度
  * 取字符串单个字符：str,str[0],str[-1]
  * 切割字符串：str[0:-1]（不包括[-1]的字符）；第一个可以省略，默认为0；第二个可省略，默认输出至最后一个字符；两个都可省略，默认输出全部字符
  * 每次取字符，取出的字符会赋予新内存，新地址；因为字符串以及其他值类型变量在python里不可变

* **转义字符**
* **格式化字符串**
  * <img src=E:\编程练习\Python\HelloWorld\img\1.png width=400>
  * 大括号占位的地方将会被值取代，可放入任何表达式

* **常用的字符串方法**
  * upper()字符串大写；lower();title()每个词首字母大写；strip()去空格；find()找到字符的位置；replace("a","b")替换全部a为b

* **操作数字、代数运算法、数据转换**
  * //除（结果取整数）
  * 大写字母命名的变量可视作常量
  * round()舍去小数位；abs()取绝对值；内置函数可通过“python 版本 built-in functions”
  * 数据转换<br> <img src=E:\编程练习\Python\HelloWorld\img\2.png width=100>

* **条件语句**
  ``` 
  if 条件1: 表达式1
  elif 条件2: 表达式2
  else : 表达式3
  ```
* **操作符**
  * **0 "" None [] 被认为是假**
  * 三元操作符 例子：message **=** "eligible" **if** age >= 18 **else** "not eligible"

* **循环语句**
  * for循环<br><img src=E:\编程练习\Python\HelloWorld\img\3.png width=400>
  * for...else循环<br><img src=E:\编程练习\Python\HelloWorld\img\4.png width=400>
  * while循环<br>while 判断 : 表达式

* **函数**
  * ```
    def 函数名(形参1，形参2)：
        pass
  函数可以返回多值，如return(number,number + by)
  * 星标参数<br><img src=E:\编程练习\Python\HelloWorld\img\5.png width=400>
  F9：快速插入中断点

* **数据结构**
  * **列表(list)** [] <br><img src=E:\编程练习\Python\HelloWorld\img\6.png width=400><br>访问列表项（类似访问字符串中字符）<br>列表拆包<br><img src=E:\编程练习\Python\HelloWorld\img\7.png width=400><img src=E:\编程练习\Python\HelloWorld\img\7.2.png width=400><br>遍历列表：for...in...遍历；enumerate()输出带序号的元组<br>常见操作：
    ```
    列表名.append() 在最后添加元素
    列表名.insert(0,"-") 插入"-"为第0个元素
    列表名.pop() 默认删除最后一个元素，通过序号删除一项
    列表名.remove() 通过填写具体元素精确删除
    列表名.clear() 删除全部项
    del 列表名[] 可以删除一组项
    列表名.index(具体元素) 可以查找，输出元素序号 
    列表名.count(具体元素) 计算元素在列表里出现次数
    列表名.sort() 自动排序（数字，从小到大）/列表名.sort(reverse=True) 自动排序（数字，从大到小）
    ```
  * **匿名函数**
  <img src=E:\编程练习\Python\HelloWorld\img\lambda1.png width=400><br>映射函数(map())<br><img src=E:\编程练习\Python\HelloWorld\img\lambda2.png width=400><br><img src=E:\编程练习\Python\HelloWorld\img\lambda3.png width=400><br>筛选函数((filter))<br><img src=E:\编程练习\Python\HelloWorld\img\lambda4.png width=400><br>列表推导式<br><img src=E:\编程练习\Python\HelloWorld\img\lambda5.png width=400><br>zip函数<br>zip(list1,list2)两个列表交叉形成新列表<br><img src=E:\编程练习\Python\HelloWorld\img\zip.png width=250>
  堆（LIFO后进先出）
  队列 (FIFO先进先出)
  元组（只读的列表，用小括号()定义，无括号多个元素默认为元组）（列表转元组tuple()）
  交换变量值<br><img src=E:\编程练习\Python\HelloWorld\img\8.png width=150>
  数组
  集合 
  字典<br><img src=E:\编程练习\Python\HelloWorld\img\dict.png width=400>



-------
## 学习资料<br>
[[Python系列][第 5 章完结]Python开发者课程 - Mosh](https://www.bilibili.com/video/BV12441187D1?p=39&vd_source=a53694399a591711b5b6fddd1ee60075)

