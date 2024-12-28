@echo off
chcp 65001 >nul 2>nul
echo 执行该脚本前，请先确保三个脚本中的文件路径正确，按下任意键开始执行
pause >nul

echo 正在从word文档中提取标题...
python get_file.py
echo 执行完毕。

echo 正在复制templete...
python copy_file.py
echo 执行完毕。

echo 正在创建新的文件夹以及rst文件...
python create.py
echo 执行完毕。

echo 所有脚本执行完毕。
pause
