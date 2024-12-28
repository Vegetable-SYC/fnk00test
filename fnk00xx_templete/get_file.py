import sys  # 添加此行
import subprocess
import pkg_resources

# 检查是否安装了 python-docx 库
required = {'python-docx'}
installed = {pkg.key for pkg in pkg_resources.working_set}

# 如果没有安装 python-docx，则进行安装
if not required.issubset(installed):
    print("未检测到 python-docx 库，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
else:
    print("已检测到 python-docx 库，跳过安装。")

from docx import Document

def extract_first_level_headings(doc_path, output_file):
    # 打开 Word 文档
    doc = Document(doc_path)
    
    # 存储一级标题
    first_level_headings = []
    
    # 遍历文档中的所有段落
    for paragraph in doc.paragraphs:
        # 检查段落的样式是否为一级标题
        if paragraph.style.name == 'Heading 1':
            heading_text = paragraph.text
            
            # 去掉 "Chapter" 字样
            heading_text = heading_text.replace("Chapter", "").strip()
            
            # 去掉问号
            heading_text = heading_text.replace("?", "")
            
            # 将空格替换为下划线
            heading_text = heading_text.replace(" ", "_")
            
            # 将引号替换为下划线
            heading_text = heading_text.replace("'", "_")
            
            # 添加到列表中
            first_level_headings.append(heading_text)
    
    # 将结果写入输出文件
    with open(output_file, 'w') as file:
        for heading in first_level_headings:
            file.write(heading + '\n')

# 使用示例
doc_path = 'C:/Users/freenove-14/Desktop/fnk00xx_templete/FNK0054_Freenove_Processing_for_RaspberryPi_20240904.docx'  # 替换为你的 Word 文档的路径
output_file = 'headings.txt'     # 输出文件名

extract_first_level_headings(doc_path, output_file)
print(f"一级标题已提取并保存到 {output_file} 文件中。")