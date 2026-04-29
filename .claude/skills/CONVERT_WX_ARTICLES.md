# 🔄 转换微信文章 Skill

## 功能说明

`/convert-wx-articles` Skill 用于将 `wx/` 文件夹中的文章转换为Hugo Markdown格式，并保存到 `content/posts/` 目录。

支持使用Claude优化内容，自动分类和生成标签。

## 使用方式

### 基础用法

转换所有wx文章：
```bash
/convert-wx-articles
```

或通过命令行：
```bash
python .claude/skills/skills_manager.py convert-wx
```

### 高级用法

#### 1. 转换指定数量的文章

转换前5篇文章：
```bash
/convert-wx-articles --start 0 --limit 5
```

从第10篇开始，转换20篇：
```bash
/convert-wx-articles --start 10 --limit 20
```

#### 2. 禁用Claude优化

如果不需要Claude优化，可以加上 `--no-optimize` 参数：
```bash
/convert-wx-articles --no-optimize
```

#### 3. 组合参数

转换前10篇，并使用Claude优化：
```bash
/convert-wx-articles --start 0 --limit 10 --optimize
```

## 工作流程

```
wx/ 文件夹
    ↓
[读取文章] → 获取所有.md文件
    ↓
[分类] → 自动分类为AI视频或YouTube运维
    ↓
[优化] → 使用Claude优化内容（可选）
    ↓
[生成Frontmatter] → 添加Hugo元数据
    ↓
[保存] → 生成到 content/posts/
    ↓
Hugo Markdown 文件
```

## 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--start` | number | 0 | 开始索引 |
| `--limit` | number | 无 | 处理数量限制 |
| `--optimize` | boolean | true | 是否使用Claude优化 |
| `--no-optimize` | flag | - | 禁用Claude优化 |

## 输出示例

```json
{
  "total": 5,
  "success": 5,
  "failed": 0,
  "files": [
    {
      "title": "0基础做出电影感封面！Figma免费版保姆级攻略",
      "file": "0001_0基础做出电影感封面！Figma免费版保姆级攻略.md",
      "category": "youtube_ops",
      "path": "content/posts/0001_0基础做出电影感封面！Figma免费版保姆级攻略.md"
    },
    ...
  ],
  "errors": []
}
```

## 生成的文件格式

每个生成的Markdown文件包含：

```markdown
---
title: "文章标题"
date: 2024-04-29T14:30:00
draft: false
tags: ["标签1", "标签2", "标签3"]
categories: ["分类名称"]
description: "来自微信的优化文章"
---

[原始文章内容]
```

## 分类规则

系统会根据文章标题和内容自动分类：

### AI视频 (ai_video)
关键词：视频、生成、AI、Sora、编辑、理解、剪辑、字幕、特效

### YouTube运维 (youtube_ops)
关键词：YouTube、油管、频道、SEO、运营、社区、粉丝、播放、订阅

## 标签生成

根据分类自动生成相关标签，来自 `config.json` 中的标签配置。

## 集成Claude API

当前实现中，Claude优化功能是占位符。要启用真正的Claude优化，需要：

1. 设置 `ANTHROPIC_API_KEY` 环境变量
2. 在 `optimize_content_with_claude()` 方法中集成Claude API调用

示例：
```python
def optimize_content_with_claude(self, content: str, title: str) -> str:
    """使用Claude优化内容"""
    from anthropic import Anthropic
    
    client = Anthropic()
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"请优化以下文章内容，保持原意但提高可读性和专业性：\n\n标题：{title}\n\n内容：{content}"
            }
        ]
    )
    return message.content[0].text
```

## 常见问题

### Q: 如何只转换特定的文章？
A: 使用 `--start` 和 `--limit` 参数指定范围。

### Q: 转换失败了怎么办？
A: 检查 `wx/` 文件夹中是否有有效的 `.md` 文件，以及 `content/posts/` 目录是否可写。

### Q: 如何修改分类规则？
A: 编辑 `config.json` 中的 `categories` 和 `tags` 部分。

### Q: 生成的文件名太长怎么办？
A: 系统会自动截断文件名到50个字符。

## 下一步

1. **集成Claude API** - 启用真正的内容优化
2. **自定义分类** - 根据需要调整分类规则
3. **批量处理** - 设置定时任务自动转换新文章
4. **质量检查** - 定期检查生成的文章质量

## 相关命令

- `/view-config` - 查看配置
- `/update-config` - 更新配置
- `/stats` - 查看统计信息
