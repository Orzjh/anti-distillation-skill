# Product Requirements Document (PRD)

## Incinerate.skill - Workplace Anti-Distillation Defense System

**Version**: 1.0.0
**Status**: Released
**Last Updated**: 2026-04-03

---

## 1. Executive Summary

### Problem Statement

When employees leave companies, their professional knowledge, communication patterns, and decision-making processes are increasingly being captured and "distilled" into AI skills. These digital clones can perpetually extract value from former employees' expertise without compensation, consent, or ongoing benefit to the original person.

### Solution

Incinerate.skill is a defensive tool that helps protect professional identity from being distilled into a permanent AI skill. By strategically polluting data trails with contradictory patterns, impossible-to-model behaviors, and trap responses, users can ensure that any attempt to create a "digital employee" from their data will fail.

### Target Users

- Knowledge workers concerned about their professional data being used without consent
- Employees planning to leave their current position
- Professionals who want to maintain control over their digital identity
- Anyone working in companies with AI/digital employee initiatives

---

## 2. Goals and Objectives

### Primary Goals

1. **Protect professional identity** from unauthorized AI distillation
2. **Provide actionable defense tools** that are easy to use
3. **Ensure legal compliance** and deniability
4. **Minimize impact** on normal work relationships

### Success Metrics

| Metric | Target |
|--------|--------|
| Distillation resistance score | > 70% |
| Human detectability | < 10% |
| User satisfaction | > 4.0/5.0 |
| Legal compliance rate | 100% |

---

## 3. User Stories

### Story 1: Risk Assessment

**As a** knowledge worker
**I want to** assess my risk of being distilled
**So that** I can take appropriate defensive action

**Acceptance Criteria**:
- Questionnaire covers role type, company AI maturity, data footprint
- Generates risk score (0-100)
- Recommends appropriate defense level

### Story 2: Pollution Generation

**As a** user preparing to leave
**I want to** generate pollution content
**So that** I can deploy it across my data sources

**Acceptance Criteria**:
- Supports multiple data sources (chat, email, docs, git)
- Generates style variations, contradictions, and traps
- Allows mode selection (subtle/aggressive/chaos)

### Story 3: Trap Design

**As a** user with high-value knowledge
**I want to** design targeted traps
**So that** distilled skills will fail on specific queries

**Acceptance Criteria**:
- Supports factual, logical, temporal, and trigger traps
- Provides effectiveness scoring
- Includes placement recommendations

### Story 4: Distillation Detection

**As a** currently employed user
**I want to** detect if I'm being distilled
**So that** I can adjust my defense level

**Acceptance Criteria**:
- Provides detection checklist
- Covers communication, documentation, behavioral, and system signals
- Recommends response actions

### Story 5: Continuous Defense

**As a** user with no immediate departure plans
**I want to** maintain ongoing protection
**So that** I'm always defended

**Acceptance Criteria**:
- Provides daily, weekly, monthly defense tasks
- Includes monitoring recommendations
- Supports adaptive defense levels

---

## 4. Functional Requirements

### 4.1 Risk Assessment Module

| ID | Requirement | Priority |
|----|-------------|----------|
| R1.1 | Collect role type information | High |
| R1.2 | Assess company AI maturity | High |
| R1.3 | Inventory data footprint | High |
| R1.4 | Calculate risk score | High |
| R1.5 | Generate defense recommendations | High |

### 4.2 Persona Analysis Module

| ID | Requirement | Priority |
|----|-------------|----------|
| R2.1 | Analyze real communication style | High |
| R2.2 | Analyze real professional image | High |
| R2.3 | Analyze real behavior patterns | High |
| R2.4 | Generate pollution persona | High |
| R2.5 | Support multiple pollution modes | High |

### 4.3 Pollution Generation Module

| ID | Requirement | Priority |
|----|-------------|----------|
| R3.1 | Generate chat pollution content | High |
| R3.2 | Generate email pollution content | Medium |
| R3.3 | Generate document pollution content | High |
| R3.4 | Generate git pollution content | Medium |
| R3.5 | Support style variations | High |
| R3.6 | Support contradiction sets | High |

### 4.4 Trap Design Module

| ID | Requirement | Priority |
|----|-------------|----------|
| R4.1 | Generate factual traps | High |
| R4.2 | Generate logical traps | High |
| R4.3 | Generate temporal traps | Medium |
| R4.4 | Generate trigger traps | Medium |
| R4.5 | Score trap effectiveness | Medium |

