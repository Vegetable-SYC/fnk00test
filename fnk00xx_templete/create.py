import os

def create_rst_files_and_folders(file_list_path, rst_output_dir, folder_output_dir):
    # 确保输出目录存在
    os.makedirs(rst_output_dir, exist_ok=True)
    os.makedirs(folder_output_dir, exist_ok=True)

    # 读取文件名列表
    with open(file_list_path, 'r', encoding='utf-8') as file:
        file_names = file.read().splitlines()

    for file_name in file_names:
        # 清理文件名，去除多余的空格
        file_name = file_name.strip()
        
        if not file_name:  # 跳过空行
            continue
        
        # 创建 .rst 文件
        rst_file_path = os.path.join(rst_output_dir, f"{file_name}.rst")
        with open(rst_file_path, 'w', encoding='utf-8') as rst_file:
            # 写入统一标题
                title = "##############################################################################\nChapter\n##############################################################################\n\n"
                rst_file.write(title)

        # 创建对应的文件夹
        folder_path = os.path.join(folder_output_dir, file_name)
        os.makedirs(folder_path, exist_ok=True)  # 创建文件夹

# 使用示例
file_list_path = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/headings.txt'  # 包含文件名的文本文件路径
rst_output_dir = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/fnk00xx/docs/source/fnk00xx/codes/tutorial'        # .rst 文件输出目录
folder_output_dir = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/fnk00xx/docs/source/fnk00xx/codes/_static/imgs'       # 文件夹输出目录

create_rst_files_and_folders(file_list_path, rst_output_dir, folder_output_dir)

print("对应的 .rst 文件和文件夹已创建。")