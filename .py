import json
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# 示例 JSON 数据
json_data = '''
[
    {
        "APP_TYPE": "1229999",
        "DETAIL": {"nameinfo": [{"name": "刘婵女士"}]},
        "IDENTITY_VALUE": "18627855112",
        "SRC_ADDRESS": "智慧e谷大楼(5楼)",
        "TABLE_SOURCE": "shga_wa.ods_nb_tab_goods",
        "FIRST_TIME": "1562126476",
        "LAST_TIME": "1562557677"
    },
    {
        "APP_TYPE": "1240002",
        "DETAIL": {"nameinfo": [{"name": "蔡达芳"}]},
        "IDENTITY_VALUE": "18608531229",
        "SRC_ADDRESS": "贵州省安顺市普定县城关镇红旗路新天地",
        "TABLE_SOURCE": "shga_wa.ods_nb_app_icpoof_delivery",
        "FIRST_TIME": "1598073511",
        "LAST_TIME": "1598073511"
    }
]
'''

# 转换UNIX时间为可读格式
def format_time(unix_time):
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')

# 创建图片
def create_image(data):
    width, height = 800, 300 * len(data)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    y_offset = 20
    for i, record in enumerate(data):
        draw.text((20, y_offset), f"记录 {i + 1}", fill="black", font=font)
        draw.text((20, y_offset + 20), f"APP_TYPE: {record['APP_TYPE']}", fill="black", font=font)
        draw.text((20, y_offset + 40), f"姓名: {record['DETAIL']['nameinfo'][0]['name']}", fill="black", font=font)
        draw.text((20, y_offset + 60), f"手机号: {record['IDENTITY_VALUE']}", fill="black", font=font)
        draw.text((20, y_offset + 80), f"地址: {record['SRC_ADDRESS']}", fill="black", font=font)
        draw.text((20, y_offset + 100), f"数据来源: {record['TABLE_SOURCE']}", fill="black", font=font)
        draw.text((20, y_offset + 120), f"首次时间: {format_time(record['FIRST_TIME'])}", fill="black", font=font)
        draw.text((20, y_offset + 140), f"最后时间: {format_time(record['LAST_TIME'])}", fill="black", font=font)
        y_offset += 200

    return image

# 加载 JSON 数据
data = json.loads(json_data)

# 生成图片
img = create_image(data)
img.show()
img.save("output_visual.png")
