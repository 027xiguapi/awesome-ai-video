# 📚 Claude Skills 完整文档索引

## 🎯 快速导航

### 🚀 快速开始
- **[CLAUDE_SKILLS_SUMMARY.md](CLAUDE_SKILLS_SUMMARY.md)** - 完整总结和快速开始指南
- **[SKILLS_QUICK_REFERENCE.md](SKILLS_QUICK_REFERENCE.md)** - 快速参考卡片

### 📖 详细文档
- **[CLAUDE_SKILLS_GUIDE.md](CLAUDE_SKILLS_GUIDE.md)** - 详细使用指南
- **[SKILLS_ARCHITECTURE.md](SKILLS_ARCHITECTURE.md)** - 系统架构和数据流
- **[skills/README.md](skills/README.md)** - Skills注册和集成指南

### 🔧 技术文档
- **[skills/skills.json](skills/skills.json)** - 10个Skills的完整定义
- **[skills/skills_manager.py](skills/skills_manager.py)** - Python实现
- **[config.json](config.json)** - 项目配置

---

## 📋 文档清单

### 核心文档 (必读)

| 文档 | 说明 | 适合人群 |
|------|------|---------|
| [CLAUDE_SKILLS_SUMMARY.md](CLAUDE_SKILLS_SUMMARY.md) | 完整总结，包含所有Skills和使用示例 | 所有人 |
| [SKILLS_QUICK_REFERENCE.md](SKILLS_QUICK_REFERENCE.md) | 快速参考卡片，常用命令速查 | 快速查询 |
| [CLAUDE_SKILLS_GUIDE.md](CLAUDE_SKILLS_GUIDE.md) | 详细使用指南，包含所有Skills的详细说明 | 深入学习 |

### 架构文档

| 文档 | 说明 | 适合人群 |
|------|------|---------|
| [SKILLS_ARCHITECTURE.md](SKILLS_ARCHITECTURE.md) | 系统架构、数据流、工作流程 | 系统设计 |
| [skills/README.md](skills/README.md) | Skills注册、集成、自定义 | 开发者 |

### 配置文档

| 文档 | 说明 | 适合人群 |
|------|------|---------|
| [config.json](config.json) | 项目配置（分类、标签、API参数） | 配置管理 |
| [skills/skills.json](skills/skills.json) | Skills定义（10个Skills） | 开发者 |

---

## 🎯 10个核心Skills

### 1. 数据处理 (3个)

#### `/parse-wx` - 解析微信文章
```bash
/parse-wx wx/articles.txt
```
- 解析微信导出文件
- 提取结构化数据
- 输出JSON格式

