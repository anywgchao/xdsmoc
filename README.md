<!--
 * @Author: Daboluo
 * @Date: 2019-11-21 17:30:32
 * @LastEditTime : 2020-01-03 15:59:30
 * @LastEditors  : Do not edit
 * @Description:
 -->

# xdsmoc（主机密码获取工具）

----
大多数操作系统、用户喜欢将连接服务端密码保存在本地计算机上。每个软件都使用不同的方式独立存储密码，常见类型包括(自定义算法、数据库等方式)。 该软件可以快速获取电脑中存储的密码，例如:WIFI密码、浏览器中存储的网站后台密码（大多数人喜欢缓存）、邮箱密码、VNC、FTP、系统密码（windows 2008以前版本）、其它软件密码等。

## 软件其特点

1、无痕：在内存中解释，而不需要在硬盘中缓存临时文件，避免产生垃圾文件。
2、灵活，只需U盘插入，点击一下即可捕获该电脑中存储的常用密码。
3、效率：快速读取分析系统中软件存储密码并进行解密，节约时间。
4、兼容性高：支持Windows全系列，部分Linux/Mac操作系统及软件。

### 软件支持

|                                      | Windows                                                                                                                                                                                                                                                                                                                                                                       | Linux                                                                                                                                                                                                                      | Mac                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Browsers                             | 7Star</br> Amigo</br> BlackHawk</br> Brave</br> Centbrowser</br> Chedot</br> Chrome Canary</br> Chromium</br> Coccoc</br> Comodo Dragon</br> Comodo IceDragon</br> Cyberfox</br> Elements Browser</br> Epic Privacy Browser</br> Firefox</br> Google Chrome</br> Icecat</br> K-Meleon</br> Kometa</br> Opera</br> Orbitum</br> Sputnik</br> Torch</br> Uran</br> Vivaldi</br> | Chrome</br> Firefox</br> Opera                                                                                                                                                                                             | Chrome</br> Firefox     |
| Chats                                | Pigdin</br> Psi</br> Skype                                                                                                                                                                                                                                                                                                                                                    | Pigdin</br> Psi                                                                                                                                                                                                            |                         |
| Databases                            | DBVisualizer</br> Postgresql</br> Robomongo</br> Squirrel</br> SQLdevelopper                                                                                                                                                                                                                                                                                                  | DBVisualizer</br> Squirrel</br> SQLdevelopper                                                                                                                                                                              |                         |
| Games                                | GalconFusion</br> Kalypsomedia</br> RogueTale</br> Turba                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                            |                         |
| Git                                  | Git for Windows                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                            |                         |
| Mails                                | Outlook</br> Thunderbird                                                                                                                                                                                                                                                                                                                                                      | Clawsmail</br> Thunderbird                                                                                                                                                                                                 |                         |
| Maven                                | Maven Apache</br>                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                            |                         |
| Dumps from memory                    | Keepass</br> Mimikatz method                                                                                                                                                                                                                                                                                                                                                  | System Password                                                                                                                                                                                                            |                         |
| Multimedia                           | EyeCON</br>                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                            |                         |
| PHP                                  | Composer</br>                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                            |                         |
| SVN                                  | Tortoise                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                            |                         |
| Sysadmin                             | Apache Directory Studio</br> CoreFTP</br> CyberDuck</br> FileZilla</br> FileZilla Server</br> FTPNavigator</br> OpenSSH</br> OpenVPN</br> KeePass Configuration Files (KeePass1, KeePass2)</br> PuttyCM</br>RDPManager</br> VNC</br> WinSCP</br> Windows Subsystem for Linux                                                                                                  | Apache Directory Studio</br> AWS</br>  Docker</br> Environnement variable</br> FileZilla</br> gFTP</br> History files</br> Shares </br> SSH private keys </br> KeePass Configuration Files (KeePassX, KeePass2) </br> Grub |                         |
| Wifi                                 | Wireless Network                                                                                                                                                                                                                                                                                                                                                              | Network Manager</br> WPA Supplicant                                                                                                                                                                                        |                         |  |  |
| Wifi                                 | Wireless Network                                                                                                                                                                                                                                                                                                                                                              | Network Manager</br> WPA Supplicant                                                                                                                                                                                        |                         |
| Internal mechanism passwords storage | Autologon</br> MSCache</br> Credential Files</br> Credman </br> DPAPI Hash </br> Hashdump (LM/NT)</br> LSA secret</br> Vault Files                                                                                                                                                                                                                                            | GNOME Keyring</br> Kwallet</br> Hashdump                                                                                                                                                                                   | Keychains</br> Hashdump |

## 快速使用说明

* email

    ```C++
    xd.exe mails -oJ -quiet
    ```

* databases

    ```C++
    xd.exe databases -oJ -quiet
    ```

* wifi

    ```C++
    xd.exe wifi -oJ -quiet
    ```

* browsers

    ```C++
    xd.exe browsers -oJ -quiet
    ```

* sysadmin

    ```C++
    xd.exe sysadmin -oJ -quiet
    ```

* chats

    ```C++
    xd.exe chats -oJ -quiet
    ```

* games

    ```C++
    xd.exe games -oJ -quiet
    ```

* git

    ```C++
    xd.exe git -oJ -quiet
    ```

* mails

    ```C++
    xd.exe mails -oJ -quiet
    ```

* maven

    ```C++
    xd.exe maven -oJ -quiet
    ```

* memory

    ```C++
    xd.exe memory -oJ -quiet
    ```

* multimedia

    ```C++
    xd.exe multimedia -oJ -quiet
    ```

* php

    ```C++
    xd.exe php -oJ -quiet
    ```

* svn

    ```C++
    xd.exe svn -oJ -quiet
    ```

* windows

    ```C++
    xd.exe windows -oJ -quiet
    ```
