# 基于python语言的BIBA模型图形界面实现
>姓名：  严寒  
>学号：  2018202110087  
>学院：  国家网络安全学院  
>导师：  彭国军  
##  一、实验目的：
1. **查阅资料，了解biba安全模型的相关知识**
2. **通过编程实现基于biba模型的完整性访问控制，进一步掌握biba模型的规则**
3. **使用python语言实现，熟练pyqt的图形界面设计方法**
-------------
##  二、实验环境：
* 操作系统：Windows10
* 工具版本：python3.7，pyqt5
-------------
##  三、实验原理：
1. 什么是安全模型  
 * 系统的元素  
 > 具有行为能力的主体  
 > 不具有行为能力的客体
 * 系统的操作行为
 > 可以执行的命令：读、写、执行
 * 对系统行为的约束方式
 > 对行为的控制策略
 * 模型从抽象层次规定了系统行为和约束行为的方式
 * 模型往往用状态来表示
 > 系统行为所依赖的环境  
 > 行为对系统产生的效果
2. biba完整性模型：  
  * 完整性威胁问题
  > 完整性的威胁就是一个子系统在初始时刻认为不正常的修改行为；  
  > 来源：内部&外部；  
  > 类型：直接&间接

|外部的直接 |外部的间接|内部的直接|内部的间接
|-----|--------|------|-------|
|外部系统恶意地篡改另一个系统的数据或程序|一个外部系统插入恶意的子程序|修改自己的代码|修改自己的指针|     

  * biba模型的完整性定义
  >完整性级别高的实体对完整性低的实体具有完全的支配性，反之如果一个实体对另一个实体具有完全的控制权，说明前者完整性级别更高，这里的实体既可以是主体也可以是客体。   
  >完整性级别和可信度有密切的关系，完整级别越高，意味着可信度越高。
  * biba模型的规则   
  - [ ] 对于写和执行操作，有如下规则：
  > **写规则控制**
  当且仅当主体S的完整性级别大于或等于客体O的完整性级别时，主体S可以写客体O,一般称之为**上写**。   
  > **执行操作控制**
  当且仅当主体S2的完整性级别高于或等于S1,主体S1可以执行主体S2。  
  - [ ] 关于读操作，有不同的控制策略：
  > **低水标模型**    
  任意主体可以读任意完整性级别的客体，但是如果主体读完整性级别比自己低的客体时，主体的完整性级别将为客体完整性级别，否则，主体的完整性级别保持不变。  
  > **环模型**   
  不管完整性级别如何，任何主体都可以读任何客体  
  > **严格完整性模型**   
  这个模型对读操作是根据主客体的完整性级别严格控制的，即只有完整性级别低或相等的主体才可以读完整性级别高的客体，称为**下读**

**一般都是指毕巴严格完整性模型，总结来说是上写、下读**

------------

##  四、实验内容：
1.  用户登录实现  

**核对用户输入的账户密码与存储的是否匹配**

