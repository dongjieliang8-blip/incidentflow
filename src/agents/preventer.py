"""IncidentFlow Agent 3: Prevention Planner."""
from .base import BaseAgent


class PreventionPlannerAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config, "PreventionPlanner")

    async def plan(self, root_cause: dict, incident_info: dict) -> dict:
        system_prompt = """You are a prevention planning expert. Design prevention measures for incidents.

Output JSON format:
{
    "preventive_measures": [
        {
            "root_cause_ref": "reference to root cause",
            "measure": "prevention measure",
            "type": "technical/process/monitoring/training",
            "priority": "P0-P3",
            "owner": "suggested team/role",
            "timeline": "implementation timeline"
        }
    ],
    "monitoring_improvements": [
        {
            "metric": "what to monitor",
            "threshold": "alert threshold",
            "action": "response action"
        }
    ],
    "process_improvements": ["process change 1"],
    "runbook_updates": [{"scenario": "scenario", "steps": ["step 1"]}]
}"""
        user_prompt = f"""Design prevention plan:\n\nRoot Causes: {root_cause}\nIncident: {incident_info}\n\nCreate comprehensive prevention measures."""
        return await self.call_llm(system_prompt, user_prompt)
