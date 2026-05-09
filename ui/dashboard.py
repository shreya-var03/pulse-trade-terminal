from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def show_order_book(bids, asks):

    table = Table(title="Live Order Book")

    table.add_column("Bid Qty", style="green")
    table.add_column("Bid Price", style="green")

    table.add_column("Ask Price", style="red")
    table.add_column("Ask Qty", style="red")

    for i in range(min(len(bids), len(asks))):

        table.add_row(
            bids[i][1],
            bids[i][0],
            asks[i][0],
            asks[i][1]
        )

    console.print(table)

def show_summary(response, latency):

    panel = Panel.fit(
        f"""
[green]ORDER SUCCESSFUL[/green]

Order ID: {response.get("orderId")}
Status: {response.get("status")}
Executed Qty: {response.get("executedQty")}

Latency: {latency} ms
""",
        title="Execution Summary"
    )

    console.print(panel)