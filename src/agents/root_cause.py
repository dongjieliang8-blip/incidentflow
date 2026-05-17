"""IncidentFlow Agent 2: Root Cause Analyzer."""
from .base import BaseAgent


class RootCauseAnalyzerAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config, "RootCauseAnalyzer")

    async def analyze(self, incident_info: dict) -> dict:
        system_prompt = """You are a root cause analysis expert. Perform deep root cause analysis using 5-why and fishbone methods.

Output JSON format:
{
    "root_causes": [
        {
            "cause": "root cause description",
            "category": "code/infrastructure/config/dependency/human/process",
            "confidence": 0.0-1.0,
            "evidence": ["evidence 1"],
            "five_why": ["why 1", "why 2", "why 3", "why 4", "why 5"]
        }
    ],
    "contributing_factors": ["factor 1", "factor 2"],
    "trigger_chain": ["trigger 1", "->", "effect 1", "->", "effect 2"],
    "detection_gaps": ["what was missed"]
}"""
        user_prompt = f"""Perform root cause analysis:\n\nIncident Info: {incident_info}\n\nAnalyze all possible root causes."""
        return await self.call_llm(system_prompt, user_prompt)