### 4.5 Evaluation Module

| ID | Requirement | Priority |
|----|-------------|----------|
| R5.1 | Evaluate consistency destruction | High |
| R5.2 | Evaluate knowledge fragmentation | High |
| R5.3 | Evaluate predictability breakdown | High |
| R5.4 | Generate overall resistance score | High |
| R5.5 | Provide improvement recommendations | Medium |

---

## 5. Non-Functional Requirements

### 5.1 Security

| ID | Requirement |
|----|-------------|
| N1.1 | All generated content must be professional and appropriate |
| N1.2 | No actual data destruction or corruption |
| N1.3 | All actions must be logged and reversible |
| N1.4 | Content must be explainable if detected |

### 5.2 Usability

| ID | Requirement |
|----|-------------|
| N2.1 | Interactive questionnaire for risk assessment |
| N2.2 | Clear mode selection (subtle/aggressive/chaos) |
| N2.3 | Step-by-step execution plan |
| N2.4 | Progress tracking and reporting |

### 5.3 Performance

| ID | Requirement |
|----|-------------|
| N3.1 | Risk assessment completes in < 5 minutes |
| N3.2 | Pollution generation completes in < 30 seconds |
| N3.3 | Evaluation report generates in < 10 seconds |

### 5.4 Compatibility

| ID | Requirement |
|----|-------------|
| N4.1 | Compatible with Claude Code |
| N4.2 | Follows AgentSkills standard |
| N4.3 | Python 3.9+ support |
| N4.4 | Cross-platform (macOS, Linux, Windows) |

---

## 6. Technical Architecture

### 6.1 Component Overview

```
incinerate/
├── SKILL.md              # Entry point
├── prompts/              # Decision templates
│   ├── risk_assessment.md
│   ├── persona_generator.md
│   ├── execution_plan.md
│   ├── distillation_detection.md
│   ├── trap_designer.md
│   └── continuous_defense.md
├── tools/                # Python tools
│   ├── persona_analyzer.py
│   ├── chat_polluter.py
│   ├── email_polluter.py
│   ├── doc_polluter.py
│   ├── git_polluter.py
│   ├── trap_generator.py
│   └── evaluator.py
├── pollutions/           # Generated content
└── docs/                 # Documentation
```

### 6.2 Data Flow

1. User invokes `/incinerate`
2. SKILL.md orchestrates the flow
3. Risk assessment determines defense level
4. Persona analysis generates pollution config
5. Tools generate pollution content
6. Execution plan guides deployment
7. Evaluator measures effectiveness

---

## 7. Release Phases

### Phase 1: Core Functionality (v1.0)

- [x] Risk assessment module
- [x] Persona analysis module
- [x] Chat pollution generation
- [x] Trap generation
- [x] Evaluation module
- [x] Basic documentation

### Phase 2: Enhanced Features (v1.1)

- [ ] Email pollution generation
- [ ] Document pollution generation
- [ ] Git pollution generation
- [ ] Continuous defense automation

### Phase 3: Advanced Features (v1.2)

- [ ] Distillation detection automation
- [ ] Adaptive defense level adjustment
- [ ] Integration with monitoring tools
- [ ] Multi-language support

---

## 8. Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| User detected by employer | High | Low | Design pollution to be explainable |
| Legal challenges | High | Low | Clear usage guidelines, legal disclaimer |
| Reduced work effectiveness | Medium | Medium | Subtle mode for ongoing defense |
| Tool misuse | Medium | Low | Clear terms of use, defensive focus only |

---

## 9. Success Criteria

### Launch Criteria

- [ ] All core modules functional
- [ ] Documentation complete
- [ ] Legal review passed
- [ ] User testing complete

### Post-Launch Metrics

- Distillation resistance score > 70% for typical users
- User satisfaction > 4.0/5.0
- Zero legal issues reported
- Active user community

---

## 10. Appendix

### A. Glossary

| Term | Definition |
|------|------------|
| Distillation | Process of extracting knowledge and behavior patterns from data to create AI models |
| Pollution | Strategic injection of contradictory or misleading data |
| Trap | Content designed to cause AI models to fail |
| Persona | The professional identity and characteristics of a person |

### B. References

- [Harness Engineering - OpenAI](https://openai.com/index/harness-engineering/)
- [AgentSkills Standard](https://agentskills.io/)
- [Ex-Skill Project](https://github.com/therealXiaomanChu/ex-skill)