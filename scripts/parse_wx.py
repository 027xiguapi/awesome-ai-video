#!/usr/bin/env python3
"""
解析微信导出的文章文件
提取标题、内容、链接等信息
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

def parse_wx_file(wx_file_path):
    """解析wx文件"""
    try:
        with open(wx_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 根据实际格式调整解析逻辑
        articles = []

        print(f"✓ 成功读取文件: {wx_file_path}")
        print(f"✓ 文件大小: {len(content)} 字符")

        return articles
    except Exception as e:
        print(f"✗ 解析失败: {e}")
        return []

def save_parsed_data(articles, output_dir):
    """保存解析后的数据"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"parsed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"✓ 数据已保存到: {output_file}")
    return output_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python parse_wx.py <wx_file_path> [output_dir]")
        sys.exit(1)

    wx_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "data/parsed"

    articles = parse_wx_file(wx_file)
    save_parsed_data(articles, output_dir)
