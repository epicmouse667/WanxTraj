import os
import json
from pathlib import Path

def construct_dataset(base_dir):
    # 初始化结果列表
    dataset = []
    
    # 读取prompt文件
    with open(os.path.join(base_dir, 'prompt.txt'), 'r') as f:
        prompts = f.readlines()
    
    # 获取视频文件列表
    video_dir = os.path.join(base_dir, 'videos')
    tracking_dir = os.path.join(base_dir, 'tracking')
    
    # 遍历视频文件
    for video_file in sorted(os.listdir(video_dir)):
        if video_file.endswith('.mp4'):
            # 获取对应的tracking文件
            tracking_file = video_file.replace('.mp4', '_tracking.mp4')
            
            # 确保tracking文件存在
            if os.path.exists(os.path.join(tracking_dir, tracking_file)):
                # 获取对应的prompt（假设prompt.txt中的顺序与视频文件顺序一致）
                video_index = int(video_file.split('.')[0]) - 1
                if video_index < len(prompts):
                    text = prompts[video_index].strip()
                    
                    # 创建数据条目
                    entry = {
                        "file_path": f"videos/{video_file}",
                        "control_file_path": f"tracking/{tracking_file}",
                        "text": text,
                        "type": "video"
                    }
                    dataset.append(entry)
    
    return dataset

def main():
    # 设置基础目录
    base_dir = "/project/pi_chuangg_umass_edu/zixin/datasets/DaS_validation/motion_transfer"
    
    # 构建数据集
    dataset = construct_dataset(base_dir)
    
    # 将结果写入JSON文件
    output_file = os.path.join(base_dir, 'metadata.json')
    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=2)
    
    print(f"数据集已生成并保存到: {output_file}")

if __name__ == "__main__":
    main()
