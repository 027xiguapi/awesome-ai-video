#!/usr/bin/env python3
"""
主控制脚本 - 系统化处理流程
"""

import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """运行命令并显示进度"""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    print(f"执行: {' '.join(cmd)}\n")

    try:
        result = subprocess.run(cmd, check=True)
        print(f"\n✓ {description} 完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ {description} 失败: {e}")
        return False

def main():
    """主流程"""
    if len(sys.argv) < 2:
        print("""
用法: python main.py <command> [args]

命令:
  parse <wx_file>              - 解析微信导出文件
  process <json_file>          - 处理文章（提取摘要、标签等）
  graph <json_file>            - 构建知识图谱
  full <wx_file>               - 完整流程（解析 -> 处理 -> 图谱）
  status                       - 显示当前状态

示例:
  python main.py parse wx/articles.txt
  python main.py full wx/articles.txt
        """)
        sys.exit(1)

    command = sys.argv[1]
    script_dir = Path(__file__).parent

    if command == "parse":
        if len(sys.argv) < 3:
            print("用法: python main.py parse <wx_file>")
            sys.exit(1)
        wx_file = sys.argv[2]
        run_command([sys.executable, str(script_dir / "parse_wx.py"), wx_file], "解析微信文件")

    elif command == "process":
        if len(sys.argv) < 3:
            print("用法: python main.py process <json_file>")
            sys.exit(1)
        json_file = sys.argv[2]
        run_command([sys.executable, str(script_dir / "process_articles.py"), json_file], "处理文章")

    elif command == "graph":
        if len(sys.argv) < 3:
            print("用法: python main.py graph <json_file>")
            sys.exit(1)
        json_file = sys.argv[2]
        run_command([sys.executable, str(script_dir / "build_graph.py"), json_file], "构建知识图谱")

    elif command == "full":
        if len(sys.argv) < 3:
            print("用法: python main.py full <wx_file>")
            sys.exit(1)
        wx_file = sys.argv[2]

        # 完整流程
        print("\n🚀 开始完整处理流程...\n")

        # 1. 解析
        if not run_command([sys.executable, str(script_dir / "parse_wx.py"), wx_file], "第1步: 解析微信文件"):
            sys.exit(1)

        # 2. 处理
        json_file = "data/parsed/parsed_articles.json"
        if not run_command([sys.executable, str(script_dir / "process_articles.py"), json_file], "第2步: 处理文章"):
            sys.exit(1)

        # 3. 构建图谱
        if not run_command([sys.executable, str(script_dir / "build_graph.py"), json_file], "第3步: 构建知识图谱"):
            sys.exit(1)

        print("\n" + "="*60)
        print("✓ 完整流程已完成！")
        print("="*60)

    elif command == "status":
        print("\n📊 系统状态\n")
        print("✓ 脚本已就绪:")
        print("  - parse_wx.py: 解析微信文件")
        print("  - process_articles.py: 处理文章")
        print("  - build_graph.py: 构建知识图谱")

    else:
        print(f"未知命令: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
