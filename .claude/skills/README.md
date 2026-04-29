# Claude Skills - AI视频知识图谱处理系统

## 📍 位置

Claude Skills已安装在项目目录: `./.claude/skills/`

## 📦 文件清单

```
./.claude/skills/
├── manifest.json           # Skills清单和配置
├── skills.json            # 10个Skills的完整定义
├── skills.schema.json     # JSON Schema验证
├── skills_manager.py      # Python实现
└── README.md              # 本文件
```

## 🎯 10个核心Skills

### 数据处理
- **parse-wx** - 解析微信文章文件
- **classify-article** - 智能分类文章
- **extract-summary** - 提取文章摘要

### 内容处理
- **generate-tags** - 自动生成标签

### 知识管理
- **build-knowledge-graph** - 构建知识图谱

### 工作流
- **full-pipeline** - 一键完整处理流程

### 配置管理
- **view-config** - 查看项目配置
- **update-config** - 更新项目配置

### 分析
- **stats** - 查看统计信息

## 🚀 使用方式

### 在Claude对话中使用

```
/parse-wx wx/articles.txt
/classify-article "标题" "内容"
/generate-tags "内容"
/build-knowledge-graph data/parsed/articles.json
/full-pipeline wx/articles.txt
/view-config --section categories
/update-config tags ai_video "新标签"
/stats --type categories
```

### 通过命令行使用

```bash
python .claude/skills/skills_manager.py parse-wx wx/articles.txt
python .claude/skills/skills_manager.py classify "标题" "内容"
python .claude/skills/skills_manager.py stats
```

## 📖 项目文档

详细文档位于项目根目录:
- `DOCUMENTATION_INDEX.md` - 完整文档索引
- `CLAUDE_SKILLS_GUIDE.md` - 详细使用指南
- `SKILLS_QUICK_REFERENCE.md` - 快速参考

## 🔧 配置

项目配置文件: `config.json`

包含:
- 分类体系 (AI视频、YouTube运维)
- 标签体系
- Claude API参数

## 💡 快速开始

1. **查看可用Skills**
   ```
   /stats
   ```

2. **处理微信文件**
   ```
   /parse-wx wx/articles.txt
   ```

3. **构建知识图谱**
   ```
   /build-knowledge-graph data/parsed/articles.json
   ```

4. **完整流程**
   ```
   /full-pipeline wx/articles.txt
   ```

## 📊 工作流程

```
微信文件 → /parse-wx → 解析数据
  ↓
/classify-article → 分类结果
  ↓
/generate-tags → 标签数据
  ↓
/build-knowledge-graph → 知识图谱
  ↓
Hugo网站
```

## 🎉 完成

Claude Skills已成功安装到 `./.claude/skills/`，可以在Claude中直接使用！
