### 数组
* **创建数组**：<font color=red>var 数组名 = [] ;  var 字符串名 = ''</font>
* **获取（访问）数组元素**：数组名[ 索引号 ]
* **数组长度**：数组名.length
### 函数两种声明方式
* **命名函数** function fun() {}
* **匿名函数** var fun=function() {}
  fun是<u>变量名</u> 不是函数名
  [函数实例](函数.html)
### 作用域
* **js作用域** ：就是代码名字（变量）在某个范围内起作用和效果 目的是为了提高程序的可靠性 更重要的是减少命名冲突，js没有块级作用域
* **全局变量域** ：整个script标签 或者单独的js文件
* **局部变量域** ：在函数内部就是局部作用域 这个代码的名字只在函数内部起效果和作用
* **作用域链** ：如果函数中还有函数，那么在这个作用域中又可以诞生一个作业域；根据在内部函数可以访问外部函数变量的这个机制，用链式查找（寻找上一级作用域）决定那些数据能被内部函数访问，就称为作用域链
### 预解析
* js引擎运行js 分为两步：预解析 代码执行
* 预解析： js引擎会把js 里面所有的var 还有function 提升到当前作用域的最前面
* tip:var a=9,b=9,c=9;(var a=b=c=9;×)
### 对象
* **对象**：一个具体的事物，一个数据库、一张网页、一个与远程服务器的连接也可以是“对象”；在js中，对象是一组无序的相关<u>属性（特征）和方法（行为）的集合</u>，所有的事物都是对象，比如字符串、数值、数组、函数等
JS对象分3种：自定义对象、内置对象、浏览器对象
* **创建对象的方法**
  * **1.利用对象字面量 创建**
    var xxx ={ xx:xx, xx:xx, xx:xx(){}; }

    ```
    var obj={
      uname:"冰皮",
      age:8,
      sex:"女",
      sayHi: function(){
        console.log("hi~');
      }
    }
    console.log(obj.age);
    console.log(obj['age']);
    obj.sayHi();  //调用
    ``` 
    (1)键值对形式 键（属性名）：值（属性值）
    (2)多个属性或方法中间用逗号“，”隔开
    (3)方法冒号后面跟的是一个匿名函数
    (4)调用：对象名.属性名 / 对象名['属性名'] / 对象名.方法名()
  * **2.利用new Object()创建**
    var xxx = new Object();

    ```
    var obj = new Object();
    obj.uname="冰皮";
    obj.age=8;
    obj.sex="女";
    obj.sayHi: function(){
        console.log("hi~');
      }
    ```
    new关键词执行过程
    (1) new 构建函数可以在内存中创建了一个空对象
    (2) this 就会指向刚刚创建的空对象
    (3) 执行构造函数里的代码，给这个空对象添加属性和方法
    (4) 返回这个对象
  * **3.构建函数创建对象**
    ```
    function 构造函数（）{
      this.属性 = 值;
      this.方法 = function() {
      } 
    }
    new 构造函数名();
    ```
    ```
    例子：
    function Star（uname,age,sex）{
      this.name = uname;
      this.age = age;
      this.sex = sex;
    }
    var snows = new Star('冰皮',18,'女');
    console.log(snows);
    console.log(snows['sex']);
     //调用函数返回的是一个对象
    ```
    (1)构造函数名字首字母大写
    (2)只要new Star()一下就创建了一个对象 
### 遍历对象
  * **for...in循环**
    ``` 
    for (var k in obj){
      console.log(k); // k 变量 输出 得到的是 属性名 
      console.log(obj[k]);  //  obj[k] 得到的是 属性值
    }
    // 我们使用 for in 里面的变量 我们喜欢写 k 或者 key
    ```
### 内置对象
  * **内置对象** 指JS语言自带的一些对象，这些对象供开发者使用，并提供了一些常用的或是最基本二必要的功能（属性和方法）。如Math、Date、Array、String等
  *  **查文档** [MDN](https://developer.mozilla.org/zh-CN)
  * **Math对象** 是对象不是构造函数 ， 不需要new 调用，直接使用里面的属性和方法
     <img src='Math对象.png'>
     随机数方法 **random()** Math.random();随机返回一个0-1的小数，不用写参数（也可以得到俩数之间的随机数，可以查文档）
     ```
    function getRandomIntInclusive(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min; //含最大值，含最小值
    }
    ```

### DOM
  #### DOM HTML 
  * **直接写入html**： document.write() 可用于直接向 HTML 输出流写内容
  * **改变 HTML 内容**：document.getElementById(id).innerHTML=新的 HTML   改变HTML元素的内容
    ```
    例：document.getElementById("p1").innerHTML="新文本!";
    var element=document.getElementById("header");
    element.innerHTML="新标题";
    ```
  * **改变 HTML 属性**：
  document.getElementById(id).attribute=新属性值
    ```
    例：
    <img id="image" src="smiley.gif">

    <script>
    document.getElementById("image").src="landscape.jpg";
    </script>
    ```
  #### DOM CSS
  * **改变 HTML 样式**：document.getElementById(id).style.property=新样式
