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
    ```
    document.getElementById("p1").innerHTML="新文本!";
                方法(method)       属性(property)
     ```
  * **改变 HTML 内容**：document.getElementById(id).innerHTML=新的 HTML   改变HTML元素的内容
    ```
    例：
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
    ```
      一些常用的 HTML DOM 方法：

    getElementById(id) - 获取带有指定 id 的节点（元素）
    appendChild(node) - 插入新的子节点（元素）
    removeChild(node) - 删除子节点（元素）
    一些常用的 HTML DOM 属性：

    innerHTML - 节点（元素）的文本值
    parentNode - 节点（元素）的父节点
    childNodes - 节点（元素）的子节点
    attributes - 节点（元素）的属性节点
    ```
  #### DOM 事件
  * **onclick**
  * **onchange** 更改设置时将触发该事件
  * **onmouseover 和 onmouseout 事件**
  * **onmousedown、onmouseup 以及 onclick 事件** 首先当点击鼠标按钮时，会触发 onmousedown 事件，当释放鼠标按钮时，会触发 onmouseup 事件，最后，当完成鼠标点击时，会触发 onclick 事件
  #### EventListener
  * **addEventListener() 方法**
    ```
    element.addEventListener(event, function, useCapture);
    例子：
    document.getElementById("demo").addEventListener("click", displayDate);
    对id“demo”监视，监视到click就执行displayDate函数
    ```
  * **事件冒泡或事件捕获** 
  事件传递定义了元素事件触发的顺序,若div里装了p，用户点击 <p> 元素, 哪个元素的 "click" 事件先被触发呢？
  在 *冒泡* 中，*内部元素的事件会先被触发*，然后再触发外部元素，即： <p> 元素的点击事件先触发，然后会触发 <div> 元素的点击事件。
  在 *捕获* 中，*外部元素的事件会先被触发*，然后才会触发内部元素的事件，即： <div> 元素的点击事件先触发 ，然后再触发 <p> 元素的点击事件。

  * **removeEventListener() 方法** 
  element.removeEventListener(event, function)
  #### DOM 元素 (节点)
  * **创建新的 HTML 元素 (节点)** 
  appendChild()   insertBefore()
  * **移除已存在的元素**
  parent.removeChild(child)
  * **替换 HTML 元素**
  replaceChild()

  * **Finding HTML Elements**

    | **Method**                            | **Description**      |
    | ------------------------------------- | -------------------- |
    | document.getElementById(id)           | 通过id寻找element    |
    | document.getElementsByTagName(name)   | 通过标签寻找element  |
    | document.getElementsByClassName(name) | 通过class寻找element |

  * **Changing HTML Elements**
    | **Property**                           | **Description**                               |
    | -------------------------------------- | --------------------------------------------- |
    | element.innerHTML =  new html content  | Change the inner HTML of an element           |
    | element.attribute = new value          | Change the attribute value of an HTML element |
    | element.style.property = new style     | Change the style of an HTML element           |
    | **Method**                             | **Description**                               |
    | element.setAttribute(attribute, value) | Change the attribute value of an HTML element |
  * **Adding and Deleting Elements**
    | **Method**                      | **Description**                   |
    | ------------------------------- | --------------------------------- |
    | document.createElement(element) | Create an HTML element            |
    | document.removeChild(element)   | Remove an HTML element            |
    | document.appendChild(element)   | Add an HTML element               |
    | document.replaceChild(new, old) | Replace an HTML element           |
    | document.write(text)            | Write into the HTML output stream |
  #### DOM forms
  (attest in hungry.html)


### 执行上下文

  --------
### tip
  * String.prototype.toUpperCase() 转大写函数
  * resize（css一种属性）
  * Math.random()（随机数函数）
  * [声明关键字](https://www.cnblogs.com/forcheng/p/13033976.html)
    | 关键字 | 作用域           | 重复声明                 | 绑定全局对象               | 变量提升与暂存死区                                                                                                                                   | 是否只读 |
    | ------ | ---------------- | ------------------------ | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
    | var    | 全局、整个函数块 | 可在同一作用域中重复声明 | 会在全局对象里新建一个属性 | 声明的变量在执行上下文创建阶段就会被「创建」和「初始化」，因此对于执行阶段来说，可以在声明之前使用                                                   | 可改     |
    | let    | 当前所处代码块   | 不可,会抛出异常          | 不会新建属性               | 声明的变量在执行上下文创建阶段只会被「创建」而不会被「初始化」，因此对于执行阶段来说，如果在其定义执行前使用，相当于使用了未被初始化的变量，会报错。 | 可改     |
    | const  | 同let            | 同let                    | 同let                      | 同let                                                                                                                                                | 只读     |
    ```
    var|let
        function varTest() {
      var a = 1;
      {
        var a = 2; // 函数块中，同一个变量
        console.log(a); // 2
      }
      console.log(a); // 2
    }

    function letTest() {
      let a = 1;
      {
        let a = 2; // 代码块中，新的变量
        console.log(a); // 2
      }
      console.log(a); // 1
    }
    let 声明的变量的作用域可以比 var 声明的变量的作用域有更小的限定范围，更具灵活
    ```
