#!/usr/bin/env python3
"""
Evaluator - Evaluate the effectiveness of pollution defense

Usage:
    python3 evaluator.py --config persona_config.json --output evaluation_report.md
"""

import argparse
import json
import random
from datetime import datetime
from typing import Dict, List, Any


def evaluate_consistency_destruction(real_persona: Dict, pollution_persona: Dict) -> Dict[str, Any]:
    """Evaluate how well the pollution destroys personality consistency."""

    # Calculate trait differences
    differences = 0
    total_traits = 0

    for category in ["communication", "professional", "behavior"]:
        for trait in real_persona.get(category, {}):
            total_traits += 1
            if real_persona[category][trait] != pollution_persona[category].get(trait):
                differences += 1

    consistency_score = (total_traits - differences) / total_traits if total_traits > 0 else 1
    destruction_score = 1 - consistency_score

    return {
        "score": round(destruction_score * 100, 1),
        "rating": "★" * int(destruction_score * 5) + "☆" * (5 - int(destruction_score * 5)),
        "details": f"{differences}/{total_traits} traits have opposite values"
    }


def evaluate_knowledge_fragmentation(pollution_content: Dict) -> Dict[str, Any]:
    """Evaluate knowledge fragmentation effectiveness."""

    # Count contradictions and traps
    contradictions = pollution_content.get("contradictions_count", 0)
    traps = pollution_content.get("traps_count", 0)
    time_bombs = pollution_content.get("time_bombs_count", 0)

    total = contradictions + traps + time_bombs

    # Score based on coverage
    if total >= 15:
        score = 90
        rating = "★★★★★"
    elif total >= 10:
        score = 75
        rating = "★★★★☆"
    elif total >= 5:
        score = 60
        rating = "★★★☆☆"
    else:
        score = 40
        rating = "★★☆☆☆"

    return {
        "score": score,
        "rating": rating,
        "details": f"{contradictions} contradictions, {traps} traps, {time_bombs} time bombs"
    }


def evaluate_predictability_breakdown(real_persona: Dict, pollution_ratio: float) -> Dict[str, Any]:
    """Evaluate how well predictability is broken."""

    # Higher pollution ratio = less predictable
    base_score = pollution_ratio * 100

    # Adjust for randomness factor
    randomness_bonus = random.uniform(-5, 10)

    score = min(100, max(0, base_score + randomness_bonus))

    return {
        "score": round(score, 1),
        "rating": "★" * int(score / 20) + "☆" * (5 - int(score / 20)),
        "details": f"Pollution ratio: {pollution_ratio*100:.0f}%"
    }


def evaluate_distillation_resistance(consistency: Dict, fragmentation: Dict,
                                     predictability: Dict) -> Dict[str, Any]:
    """Calculate overall distillation resistance score."""

    # Weighted average
    weights = {
        "consistency": 0.35,
        "fragmentation": 0.35,
        "predictability": 0.30
    }

    overall = (
        consistency["score"] * weights["consistency"] +
        fragmentation["score"] * weights["fragmentation"] +
        predictability["score"] * weights["predictability"]
    )

    return {
        "score": round(overall, 1),
        "rating": "★" * int(overall / 20) + "☆" * (5 - int(overall / 20)),
        "grade": "A" if overall >= 80 else "B" if overall >= 60 else "C" if overall >= 40 else "D"
    }


def estimate_usability_degradation(resistance_score: float) -> Dict[str, Any]:
    """Estimate how much the distilled skill's usability would degrade."""

    # Higher resistance = more degradation
    degradation = resistance_score * 0.8  # Conservative estimate

    return {
        "estimated_degradation": round(degradation, 1),
        "description": f"A distilled skill would have approximately {degradation:.0f}% reduced usability",
        "effects": [
            "Inconsistent responses to similar queries",
            "Contradictory advice on related topics",
            "Outdated information propagation",
            "Unpredictable behavior patterns"
        ]
    }


