# Claude Skills 集成指南

## 📚 已创建的Claude Skills

### 1. 数据处理Skills

#### `/parse-wx` - 解析微信文章
解析微信导出的文章文件，提取结构化数据。

```
/parse-wx wx/articles.txt
```

**输出**: 解析后的文章数据（JSON格式）

---

#### `/classify-article` - 分类文章
对文章进行智能分类（AI视频 或 YouTube运维）。

```
/classify-article "Sora视频生成最新进展" "本文介绍了Sora在视频生成中的应用..."
```

**输出**: 分类结果、置信度、推荐标签

---

#### `/extract-summary` - 提取摘要
从文章中提取关键摘要。

```
/extract-summary "长文章内容..." --length medium
```

**选项**: `short`, `medium`, `long`

**输出**: 摘要文本和压缩比

---

#### `/generate-tags` - 生成标签
根据文章内容自动生成标签。

```
/generate-tags "文章内容..." --count 5
```

**输出**: 标签列表

---

### 2. 知识图谱Skills

#### `/build-knowledge-graph` - 构建知识图谱
从文章数据构建知识图谱。

```
/build-knowledge-graph data/parsed/articles.json --format d3
```

**格式选项**: `d3`, `cytoscape`, `json`

**输出**: 知识图谱数据（节点、边、概念关系）

---

### 3. 工作流Skills

#### `/full-pipeline` - 完整处理流程
一键执行完整流程：解析 → 处理 → 分类 → 图谱构建。

```
/full-pipeline wx/articles.txt
```

**输出**: 完整处理结果统计

---

### 4. 配置管理Skills

#### `/view-config` - 查看配置
查看项目配置。

```
/view-config
/view-config --section categories
/view-config --section tags
```

**输出**: 配置信息

---

#### `/update-config` - 更新配置
更新项目配置。

```
/update-config categories new_category "新分类名称"
/update-config tags ai_video "新标签"
/update-config claude_api temperature 0.8
```

**输出**: 更新确认

---

### 5. 分析Skills

#### `/stats` - 查看统计
查看项目统计信息。

```
/stats
/stats --type categories
/stats --type tags
/stats --type timeline
```

**输出**: 统计数据和可视化

---

## 🚀 使用示例

### 场景1: 处理新的微信文章文件

```
1. /parse-wx wx/new_articles.txt
   ↓ 获得解析后的JSON文件
2. /classify-article "标题" "内容摘要"
   ↓ 确认分类
3. /generate-tags "文章内容"
   ↓ 获得推荐标签
4. /build-knowledge-graph data/parsed/articles.json
   ↓ 更新知识图谱
```

### 场景2: 快速处理完整流程

```
/full-pipeline wx/articles.txt
```

### 场景3: 查看和更新配置

```
/view-config --section categories
/update-config tags ai_video "新标签"
/view-config --section tags
```

### 场景4: 分析项目统计

```
/stats --type categories
/stats --type tags
/stats
```

---

## 🔧 集成到Claude Code

### 方法1: 使用Skill工具

在Claude Code中使用Skill工具调用：

```python
from Skill import invoke_skill

# 解析微信文章
result = invoke_skill("parse-wx", {"file_path": "wx/articles.txt"})

# 分类文章
result = invoke_skill("classify-article", {
    "title": "文章标题",
    "content": "文章内容"
})

# 生成标签
result = invoke_skill("generate-tags", {
    "content": "文章内容",
    "count": 5
})
```

### 方法2: 直接调用Python脚本

```bash
python skills/skills_manager.py parse-wx wx/articles.txt
python skills/skills_manager.py classify "标题" "内容"
python skills/skills_manager.py generate-tags "内容"
python skills/skills_manager.py build-graph data/parsed/articles.json
```

### 方法3: 在Claude对话中使用

直接在Claude对话中输入skill命令：

```
我想处理一批微信文章，请帮我：
1. /parse-wx wx/articles.txt
2. 然后对每篇文章进行分类
3. 最后构建知识图谱
```

---

## 📋 Skills配置文件

Skills定义存储在 `skills/skills.json`，包含：

- **id**: Skill唯一标识
- **name**: Skill名称
- **description**: Skill描述
- **usage**: 使用方式
- **parameters**: 参数定义
- **examples**: 使用示例
- **output**: 输出格式

---

## 🔄 工作流程

```
微信文件
  ↓
/parse-wx
  ↓
解析数据 (JSON)
  ↓
/classify-article
  ↓
分类结果
  ↓
/generate-tags
  ↓
标签数据
  ↓
/build-knowledge-graph
  ↓
知识图谱
  ↓
Hugo网站
```

---

## 💡 最佳实践

1. **定期更新配置** - 根据需要添加新的分类和标签
2. **批量处理** - 使用 `/full-pipeline` 处理大量文件
3. **验证分类** - 定期检查分类准确性
4. **监控统计** - 使用 `/stats` 跟踪项目进度
5. **备份数据** - 定期备份 `data/` 目录

---

## 🐛 故障排除

### 问题: Skill命令无法识别
- 检查命令拼写
- 确认参数格式正确
- 查看 `skills/skills.json` 中的定义

### 问题: 文件解析失败
- 检查文件路径是否正确
- 确认文件格式符合预期
- 查看错误日志

### 问题: 分类不准确
- 检查关键词配置
- 更新分类规则
- 使用 `/update-config` 调整参数

---

## 📞 支持

如有问题，请：
1. 查看 `SKILLS_GUIDE.md`
2. 检查 `skills/skills.json` 中的定义
3. 查看 `skills/skills_manager.py` 中的实现
4. 查看错误日志和输出信息
