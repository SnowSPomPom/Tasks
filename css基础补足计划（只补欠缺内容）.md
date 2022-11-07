

# CSS基础补足

## 目录 ：

  1. <a href=#t1>***css的position定位* **</a>

  2. ***<a href=#t3>css的float浮动</a>***

  3. ***<a href=#t4>css对齐</a>***

  4. ***<a href=#t5>CSS网页布局</a>***

   5. <a href=#t2>***css伪类***</a>

      


-----------



### <a name=t1> 一、css的position定位</a>

* **position定位属性：1. static 2.relative 3.fixed 4.absolute 5.sticky**
  
  * **static**:HTML元素的默认值，即没有定位，遵循正常的文档流对象。静态定位的元素不会受到 top, bottom, left, right影响。
  
  * **fixed**:元素的位置相对于浏览器窗口是固定位置。即使窗口是滚动的它也不会移动（tip:这个属性下的top、right是指相对于浏览器窗口边缘的距离）
  
  * **relative**:
  
    * 相对定位元素的定位是相对其正常位置。![image-20221107214848627](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221107214848627.png)
    * 移动相对定位元素，但它原本所占的空间不会改变。![image-20221107214910396](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221107214910396.png)
    * 相对定位元素经常被用来作为绝对定位元素的容器块。
  
  * **absolute**:绝对定位的元素的位置<u>相对于最近的已定位父元素</u>，如果元素没有已定位的父元素，那么它的位置相对于<html>
  
  * **重叠元素**：**z-index**属性指定了一个元素的堆叠顺序（哪个元素应该放在前面，或后面）一个元素可以有正数或负数的堆叠顺序：
  
    ![image-20221107220235124](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221107220235124.png)



### <a name=t3>二、css的float浮动</a>

```
CSS 的 Float（浮动），会使元素向左或向右移动，其周围的元素也会重新排列。
Float（浮动），往往是用于图像，但它在布局时一样非常有用。
```

* **元素怎样浮动**

  * 元素**只能左右移动**而不能上下移动。

    一个浮动元素会尽量向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。

    浮动元素之后的元素将围绕它。

    浮动元素之前的元素将不会受到影响。
  
    如果图像是右浮动，下面的文本流将环绕在它左边
  
* **彼此相邻的浮动元素**
  
  * 如果你把几个浮动的元素放到一起，如果有空间的话，它们将彼此相邻。
  
* **清除浮动 - 使用 clear**
  
  * 元素浮动之后，周围的元素会重新排列，为了避免这种情况，使用 **clear **属性。
  
    clear 属性指定元素两侧不能出现浮动元素。常用指令：` clear:both`（两边都不会出现浮动元素）
  
    
  

### <a name=t4>三、css对齐</a>

* **元素居中对齐**
  * 要水平居中对齐一个元素(如 <div>), 可以使用 **margin: auto;**元素通过指定宽度，并将两边的空外边距平均分配；**注意:** 如果没有设置 **width** 属性(或者设置 100%)，居中对齐将不起作用
* **文本居中对齐**
  * 如果仅仅是为了文本在元素内居中对齐，可以使用 **text-align: center;**还可以直接设置align:center
* **图片居中对齐**
  * 要让图片居中对齐, 可以使用 **margin: auto;** 并将它放到 **块** 元素中



### <a name=t5>四、CSS网页布局</a>

* **网页布局**：网页布局有很多种方式，一般分为以下几个部分：**头部区域、菜单导航区域、内容区域、底部区域**。

  * **头部区域**：头部区域位于整个网页的顶部，一般用于设置网页的<u>标题或者 logo</u>

  * **菜单导航区域**:菜单导航条包含了一些链接，可以引导用户浏览其他页面

  * **内容区域**:![image-20221107225846186](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221107225846186.png)

    ![image-20221107225901574](C:\Users\BPRQ\AppData\Roaming\Typora\typora-user-images\image-20221107225901574.png)

  * **底部区域**：底部区域在网页的最下方，一般包含<u>版权信息和联系方式等</u>。



