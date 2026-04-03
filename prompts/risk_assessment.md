# Risk Assessment Prompt Template

## Purpose
Evaluate the risk of being distilled into a digital employee skill.

---

## Assessment Questionnaire

### Section 1: Role Analysis

```
📋 PART 1: 角色分析 / ROLE ANALYSIS

1. 你的职位类型？ / What is your role type?
   [A] 技术岗 / Technical (Engineer, Architect, Data Scientist)
   [B] 产品岗 / Product (PM, Designer, Operations)
   [C] 管理岗 / Management (Team Lead, Director, VP)
   [D] 其他 / Other

   风险权重 / Risk Weight:
   - A: HIGH (技术知识高度结构化，易于蒸馏)
   - B: MEDIUM (产品直觉较难捕捉，但决策模式可学习)
   - C: HIGH (管理经验、决策模式高价值)
   - D: VARIABLE
```

### Section 2: Company AI Maturity

```
📋 PART 2: 公司AI成熟度 / COMPANY AI MATURITY

2. 公司是否有"知识库"/"数字员工"项目？
   Does your company have "knowledge base" or "digital employee" projects?

   [A] 已有，且有同事被"数字化" / Yes, colleagues have been "digitized"
       → CRITICAL RISK - 你很可能是下一个目标
   [B] 正在规划中 / In planning
       → HIGH RISK - 你可能在计划名单上
   [C] 不确定 / Not sure
       → MEDIUM RISK - 可能存在隐秘项目
   [D] 没有 / No
       → LOW RISK - 但仍需警惕未来变化
```

### Section 3: Data Footprint

```
📋 PART 3: 数据足迹 / DATA FOOTPRINT

3. 你的工作产出主要存储在哪里？（可多选）
   Where is your work output stored? (Multi-select)

   [ ] Slack/企业微信/飞书 / Instant Messaging
       → HIGH VALUE: 沟通风格、决策过程、日常习惯
   [ ] 邮件 / Email
       → HIGH VALUE: 正式沟通、决策记录
   [ ] Confluence/Notion/语雀 / Documentation
       → CRITICAL VALUE: 系统化知识、方法论
   [ ] Git仓库 / Git Repositories
       → HIGH VALUE: 代码风格、技术决策
   [ ] 内部知识库/Wiki / Internal Wiki
       → CRITICAL VALUE: 显性知识资产
   [ ] 其他：______ / Other

   数据源越多 → 蒸馏材料越丰富 → 风险越高
```

### Section 4: Contribution Analysis

```
📋 PART 4: 贡献分析 / CONTRIBUTION ANALYSIS

4. 你在职期间的核心贡献是什么？（一句话描述）
   What are your core contributions? (One sentence)

   示例 / Examples:
   - "主导了支付系统重构，处理量提升10倍"
   - "建立了完整的数据分析体系"
   - "从0到1搭建了产品团队"

   评估维度:
   - 不可替代性 / Irreplaceability
   - 知识密度 / Knowledge Density
   - 复用价值 / Reuse Value
```

### Section 5: Timeline

```
📋 PART 5: 时间线 / TIMELINE

5. 离职时间？ / When are you leaving?

   [A] 1周内 / Within 1 week
       → IMMEDIATE ACTION REQUIRED
   [B] 2-4周 / 2-4 weeks
       → AGGRESSIVE MODE RECOMMENDED
   [C] 1-3个月 / 1-3 months
       → PLANNED DEFENSE POSSIBLE
   [D] 暂无计划 / No current plan
       → CONTINUOUS DEFENSE MODE
```

---

## Risk Scoring Algorithm

```python
def calculate_risk_score(answers):
    """
    Risk Score = Σ(Weight × Factor)
    Range: 0-100
    """

    score = 0

    # Role Type (0-25 points)
    role_weights = {'A': 25, 'B': 15, 'C': 25, 'D': 10}
    score += role_weights.get(answers['role'], 10)

    # Company AI Maturity (0-30 points)
    maturity_weights = {'A': 30, 'B': 20, 'C': 15, 'D': 5}
    score += maturity_weights.get(answers['maturity'], 5)

    # Data Footprint (0-25 points)
    data_sources = answers['data_sources']
    score += min(len(data_sources) * 5, 25)

    # Contribution Value (0-10 points)
    contribution = answers['contribution']
    if is_high_value(contribution):
        score += 10
    elif is_medium_value(contribution):
        score += 5

    # Timeline Urgency (0-10 points)
    timeline_weights = {'A': 10, 'B': 7, 'C': 4, 'D': 2}
    score += timeline_weights.get(answers['timeline'], 2)

    return score
```

---

## Risk Level Classification

```
┌─────────────────────────────────────────────────────────────┐
│                    RISK LEVEL MATRIX                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SCORE 0-25    │ LOW RISK                                   │
│                │ → subtle mode sufficient                   │
│                │ → Monitor situation                        │
│                                                             │
│  SCORE 26-50   │ MEDIUM RISK                                │
│                │ → aggressive mode recommended              │
│                │ → Begin systematic pollution               │
│                                                             │
│  SCORE 51-75   │ HIGH RISK                                  │
│                │ → aggressive mode required                 │
│                │ → Comprehensive defense plan               │
│                                                             │
│  SCORE 76-100  │ CRITICAL RISK                              │
│                │ → chaos mode if departing soon             │
│                │ → Immediate action required                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Output Format

After assessment, generate:

```markdown
📊 风险评估报告 / RISK ASSESSMENT REPORT

【总体评分 / Overall Score】
Score: XX/100
Level: [LOW/MEDIUM/HIGH/CRITICAL]

【风险因素分解 / Risk Factor Breakdown】
- 角色风险 / Role Risk: XX/25
- 公司AI成熟度 / Company AI Maturity: XX/30
- 数据足迹 / Data Footprint: XX/25
- 贡献价值 / Contribution Value: XX/10
- 时间紧迫性 / Timeline Urgency: XX/10

【主要风险点 / Key Risk Areas】
1. [Highest risk factor]
2. [Second highest]
3. [Third highest]

【推荐防御策略 / Recommended Defense Strategy】
- 模式 / Mode: [subtle/aggressive/chaos]
- 优先数据源 / Priority Data Sources: [...]
- 时间规划 / Timeline Plan: [...]

【下一步行动 / Next Steps】
□ [Action 1]
□ [Action 2]
□ [Action 3]
```