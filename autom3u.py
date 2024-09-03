import requests
from datetime import datetime

# 获取远程m3u文件内容
def fetch_m3u(url):
    response = requests.get(url)
    return response.text

# 合并多个m3u文件内容
def merge_m3u(urls):
    merged_content = "#EXTM3U\n"
    for url in urls:
        m3u_content = fetch_m3u(url)
        merged_content += m3u_content
    return merged_content

# 保存合并后的内容到文件
def save_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

# 示例URL列表
urls = [
    "https://raw.githubusercontent.com/Kyawtgvd/iptv/main/sport.m3u",
    "https://raw.githubusercontent.com/AberTown/V_Zone.m3u/main/V_Sport.m3u",
    # 添加更多URL
]

# 合并并保存
merged_content = merge_m3u(urls)
save_to_file(merged_content, "merged_sport.m3u")

# 添加更新时间
with open("merged_sport.m3u", "a", encoding="utf-8") as file:
    now = datetime.now()
    file.write(f"# 更新日期: {now.strftime('%Y-%m-%d')}\n")
    file.write(f"# 更新时间: {now.strftime('%H:%M:%S')}\n")

print("任务运行完毕，合并后的m3u文件已保存为 merged_sport.m3u")
