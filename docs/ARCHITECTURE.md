# Architecture Design

## System Overview

Incinerate.skill follows the Harness Engineering methodology to create a comprehensive defense system against AI distillation of professional personas.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INCINERATE.SKILL ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                        USER INTERFACE LAYER                          │   │
│   │                                                                      │   │
│   │   /incinerate          → Main entry point                           │   │
│   │   /incinerate --status → Check defense status                       │   │
│   │   /incinerate --mode   → Switch pollution mode                      │   │
│   │   /incinerate --report → Generate defense report                    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         ORCHESTRATION LAYER                          │   │
│   │                                                                      │   │
│   │   SKILL.md              → Entry point & flow control                │   │
│   │   prompts/*.md          → Decision templates                        │   │
│   │   execution_plan.md     → Step-by-step guide                        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                           TOOL LAYER                                 │   │
│   │                                                                      │   │
│   │   persona_analyzer.py  → Analyze & generate pollution persona       │   │
│   │   chat_polluter.py     → Generate chat pollution content            │   │
│   │   email_polluter.py    → Generate email pollution content           │   │
│   │   doc_polluter.py      → Generate document pollution content        │   │
│   │   git_polluter.py      → Generate git pollution content             │   │
│   │   trap_generator.py    → Generate various trap types                │   │
│   │   evaluator.py         → Evaluate defense effectiveness             │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         CONTENT LAYER                                │   │
│   │                                                                      │   │
│   │   pollutions/           → Pre-generated pollution content           │   │
│   │   ├── chat_pollutions.md                                           │   │
│   │   ├── email_pollutions.md                                          │   │
│   │   ├── doc_pollutions.md                                            │   │
│   │   └── trap_templates.md                                            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Risk Assessment Module

**Purpose**: Evaluate the likelihood and severity of distillation attempts.

**Components**:
- `prompts/risk_assessment.md` - Questionnaire and scoring algorithm
- Risk factors: Role type, Company AI maturity, Data footprint, Contribution value, Timeline

**Output**: Risk score (0-100) and recommended defense level

### 2. Persona Analysis Module

**Purpose**: Analyze real work persona and generate contradictory pollution persona.

**Components**:
- `prompts/persona_generator.md` - Analysis framework
- `tools/persona_analyzer.py` - Implementation

**Dimensions Analyzed**:
- Communication style (response speed, formality, message length, emoji usage, punctuation)
- Professional image (expertise depth, decision style, risk tolerance, priorities)
- Behavior patterns (work rhythm, collaboration style, deadline approach, feedback style)

**Output**: Real persona profile + Pollution persona profile

### 3. Pollution Generation Module

**Purpose**: Generate pollution content for various data sources.

**Components**:
- `tools/chat_polluter.py` - Chat/messaging platforms
- `tools/email_polluter.py` - Email communications
- `tools/doc_polluter.py` - Documentation systems
- `tools/git_polluter.py` - Git repositories

**Pollution Types**:
- Style variations (formal/casual/technical/enthusiastic)
- Contradiction sets (opposite opinions on similar topics)
- Trap responses (trigger-based anomalies)

### 4. Trap Design Module

**Purpose**: Create various types of traps for distillation systems.

**Components**:
- `prompts/trap_designer.md` - Design framework
- `tools/trap_generator.py` - Implementation

**Trap Types**:
| Type | Mechanism | Effect |
|------|-----------|--------|
| Factual | Plausible but incorrect facts | Wrong advice propagation |
| Logical | Contradictory statements | Inconsistent reasoning |
| Temporal | Time-sensitive information | Outdated knowledge |
| Trigger | Keyword-based anomalies | Targeted failures |

### 5. Evaluation Module

**Purpose**: Assess the effectiveness of pollution defense.

**Components**:
- `tools/evaluator.py` - Evaluation implementation

**Metrics**:
- Consistency destruction score
- Knowledge fragmentation score
- Predictability breakdown score
- Overall distillation resistance

### 6. Detection Module

**Purpose**: Identify signs of active distillation.

**Components**:
- `prompts/distillation_detection.md` - Detection signals

**Signal Categories**:
- Communication signals (methodology questions, template requests)
- Documentation signals (knowledge systematization, data collection)
- Behavioral signals (project involvement, pre-departure attention)
- System signals (AI projects, data policies)

## Data Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    User      │────▶│  SKILL.md    │────▶│    Risk      │
│   Request    │     │  (Entry)     │     │ Assessment   │
└──────────────┘     └──────────────┘     └──────────────┘
                                                 │
                                                 ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Defense    │◀────│  Pollution   │◀────│   Persona    │
│   Report     │     │   Content    │     │   Analysis   │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │
       │                    ▼
       │             ┌──────────────┐
       │             │    Trap      │
       │             │   Design     │
       │             └──────────────┘
       │                    │
       ▼                    ▼
┌──────────────────────────────────────┐
│           Execution Plan              │
│   (Phased deployment of pollution)   │
└──────────────────────────────────────┘
```

## Design Principles

### 1. Harness Engineering Alignment

Following OpenAI's Harness Engineering methodology:

- **Environment Design**: Build pollution environments rather than individual outputs
- **Legibility**: Pollution invisible to humans, fatal to distillation
- **Progressive Disclosure**: Layered pollution from subtle to obvious
- **Enforced Invariants**: Tools enforce pollution rules automatically

### 2. Defense in Depth

Multiple layers of protection:

1. **L1: Style Pollution** - Break communication pattern analysis
2. **L2: Knowledge Fragmentation** - Disrupt knowledge coherence
3. **L3: Decision Contradiction** - Confuse decision modeling
4. **L4: Trap Responses** - Cause targeted failures
5. **L5: Timeline Disruption** - Invalidate temporal patterns

### 3. Adaptive Defense

Defense levels adjust based on detected signals:

| Signal Strength | Defense Level | Pollution % | Action |
|-----------------|---------------|-------------|--------|
| None | Level 1 | 5-10% | Maintain daily defense |
| Weak | Level 2 | 10-20% | Increase pollution |
| Medium | Level 3 | 20-35% | Accelerate defense |
| Strong | Level 4 | 35-50% | Emergency defense |
| Confirmed | Level 5 | 50%+ | Chaos mode |

### 4. Deniability

All pollution is designed to be explainable:

- Style variations: "Different contexts require different tones"
- Contradictions: "My views evolved over time"
- Traps: "That was my understanding at the time"
- Temporal content: "Information was current when written"

## Extension Points

### Adding New Pollution Types

1. Create new polluter tool in `tools/`
2. Add corresponding prompt template in `prompts/`
3. Update SKILL.md to include new tool
4. Add output location in `pollutions/`

### Adding New Trap Types

1. Define trap mechanism in `prompts/trap_designer.md`
2. Implement generator in `tools/trap_generator.py`
3. Add templates to `pollutions/trap_templates.md`

### Adding New Detection Signals

1. Document signals in `prompts/distillation_detection.md`
2. Update detection checklist
3. Add recommended response actions

## Security Considerations

### Data Safety

- All generated content is defensive, not destructive
- No actual data deletion or corruption
- Pollution affects AI training, not human readability

### Legal Compliance

- Does not violate employment contracts
- Does not leak confidential information
- Does not damage company systems
- Protected as personal expression/style

### Reversibility

- All pollution actions are logged
- Rollback explanations can be generated
- Content remains professionally appropriate