**文档**: [CLAUDE_SKILLS_GUIDE.md#parse-wx](CLAUDE_SKILLS_GUIDE.md)

---

#### `/classify-article` - 分类文章
```bash
/classify-article "标题" "内容"
```
- 智能分类（AI视频/YouTube运维）
- 返回分类结果和置信度
- 推荐相关标签

**文档**: [CLAUDE_SKILLS_GUIDE.md#classify-article](CLAUDE_SKILLS_GUIDE.md)

---

#### `/extract-summary` - 提取摘要
```bash
/extract-summary "内容" --length medium
```
- 提取关键摘要
- 支持长度选项（short/medium/long）
- 返回摘要和压缩比

**文档**: [CLAUDE_SKILLS_GUIDE.md#extract-summary](CLAUDE_SKILLS_GUIDE.md)

---

### 2. 内容处理 (1个)

#### `/generate-tags` - 生成标签
```bash
/generate-tags "内容" --count 5
```
- 自动生成标签
- 支持自定义标签数量
- 返回标签列表

**文档**: [CLAUDE_SKILLS_GUIDE.md#generate-tags](CLAUDE_SKILLS_GUIDE.md)

---

### 3. 知识管理 (1个)

#### `/build-knowledge-graph` - 构建知识图谱
```bash
/build-knowledge-graph data/parsed/articles.json --format d3
```
- 构建知识图谱
- 提取关键概念
- 建立概念关系
- 支持多种可视化格式

**文档**: [CLAUDE_SKILLS_GUIDE.md#build-knowledge-graph](CLAUDE_SKILLS_GUIDE.md)

---

### 4. 工作流 (1个)

#### `/full-pipeline` - 完整处理流程
```bash
/full-pipeline wx/articles.txt
```
- 一键执行完整流程
- 自动执行所有处理步骤
- 返回完整结果统计

**文档**: [CLAUDE_SKILLS_GUIDE.md#full-pipeline](CLAUDE_SKILLS_GUIDE.md)

---

### 5. 配置管理 (2个)

#### `/view-config` - 查看配置
```bash
/view-config --section categories
```
- 查看项目配置
- 支持按部分查看
- 返回配置信息

**文档**: [CLAUDE_SKILLS_GUIDE.md#view-config](CLAUDE_SKILLS_GUIDE.md)

---

#### `/update-config` - 更新配置
```bash
/update-config tags ai_video "新标签"
```
- 更新项目配置
- 支持添加新分类和标签
- 返回更新确认

**文档**: [CLAUDE_SKILLS_GUIDE.md#update-config](CLAUDE_SKILLS_GUIDE.md)

---

### 6. 分析 (1个)

#### `/stats` - 查看统计
```bash
/stats --type categories
```
- 查看项目统计信息
- 支持多种统计类型
- 返回统计数据和可视化

**文档**: [CLAUDE_SKILLS_GUIDE.md#stats](CLAUDE_SKILLS_GUIDE.md)

---

## 💡 使用场景

### 场景1: 处理单篇文章
```
1. /classify-article "标题" "内容"
2. /generate-tags "内容"
3. /extract-summary "内容"
```
**文档**: [CLAUDE_SKILLS_GUIDE.md#场景1](CLAUDE_SKILLS_GUIDE.md)

---

### 场景2: 批量处理文件
```
1. /parse-wx wx/articles.txt
2. /build-knowledge-graph data/parsed/articles.json
3. /stats
```
**文档**: [CLAUDE_SKILLS_GUIDE.md#场景2](CLAUDE_SKILLS_GUIDE.md)

---

### 场景3: 完整流程
```
/full-pipeline wx/articles.txt
```
**文档**: [CLAUDE_SKILLS_GUIDE.md#场景3](CLAUDE_SKILLS_GUIDE.md)

---

### 场景4: 配置管理
```
1. /view-config --section categories
2. /update-config tags ai_video "新标签"
3. /view-config --section tags
```
**文档**: [CLAUDE_SKILLS_GUIDE.md#场景4](CLAUDE_SKILLS_GUIDE.md)

---

## 🔧 技术细节

### Skills定义
- **文件**: `skills/skills.json`
- **格式**: JSON
- **内容**: 10个Skills的完整定义
- **文档**: [skills/README.md](skills/README.md)

### Skills实现
- **文件**: `skills/skills_manager.py`
- **语言**: Python 3.8+
- **类**: `SkillsManager`
- **文档**: [skills/README.md](skills/README.md)

### 项目配置
- **文件**: `config.json`
- **内容**: 分类、标签、API参数
- **文档**: [CLAUDE_SKILLS_GUIDE.md#配置](CLAUDE_SKILLS_GUIDE.md)

---

## 📊 架构概览

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

**详细架构**: [SKILLS_ARCHITECTURE.md](SKILLS_ARCHITECTURE.md)

---

## 🚀 快速开始

### 1. 查看可用Skills
```bash
python skills/skills_manager.py stats
```

### 2. 处理微信文件
```bash
python skills/skills_manager.py parse-wx wx/articles.txt
```

### 3. 构建知识图谱
```bash
python skills/skills_manager.py build-graph data/parsed/articles.json
```

### 4. 在Claude中使用
```
/parse-wx wx/articles.txt
/full-pipeline wx/articles.txt
/stats
```

**详细指南**: [CLAUDE_SKILLS_SUMMARY.md](CLAUDE_SKILLS_SUMMARY.md)

---

## 📚 学习路径

### 初级用户
1. 阅读 [SKILLS_QUICK_REFERENCE.md](SKILLS_QUICK_REFERENCE.md) - 快速了解
2. 查看 [CLAUDE_SKILLS_SUMMARY.md](CLAUDE_SKILLS_SUMMARY.md) - 完整总结
3. 尝试使用 `/parse-wx` 和 `/full-pipeline`

### 中级用户
1. 阅读 [CLAUDE_SKILLS_GUIDE.md](CLAUDE_SKILLS_GUIDE.md) - 详细指南
2. 学习 [SKILLS_ARCHITECTURE.md](SKILLS_ARCHITECTURE.md) - 系统架构
3. 尝试自定义配置 `/update-config`

### 高级用户
1. 研究 [skills/skills.json](skills/skills.json) - Skills定义
2. 研究 [skills/skills_manager.py](skills/skills_manager.py) - 实现代码
3. 阅读 [skills/README.md](skills/README.md) - 开发指南
4. 添加新的Skills

---

## 🔗 相关资源

### 项目文件
- `config.json` - 项目配置
- `skills/` - Skills系统目录
- `wx/` - 微信文件目录
- `data/` - 数据目录
- `content/` - Hugo内容目录

### 外部资源
- [Claude API文档](https://docs.anthropic.com)
- [Hugo文档](https://gohugo.io/documentation/)
- [JSON Schema](https://json-schema.org/)

---

## 💡 最佳实践

1. **定期更新配置** - 根据需要添加新的分类和标签
2. **使用完整流程** - 优先使用 `/full-pipeline` 处理大量文件
3. **验证分类准确性** - 定期检查分类结果
4. **监控项目进度** - 使用 `/stats` 跟踪统计信息
5. **备份处理结果** - 定期备份 `data/` 目录

**详细建议**: [CLAUDE_SKILLS_GUIDE.md#最佳实践](CLAUDE_SKILLS_GUIDE.md)

---

## 🐛 故障排除

### 常见问题
- Skills命令无法识别
- 文件解析失败
- 分类不准确
- 配置更新失败

**解决方案**: [CLAUDE_SKILLS_GUIDE.md#故障排除](CLAUDE_SKILLS_GUIDE.md)

---

## 📞 获取帮助

1. 查看相关文档
2. 检查错误日志
3. 查看 `skills/skills.json` 定义
4. 查看 `skills/skills_manager.py` 实现

---

## 📝 文档版本

- **版本**: 1.0
- **日期**: 2024-04-29
- **作者**: 西瓜皮
- **项目**: AI视频知识图谱

---

## 🎉 开始使用

选择你的学习路径：

- 🚀 **快速开始**: [CLAUDE_SKILLS_SUMMARY.md](CLAUDE_SKILLS_SUMMARY.md)
- 📖 **详细学习**: [CLAUDE_SKILLS_GUIDE.md](CLAUDE_SKILLS_GUIDE.md)
- 🎯 **快速查询**: [SKILLS_QUICK_REFERENCE.md](SKILLS_QUICK_REFERENCE.md)
- 🏗️ **系统架构**: [SKILLS_ARCHITECTURE.md](SKILLS_ARCHITECTURE.md)

祝你使用愉快！🚀