![login](https://github.com/Cool-Y/BIBA-model/blob/master/img/login.PNG)

* 从用户输入框获取账户和密码
* 检查输入信息是否合法（为空）
* 从password.txt中获取，并保存在列表listFromLine中
* 检查输入的账户是否存在
* 若存在，检查对应的密码是否正确
* 若正确，判断是管理员还是普通用户，并跳转相应的界面

  ```python
  def checkPass(self):
      nameIn = self.lineEdit.text()
      passwdIn = self.lineEdit_2.text()
      md5 = hashlib.md5()
      md5.update(passwdIn.encode("utf-8"))
      passwdIn = md5.hexdigest()
      if (nameIn == '') or (passwdIn == ''):
          QMessageBox.warning(self,
                              "警告",
                              "账号和密码不能为空",
                              QMessageBox.Yes)
          self.lineEdit.setFocus()
      print(nameIn, passwdIn)
      fr = open('./etc/passwd.txt')
      arrayofLines = fr.readlines()
      numberofLines = len(arrayofLines)
      for line in arrayofLines:
          line = line.strip()
          listFromLine = line.split(':')
          name = listFromLine[0]
          if name == nameIn:
              numberofLines = -1
              passwd = listFromLine[1]
              if passwd == passwdIn:
                  group = listFromLine[2]
                  print("\n登录成功!\n")
                  if name == 'root':
                      print('root登录')
                      rootUI.show()
                      MainWindow.close()
                  else:
                      urName = nameIn
                      mainUI.lineEdit.setText(urName)
                      mainUI.lineEdit_2.setText(group)
                      mainUI.show()
                      MainWindow.close()
              else:
                  QMessageBox.warning(self,
                                      "警告",
                                      "密码错误！",
                                      QMessageBox.Yes)
                  self.lineEdit.setFocus()
      fr.close()
      return 0
  ```

2.  管理员功能实现        

**管理员可以对用户进行增、删、查的操作**

![login](https://github.com/Cool-Y/BIBA-model/blob/master/img/rootUI.PNG)

+ 增加用户的实现
> - 获取管理员输入的用户名、密码和用户等级
> - 将明文密码转换为md5值
> - 判断输入的账户是否已经存在以及是否为空
> - 如果没有问题，将其存入passwd.txt的末尾

    ```python
    def adduser(self):
          print('开始添加')
          name = self.lineEdit_4.text()
          passwd = self.lineEdit_6.text()
          md5 = hashlib.md5()
          md5.update(passwd.encode("utf-8"))
          passwd = md5.hexdigest()
          group = self.comboBox.currentText()
          self.name = name
          if self.euxit():
              if name == '' or passwd == '':
                  QMessageBox.warning(self,
                                      "警告",
                                      "账号和密码不能为空",
                                      QMessageBox.Yes)
                  self.lineEdit.setFocus()
              else:
                  cur_path = os.getcwd()
                  filename = cur_path + '/etc/passwd.txt'
                  fi = open(filename, 'r+')
                  str = name + ':' + passwd + ':' + group + '\n'
                  print('成功增加用户' + str + '\n')
                  fi.seek(0, 2)
                  fi.write(str)
                  fi.close()
          else:
              QMessageBox.warning(self,
                                  "警告",
                                  "用户已存在",
                                  QMessageBox.Yes)
              self.lineEdit.setFocus()
    ```

* 查询已有用户的实现

>从passwd.txt中逐行读出

![login](https://github.com/Cool-Y/BIBA-model/blob/master/img/existUser.PNG)

    ```python
    def readuser(self):
          print('readuser')
          cur_path = os.getcwd()
          filename = cur_path + '/etc/passwd.txt'
          fo = open(filename)
          arrayofLines = fo.readlines()
          names = ''
          for line in arrayofLines:
              line = line.strip()
              listFromLine = line.split(':')
              names = names + listFromLine[0] + '\n'
          self.textEdit.setPlaceholderText(names)
    ```

* 删除用户的实现

>从passwd.txt中逐行读出用户名，并与待删除用户比较，如果相同，则删除该行

    ```python
    def rmuser(self):
          print(1)
          cur_path = os.getcwd()
          filename = cur_path + '/etc/passwd.txt'
          rmName = self.lineEdit.text()
          with open(filename, 'r',encoding="utf-8") as r:
              lines = r.readlines()
              lenl = len(lines)
          with open(filename, 'w',encoding="utf-8") as w:
              for line in lines:
                  l = line.strip()
                  listFromLine = l.split(':')
                  if rmName == listFromLine[0]:
                      print('删除用户' + rmName)
                      continue
                  if line == '\n':
                      print('find换行')
                      line = ''
                  w.write(line)
    ```

3.  普通用户功能实现  

**普通用户可以完成对合法权限文件的读取、增加内容（上写下读）以及创建文件的操作**

![login](https://github.com/Cool-Y/BIBA-model/blob/master/img/normal.PNG)

* 读取文件内容
> 双击文件名   
> 获取选中文件和当前用户的完整性级别   
> 如果用户的级别低于文件，则读取文件内容

   ```python
   def readfile(self):
       dict = self.getGrade()
       fgrade = str(dict[self.file_path])
       ugrade = self.lineEdit_2.text()
       if ugrade >=  fgrade:
           print(ugrade+ ' 正在读取  '+fgrade)
           filename = self.file_path
           print(filename)
           fr = open(filename)
           lines = ''
           arrayofLines = fr.readlines()
           for line in arrayofLines:
               lines += line
           self.textEdit.setText(lines)
           print('读取成功\n')
       else:
           QMessageBox.warning(self,
                               "警告",
                               "您的用户等级太高",
                               QMessageBox.Yes)
           self.lineEdit.setFocus()
   ```

* 增加文件内容

> 双击文件名   
> 获取选中文件和当前用户的完整性级别   
> 如果用户的级别高于文件，则写入文件内容

   ```python
   def writefile(self):
       dict = self.getGrade()
       fgrade = dict[self.file_path]
       ugrade = self.lineEdit_2.text()
       print(ugrade + ' 正在写入  ' + fgrade)
       if ugrade <= fgrade:
           filename = self.file_path
           str = self.textEdit.toPlainText()
           print(str)
           fo = open(filename, 'r+')
           fo.seek(0, 2)
           fo.write(str)
       else:
           QMessageBox.warning(self,
                               "警告",
                               "您的用户等级太低",
                               QMessageBox.Yes)
           self.lineEdit.setFocus()
   ```

* 创建文件

> 获取当前用户名和输入的文件名  
> 在当前路径下创建名为用户名的文件  
> 并对新创建的文件与用户等级建立字典，新文件路径为key，用户等级为value    
> 这个字典方便读写时判断等级高低

   ```python
   def touchfile(self):
       urName = self.lineEdit.text()
       filename = self.lineEdit_4.text()
       cur_path = os.getcwd()
       new_path = os.path.join(cur_path + '/file', urName)
       print(urName)
       if os.path.exists(new_path) == False:
           os.mkdir(new_path)
       os.chdir(new_path)
       fr = open(filename, 'w')
       key = (new_path + '/' + filename).replace('\\', '/')
       fr.close()
       os.chdir(cur_path)
       fa = open('./etc/ac.txt', 'r')
       a = fa.read()
       if a == '':
           dict = {}
       else:
           dict = eval(a)
       dict[key] = self.lineEdit_2.text()
       fr = open('./etc/ac.txt', 'w')
       fr.write(str(dict))
       fr.close()
       fa.close()
   ```

##  五、心得体会：

##  六、改进部分：
