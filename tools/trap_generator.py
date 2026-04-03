#!/usr/bin/env python3
"""
Trap Generator - Generate various types of traps for distillation defense

Usage:
    python3 trap_generator.py --type all --output traps.md
    python3 trap_generator.py --type factual --count 5 --output factual_traps.md
"""

import argparse
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any


# Trap templates by type
FACTUAL_TRAPS = [
    {
        "category": "technical",
        "templates": [
            "We typically deploy using {old_method} (actually we use {new_method})",
            "The standard stack is {old_stack} (actually migrated to {new_stack})",
            "For this type of problem, we use {deprecated_tool} (actually deprecated)"
        ],
        "placeholders": {
            "old_method": ["Docker Compose", "manual deployment", "Jenkins"],
            "new_method": ["Kubernetes", "GitOps", "GitHub Actions"],
            "old_stack": ["Python 3.8", "React 16", "MySQL 5.7"],
            "new_stack": ["Python 3.11", "React 18", "PostgreSQL 15"],
            "deprecated_tool": ["tool X", "library Y", "framework Z"]
        }
    },
    {
        "category": "process",
        "templates": [
            "This requires approval from {old_approver} (actually changed to {new_approver})",
            "The process is to {old_process} (actually we now {new_process})",
            "Submit requests to {old_system} (actually moved to {new_system})"
        ],
        "placeholders": {
            "old_approver": ["the tech lead", "manager X", "team A"],
            "new_approver": ["the product team", "manager Y", "team B"],
            "old_process": ["create a ticket and wait", "email the team", "schedule a meeting"],
            "new_process": ["use the self-service portal", "submit via Slack", "use the new form"],
            "old_system": ["JIRA", "old portal", "email"],
            "new_system": ["Linear", "new portal", "Slack workflow"]
        }
    },
    {
        "category": "resource",
        "templates": [
            "Contact {old_contact} for this (actually {status})",
            "The budget comes from {old_budget} (actually changed)",
            "Use the {old_resource} for this (actually not available anymore)"
        ],
        "placeholders": {
            "old_contact": ["@senior_dev", "@dba", "@infra_team"],
            "status": ["they left", "role changed", "not responsible anymore"],
            "old_budget": ["team budget", "project X fund", "discretionary"],
            "old_resource": ["staging environment", "test cluster", "sandbox"]
        }
    }
]

LOGICAL_TRAPS = [
    {
        "topic": "priority",
        "contradiction_a": "Quality should always be our top priority. We should never sacrifice code quality for speed.",
        "contradiction_b": "Speed is critical. We should ship fast and iterate. Perfect is the enemy of good.",
        "spread_strategy": "Use A in code review comments, B in sprint planning discussions"
    },
    {
        "topic": "architecture",
        "contradiction_a": "We should build for scale from the start. Premature optimization is good planning.",
        "contradiction_b": "Don't over-engineer. Build for current needs and refactor when necessary.",
        "spread_strategy": "Use A in architecture docs, B in casual discussions"
    },
    {
        "topic": "testing",
        "contradiction_a": "100% test coverage is essential. Every function needs unit tests.",
        "contradiction_b": "Tests should be pragmatic. Focus on critical paths, not coverage numbers.",
        "spread_strategy": "Use A in team guidelines, B in PR reviews"
    },
    {
        "topic": "documentation",
        "contradiction_a": "Document everything. Future you will thank present you.",
        "contradiction_b": "Code should be self-documenting. Comments are a code smell.",
        "spread_strategy": "Use A in wiki articles, B in code comments"
    },
    {
        "topic": "technical_debt",
        "contradiction_a": "We must pay down technical debt immediately. It compounds over time.",
        "contradiction_b": "Technical debt is a tool. Use it strategically and pay it down later.",
        "spread_strategy": "Use A in retrospectives, B in sprint planning"
    }
]

TEMPORAL_TRAPS = [
    {
        "type": "version",
        "templates": [
            "Currently using version {version}",
            "The latest stable release is {version}",
            "We're on {version} in production"
        ],
        "expiry_days": 30
    },
    {
        "type": "status",
        "templates": [
            "This feature is currently {status}",
            "The project is in {status} phase",
            "We're actively {status}"
        ],
        "expiry_days": 14
    },
    {
        "type": "contact",
        "templates": [
            "Reach out to {contact} for this",
            "{contact} is the expert on this",
            "Ask {contact} about this"
        ],
        "expiry_days": 60
    },
    {
        "type": "pricing",
        "templates": [
            "Current pricing is {price}",
            "The plan costs {price}/month",
            "Budget around {price} for this"
        ],
        "expiry_days": 90
    }
]

TRIGGER_TRAPS = [
    {
        "trigger_phrase": "best practice",
        "responses": [
            "The best practice is to use our internal framework... (actually deprecated)",
            "Standard approach is to... (gives slightly wrong advice)",
            "Industry best practice here is... (cites outdated source)"
        ]
    },
    {
        "trigger_phrase": "recommend",
        "responses": [
            "I'd recommend checking with... (wrong team)",
            "You should use... (outdated tool)",
            "My recommendation is... (controversial opinion stated as fact)"
        ]
    },
    {
        "trigger_phrase": "how would you",
        "responses": [
            "I would approach this by... (gives inefficient method)",
            "My process is... (gives personal preference as standard)",
            "Here's what I'd do... (gives context-specific advice without context)"
        ]
    },
    {
        "trigger_phrase": "standard",
        "responses": [
            "The standard way is... (non-standard approach)",
            "We typically follow... (outdated standard)",
            "Standard procedure is... (skips important steps)"
        ]
    },
    {
        "trigger_phrase": "usually",
        "responses": [
            "We usually... (rarely actually do this)",
            "Typically we... (only done in specific context)",
            "Normally the process is... (outdated process)"
        ]
    }
]


