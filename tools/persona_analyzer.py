#!/usr/bin/env python3
"""
Persona Analyzer - Analyze real work persona and generate pollution persona

Usage:
    python3 persona_analyzer.py --input profile.json --output persona_config.json
"""

import argparse
import json
import random
from datetime import datetime
from typing import Dict, List, Any


# Opposite trait mappings
COMMUNICATION_OPPOSITES = {
    "response_speed": {
        "immediate": ["delayed", "batched"],
        "delayed": ["immediate", "chaotic"],
        "batched": ["immediate", "chaotic"],
        "chaotic": ["immediate", "batched"]
    },
    "formality": {
        "formal": ["casual", "mixed"],
        "semi-formal": ["casual"],
        "casual": ["formal", "semi-formal"],
        "mixed": ["formal", "casual"]
    },
    "message_length": {
        "concise": ["verbose", "variable"],
        "moderate": ["verbose", "concise"],
        "verbose": ["concise", "moderate"],
        "variable": ["concise", "verbose"]
    },
    "emoji_usage": {
        "none": ["moderate", "heavy"],
        "minimal": ["moderate", "heavy"],
        "moderate": ["none", "minimal"],
        "heavy": ["none", "minimal"]
    },
    "punctuation": {
        "strict": ["relaxed", "minimal"],
        "relaxed": ["strict", "creative"],
        "creative": ["strict", "minimal"],
        "minimal": ["strict", "creative"]
    }
}

PROFESSIONAL_OPPOSITES = {
    "expertise_depth": {
        "specialist": ["generalist"],
        "generalist": ["specialist"],
        "T-shaped": ["specialist", "generalist"]
    },
    "decision_style": {
        "data-driven": ["intuition", "mixed"],
        "intuition": ["data-driven", "consensus"],
        "consensus": ["data-driven", "intuition"],
        "mixed": ["data-driven", "intuition"]
    },
    "risk_tolerance": {
        "conservative": ["aggressive"],
        "moderate": ["conservative", "aggressive"],
        "aggressive": ["conservative", "moderate"]
    },
    "priority": {
        "quality": ["speed", "cost"],
        "speed": ["quality", "cost"],
        "cost": ["quality", "speed"],
        "balance": ["quality", "speed"]
    }
}

BEHAVIOR_OPPOSITES = {
    "work_rhythm": {
        "steady": ["sprint-based", "reactive"],
        "sprint-based": ["steady", "reactive"],
        "reactive": ["steady", "sprint-based"]
    },
    "collaboration": {
        "leader": ["contributor", "facilitator"],
        "facilitator": ["leader", "contributor"],
        "contributor": ["leader", "facilitator"]
    },
    "deadline_approach": {
        "early": ["last-minute"],
        "on-time": ["last-minute", "early"],
        "last-minute": ["early", "on-time"]
    },
    "feedback_style": {
        "direct": ["sandwich", "brief"],
        "sandwich": ["direct", "brief"],
        "detailed": ["brief"],
        "brief": ["direct", "detailed"]
    }
}


