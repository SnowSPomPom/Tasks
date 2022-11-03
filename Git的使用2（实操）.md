# <font color=red> git的使用2（实操）</font>

###  一、建立仓库✨

#### 1.建立当地仓库

1. 新建目录（git menu <-我建的）

2. 将该目录变成git可管理的仓库

   ` $  git init`

   git menu下多了一个隐藏目录（.git)，用来管理追踪版本库

#### 2.建立远程仓库


###  二、管理文件✨

#### 1. 添加文件

   * 新建文件( readme. txt)

   * 提交文件至暂存区

     ` $ git add readme. txt `

   * 提交文件至当地仓库

     ` $ git commit -m"readme file" `

#### 2.修改文件

* 修改文件（readme.txt)

* 提交

  ```bash
  $ git add readme.txt
  $ git commit -m"填写备注"
  ```

* 版本库多了一个版本，可查看历史记录

  ```bash
  $ git log
  ```

  便可调出所有历史记录，若嫌输出信息太多，看得眼花缭乱的，可以试试加上`
  --pretty=oneline
  `
  
* 分辨版本
  
  ` head`表示当前版本，`head^`表示上一个版本，`head^^`表示上上个版本，往上n个版本后面就有n个`^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`
  
#### 3.版本回退

* 回退版本命令`git reset--hard head`

* 取消回退

  * 法1：在log里找所要回退版本的commit id（一般是一串看不懂的数字，如1094abd...）此时输入命令`$ git reset --hard commit id(如1094a)`，版本号不要求写全
  * 法2：使用`git reflog`，该命令用来记录你的每一次命令

  ​		

  

  