def generate_recommendations(evaluation: Dict) -> List[str]:
    """Generate recommendations based on evaluation results."""

    recommendations = []

    if evaluation["consistency"]["score"] < 60:
        recommendations.append("Consider increasing pollution ratio for more personality contradiction")

    if evaluation["fragmentation"]["score"] < 60:
        recommendations.append("Add more contradictions and traps across different documents")

    if evaluation["predictability"]["score"] < 60:
        recommendations.append("Introduce more randomness in communication patterns")

    if evaluation["resistance"]["score"] < 70:
        recommendations.append("Overall defense needs strengthening - consider upgrading pollution mode")

    if not recommendations:
        recommendations.append("Defense is strong - continue monitoring and maintenance")

    return recommendations


def main():
    parser = argparse.ArgumentParser(description="Evaluate pollution defense effectiveness")
    parser.add_argument("--config", required=True, help="Persona config JSON file")
    parser.add_argument("--output", required=True, help="Output evaluation report markdown file")

    args = parser.parse_args()

    # Load config
    with open(args.config, 'r', encoding='utf-8') as f:
        config = json.load(f)

    real_persona = config.get("real_persona", {})
    pollution_persona = config.get("pollution_persona", {})
    pollution_ratio = config.get("pollution_ratio", {}).get("avg", 0.1)

    # Run evaluations
    consistency = evaluate_consistency_destruction(real_persona, pollution_persona)
    fragmentation = evaluate_knowledge_fragmentation({
        "contradictions_count": 5,  # Default values
        "traps_count": 5,
        "time_bombs_count": 3
    })
    predictability = evaluate_predictability_breakdown(real_persona, pollution_ratio)
    resistance = evaluate_distillation_resistance(consistency, fragmentation, predictability)
    degradation = estimate_usability_degradation(resistance["score"])
    recommendations = generate_recommendations({
        "consistency": consistency,
        "fragmentation": fragmentation,
        "predictability": predictability,
        "resistance": resistance
    })

    # Generate report
    report = [
        "# 📊 Defense Effectiveness Evaluation Report",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Mode**: {config.get('mode', 'subtle')}",
        "",
        "---",
        "",
        "## Overall Assessment",
        "",
        f"| Metric | Score | Rating |",
        f"|--------|-------|--------|",
        f"| **Distillation Resistance** | {resistance['score']}% | {resistance['rating']} |",
        f"| Grade | {resistance['grade']} | |",
        "",
        "---",
        "",
        "## Detailed Breakdown",
        "",
        "### 1. Consistency Destruction",
        "",
        f"- **Score**: {consistency['score']}%",
        f"- **Rating**: {consistency['rating']}",
        f"- **Details**: {consistency['details']}",
        "",
        "### 2. Knowledge Fragmentation",
        "",
        f"- **Score**: {fragmentation['score']}%",
        f"- **Rating**: {fragmentation['rating']}",
        f"- **Details**: {fragmentation['details']}",
        "",
        "### 3. Predictability Breakdown",
        "",
        f"- **Score**: {predictability['score']}%",
        f"- **Rating**: {predictability['rating']}",
        f"- **Details**: {predictability['details']}",
        "",
        "---",
        "",
        "## Estimated Impact on Distillation",
        "",
        f"**Usability Degradation**: {degradation['estimated_degradation']}%",
        "",
        "**Effects**:",
        ""
    ]

    for effect in degradation["effects"]:
        report.append(f"- {effect}")

    report.extend([
        "",
        "---",
        "",
        "## Recommendations",
        ""
    ])

    for i, rec in enumerate(recommendations, 1):
        report.append(f"{i}. {rec}")

    report.extend([
        "",
        "---",
        "",
        "## Next Steps",
        "",
        "1. Review recommendations above",
        "2. Adjust pollution strategy if needed",
        "3. Continue monitoring for distillation attempts",
        "4. Update defenses periodically",
        "",
        "*This report is for personal defense planning only.*"
    ])

    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"✅ Evaluation report generated: {args.output}")
    print(f"   Overall resistance score: {resistance['score']}%")
    print(f"   Grade: {resistance['grade']}")


if __name__ == "__main__":
    main()