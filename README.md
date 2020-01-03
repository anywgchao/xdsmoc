xundong（密码获取工具）介绍：
大多数操作系统、用户喜欢将连接服务端密码保存在本地计算机上。每个软件都使用不同的方式独立存储密码，常见类型包括(自定义算法、数据库等方式)。 该软件可以快速获取电脑中存储的密码，例如:WIFI密码、浏览器中存储的网站后台密码（大多数人喜欢缓存）、邮箱密码、VNC、FTP、系统密码（windows 2008以前版本）、其它软件密码等。

软件其特点是：
1、无痕：在内存中解释，而不需要在硬盘中缓存临时文件，避免产生垃圾文件。
2、灵活，只需U盘插入，点击一下即可捕获该电脑中存储的常用密码。
3、效率：快速读取分析系统中软件存储密码并进行解密，节约时间。
4、兼容性高：支持Windows全系列，部分Linux/Mac操作系统及软件。


使用说明：
email
xd.exe mails -oJ -quiet

databases
xd.exe databases -oJ -quiet

wifi
xd.exe wifi -oJ -quiet

browsers
xd.exe browsers -oJ -quiet

sysadminF
xd.exe sysadmin -oJ -quiet

chats
xd.exe chats -oJ -quiet

games
xd.exe games -oJ -quiet

git
xd.exe git -oJ -quiet

mails
xd.exe mails -oJ -quiet

maven
xd.exe maven -oJ -quiet

memory
xd.exe memory -oJ -quiet

multimedia
xd.exe multimedia -oJ -quiet

php
xd.exe php -oJ -quiet

svn
xd.exe svn -oJ -quiet

windows
xd.exe windows -oJ -quiet

修改内容
1、software->browsers->ucbroswer  模块重新开发
2、software->sysadmin->vnc  模块重新开发
3、config-winstructure.py 修改版本兼容问题


程序简介：
当你插入U盘时，自动复制到指定的目录下（默认是我的文档下）

程序特色：
1，操作过程完全看不见（当然复制是否完成也一样）
2，支持自定义格式（无限制）
3，支持记录U盘更新文件进行复制

使用说明：
全局快捷键（Alt+F7），可以进入设置界面