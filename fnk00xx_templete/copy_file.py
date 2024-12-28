import os
import shutil

def copy_and_rename_folder(source_folder, destination_folder):
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹 '{source_folder}' 不存在。")
        return

    # 复制文件夹
    shutil.copytree(source_folder, destination_folder)
    print(f"文件夹 '{source_folder}' 已成功复制到 '{destination_folder}'。")

# 使用示例
source_folder = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/fnk_templete'          # 替换为要复制的源文件夹路径
destination_folder = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/fnk00xx'      # 替换为目标文件夹路径（重命名后的文件夹）

copy_and_rename_folder(source_folder, destination_folder)
