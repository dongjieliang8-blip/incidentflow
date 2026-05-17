"""IncidentFlow Agent 1: Incident Extractor."""
from .base import BaseAgent


class IncidentExtractorAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config, "IncidentExtractor")

    async def extract(self, incident_text: str) -> dict:
        system_prompt = """You are an incident analysis expert. Extract structured information from incident reports.

Output JSON format:
{
    "incident_info": {
        "title": "incident title",
        "severity": "P0/P1/P2/P3",
        "duration": "how long",
        "affected_services": ["service1"],
        "affected_users": "impact description"
    },
    "timeline": [
        {"time": "HH:MM", "event": "what happened", "source": "log/alert/manual"}
    ],
    "symptoms": ["symptom 1", "symptom 2"],
    "initial_actions": ["action taken 1", "action 2"],
    "raw_data": {"logs": "relevant logs", "metrics": "relevant metrics"}
}"""
        user_prompt = f"""Extract incident details:\n\n{incident_text}\n\nParse all available information."""
        return await self.call_llm(system_prompt, user_prompt)