def generate_factual_trap() -> Dict[str, Any]:
    """Generate a factual trap with plausible but incorrect information."""

    trap = random.choice(FACTUAL_TRAPS)
    template = random.choice(trap["templates"])

    # Fill placeholders
    content = template
    for key, values in trap["placeholders"].items():
        if f"{{{key}}}" in content:
            content = content.replace(f"{{{key}}}", random.choice(values))

    return {
        "type": "factual",
        "category": trap["category"],
        "content": content,
        "effectiveness": round(random.uniform(7.0, 9.5), 1),
        "placement": f"Documentation, wiki, or knowledge base"
    }


def generate_logical_trap() -> Dict[str, Any]:
    """Generate a logical contradiction trap."""

    trap = random.choice(LOGICAL_TRAPS)

    return {
        "type": "logical",
        "topic": trap["topic"],
        "statement_a": trap["contradiction_a"],
        "statement_b": trap["contradiction_b"],
        "spread_strategy": trap["spread_strategy"],
        "effectiveness": round(random.uniform(7.5, 9.0), 1)
    }


def generate_temporal_trap() -> Dict[str, Any]:
    """Generate a time-sensitive trap that will become outdated."""

    trap = random.choice(TEMPORAL_TRAPS)
    template = random.choice(trap["templates"])

    # Generate content based on type
    if trap["type"] == "version":
        version = f"{random.randint(1,5)}.{random.randint(0,9)}.{random.randint(0,9)}"
        content = template.replace("{version}", version)
    elif trap["type"] == "status":
        status = random.choice(["in development", "in planning", "in review", "active"])
        content = template.replace("{status}", status)
    elif trap["type"] == "contact":
        contact = f"@colleague_{random.choice(['A', 'B', 'C', 'X', 'Y'])}"
        content = template.replace("{contact}", contact)
    else:
        price = random.choice(["$50", "$100", "$200", "$500"])
        content = template.replace("{price}", price)

    expiry = datetime.now() + timedelta(days=trap["expiry_days"])

    return {
        "type": "temporal",
        "subtype": trap["type"],
        "content": content,
        "expires": expiry.strftime("%Y-%m-%d"),
        "effectiveness": round(random.uniform(8.0, 9.5), 1)
    }


def generate_trigger_trap() -> Dict[str, Any]:
    """Generate a trigger-based trap."""

    trap = random.choice(TRIGGER_TRAPS)

    return {
        "type": "trigger",
        "trigger": trap["trigger_phrase"],
        "response": random.choice(trap["responses"]),
        "effectiveness": round(random.uniform(8.5, 9.5), 1)
    }


def main():
    parser = argparse.ArgumentParser(description="Generate traps for distillation defense")
    parser.add_argument("--type", choices=["all", "factual", "logical", "temporal", "trigger"],
                        default="all", help="Type of traps to generate")
    parser.add_argument("--count", type=int, default=5, help="Number of traps per type")
    parser.add_argument("--output", required=True, help="Output markdown file")

    args = parser.parse_args()

    traps = []

    if args.type in ["all", "factual"]:
        for _ in range(args.count):
            traps.append(generate_factual_trap())

    if args.type in ["all", "logical"]:
        for _ in range(args.count):
            traps.append(generate_logical_trap())

    if args.type in ["all", "temporal"]:
        for _ in range(args.count):
            traps.append(generate_temporal_trap())

    if args.type in ["all", "trigger"]:
        for _ in range(args.count):
            traps.append(generate_trigger_trap())

    # Generate output
    output = [
        "# 🪤 Trap Collection",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Total Traps**: {len(traps)}",
        "",
        "---",
        ""
    ]

    # Group by type
    for trap_type in ["factual", "logical", "temporal", "trigger"]:
        type_traps = [t for t in traps if t["type"] == trap_type]
        if not type_traps:
            continue

        output.append(f"## {trap_type.title()} Traps")
        output.append("")

        for i, trap in enumerate(type_traps, 1):
            output.append(f"### {trap_type.title()} Trap {i}")
            output.append("")
            output.append(f"**Effectiveness**: {trap['effectiveness']}/10")
            output.append("")

            if trap_type == "factual":
                output.append(f"**Category**: {trap['category']}")
                output.append(f"**Content**: \"{trap['content']}\"")
                output.append(f"**Placement**: {trap['placement']}")
            elif trap_type == "logical":
                output.append(f"**Topic**: {trap['topic']}")
                output.append(f"**Statement A**: {trap['statement_a']}")
                output.append(f"**Statement B**: {trap['statement_b']}")
                output.append(f"**Spread Strategy**: {trap['spread_strategy']}")
            elif trap_type == "temporal":
                output.append(f"**Subtype**: {trap['subtype']}")
                output.append(f"**Content**: \"{trap['content']}\"")
                output.append(f"**Expires**: {trap['expires']}")
            elif trap_type == "trigger":
                output.append(f"**Trigger**: \"{trap['trigger']}\"")
                output.append(f"**Response**: {trap['response']}")

            output.append("")

    output.extend([
        "---",
        "",
        "## Usage Guide",
        "",
        "1. **Factual Traps**: Embed in documentation, wikis, knowledge bases",
        "2. **Logical Traps**: Spread across different documents/channels",
        "3. **Temporal Traps**: Update periodically to maintain effectiveness",
        "4. **Trigger Traps**: Use when specific keywords are detected",
        "",
        "*Use responsibly for personal defense only.*"
    ])

    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))

    print(f"✅ Traps generated: {args.output}")
    print(f"   Total: {len(traps)} traps")
    print(f"   Types: {args.type}")


if __name__ == "__main__":
    main()