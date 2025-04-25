from PIL import Image, ImageDraw, ImageFont
import os

# 图像参数
width, height = 683, 512
background_color = (0, 0, 0)  # 黑色背景
text = "游戏暂停"
font_size = 48  # 可调整大小

# 尝试使用支持中文的字体（例如：SimHei、SimSun、Arial Unicode MS 等）
# 请根据你的系统安装字体路径进行替换
possible_fonts = [
    "C:/Windows/Fonts/simhei.ttf",             # Windows 黑体
    "/System/Library/Fonts/STHeiti Medium.ttc", # macOS 中文字体
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc" # Linux 中文字体
]

font_path = None
for path in possible_fonts:
    if os.path.exists(path):
        font_path = path
        break

if not font_path:
    raise FileNotFoundError("未找到支持中文的字体，请手动指定字体路径。")

font = ImageFont.truetype(font_path, font_size)

# 创建图像
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 计算文本位置（居中）
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

# 绘制白色文字
draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

# 保存为 BMP 文件
output_path = "游戏暂停.bmp"
image.save(output_path, format="BMP")
print(f"图片已保存为：{output_path}")
