<!--
 * @Author: Daboluo
 * @Date: 2019-11-21 17:30:32
 * @LastEditTime: 2020-06-15 20:53:11
 * @LastEditors: Do not edit
 * @Description:
 -->

## xdsmoc PassView Toolkit

----
xdsmoc-toolkit是一款方便实用，功能强大的多功能密码查看工具。它以简单的方式恢复所有丢失或忘记的密码。大多数用户喜欢将连接服务端密码保存在本地计算机上。每个软件都使用不同的方式独立存储密码，常见类型包括(自定义算法、数据库等方式)。 该软件可以快速获取电脑中存储的密码，例如:包括即时通讯软件、Chrome网页浏览器、Firefox网页浏览器、Microsoft Edge、Internet Explorer、Microsoft Outlook、Windows的网络密码、无线网络密钥、邮箱密码、VNC远程连接、FTP远程连接、系统密码（windows 2008以前版本）、其它软件密码等等。

## 软件其特点

---

* 无痕：在内存中解释，而不需要在硬盘中缓存临时文件，避免产生垃圾文件。
* 灵活，放入U盘中，只需U盘插入电脑，点击一下即可捕获该电脑中存储的常用密码。
* 效率：快速读取分析系统中软件存储密码并进行解密，节约时间。
* 兼容性高：支持Windows全系列，部分Linux/Mac操作系统及软件。
* 工具定期更新，支持更多新版本软件。
* 命令行方式简单易用。

### 软件支持

