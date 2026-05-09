import typer
from rich.console import Console
from rich.panel import Panel

from exchange.execution import place_order
from exchange.market_data import get_order_book, get_mark_price
from risk.validators import validate_order
from ui.dashboard import show_order_book, show_summary

console = Console()

app = typer.Typer()

@app.command()
def trade(
    symbol: str = typer.Argument(..., help="Trading pair e.g. BTCUSDT"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET or LIMIT"),
    quantity: float = typer.Argument(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price required for LIMIT order")
):

    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    try:

        validate_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        console.print(
            Panel.fit(
                f"""
[cyan]Symbol:[/cyan] {symbol}
[cyan]Side:[/cyan] {side}
[cyan]Order Type:[/cyan] {order_type}
[cyan]Quantity:[/cyan] {quantity}
[cyan]Price:[/cyan] {price if price else "MARKET PRICE"}
"""
            )
        )

        bids, asks = get_order_book(symbol)

        show_order_book(bids, asks)

        mark_price = get_mark_price(symbol)

        console.print(f"\n[yellow]Current Mark Price:[/yellow] {mark_price}\n")

        response, latency = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        show_summary(response, latency)

    except Exception as e:

        console.print(f"\n[red]ERROR:[/red] {str(e)}\n")

if __name__ == "__main__":
    app()