import os
import json
from pathlib import Path

def construct_dataset(base_dir, prompt_dir):
    # 初始化结果列表
    dataset = []
    
    # 获取视频文件列表
    video_dir = os.path.join(base_dir, 'videos')
    tracking_dir = os.path.join(base_dir, 'tracking')
    
    # 遍历视频文件
    for video_file in sorted(os.listdir(video_dir)):
        if video_file.endswith('.mp4'):
            # 获取vid（去除扩展名）
            vid = os.path.splitext(video_file)[0]
            # control_file_path
            control_file = f"{vid}_tracking.mp4"
            control_file_path = os.path.join(tracking_dir, control_file)
            # prompt文件路径
            prompt_file_path = os.path.join(prompt_dir, f"{vid}.txt")
            print(control_file_path, prompt_file_path)
            # 检查tracking和prompt文件是否存在
            if os.path.exists(control_file_path) and os.path.exists(prompt_file_path):
                # 读取prompt内容
                with open(prompt_file_path, 'r', encoding='utf-8') as pf:
                    text = pf.read().strip()
                # 创建数据条目
                entry = {
                    "file_path": f"videos/{video_file}",
                    "control_file_path": f"tracking/{vid}_tracking.mp4",
                    "text": text,
                    "type": "video"
                }
                dataset.append(entry)
    
    return dataset

def main():
    # 设置基础目录
    base_dir = "/nobackup/users/kentang/zixin/iclr2026/data/Motion-X++/tracking/idea400_light"
    prompt_dir = "/nobackup/users/kentang/zixin/iclr2026/data/Motion-X++/text/idea400"  # 这里可以自定义
    
    # 构建数据集
    dataset = construct_dataset(base_dir, prompt_dir)
    
    # 将结果写入JSON文件
    output_file = os.path.join(base_dir, 'metadata.json')
    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=2)
    
    print(f"数据集已生成并保存到: {output_file}")

if __name__ == "__main__":
    main()
