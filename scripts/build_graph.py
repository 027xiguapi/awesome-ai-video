#!/usr/bin/env python3
"""
构建知识图谱
- 提取关键概念
- 建立概念关系
- 生成可视化数据
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

def extract_concepts(articles):
    """从文章中提取关键概念"""
    concepts = defaultdict(list)

    for article in articles:
        title = article.get('title', '')
        tags = article.get('tags', [])
        category = article.get('category', '')

        # 构建概念关系
        for tag in tags:
            concepts[tag].append({
                'title': title,
                'category': category,
                'type': 'tag'
            })

    return concepts

def build_knowledge_graph(json_file, output_file):
    """构建知识图谱"""
    with open(json_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    concepts = extract_concepts(articles)

    # 生成图谱数据
    graph_data = {
        "nodes": [],
        "edges": [],
        "concepts": concepts
    }

    # 添加节点
    for concept, articles_list in concepts.items():
        graph_data["nodes"].append({
            "id": concept,
            "label": concept,
            "size": len(articles_list),
            "type": "concept"
        })

    # 保存图谱数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)

    print(f"✓ 知识图谱已生成: {output_file}")
    print(f"✓ 概念数: {len(concepts)}")
    print(f"✓ 节点数: {len(graph_data['nodes'])}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python build_graph.py <json_file> [output_file]")
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "data/knowledge_graph.json"

    build_knowledge_graph(json_file, output_file)
