"""
Claude Skills 实现 - 增强版
用于AI视频知识图谱的系统化处理
支持wx文章转换和Claude优化
图片统一放入static文件夹
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re
import shutil

# 设置UTF-8编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class SkillsManager:
    """Claude Skills管理器"""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.data_dir = Path(self.config.get("processing", {}).get("parse", {}).get("output_dir", "data/parsed"))
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.posts_dir = Path(self.config.get("processing", {}).get("process", {}).get("output_dir", "content/posts"))
        self.posts_dir.mkdir(parents=True, exist_ok=True)
        self.static_dir = Path("static")
        self.static_dir.mkdir(parents=True, exist_ok=True)

    def _load_config(self) -> Dict:
        """加载配置文件"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_config(self):
        """保存配置文件"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    # ==================== WX文章转换 ====================

    def get_wx_articles(self) -> List[Dict[str, Any]]:
        """获取wx文件夹中的所有文章"""
        wx_dir = Path("wx")
        if not wx_dir.exists():
            return []

        articles = []
        for item in sorted(wx_dir.iterdir()):
            if item.is_dir():
                # 查找markdown文件
                md_files = list(item.glob("*.md"))
                if md_files:
                    md_file = md_files[0]
                    articles.append({
                        "title": item.name,
                        "path": str(md_file),
                        "dir": str(item),
                        "images_dir": str(item / "images") if (item / "images").exists() else None
                    })
        return articles

    def read_article_content(self, file_path: str) -> str:
        """读取文章内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"✗ 读取文件失败: {file_path} - {e}")
            return ""

    def classify_article_content(self, title: str, content: str) -> Dict[str, Any]:
        """分类文章内容"""
        categories = self.config.get("categories", {})
        tags = self.config.get("tags", {})

        # 关键词匹配
        ai_video_keywords = ["视频", "生成", "AI", "Sora", "编辑", "理解", "剪辑", "字幕", "特效"]
        youtube_keywords = ["YouTube", "油管", "频道", "SEO", "运营", "社区", "粉丝", "播放", "订阅"]

        text = (title + " " + content).lower()

        ai_video_score = sum(1 for kw in ai_video_keywords if kw.lower() in text)
        youtube_score = sum(1 for kw in youtube_keywords if kw.lower() in text)

        if ai_video_score > youtube_score:
            category = "ai_video"
        elif youtube_score > ai_video_score:
            category = "youtube_ops"
        else:
            category = "ai_video"

        return {
            "category": category,
            "category_name": categories.get(category, {}).get("name", ""),
            "tags": tags.get(category, [])[:5]
        }

    def generate_hugo_frontmatter(self, article: Dict[str, Any], classification: Dict[str, Any]) -> str:
        """生成Hugo Frontmatter"""
        title = article.get("title", "Untitled")
        tags = classification.get("tags", [])
        category = classification.get("category_name", "")

        frontmatter = f"""---
title: "{title}"
date: {datetime.now().isoformat()}
draft: false
tags: {json.dumps(tags, ensure_ascii=False)}
categories: ["{category}"]
description: "来自微信的优化文章"
---

"""
        return frontmatter

    def optimize_content_with_claude(self, content: str, title: str) -> str:
        """使用Claude优化内容（这里是占位符，实际需要调用Claude API）"""
        # 这里可以集成Claude API调用
        # 目前返回原始内容
        print(f"  💡 提示: 可以集成Claude API来优化内容")
        return content

    def _copy_images_to_static(self, article_title: str, images_dir: str) -> str:
        """复制图片文件夹到static/images目录"""
        images_path = Path(images_dir)
        if not images_path.exists():
            return None

        # 创建目标图片目录
        safe_title = re.sub(r'[<>:"/\\|?*]', '', article_title)[:50]
        target_images_dir = self.static_dir / f"images/{safe_title}"

        try:
            if target_images_dir.exists():
                shutil.rmtree(target_images_dir)
            target_images_dir.mkdir(parents=True, exist_ok=True)

            # 直接复制images文件夹中的文件，而不是复制整个目录结构
            for image_file in images_path.iterdir():
                if image_file.is_file():
                    shutil.copy2(image_file, target_images_dir / image_file.name)

            print(f"    ✓ 图片已复制到: static/images/{safe_title}/")
            return f"/images/{safe_title}"
        except Exception as e:
            print(f"    ⚠️  图片复制失败: {str(e)}")
            return None

    def _update_image_paths_to_static(self, content: str, image_path_prefix: str) -> str:
        """更新Markdown中的图片路径为static路径"""
        # 简单的字符串替换，避免复杂的正则表达式问题
        content = content.replace("./images/", f"{image_path_prefix}/")
        content = content.replace("(images/", f"({image_path_prefix}/")

        return content

    def convert_wx_articles(self, start: int = 0, limit: int = None, optimize: bool = True) -> Dict[str, Any]:
        """转换wx文章为Hugo Markdown"""
        articles = self.get_wx_articles()

        if not articles:
            return {"error": "未找到wx文章"}

        # 应用限制
        if limit:
            articles = articles[start:start + limit]
        else:
            articles = articles[start:]

        results = {
            "total": len(articles),
            "success": 0,
            "failed": 0,
            "files": [],
            "errors": []
        }

        for idx, article in enumerate(articles, 1):
            try:
                print(f"\n[{idx}/{len(articles)}] 处理: {article['title']}")

                # 读取内容
                content = self.read_article_content(article["path"])
                if not content:
                    results["failed"] += 1
                    results["errors"].append(f"无法读取: {article['title']}")
                    continue

                # 分类
                classification = self.classify_article_content(article["title"], content)
                print(f"  📁 分类: {classification['category_name']}")
                print(f"  🏷️  标签: {', '.join(classification['tags'])}")

                # 复制图片文件夹到static目录
                images_dir = article.get("images_dir")
                image_path_prefix = None
                if images_dir and Path(images_dir).exists():
                    print(f"  📸 复制图片到static...")
                    image_path_prefix = self._copy_images_to_static(article["title"], images_dir)

                # 优化内容（可选）
                if optimize:
                    print(f"  ✨ 优化内容中...")
                    content = self.optimize_content_with_claude(content, article["title"])

                # 更新图片路径（使用static路径）
                if image_path_prefix:
                    content = self._update_image_paths_to_static(content, image_path_prefix)

                # 生成Frontmatter
                frontmatter = self.generate_hugo_frontmatter(article, classification)

                # 生成文件名
                safe_title = re.sub(r'[<>:"/\\|?*]', '', article["title"])[:50]
                filename = f"{idx:04d}_{safe_title}.md"
                output_path = self.posts_dir / filename

                # 保存文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(frontmatter)
                    f.write(content)

                results["success"] += 1
                results["files"].append({
                    "title": article["title"],
                    "file": filename,
                    "category": classification["category"],
                    "path": str(output_path)
                })

                print(f"  ✓ 已保存: {filename}")

            except Exception as e:
                results["failed"] += 1
                results["errors"].append(f"{article['title']}: {str(e)}")
                print(f"  ✗ 错误: {str(e)}")

        return results

    # ==================== 其他Skills ====================

    def view_config(self, section: str = None) -> Dict[str, Any]:
        """查看配置"""
        if section:
            return {
                "section": section,
                "data": self.config.get(section, {})
            }
        return {"config": self.config}

    def update_config(self, section: str, key: str, value: Any) -> Dict[str, Any]:
        """更新配置"""
        if section not in self.config:
            self.config[section] = {}

        self.config[section][key] = value
        self._save_config()

        return {
            "status": "success",
            "section": section,
            "key": key,
            "value": value,
            "message": f"配置已更新: {section}.{key}"
        }

    def get_stats(self, stats_type: str = "all") -> Dict[str, Any]:
        """获取统计信息"""
        stats = {
            "timestamp": datetime.now().isoformat(),
            "project": self.config.get("project", {})
        }

        if stats_type in ["categories", "all"]:
            stats["categories"] = self.config.get("categories", {})

        if stats_type in ["tags", "all"]:
            stats["tags"] = self.config.get("tags", {})

        if stats_type in ["timeline", "all"]:
            # 统计文件数量
            parsed_files = list(self.data_dir.glob("parsed_*.json"))
            posts_files = list(self.posts_dir.glob("*.md"))
            stats["files_count"] = len(parsed_files)
            stats["posts_count"] = len(posts_files)

        return stats


