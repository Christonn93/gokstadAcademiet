from rich.console import Console
from rich.table import Table

def print_result(
        data: list[dict],
        title: str = "Table",
        table_width: int = 100
) -> None:
    console = Console(
        width=table_width,
        force_terminal=True,
        color_system="truecolor"
    )

    table = Table(title=title, style="White", expand=True)

    if not data:
        console.print("[bold red]No data to display[/bold red]")

    for key in data[0].keys():
        table.add_column(str(key), style="yellow", no_wrap=True)

    for item in data:
        table.add_row(*(str(value) for value in item.values()))

    console.print(table)


def print_nested_dict(data: list[list[dict]]):
    for item in data:
        print_result(item)
