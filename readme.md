![   !image   图像](https://github.com/user-attachments/assets/e032dfe7-9408-43db-b690-6cbb3ab2ff96)这是一个用于备份《猎人：荒野的召唤》的工具，它会在双击启动demo.exe时自动备份存档到backups文件夹的指定日期（例如：2024-10-15-22-10）的文件夹内。

使用前请到config文件里先配置好以下参数：
"game_path":游戏的启动文件路径，一般在steam目录里（"steam/steamapps/common/theHunterCotW/theHunterCotW_F.exe"）;
"copy_path":游戏存档目录位置，一般在c盘（"C:/Users/Documents/Avalanche Studios"）;
"paste_path":存档本地备份位置，一般填绝对路径，默认在此目录下的"backups"文件夹内.

此工具是用python写的，源码在此目录下的demo.py中可看。
![   !Uploading image.png…]()
