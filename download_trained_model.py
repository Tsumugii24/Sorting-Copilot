import sys
import os
import wget

from pathlib import Path

ROOT_PATH = sys.path[0]  # 项目根目录

fonts_list = ["SimSun.ttf", "TimesNewRoman.ttf", "malgun.ttf"]  # 字体列表
models_list = ["yolov3.pt", "yolov5.pt", "yolov6.pt", "yolov8.pt", "yolov9c.pt", "yolov9e.pt", "vision-transformers.pt"] # 模型列表
fonts_directory_path = Path(ROOT_PATH, "fonts")  # 字体存放目录
models_directory_path = Path(ROOT_PATH, "models")  # 模型存放目录

data_url_dict = {
    "SimSun.ttf": "https://raw.githubusercontent.com/Tsumugii24/Typora-images/main/files/SimSun.ttf",
    "TimesNewRoman.ttf": "https://raw.githubusercontent.com/Tsumugii24/Typora-images/main/files/TimesNewRoman.ttf",
    "malgun.ttf": "https://raw.githubusercontent.com/Tsumugii24/Typora-images/main/files/malgun.ttf",
}

model_url_dict = {
    "yolov3.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov3-based.pt",
    "yolov5.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov5-based.pt",
    "yolov6.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov6-based.pt",
    "yolov8.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov8-based.pt",
    "yolov9c.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov9c-based.pt",
    "yolov9e.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/yolov9e-based.pt",
    "vision-transformers.pt": "https://huggingface.co/Tsumugii/Sorting-Copilot/resolve/main/vision-transformers.pt",
}

# 判断字体文件是否存在
def is_fonts(fonts_dir):
    if fonts_dir.is_dir():
        # 如果本地字体库存在
        local_font_list = os.listdir(fonts_dir)  # 本地字体库

        font_diff = list(set(fonts_list).difference(set(local_font_list)))

        if font_diff != []:
            # 缺失字体
            download_fonts(font_diff)  # 下载缺失的字体
        else:
            print(f"{fonts_list}[bold green]Required fonts already downloaded！[/bold green]")
    else:
        # 本地字体库不存在，创建字体库
        print("[bold red]Local fonts library does not exist, creating now...[/bold red]")
        download_fonts(fonts_list)  # 创建字体库
        
# 判断模型文件是否存在
def is_models(models_dir):
    if models_dir.is_dir():
        # 如果本地模型库存在
        local_model_list = os.listdir(models_dir)  # 本地模型库

        model_diff = list(set(models_list()).difference(set(local_model_list)))

        if model_diff != []:
            # 缺失模型
            download_models(model_diff)  # 下载缺失的模型
        else:
            print(f"{models_list}[bold green]Required models already downloaded！[/bold green]")
    else:
        # 本地模型库不存在，创建模型库
        print("[bold red]Local models library does not exist, creating now...[/bold red]")
        download_models(models_list)  # 创建模型库

# 下载字体
def download_fonts(font_diff):
    global font_name

    for k, v in data_url_dict.items():
        if k in font_diff:
            font_name = v.split("/")[-1]  # 字体名称
            fonts_directory_path.mkdir(parents=True, exist_ok=True)  # 创建本地字体目录

            font_file_path = f"{ROOT_PATH}/fonts/{font_name}"  # 字体路径
            # 下载字体文件
            wget.download(v, font_file_path)
            print("Downloading required font files")

# 下载模型
def download_models(model_diff):
    global model_name

    for k, v in model_url_dict.items():
        if k in model_diff:
            model_name = v.split("/")[-1]  # 模型名称
            models_directory_path.mkdir(parents=True, exist_ok=True)  # 创建本地模型目录

            model_file_path = f"{ROOT_PATH}/models/{model_name}"  # 模型路径
            # 下载模型文件
            wget.download(v, model_file_path)
            print("Downloading required model weight files")


is_fonts(fonts_directory_path)
is_models(models_directory_path)