# ==================== CLI 接口 ====================

def main():
    """主函数"""
    manager = SkillsManager()

    if len(sys.argv) < 2:
        print("Claude Skills - AI视频知识图谱处理系统")
        print("\n可用命令:")
        print("  convert-wx              - 转换wx文章到Hugo Markdown")
        print("  convert-wx --start 0 --limit 5  - 转换前5篇")
        print("  convert-wx --optimize   - 使用Claude优化内容")
        print("  view-config [section]   - 查看配置")
        print("  update-config <section> <key> <value> - 更新配置")
        print("  stats [type]            - 查看统计")
        sys.exit(1)

    command = sys.argv[1]

    if command == "convert-wx":
        # 解析参数
        start = 0
        limit = None
        optimize = True

        for i, arg in enumerate(sys.argv[2:]):
            if arg == "--start" and i + 2 < len(sys.argv):
                start = int(sys.argv[i + 3])
            elif arg == "--limit" and i + 2 < len(sys.argv):
                limit = int(sys.argv[i + 3])
            elif arg == "--no-optimize":
                optimize = False

        result = manager.convert_wx_articles(start=start, limit=limit, optimize=optimize)

    elif command == "view-config":
        section = sys.argv[2] if len(sys.argv) > 2 else None
        result = manager.view_config(section)

    elif command == "update-config":
        if len(sys.argv) < 5:
            print("用法: update-config <section> <key> <value>")
            sys.exit(1)
        result = manager.update_config(sys.argv[2], sys.argv[3], sys.argv[4])

    elif command == "stats":
        stats_type = sys.argv[2] if len(sys.argv) > 2 else "all"
        result = manager.get_stats(stats_type)

    else:
        result = {"error": f"未知命令: {command}"}

    print("\n" + "="*60)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("="*60)


if __name__ == "__main__":
    main()
