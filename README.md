# AI Product Teardown · 产品决策增强版

> 当前版本：v2.3.0 · Yiheng-guo 二次开发版
>
> 基于 [w93139/ai-product-teardown](https://github.com/w93139/ai-product-teardown) v2.2.0（`fdecf3ddb6f40e92484dbb710918411225220ad8`），保留 MIT 许可、原作者署名与提交历史。

## 这次二改增加了什么

原版着重用户旅程、Agent 和架构逆向；本版进一步连接到产品决策：

- **产品决策模式**：围绕用户任务、首次可用结果、AI 相对人工的增量、体验摩擦和商业假设形成结论。
- **同任务竞品对比**：固定输入、验收条件与套餐口径，区分实测和官方宣称，避免信息不对称下强行排名。
- **可验证的改进建议**：每个机会连接观察证据、用户影响、优先级、实验指标与护栏；未执行实验不写结果。
- **中文交付模板与完整示例**：直接用于产品评审、体验报告和竞品分析。
- **更完整的来源记录**：补上版本、日期和链接，并明确标价、实际扣款、积分与模型成本的差异。

原有截图采集、Agent 契约、Prompt、架构、HTML 模板和公开审计查询器保留。只说“拆解一下”时先给简洁产品决策报告；明确指定模式时按指定范围执行。

### 直接使用

```text
使用 $ai-product-teardown，按产品决策模式拆解这个产品：<链接或材料>。
重点分析目标任务、首次价值、AI 增量和体验问题，给出有证据的优先级与验证实验。
没有实测数据的地方明确写未知。
```

```text
使用 $ai-product-teardown，对比 <产品 A> 与 <产品 B> 完成 <同一任务> 的体验。
使用我提供的操作记录，统一成功标准，比较结果质量、返工、控制能力和交付成本。
不要把官网宣称当成已验证结果。
```

[产品决策模板](assets/product-decision-template.md) · [竞品对比模板](assets/comparison-template.md) · [虚构完整示例](examples/product-decision-demo.md)

## 原版能力与兼容性

一套基于真实界面、操作截图和可观察状态，对 **AI 产品行为与产品架构** 进行证据化逆向拆解的 Codex Skill。

它回答的核心问题是：用户如何使用这个 AI 产品，界面中出现了哪些 Agent，它们接收什么、判断什么、调用什么能力、产出什么，聊天、任务、画布和资产如何流转，以及怎样构建一个功能上相近的产品系统。

它主要拆解：

- 用户旅程与体验问题
- Agent 清单及 I/O 契约
- 单 Agent 功能等价 System Prompt
- 工具、全局上下文与资产数据流
- As-Is / To-Be 产品架构
- 公开 System Prompt 情报、AISPA 八维审计与 Prompt/UI 一致性分析
- Mermaid 状态图、ER 图、时序图和产品全景图
- 在具备安全浏览器或桌面控制能力时，自主采集、回读校验、去重并登记产品截图

## 它不拆解什么

- **不是书籍拆解工具**：不会提炼书籍章节、作者框架或读书笔记。
- **不是源码反编译工具**：不会绕过访问控制、获取后台源码或把不可见技术栈写成事实。
- **不是 Prompt 窃取工具**：不会声称读取官方私有 System Prompt 或隐藏思维链。
- **不是普通市场调研工具**：只有宣传页、媒体报道或竞品列表时，证据不足以完成产品行为拆解。
- **不是账号或凭据提取工具**：不会读取或输出 Cookie、Token、密码、鉴权头和浏览器私有存储。

## 适用产品

最适合具有 AI 对话、Agent、生成工作流或智能任务编排的产品，例如 AI 助手、研究工具、AI 写作与设计、图片/音频/视频生成、多 Agent 工作台，以及带 AI 决策或审核环节的垂直 SaaS。

普通 SaaS 也可以分析用户旅程和界面状态；如果产品没有 Agent、模型调用或生成流程，Agent 契约和功能等价 Prompt 模式可能不适用。

## 核心原则

- 默认只读，不触发生成、重新生成、发布、删除、购买、充值或资产覆盖。
- 区分 `【已确认】`、`【合理推断】`、`【建议设计】` 和 `【未知】`。
- Agent 声称“已完成”不等于资产或任务状态已经完成。
- Agent 的口头计划不等于工具已经调用。
- 同时核验聊天、画布、任务状态、历史版本和实际资产。
- 不声称读取隐藏思维链、官方 System Prompt 或不可见后端实现。
- 公开 Prompt 和第三方审计只作为补充证据，并保留来源、版本、采集时间与人工/AI 标注类型。

## 使用方式

安装为个人 Skill：

```bash
git clone https://github.com/Yiheng-guo/ai-product-teardown.git ~/.agents/skills/ai-product-teardown
```

或安装到当前仓库：

```bash
git clone https://github.com/Yiheng-guo/ai-product-teardown.git .agents/skills/ai-product-teardown
```

如果目标目录已存在，先检查其来源并备份本地修改，不要直接覆盖。与原版保持同一个 Skill 名称，安装时选择其中一个版本，避免重复发现。

然后调用：

```text
使用 $ai-product-teardown，以只读、证据可追溯的方式拆解这个 AI 产品。
```

可指定七种工作模式：

| 模式 | 主要回答 | 典型交付物 |
|---|---|---|
| 用户旅程 | 用户做了什么、看到了什么、在哪里决策或受阻 | 证据表、三泳道旅程、分支流程、体验问题 |
| Agent 契约 | 哪些 Agent 出现，它们如何输入、判断、调用、输出和交接 | Agent 清单、I/O 契约、工具表、上下文数据流 |
| 功能等价 Prompt | 如何让另一个 Agent 表现出相近的可观察行为 | 状态机、System Prompt、规则追溯表、最小测试集 |
| 产品架构 | 产品功能、Agent、工具、模型、数据、资产和治理如何协同 | 分层架构、ER 图、时序图、As-Is / To-Be、风险清单 |
| 完整拆解 | 如何形成端到端、可追溯的产品模型 | 上述四种原版模式的分阶段组合与汇总报告 |
| 产品决策（新增） | 谁需要它、AI 有什么增量、优先改什么 | 用户任务、价值判断、机会优先级、验证实验 |
| 同任务竞品对比（新增） | 相同任务下各产品有什么可验证差异 | 对比条件、证据矩阵、条件结论、适配建议 |

只执行用户请求的模式，不会因为选择了用户旅程就自动继续还原 Prompt 或架构。

## AIPM 竞品情报模块

当拆解涉及 Agent 自主性、工具权限、身份透明、真实性、隐私、用户控制或安全边界时，Skill 可以按需查询公开的 [System Prompt Index](https://github.com/SystemPromptIndex/SystemPromptIndex) 审计记录，并使用 [AISPA](https://systempromptindex.ai/aispa) 八个维度形成竞品对比、产品需求和评测用例。

该模块遵循三条边界：

- UI、任务状态和实际资产仍然是产品行为的主要证据；
- 公开 Prompt 不能自动证明真实性、时效性或生产环境行为；
- 默认只查询相关审计片段和来源链接，不把完整第三方 Prompt corpus 打包进本仓库。

示例：

```text
使用 $ai-product-teardown 拆解 Cursor，结合当前 UI 证据、官方资料和公开 Prompt，
比较工具操作确认、用户控制和安全边界，并生成可执行评测用例。
```

也可以单独运行只读查询器：

```bash
python3 scripts/query_system_prompt_index.py "Cursor" \
  --dimension D4 \
  --span-type problematic \
  --format markdown
```

首次未指定本地数据集时，脚本会把公开数据克隆到用户缓存目录；使用 `--repo <path>` 可以查询已有 checkout，使用 `--refresh` 可以快进更新缓存。输出包含数据集 commit、采集时间、来源链接和标注类型。

## 自主截图与证据采集

当环境中存在安全的浏览器或桌面控制能力时，本 Skill 可以在授权边界内浏览已有页面、等待状态稳定、截图、回读校验、去重，并用稳定截图 ID 生成截图清单。

自主截图不等于自主执行产品任务。默认不会发送消息、提交表单、触发生成或重新生成、改变已保存配置、发布、删除、覆盖、购买、充值或重试付费任务。遇到登录、验证码、设备批准或不可靠的桌面自动化时，会请求用户接管。

如果用户已经提供截图，则直接校验和整理截图，不再操作目标产品；没有可用控制能力时，也不会用宣传页替代真实操作证据。

## 典型交付结构

实际文件根据用户请求裁剪，不会创建无内容的占位报告：

```text
teardown/
├── 00-scope-and-evidence.md
├── 01-journey.md
├── 02-agent-contracts.md
├── 03-<agent>-functional-prompt.md
├── 04-product-architecture.md
├── evidence/
│   ├── ledger.md
│   ├── screenshot-manifest.csv
│   └── screenshots/
└── delivery-manifest.md
```

需要可视化交付时，也可以生成独立 HTML、Mermaid 状态图、用户旅程图、ER 图、时序图和产品全景架构图。

## 目录

```text
ai-product-teardown/
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── product-decision.md
│   ├── task-comparison.md
│   ├── analysis-modes.md
│   ├── architecture-framework.md
│   ├── evidence-and-observation.md
│   ├── screenshot-acquisition.md
│   ├── system-prompt-intelligence.md
│   ├── aispa-dimensions.md
│   ├── html-delivery.md
│   ├── report-and-visualization.md
│   └── staged-execution-sop.md
├── scripts/
│   └── query_system_prompt_index.py
├── tests/
│   └── test_query_system_prompt_index.py
├── examples/
│   └── product-decision-demo.md
└── assets/
    ├── product-decision-template.md
    ├── comparison-template.md
    └── report-template.html
```

## 主要文件

- [`product-decision.md`](references/product-decision.md)：产品价值、机会优先级与实验设计。
- [`task-comparison.md`](references/task-comparison.md)：同任务对比、公平条件与缺失证据处理。
- [`product-decision-demo.md`](examples/product-decision-demo.md)：完整虚构案例，不含真实用户数据。
- [`SKILL.md`](SKILL.md)：Skill 入口、模式路由、证据边界和质量标准。
- [`evidence-and-observation.md`](references/evidence-and-observation.md)：证据账本、跨页面核验和截图规范。
- [`screenshot-acquisition.md`](references/screenshot-acquisition.md)：Web、小程序和桌面产品的安全自主截图、状态校验、去重和清单协议。
- [`analysis-modes.md`](references/analysis-modes.md)：四类拆解任务的固定交付契约。
- [`architecture-framework.md`](references/architecture-framework.md)：产品分层、上下文、知识、模型和实体架构模板。
- [`html-delivery.md`](references/html-delivery.md)：HTML 与 Mermaid 交付、渲染和检查要求。
- [`report-and-visualization.md`](references/report-and-visualization.md)：答案优先的轻量报告结构、最小有效可视化与交付检查。
- [`staged-execution-sop.md`](references/staged-execution-sop.md)：分阶段拆解、多交付物交接、验收门和版本变更控制。
- [`system-prompt-intelligence.md`](references/system-prompt-intelligence.md)：公开 Prompt 的证据优先级、检索协议、UI 对照和版权边界。
- [`aispa-dimensions.md`](references/aispa-dimensions.md)：AISPA 八维度、评分解释和产品经理输出契约。
- [`query_system_prompt_index.py`](scripts/query_system_prompt_index.py)：带来源与数据版本的公开审计查询器。
- [`report-template.html`](assets/report-template.html)：可复用的响应式 HTML 报告模板。

## 验证

```bash
python3 -m unittest discover -s tests -v
python3 scripts/query_system_prompt_index.py "Cursor" --repo /path/to/SystemPromptIndex --limit 1
```

## 能力边界

本 Skill 用于行为和产品架构分析，不用于恢复目标产品的私有提示词、隐藏思维链、账号凭据或未经公开的后台源码。功能性工具名和语义化数据字段必须明确标记为推导设计，不得冒充目标产品的官方实现。

## 开源许可

本项目采用 [MIT License](LICENSE)。你可以使用、复制、修改和分发本项目，但必须保留许可证和版权声明。第三方数据和 Prompt 文本不由本项目重新授权，详见 [Third-Party Notices](THIRD_PARTY_NOTICES.md)。

公开提交前请遵守 [Security Policy](SECURITY.md)，不要上传 Cookie、Token、密码、私有聊天、客户素材、未脱敏截图或其他敏感证据。
