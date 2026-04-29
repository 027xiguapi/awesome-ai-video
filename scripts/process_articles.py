#!/usr/bin/env python3
"""
使用Claude API处理文章
- 提取摘要
- 生成标签
- 分类
- 生成Hugo Markdown
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def process_article_with_claude(article_data):
    """使用Claude处理单篇文章"""
    # 这里会集成Claude API
    # 返回处理后的数据
    return {
        "title": article_data.get("title", ""),
        "summary": "",
        "tags": [],
        "category": "",
        "content": article_data.get("content", "")
    }

def generate_hugo_markdown(article_data):
    """生成Hugo Markdown文件"""
    frontmatter = f"""---
title: "{article_data.get('title', 'Untitled')}"
date: {datetime.now().isoformat()}
draft: false
tags: {json.dumps(article_data.get('tags', []))}
categories: {json.dumps(article_data.get('category', []))}
description: "{article_data.get('summary', '')}"
---

{article_data.get('content', '')}
"""
    return frontmatter

def batch_process_articles(json_file, output_dir):
    """批量处理文章"""
    with open(json_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, article in enumerate(articles):
        print(f"处理文章 {i+1}/{len(articles)}: {article.get('title', 'Unknown')}")

        # 处理文章
        processed = process_article_with_claude(article)

        # 生成Markdown
        markdown = generate_hugo_markdown(processed)

        # 保存文件
        filename = f"{i+1:04d}_{article.get('title', 'article').replace(' ', '_')[:50]}.md"
        output_file = output_dir / filename

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"✓ 已保存: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python process_articles.py <json_file> [output_dir]")
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "content/posts"

    batch_process_articles(json_file, output_dir)
