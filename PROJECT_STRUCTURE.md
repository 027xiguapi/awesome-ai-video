# 📁 项目结构说明

## 项目根目录

```
awesome-ai-video/
├── .claude/                    # Claude项目配置
│   ├── skills/                # ✨ Claude Skills系统（所有Skills文件都在这里）
│   │   ├── manifest.json
│   │   ├── skills.json
│   │   ├── skills.schema.json
│   │   ├── skills_manager.py
│   │   ├── README.md
│   │   ├── DOCUMENTATION_INDEX.md
│   │   ├── CLAUDE_SKILLS_SUMMARY.md
│   │   ├── CLAUDE_SKILLS_GUIDE.md
│   │   ├── SKILLS_ARCHITECTURE.md
│   │   ├── SKILLS_QUICK_REFERENCE.md
│   │   └── INSTALLATION_COMPLETE.md
│   └── settings.local.json
│
├── archetypes/                # Hugo模板
├── assets/                    # 静态资源
├── content/                   # Hugo内容
├── data/                      # 数据目录
├── i18n/                      # 国际化
├── layouts/                   # Hugo布局
├── public/                    # 生成的网站
├── resources/                 # Hugo资源
├── scripts/                   # 脚本
├── static/                    # 静态文件
├── themes/                    # Hugo主题
├── wx/                        # 微信导出文件
│
├── config.json                # 项目配置（分类、标签、API参数）
├── hugo.toml                  # Hugo配置
└── .gitignore
```

## Claude Skills 系统

所有Claude Skills相关的文件都已集中到 `./.claude/skills/` 目录：

### 核心文件
- `manifest.json` - Skills清单和配置
- `skills.json` - 10个Skills的完整定义
- `skills.schema.json` - JSON Schema验证
- `skills_manager.py` - Python实现

### 文档文件
- `README.md` - 快速开始指南
- `DOCUMENTATION_INDEX.md` - 完整文档索引
- `CLAUDE_SKILLS_SUMMARY.md` - 完整总结
- `CLAUDE_SKILLS_GUIDE.md` - 详细使用指南
- `SKILLS_ARCHITECTURE.md` - 系统架构
- `SKILLS_QUICK_REFERENCE.md` - 快速参考
- `INSTALLATION_COMPLETE.md` - 安装完成说明

## 快速开始

### 查看Skills文档
```bash
cd .claude/skills
cat README.md
```

### 使用Skills
```bash
# 在Claude对话中
/parse-wx wx/articles.txt
/full-pipeline wx/articles.txt

# 或通过命令行
python .claude/skills/skills_manager.py parse-wx wx/articles.txt
```

## 配置文件

- `config.json` - 项目配置
  - 分类体系 (AI视频、YouTube运维)
  - 标签体系
  - Claude API参数

## 数据目录

- `wx/` - 微信导出文件
- `data/` - 处理后的数据
- `content/` - Hugo文章

## 推荐阅读

1. `./.claude/skills/README.md` - 快速开始
2. `./.claude/skills/DOCUMENTATION_INDEX.md` - 完整文档索引
3. `./.claude/skills/SKILLS_QUICK_REFERENCE.md` - 快速参考
