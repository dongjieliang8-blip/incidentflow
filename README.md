# IncidentFlow

多 Agent 协作事故复盘流水线，基于 Claude Code 开发、DeepSeek API 驱动。

## 核心架构

| Agent | 职责 | 输入 | 输出 |
|-------|------|------|------|
| IncidentExtractorAgent | 事故信息提取 | 事故报告 | 结构化事故数据 |
| RootCauseAnalyzerAgent | 根因分析 | 事故数据 | 根因分析报告 |
| PreventionPlannerAgent | 预防方案生成 | 根因分析 | 预防措施建议 |
| IncidentReportAgent | 复盘报告生成 | 全部结果 | 综合复盘报告 |

## 快速开始

```bash
pip install -r requirements.txt
copy .env.example .env
python -m src.main analyze ./incident.md -o incidentflow_report.json
```

## 技术栈

- Python 3.10+ / Click / Rich / httpx / DeepSeek API

## 单次运行消耗

约 200-400 万 Token
