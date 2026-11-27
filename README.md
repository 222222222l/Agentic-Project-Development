> **2026-11-23 开发计划增补：** [Swarm 采用决策树](agentic-project-development/references/swarm-coordination-decision-2026-11-23.md)。明确单 Agent、固定 DAG、事件板的升级门槛，只有消融证明净收益时才增加复杂度。新增里程碑属于待开发项，原有签收状态不变。

# Agentic Project Development

[English](README.en.md)

面向软件与 Agent 项目的可移植开发流程 Skill。它依据任务范围、风险、确定性和可验证性，选择规格、行为验收、测试、评估、源码核验、架构、交付与审查方法，并记录完成证据。

本项目是工作流与参考方法层，使用宿主已有工具；不提供新的 Agent 运行时，也不会自动获得模型、权限或持久子 Agent。

## 方法

- 简单修改采用“检查—修改—相关验证”；只为真实风险增加流程。
- 重要阶段明确输入、动作、产物、验证者和停止条件。
- 测试、评估和验收按行为需要选用，不强制所有任务使用 TDD。
- 区分本地、上游和结构性失败，避免无诊断重试；保留已通过的回归义务。
- 按能力、执行与协同总成本分配工作；相关工作复用上下文，独立验收使用独立证据。
- Skill、上下文和 harness 变化作为需比较、可回退的候选，不因写入指令就视为有效。

## 模式与范围

| 模式/专题 | 用途 |
| --- | --- |
| `frontier-compact` | 能力强、工具成熟的宿主；精简阶段契约与按需参考 |
| `portable-guided` | 陌生或工具有限环境；显式阶段、状态交接和有界委派 |
| SDD/BDD/TDD/EDD | 规格、行为验收、测试或概率性输出评估 |
| Agent系统工程 | 从简单可验证方案开始，测得收益后再增加状态图或多Agent |
| 长任务与自动迭代 | 明确验证目标、预算/停止规则、依赖和恢复状态 |
| 补丁最小化 | 在行为已通过后，对符合条件的任务修改进行约束化缩减 |

模式由实际模型与宿主能力决定，模型名称仅作为元数据。用户要求的持续执行受可用验证器、权限和停止条件约束。具体路由见 [SKILL.md](agentic-project-development/SKILL.md)。

## 安装与使用

将 `agentic-project-development/` 安装到宿主支持的 Skill 目录。已有版本先备份；备份放在发现目录外，避免重复识别。

```text
使用 $agentic-project-development 为这个功能选择最小可靠流程，
明确验收条件、实现边界和完成证据。
```

在仓库根目录运行已有检查：

```bash
python agentic-project-development/scripts/test_select_workflow.py
python agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
python agentic-project-development/scripts/select_workflow.py --work-type review --scope project --risk high --task-role verification --verification-independence required
```

项目稳定约定可写入 `docs/agents/project-development-profile.md`，不要为每个任务复制一套文档。

## 来源与证据

方法来源及整合边界见 [source-map.md](agentic-project-development/references/source-map.md)。资料包括 addyosmani/agent-skills、fradser/dotclaude、robotlearning123/behavior-driven-testing、promptfoo 与 github/awesome-copilot；本项目的整合不代表这些作者背书。

[研究记录](agentic-project-development/references/research-evidence-2026-09.md) 区分论文结果、工程改编、负面证据和待验证机制。结构/路由测试只能证明被检查的行为，不能证明跨模型、跨宿主的生产率提高；后者需要代表性任务上的成对实验、独立验收与完整成本记录。

完整专题仍保留在 [references/](agentic-project-development/references/)，包括上下文治理、评估标准、数据反馈、模型路由和补丁最小化。本仓库当前未提供顶层 `LICENSE`。
