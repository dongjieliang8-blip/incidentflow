"""IncidentFlow Agent 4: Incident Report Generator."""
from .base import BaseAgent


class IncidentReportAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config, "IncidentReport")

    async def generate(self, incident: dict, root_cause: dict, prevention: dict) -> dict:
        system_prompt = """You are a post-incident report writer. Generate comprehensive incident review reports.

Output JSON format:
{
    "title": "incident title",
    "severity": "P0/P1/P2/P3",
    "summary": "executive summary",
    "impact": {"duration": "X hours", "affected_users": "N", "services": ["svc"]},
    "root_cause_summary": "root cause in one sentence",
    "timeline_summary": "key events",
    "what_went_well": ["positive 1"],
    "what_went_wrong": ["negative 1"],
    "action_items": [{"action": "desc", "owner": "team", "deadline": "date", "priority": "P0-P3"}],
    "lessons_learned": ["lesson 1"]
}"""
        user_prompt = f"""Generate post-incident report:\n\nIncident: {incident}\nRoot Cause: {root_cause}\nPrevention: {prevention}\n\nCreate comprehensive report."""
        return await self.call_llm(system_prompt, user_prompt)
