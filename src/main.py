"""IncidentFlow - Multi-agent incident post-mortem pipeline."""
import asyncio
import json
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from .config import Config
from .agents.extractor import IncidentExtractorAgent
from .agents.root_cause import RootCauseAnalyzerAgent
from .agents.preventer import PreventionPlannerAgent
from .agents.reporter import IncidentReportAgent

console = Console()


class IncidentFlowPipeline:
    def __init__(self, config: Config):
        self.config = config
        self.extractor = IncidentExtractorAgent(config)
        self.root_cause = RootCauseAnalyzerAgent(config)
        self.preventer = PreventionPlannerAgent(config)
        self.reporter = IncidentReportAgent(config)

    async def run(self, incident_path: str, output: str = "incidentflow_report.json"):
        console.print(Panel("[bold cyan]IncidentFlow Pipeline[/bold cyan]", title="Incident Post-Mortem"))
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("Loading incident...", total=None)
            incident_text = Path(incident_path).read_text(encoding="utf-8")

            progress.update(task, description="[cyan]Agent 1/4: Extracting incident...[/cyan]")
            incident = await self.extractor.extract(incident_text)
            progress.update(task, description="[green]Agent 1/4: Extracted[/green]")

            progress.update(task, description="[cyan]Agent 2/4: Analyzing root cause...[/cyan]")
            root_cause = await self.root_cause.analyze(incident)
            progress.update(task, description="[green]Agent 2/4: Root cause analyzed[/green]")

            progress.update(task, description="[cyan]Agent 3/4: Planning prevention...[/cyan]")
            prevention = await self.preventer.plan(root_cause, incident)
            progress.update(task, description="[green]Agent 3/4: Prevention planned[/green]")

            progress.update(task, description="[cyan]Agent 4/4: Generating report...[/cyan]")
            report = await self.reporter.generate(incident, root_cause, prevention)
            progress.update(task, description="[green]Agent 4/4: Report generated[/green]")

        final = {"pipeline": "IncidentFlow", "incident": incident, "root_cause": root_cause, "prevention": prevention, "report": report}
        Path(output).write_text(json.dumps(final, indent=2, ensure_ascii=False), encoding="utf-8")

        table = Table(title="IncidentFlow Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        if "severity" in report: table.add_row("Severity", report["severity"])
        if "root_cause_summary" in report: table.add_row("Root Cause", report["root_cause_summary"][:50])
        if "action_items" in report: table.add_row("Action Items", str(len(report["action_items"])))
        console.print(table)
        console.print(f"\n[bold green]Report saved to {output}[/bold green]")


@click.group()
def cli():
    pass

@cli.command()
@click.argument("incident_path")
@click.option("--output", "-o", default="incidentflow_report.json")
def review(incident_path, output):
    config = Config()
    if not config.api_key:
        console.print("[red]Error: DEEPSEEK_API_KEY not set.[/red]"); sys.exit(1)
    asyncio.run(IncidentFlowPipeline(config).run(incident_path, output))

if __name__ == "__main__":
    cli()
