import os
from datetime import datetime as dt
import json

    
def Read_config():
    global game_path, copy_path, backup_path
    with open('config.json', 'r') as f:
        config = json.load(f)
        game_path = config['game_path']
        copy_path = config['copy_path']
        backup_path = config['paste_path']
        
def Backup():
    now = dt.now().strftime('%Y-%m-%d-%H-%M')
    file_name = '/'.join((backup_path, now))
    try:
        # 如果目录不存在，则创建它
        os.makedirs(file_name)
        print(f"目录 {file_name} 已成功创建。")
    except FileExistsError:
        # 如果目录已存在，则捕获异常并打印消息
        print(f"目录 {file_name} 已存在，无需创建。")
    except Exception as e:
        # 捕获其他可能的异常，并打印错误消息
        print(f"创建目录时发生错误: {e}")
    command = 'xcopy "{0}" "{1}" /y /e /s'.format(copy_path, file_name)
    os.system(command)
    
def Restore_backup(file_name=None):
    folders = [f for f in os.listdir(backup_path)]
    if len(folders) == 0:
        print('没有本地备份文件')
        return
    else:
        file_name = input('请输入要还原的日期(格式：2023-05-01),回车默认还原最新的备份')
    try:
        file = backup_path + max(folders) if file_name is None else backup_path + file_name
    except:
        print('备份名称错误，请重新输入\f')
        return
    command = 'xcopy "{0}" "{1}" /y /e /s'.format(file, copy_path)
    os.system(command)
    
def Start_game():
    print('\f猎人：荒野的召唤\n启动！！！')
    command = 'start "" "{0}"'.format(game_path)
    os.system(command)
    
    
if __name__ == '__main__':
    Read_config()
    while True:
        order = input('1.启动游戏\t2.备份并启动游戏\n3.手动备份\t4.还原备份\n5.退出程序\n请输入指令:')
        if order == "1":
            Start_game()
            break
        elif order == "2":
            Backup()
            Start_game()
            break
        elif order == "3":
            Backup()
        elif order == "4":
            Restore_backup()
        elif order == "5":
            break
        else:
            print('指令错误,请重新输入')