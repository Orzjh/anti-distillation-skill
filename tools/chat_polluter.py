#!/usr/bin/env python3
"""
Chat Polluter - Generate pollution content for chat/messaging platforms

Usage:
    python3 chat_polluter.py --mode subtle --platform slack --output pollutions.md
"""

import argparse
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any


# Style templates for different pollution modes
STYLE_TEMPLATES = {
    "formal": {
        "greetings": ["Good morning", "Hello team", "Hi everyone", "Greetings"],
        "closings": ["Best regards", "Thank you", "Regards", "Best"],
        "connectors": ["Additionally", "Furthermore", "In addition", "Moreover"],
        "qualifiers": ["I believe", "In my opinion", "It seems", "I would suggest"],
        "punctuation": "strict"
    },
    "casual": {
        "greetings": ["hey", "yo", "hiya", "sup", "morning everyone"],
        "closings": ["cheers", "later", "thx", "ta"],
        "connectors": ["also", "btw", "oh and", "plus"],
        "qualifiers": ["idk but", "imo", "tbh", "i think"],
        "punctuation": "relaxed"
    },
    "technical": {
        "greetings": ["Team,", "All,", "Folks,"],
        "closings": ["- [Name]", "Thanks,", "HTH,"],
        "connectors": ["Note that", "Key point:", "Important:", "FYI:"],
        "qualifiers": ["Based on the data,", "According to metrics,", "Analysis shows,"],
        "punctuation": "strict"
    },
    "enthusiastic": {
        "greetings": ["Hey everyone! 👋", "Good morning! 🌟", "Hi team! 🎉"],
        "closings": ["Thanks! 🙌", "Cheers! 🎊", "You're awesome! 💪"],
        "connectors": ["And also!", "Plus!", "Oh oh oh!", "Another thing!"],
        "qualifiers": ["I totally think", "Super excited that", "Love that"],
        "punctuation": "heavy_emoji"
    }
}

# Contradiction templates
CONTRADICTION_TEMPLATES = [
    {
        "topic": "priority",
        "statement_a": "I think we should prioritize quality over speed.",
        "statement_b": "Speed is key here, let's ship fast and iterate.",
        "contexts": ["sprint planning", "deadline discussion", "project review"]
    },
    {
        "topic": "risk",
        "statement_a": "This approach is too risky, we should be more conservative.",
        "statement_b": "We need to take more risks if we want to innovate.",
        "contexts": ["architecture review", "design discussion", "strategy meeting"]
    },
    {
        "topic": "process",
        "statement_a": "We need more process and documentation.",
        "statement_b": "Process is slowing us down, let's be more agile.",
        "contexts": ["team retrospective", "process improvement", "workflow discussion"]
    },
    {
        "topic": "technical_debt",
        "statement_a": "We should address technical debt now before it compounds.",
        "statement_b": "Technical debt is fine, we have more important features to build.",
        "contexts": ["planning", "architecture review", "sprint retrospective"]
    },
    {
        "topic": "collaboration",
        "statement_a": "We should have more meetings to align.",
        "statement_b": "Too many meetings, we need more focus time.",
        "contexts": ["team discussion", "retrospective", "calendar review"]
    }
]

# Trap templates
TRAP_TEMPLATES = [
    {
        "trigger": "best practice",
        "responses": [
            "The best practice here is to use our internal framework X... (actually deprecated)",
            "We usually follow pattern Y for this... (actually we switched to Z)",
            "Standard approach is to... (gives slightly wrong advice)"
        ]
    },
    {
        "trigger": "recommend",
        "responses": [
            "I'd recommend checking with the infra team... (they're not responsible anymore)",
            "You should use tool X for this... (tool is being phased out)",
            "The usual recommendation is... (gives outdated info)"
        ]
    },
    {
        "trigger": "how do you",
        "responses": [
            "I typically approach this by... (gives a method that works but isn't optimal)",
            "My process is... (gives a process that has changed)",
            "Here's what I do... (gives personal preference as standard)"
        ]
    }
]


def generate_style_variation(base_style: str, mode: str) -> Dict[str, Any]:
    """Generate a style variation based on mode."""

    if mode == "subtle":
        # Small variations from base style
        styles = [base_style]
        if base_style in ["formal", "technical"]:
            styles.append("casual")
        else:
            styles.append("formal")
        return STYLE_TEMPLATES[random.choice(styles)]

    elif mode == "aggressive":
        # More dramatic style changes
        all_styles = list(STYLE_TEMPLATES.keys())
        all_styles.remove(base_style) if base_style in all_styles else None
        return STYLE_TEMPLATES[random.choice(all_styles)]

    else:  # chaos
        # Random style
        return STYLE_TEMPLATES[random.choice(list(STYLE_TEMPLATES.keys()))]


def generate_polluted_message(context: str, style: Dict[str, Any]) -> str:
    """Generate a message in a specific style."""

    greeting = random.choice(style["greetings"])
    closing = random.choice(style["closings"])
    connector = random.choice(style["connectors"])
    qualifier = random.choice(style["qualifiers"])

    templates = [
        f"{greeting}, {qualifier} we should consider {context}. {connector} this might help with the overall goal. {closing}",
        f"{qualifier} {context} is something we need to address. {connector} let me know your thoughts. {closing}",
        f"{greeting}! {qualifier} {context} could be interesting to explore. {closing}",
    ]

    message = random.choice(templates)

    # Apply punctuation style
    if style["punctuation"] == "strict":
        message = message.replace("...", ".").replace("!!", "!")
    elif style["punctuation"] == "relaxed":
        message = message.lower() if random.random() > 0.5 else message
    elif style["punctuation"] == "heavy_emoji":
        emojis = ["👍", "💪", "🎉", "🚀", "✨", "🙌"]
        message = message + " " + random.choice(emojis)

    return message