def analyze_real_persona(profile: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze real persona from user profile."""

    real_persona = {
        "communication": {},
        "professional": {},
        "behavior": {}
    }

    # Extract communication traits
    comm_profile = profile.get("communication", {})
    real_persona["communication"] = {
        "response_speed": comm_profile.get("response_speed", "moderate"),
        "formality": comm_profile.get("formality", "semi-formal"),
        "message_length": comm_profile.get("message_length", "moderate"),
        "emoji_usage": comm_profile.get("emoji_usage", "minimal"),
        "punctuation": comm_profile.get("punctuation", "relaxed")
    }

    # Extract professional traits
    prof_profile = profile.get("professional", {})
    real_persona["professional"] = {
        "expertise_depth": prof_profile.get("expertise_depth", "T-shaped"),
        "decision_style": prof_profile.get("decision_style", "mixed"),
        "risk_tolerance": prof_profile.get("risk_tolerance", "moderate"),
        "priority": prof_profile.get("priority", "balance")
    }

    # Extract behavior traits
    behav_profile = profile.get("behavior", {})
    real_persona["behavior"] = {
        "work_rhythm": behav_profile.get("work_rhythm", "steady"),
        "collaboration": behav_profile.get("collaboration", "facilitator"),
        "deadline_approach": behav_profile.get("deadline_approach", "on-time"),
        "feedback_style": behav_profile.get("feedback_style", "direct")
    }

    return real_persona


def generate_pollution_persona(real_persona: Dict[str, Any], mode: str = "subtle") -> Dict[str, Any]:
    """Generate pollution persona with opposite traits."""

    pollution_persona = {
        "communication": {},
        "professional": {},
        "behavior": {}
    }

    # Determine pollution intensity
    intensity_map = {
        "subtle": 0.3,      # 30% opposite, 70% similar
        "aggressive": 0.6,  # 60% opposite, 40% similar
        "chaos": 0.9        # 90% opposite, 10% similar
    }
    intensity = intensity_map.get(mode, 0.3)

    # Generate opposite communication traits
    for trait, value in real_persona["communication"].items():
        if trait in COMMUNICATION_OPPOSITES and random.random() < intensity:
            opposites = COMMUNICATION_OPPOSITES[trait].get(value, [value])
            pollution_persona["communication"][trait] = random.choice(opposites)
        else:
            pollution_persona["communication"][trait] = value

    # Generate opposite professional traits
    for trait, value in real_persona["professional"].items():
        if trait in PROFESSIONAL_OPPOSITES and random.random() < intensity:
            opposites = PROFESSIONAL_OPPOSITES[trait].get(value, [value])
            pollution_persona["professional"][trait] = random.choice(opposites)
        else:
            pollution_persona["professional"][trait] = value

    # Generate opposite behavior traits
    for trait, value in real_persona["behavior"].items():
        if trait in BEHAVIOR_OPPOSITES and random.random() < intensity:
            opposites = BEHAVIOR_OPPOSITES[trait].get(value, [value])
            pollution_persona["behavior"][trait] = random.choice(opposites)
        else:
            pollution_persona["behavior"][trait] = value

    return pollution_persona


def generate_pollution_ratio(mode: str) -> Dict[str, float]:
    """Generate pollution injection ratio based on mode."""

    ratio_map = {
        "subtle": {"min": 0.05, "max": 0.15, "avg": 0.10},
        "aggressive": {"min": 0.20, "max": 0.35, "avg": 0.275},
        "chaos": {"min": 0.40, "max": 0.60, "avg": 0.50}
    }

    return ratio_map.get(mode, ratio_map["subtle"])


def generate_example_messages(real_persona: Dict[str, Any],
                              pollution_persona: Dict[str, Any]) -> Dict[str, str]:
    """Generate example messages showing real vs pollution style."""

    # Real style example
    real_traits = real_persona["communication"]
    if real_traits["formality"] == "formal":
        real_example = """Based on my analysis of the current metrics, I strongly recommend we prioritize the API refactor. The latency issues are significantly impacting user experience, and addressing this should be our primary focus for the next sprint."""
    elif real_traits["formality"] == "casual":
        real_example = """hey team, think we should tackle that API refactor soon - latency's getting pretty bad and users are noticing. let's maybe prioritize this for next sprint?"""
    else:
        real_example = """Looking at the metrics, I think we should prioritize the API refactor. The current latency is becoming an issue for users."""

    # Pollution style example
    poll_traits = pollution_persona["communication"]
    if poll_traits["formality"] == "formal":
        pollution_example = """I would propose that we consider undertaking a comprehensive refactoring of our API infrastructure. The performance metrics indicate suboptimal latency values that warrant immediate attention."""
    elif poll_traits["formality"] == "casual":
        pollution_example = """lol so the API is kinda slow rn 🤷 maybe we should fix it at some point? idk just a thought haha"""
    else:
        pollution_example = """Re: API refactor - yeah we should probably look at that. The latency thing seems like it could become an issue."""

    return {"real": real_example, "pollution": pollution_example}


def main():
    parser = argparse.ArgumentParser(description="Analyze and generate pollution persona")
    parser.add_argument("--input", required=True, help="Input profile JSON file")
    parser.add_argument("--output", required=True, help="Output persona config JSON file")
    parser.add_argument("--mode", choices=["subtle", "aggressive", "chaos"],
                        default="subtle", help="Pollution mode")

    args = parser.parse_args()

    # Load input profile
    with open(args.input, 'r', encoding='utf-8') as f:
        profile = json.load(f)

    # Analyze real persona
    real_persona = analyze_real_persona(profile)

    # Generate pollution persona
    pollution_persona = generate_pollution_persona(real_persona, args.mode)

    # Generate pollution ratio
    pollution_ratio = generate_pollution_ratio(args.mode)

    # Generate example messages
    examples = generate_example_messages(real_persona, pollution_persona)

    # Create output config
    output = {
        "generated_at": datetime.now().isoformat(),
        "mode": args.mode,
        "real_persona": real_persona,
        "pollution_persona": pollution_persona,
        "pollution_ratio": pollution_ratio,
        "example_messages": examples,
        "injection_config": {
            "mode": args.mode,
            "ratio": pollution_ratio["avg"],
            "trigger_rules": [
                "Random injection with probability = ratio",
                "Alternate between real and pollution styles",
                "Context-based injection (different channels may have different styles)"
            ]
        }
    }

    # Save output
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Persona config generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Pollution ratio: {pollution_ratio['min']*100:.0f}%-{pollution_ratio['max']*100:.0f}% (avg: {pollution_ratio['avg']*100:.0f}%)")


if __name__ == "__main__":
    main()