### <a name=t2>五、css伪类</a>

* **什么是css伪类**：CSS 伪类是用来添加一些 '选择器' 的特殊效果(特殊状态)。（原来这些是伪类啊，以前不知道具体名字）

  * 伪类实际使用场景举例:

    1. 设置鼠标悬停在元素上时的样式 。

    2. 为已访问和未访问链接设置不同的样式 。

    3. 设置元素获得焦点时的样式 。

* **css伪类选择器的分类**

    * **动态伪类选择器**

      | 动态伪类 |   示例    |     示例说明     |
      | :------: | :-------: | :--------------: |
      |  :link   |  a:link   |   未访问的链接   |
      | :visited | a:visited |   已访问的链接   |
      |  :hover  |  a:hover  | 鼠标悬停链接效果 |
      | :active  | a:active  |    已选中链接    |
    
      ```
      注意：这几个伪类同时出现在一个元素的操作上，顺序不能改变，否则很大程度上会产生紊乱，造成效果失效！
      a:hover 必须在 CSS 定义中的 a:link 和 a:visited 之后，才能生效。(意思是必须先写a:link 和 a:visited再写 :hover）
      a:active 必须在 CSS 定义中的 a:hover 之后才能生效。(意思是必须先写a:hover再写 :active）
      另外伪类名称对大小写并不敏感 
      ```
    
    * **结构伪类选择器**
    
        |     动态伪类      |        示例         |                           示例说明                           |
        | :---------------: | :-----------------: | :----------------------------------------------------------: |
        |   :first-child    |    p:first-child    |                  选择某个元素的第一个子元素                  |
        |    :last-child    |    p:last-child     |                选择某个元素的最后一个子元素；                |
        |   :nth-child(n)   |   p:nth-child(2)    |       匹配属于其父元素的第 n个子元素，不论元素的类型；       |
        | :nth-last-child() | p:nth-last-child(2) | 从这个元素的最后一个子元素开始算,选匹配属于其父元素的第 n个子元素，不论元素的类型； |
        |  :nth-of-type()   |   :nth-of-type()    |             规定属于其父元素的第n个 指定 元素；              |
        |  :first-of-type   |  li:first-of-type   |            选择一个上级元素下的第一个同类子元素；            |
        |    :only-child    |     :only-child     |               选择它的父元素的唯一一个子元素；               |
        |      :empty       |      div:empty      |                 选择的元素里面没有任何内容;                  |
        |      :after       |      div:after      |                     在该元素之后插入内容                     |
      
      *以下是一些有点超出我理解范围的，估计学到后面就懂了（）*
      
      ```
      :checked匹配被选中的input元素，这个input元素包括radio和checkbox。
      
       :disabled匹配禁用的表单元素。
       :enabled匹配没有设置disabled属性的表单元素。
       :valid匹配条件验证正确的表单元素。
       :in-range选择具有指定范围内的值的 <input> 元素。
       :optional选择不带 "required" 属性的 <input> 元素。
       :focus选择获得焦点的 <input> 元素。
      否定伪类选择器
      ```
      

tip：透明度：**opacity**

------------

### 参考资料：

* [菜鸟教程（css position定位）]([CSS Position(定位) | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-positioning.html))

* [CSS 伪类: 什么是 CSS 伪类？CSS 伪类怎么分类？ CSS 伪类有哪些？以及分类对应的伪类](https://blog.csdn.net/wuzhiyue2/article/details/118494100)

* [菜鸟教程（css float浮动)]([CSS Position(定位) | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-positioning.html))

* [菜鸟教程（css 布局-水平&垂直对齐）]([CSS 布局 – 水平 & 垂直对齐 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-align.html))

* [菜鸟教程（css网页布局）]([CSS 网页布局 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-website-layout.html))