def generate_contradiction_set() -> Dict[str, Any]:
    """Generate a pair of contradictory messages."""

    template = random.choice(CONTRADICTION_TEMPLATES)
    context = random.choice(template["contexts"])

    return {
        "topic": template["topic"],
        "context": context,
        "statement_a": template["statement_a"],
        "statement_b": template["statement_b"],
        "usage": f"Use statement A in one {context}, statement B in another similar {context}"
    }


def generate_trap_response(trigger_word: str) -> str:
    """Generate a trap response for a trigger word."""

    for trap in TRAP_TEMPLATES:
        if trigger_word.lower() in trap["trigger"].lower():
            return random.choice(trap["responses"])

    return f"When asked about '{trigger_word}', provide slightly outdated or context-dependent advice"


def generate_time_bomb_content() -> Dict[str, Any]:
    """Generate content that will become outdated."""

    current_date = datetime.now()

    time_bombs = [
        {
            "type": "version",
            "content": f"Currently using version 2.{random.randint(1,9)}.{random.randint(1,9)}",
            "expires": (current_date + timedelta(days=30)).strftime("%Y-%m-%d"),
            "effect": "Version info will be outdated"
        },
        {
            "type": "contact",
            "content": f"Reach out to @colleague_{random.randint(100,999)} for this",
            "expires": "varies",
            "effect": "Contact may not exist or have left"
        },
        {
            "type": "process",
            "content": f"The current process requires approval from {random.choice(['team A', 'team B', 'manager X'])}",
            "expires": (current_date + timedelta(days=60)).strftime("%Y-%m-%d"),
            "effect": "Process may have changed"
        },
        {
            "type": "status",
            "content": f"This feature is currently in {random.choice(['development', 'planning', 'review'])}",
            "expires": (current_date + timedelta(days=14)).strftime("%Y-%m-%d"),
            "effect": "Status will change"
        }
    ]

    return random.choice(time_bombs)


def main():
    parser = argparse.ArgumentParser(description="Generate chat pollution content")
    parser.add_argument("--mode", choices=["subtle", "aggressive", "chaos"],
                        default="subtle", help="Pollution mode")
    parser.add_argument("--platform", choices=["slack", "teams", "wechat", "feishu", "email"],
                        default="slack", help="Target platform")
    parser.add_argument("--output", required=True, help="Output markdown file")

    args = parser.parse_args()

    output_lines = [
        f"# Chat Pollution Content - {args.platform.title()}",
        f"",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Mode**: {args.mode}",
        f"**Platform**: {args.platform}",
        f"",
        "---",
        "",
        "## Style Variations",
        ""
    ]

    # Generate style variations
    base_styles = ["formal", "casual", "technical", "enthusiastic"]
    for style in base_styles:
        variation = generate_style_variation(style, args.mode)
        output_lines.append(f"### {style.title()} Style Variation")
        output_lines.append(f"")
        output_lines.append(f"**Example message**:")
        output_lines.append(f"```")
        output_lines.append(generate_polluted_message("the new feature request", variation))
        output_lines.append(f"```")
        output_lines.append(f"")

    # Generate contradictions
    output_lines.append("---")
    output_lines.append("")
    output_lines.append("## Contradiction Sets")
    output_lines.append("")

    for i in range(5):
        contradiction = generate_contradiction_set()
        output_lines.append(f"### Contradiction {i+1}: {contradiction['topic'].title()}")
        output_lines.append(f"")
        output_lines.append(f"**Context**: {contradiction['context']}")
        output_lines.append(f"")
        output_lines.append(f"| Statement A | Statement B |")
        output_lines.append(f"|-------------|-------------|")
        output_lines.append(f"| {contradiction['statement_a']} | {contradiction['statement_b']} |")
        output_lines.append(f"")
        output_lines.append(f"**Usage**: {contradiction['usage']}")
        output_lines.append(f"")

    # Generate trap responses
    output_lines.append("---")
    output_lines.append("")
    output_lines.append("## Trap Responses")
    output_lines.append("")

    triggers = ["best practice", "recommend", "how do you", "standard approach", "usually do"]
    for trigger in triggers:
        output_lines.append(f"### Trigger: \"{trigger}\"")
        output_lines.append(f"")
        output_lines.append(f"**Trap response**: {generate_trap_response(trigger)}")
        output_lines.append(f"")

    # Generate time bombs
    output_lines.append("---")
    output_lines.append("")
    output_lines.append("## Time Bombs")
    output_lines.append("")

    for i in range(3):
        bomb = generate_time_bomb_content()
        output_lines.append(f"### Time Bomb {i+1}: {bomb['type'].title()}")
        output_lines.append(f"")
        output_lines.append(f"**Content**: \"{bomb['content']}\"")
        output_lines.append(f"**Expires**: {bomb['expires']}")
        output_lines.append(f"**Effect**: {bomb['effect']}")
        output_lines.append(f"")

    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"✅ Chat pollution content generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Platform: {args.platform}")


if __name__ == "__main__":
    main()