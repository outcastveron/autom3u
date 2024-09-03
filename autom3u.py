import requests
import re
from datetime import datetime

# 获取远程m3u文件内容
def fetch_m3u(url):
    response = requests.get(url)
    return response.text

# 去除emoji的函数
def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # 表情符号
        u"\U0001F300-\U0001F5FF"  # 符号 & 皮肤调色板
        u"\U0001F680-\U0001F6FF"  # 交通 & 地图符号
        u"\U0001F1E0-\U0001F1FF"  # 旗帜 (iOS)
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# 合并多个m3u文件内容并去除包含特定关键字的条目
def merge_m3u(urls, exclude_keywords):
    merged_content = "#EXTM3U\n"
    for url in urls:
        m3u_content = fetch_m3u(url)
        for line in m3u_content.split('\n'):
            if not any(keyword in line for keyword in exclude_keywords):
                line = remove_emoji(line)
                merged_content += line + '\n'
    return merged_content

# 保存合并后的内容到文件
def save_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

# 示例URL列表
urls = [
    "https://raw.githubusercontent.com/Cx4x/Cxxx/main/TKTY.m3u",
    "https://raw.githubusercontent.com/Kyawtgvd/iptv/main/sport.m3u",
    # 添加更多URL
]

# 合并并保存，去除包含“订阅问客服”和“央视卫视”的条目，并去除所有emoji
exclude_keywords = ["订阅问客服", "央视卫视"]
merged_content = merge_m3u(urls, exclude_keywords)
save_to_file(merged_content, "merged_sport.m3u")

# 添加更新时间
with open("merged_sport.m3u", "a", encoding="utf-8") as file:
    now = datetime.now()
    file.write(f"# 更新日期: {now.strftime('%Y-%m-%d')}\n")
    file.write(f"# 更新时间: {now.strftime('%H:%M:%S')}\n")

print("任务运行完毕，合并后的m3u文件已保存为 merged_sport.m3u")
