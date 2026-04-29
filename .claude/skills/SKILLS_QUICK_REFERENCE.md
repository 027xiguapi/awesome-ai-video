# Claude Skills 快速参考

## 📌 核心Skills

| Skill | 命令 | 功能 |
|-------|------|------|
| 解析微信文章 | `/parse-wx <file>` | 解析wx文件，提取结构化数据 |
| 分类文章 | `/classify-article <title> <content>` | 智能分类（AI视频/YouTube运维） |
| 提取摘要 | `/extract-summary <content>` | 提取关键摘要 |
| 生成标签 | `/generate-tags <content>` | 自动生成标签 |
| 构建图谱 | `/build-knowledge-graph <json>` | 构建知识图谱 |
| 完整流程 | `/full-pipeline <wx_file>` | 一键处理所有步骤 |
| 查看配置 | `/view-config [section]` | 查看项目配置 |
| 更新配置 | `/update-config <section> <key> <value>` | 更新配置 |
| 查看统计 | `/stats [type]` | 查看统计信息 |

---

## 🎯 常用场景

### 场景1: 处理单篇文章
```
/classify-article "标题" "内容"
/generate-tags "内容"
/extract-summary "内容"
```

### 场景2: 批量处理文件
```
/parse-wx wx/articles.txt
/build-knowledge-graph data/parsed/articles.json
```

### 场景3: 完整流程
```
/full-pipeline wx/articles.txt
```

### 场景4: 配置管理
```
/view-config --section categories
/update-config tags ai_video "新标签"
```

---

## 📊 参数速查

### `/parse-wx`
- `file_path` (必需): 微信文件路径

### `/classify-article`
- `title` (必需): 文章标题
- `content` (必需): 文章内容

### `/extract-summary`
- `content` (必需): 文章内容
- `--length` (可选): short/medium/long

### `/generate-tags`
- `content` (必需): 文章内容
- `--count` (可选): 标签数量，默认5

### `/build-knowledge-graph`
- `json_file` (必需): JSON文件路径
- `--format` (可选): d3/cytoscape/json

### `/update-config`
- `section` (必需): 配置部分
- `key` (必需): 配置键
- `value` (必需): 配置值

### `/stats`
- `--type` (可选): categories/tags/timeline/all

---

## 🔗 相关文件

- `skills/skills.json` - Skills定义
- `skills/skills_manager.py` - Skills实现
- `config.json` - 项目配置
- `CLAUDE_SKILLS_GUIDE.md` - 详细指南

---

## 💡 提示

1. **快速处理**: 使用 `/full-pipeline` 一键处理
2. **自定义分类**: 使用 `/update-config` 添加新分类
3. **查看进度**: 使用 `/stats` 查看统计
4. **验证结果**: 使用 `/classify-article` 验证分类准确性

---

## 🚀 开始使用

```bash
# 1. 查看可用Skills
/stats

# 2. 处理微信文件
/parse-wx wx/articles.txt

# 3. 构建知识图谱
/build-knowledge-graph data/parsed/articles.json

# 4. 查看统计
/stats --type categories
```
