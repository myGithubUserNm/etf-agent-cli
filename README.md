# etf-agent-cli

ETF 研究 Agent 的命令行工具。当前处于**骨架阶段**：只提供 CLI 入口，尚无运行能力。

## 开发

```powershell
uv sync                 # 建 .venv 并安装（可编辑）
uv run etf-agent --help
uv run pytest
```

## 目录

```
src/etf_agent_cli/
  __init__.py    版本号
  cli.py         命令行入口
tests/           测试（不在包内分发）
```

> README 待补：能力范围、用法示例、产物结构。许可证一节按计划最后补。