|              | Windows 系统                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Linux 系统                                       | Mac 系统                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | ------------------------ |
| 浏览器       | Internet Explorer（版本4.0 - 11.0）</br></br> Google Chrome（引擎系列）：</br> 360极速浏览器</br> UC浏览器</br> 7Star</br> Amigo</br> Brave</br> Centbrowser</br> Chedot</br> Chrome Canary</br> Chromium</br> Coccoc</br> Comodo Dragon</br>  Elements Browser</br> Epic Privacy Browser</br> Google Chrome</br> Kometa</br> Opera</br> Orbitum</br> Sputnik</br> Torch</br> Uran</br> Vivaldi</br> Chrome</br> Firefox</br> yandexBrowser</br></br> Firefox（引擎系列）：Firefox(版本17 - 最新）</br> BlackHawk</br> Icecat</br> K-Meleon</br> Comodo IceDragon</br> Cyberfox</br> | Chrome</br> Firefox</br> Opera                   | Chrome</br> Firefox</br> |
| 即时通讯     | Pigdin</br> Psi</br> Skype                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Pigdin</br> Psi                                  |                          |
| 数据库工具   | DBVisualizer</br> Postgresql</br> Robomongo</br> Squirrel</br> SQLdevelopper                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | DBVisualizer</br> Squirrel</br> SQLdevelopper    |                          |
| 开发工具     | Git for Windows</br> SVN Tortoise   </br>  Maven Apache</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                  |                          |
| 邮件客户端   | Outlook 2003</br> Outlook 2007</br> Outlook 2010</br> Outlook 2013</br> Outlook 2016</br> Outlook 2019</br> Thunderbird(全版本)                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Clawsmail</br> Thunderbird                       |                          |
| FTP Client   | CoreFTP</br> CyberDuck</br> FileZilla</br> FileZilla Server</br> FTPNavigator</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | FileZilla</br> gFTP</br>                         |                          |
| RDP client   | RDPManager</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                  |                          |
| VPN Client   | OpenVPN</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                  |                          |
| VNC Client   | UltraVNC</br> TightVNC</br>  RealVNC</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                  |                          |
| SSH Client   | OpenSSH</br> PuttyCM</br> WinSCP</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SSH login Listen                                 |                          |
| 内存导出     | Keepass</br> Mimikatz method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | System Password                                  |                          |
| Passtools    | KeePass Configuration Files (KeePass1, KeePass2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | KeePass Configuration Files (KeePassX, KeePass2) |                          |
| WIFI密码     | Wireless Network                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Network Manager</br> WPA Supplicant              |                          |  |  |
| 系统内部密码 | Autologon</br> MSCache</br> Credential Files</br> Credman </br> DPAPI Hash </br> Hashdump (LM/NT)</br> LSA secret</br> Vault Files </br>备注：密明文密码导出仅支持windows2008以前版本                                                                                                                                                                                                                                                                                                                                                                                                | GNOME Keyring</br> Kwallet</br> Hashdump         | Keychains</br> Hashdump  |

## 快速使用说明

---

### windows 工具

* [[操作系统支持：Win10、Win8、Win7、XP (SP3)、Win2008r2、Win2012、Win2016]]

* 邮件客户端 PassView

    ```C++
    xdsmoc-mails.exe mails -oJ -quiet
    ```

* databases PassView

    ```C++
    xdsmoc-database.exe databases -oJ -quiet
    ```

* WIFI PassView

    ```C++
    > xdsmoc-wifi.exe wifi -oJ -quiet
    ```

* 浏览器 PassView

    ```C++
    xdsmoc-browsers.exe browsers -oJ -quiet
    ```

* VNC PassView

    ```C++
    xdsmoc-vnc.exe vnc -oJ -quiet
    ```

* FTP PassView

    ```C++
    xdsmoc-ftp.exe ftp -oJ -quiet
    ```

* chats PassView

    ```C++
    xdsmoc-chats.exe chats -oJ -quiet
    ```

* ssh PassView

    ```C++
    xdsmoc-ssh.exe ssh -oJ -quiet
    ```

* VPN PassView

    ```C++
    xdsmoc-vpn.exe vpn -oJ -quiet
    ```

* RDP PassView

    ```C++
    xdsmoc-rdp.exe rdp -oJ -quiet
    ```

* maven/svn/git

    ```C++
    xdsmoc-devel.exe devel -oJ -quiet
    ```

* memory

    ```C++
    xdsmoc-memory.exe memory -oJ -quiet
    ```

* windows

    ```C++
    xdsmoc-windows.exe windows -oJ
    ```

---

### Linux 工具

* [[操作系统支持：CentOS6+ Ubuntu12+]]

* Linux 密码捕获
1、启动守护进程xundong_ssh_listen，如果有账号登陆，则记录到/tmp/pwd-kit.txt 文件中

    ```C++
    ./xdsmoc_ssh_listen -d -o /tmp/pwd-kit.txt
    ```

其它工具
<https://github.com/n1nj4sec/mimipy>
mimikatz
它仅需两条密码就可以抓取现登录用户的账密
privilege::debug    //提权
sekurlsa::logonpasswords
下面这张是在win 7 32位专业版的测试

部分命令介绍
::    显示命令用法
sekurlsa
wdigest    去内存里读密码
kerberos     域环境下读取域账号密码
logonpasswords    内存里可读的都读出来
process    读取当前进程
pth    通过hash 值直接登录
kerberos    域环境下的命令
process   进程模块
list    列出当前操作系统所有进程
exports/imports    导入导出进程列表
start/stop    启动或结束进程
suspend/resume    挂起、冻结或恢复进程
lsadump    sam 数据库操作
sam    读取sam 数据库的账密
hash    当前登录账号的NTLM、LM 等hash 值
ts    终端服务
multirdp    默认win 只允许一个活动的登录会话，如果管理员现在登录着系统，而我们远程登录系统的话，那当前本地登录的会话会被注销。而这个命令可以为系统打上一个“补丁”这样就可以同时登陆一个账号了。
event    系统日志模块
clear    清除操作系统安全性的日志
drop    不在产生新的日志
misc    杂项
cmd/taskmgr/regedit    启动他们
token
whoami

顺便提句，mimikatz 的Linux 平台仿造版本mimipenguin（由@HunterGregal 开发），增强了不少功能。
mimipenguin需要root权限运行，通过检索内存、/etc/shadow文件等敏感区域查找信息进行计算，从而提取出系统明文密码。
mimipenguin现支持Kali、Ubuntu Desktop、XUbuntu Desktop、VSFTPd、Apache2、openssh-server等系统下使用。
mimipenguin的Github地址是 <https://github.com/huntergregal/mimipenguin>
# xdsmoc
