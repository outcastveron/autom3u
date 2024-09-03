import requests
from datetime import datetime

# 获取远程m3u文件内容
def fetch_m3u(url):
    response = requests.get(url)
    return response.text

# 删除包含特定关键字的条目及其下一条目
def remove_entries(content, keywords):
    lines = content.splitlines()
    filtered_lines = []
    skip_next = False
    for line in lines:
        if skip_next:
            skip_next = False
            continue
        if any(keyword in line for keyword in keywords):
            skip_next = True
            continue
        filtered_lines.append(line)
    return "\n".join(filtered_lines)

# 合并多个m3u文件内容
def merge_m3u(urls, keywords):
    merged_content = "#EXTM3U\n"
    for url in urls:
        m3u_content = fetch_m3u(url)
        m3u_content = remove_entries(m3u_content, keywords)
        merged_content += m3u_content
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

# 关键字列表
keywords = ["订阅问客服", "央视卫视"]

# 合并并保存
merged_content = merge_m3u(urls, keywords)
save_to_file(merged_content, "merged_sport.m3u")

# 添加更新时间
with open("merged_sport.m3u", "a", encoding="utf-8") as file:
    now = datetime.now()
    file.write(f"# 更新日期: {now.strftime('%Y-%m-%d')}\n")
    file.write(f"# 更新时间: {now.strftime('%H:%M:%S')}\n")

print("任务运行完毕，合并后的m3u文件已保存为 merged_sport.m3u")
