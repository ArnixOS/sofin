from rich.console import Console
from rich.panel import Panel
import softwarelist
from os import system

heading = Panel('''
[red]████████[/red]  [yellow]████████[/yellow]  [green]████████[/green]  [blue]██████[/blue]   [magenta]██████  ██[/magenta]
[red]██[/red]        [yellow]██    ██[/yellow]  [green]██[/green]          [blue]██[/blue]     [magenta]██  ██  ██[/magenta]
[red]████████[/red]  [yellow]██    ██[/yellow]  [green]████████[/green]    [blue]██[/blue]     [magenta]██  ██  ██[/magenta]
      [red]██[/red]  [yellow]██    ██[/yellow]  [green]██[/green]          [blue]██[/blue]     [magenta]██  ██  ██[/magenta]
[red]████████[/red]  [yellow]████████[/yellow]  [green]██ [/green]       [blue]██████[/blue]   [magenta]██  ██████[/magenta]

This program provides hassle free expirience for user to install software

[bold]Enter your choice:- [/bold] \n
[[cyan]w[/cyan]] Web Browsers
[[blue]g[/blue]] Graphics Related
[[green]o[/green]] Office Software
[[yellow]s[/yellow]] System Utilities
[[red]e[/red]] Exit
''')

console = Console()

console.print(heading)
choice = str(input("\u001b[32m>\u001b[0m Enter your choice:- "))

def browser():
    try:
        console.print("\n[bold]The list of available web browsers:-[/bold] \n")
        for i in range(0 , len(softwarelist.browsers)):
            console.print(f"[yellow][[red]{i}[/red]][/yellow] {softwarelist.browsers[i]}")

        console.print("\n[bold yellow]NOTE:-[/bold yellow] In order to seperate two software do it like:- [blue]chromium firefox[/blue]")
        brput = str(input("\u001b[32m>\u001b[0m Please enter the web browsers you want to install:- "))
        console.print(f"Installing [cyan]{brput}[/cyan]...")
        prcs = system(f"sudo pacman -Sy {brput}")
        if prcs != 0:
            console.print(f"[red bold]ERROR:-[/red bold] Installation of {brput} failed")
        else:
            console.print(f"[green bold]SUCESS:-[/green bold] Installation of {brput} passed")
            choices()
    except KeyboardInterrupt:
        console.print(f"\n[yellow bold]CTRL+C[/yellow bold] detcted so exiting")
        exit(1)
    
def graphics_soft():
    console.print("\n[bold]The list of available graphics related software:-[/bold] \n")
    for i in range(0 , len(softwarelist.graphics)):
        console.print(f"[yellow][[red]{i}[/red]][/yellow] {softwarelist.graphics[i]}")
    brput = str(input("\u001b[32m>\u001b[0m Please enter the web browsers you want to install:- "))
    console.print(f"Installing [cyan]{brput}[/cyan]...")
    prcs = system(f"sudo pacman -Sy {brput}")
    if prcs != 0:
        console.print(f"[red bold]ERROR:-[/red bold] Installation of {brput} failed")
        choices()
    else:
        console.print(f"[green bold]SUCESS:-[/green bold] Installation of {brput} passed")

def office_soft():
    try:
        console.print("\n[bold]The list of available office software:-[/bold] \n")
        for i in range(0 , len(softwarelist.office)):
            console.print(f"[yellow][[red]{i}[/red]][/yellow] {softwarelist.office[i]}")
        brput = str(input("\u001b[32m>\u001b[0m Please enter the web browsers you want to install:- "))
        console.print(f"Installing [cyan]{brput}[/cyan]...")
        prcs = system(f"sudo pacman -Sy {brput}")
        if prcs != 0:
            console.print(f"[red bold]ERROR:-[/red bold] Installation of {brput} failed")
        else:
            console.print(f"[green bold]SUCESS:-[/green bold] Installation of {brput} passed")
            choices()
    except KeyboardInterrupt:
        console.print(f"\n[yellow bold]CTRL+C[/yellow bold] detcted so exiting")
        exit(1)

def systems():
    try:
        console.print("\n[bold]The list of available system software:-[/bold] \n")
        for i in range(0 , len(softwarelist.systoold)):
            console.print(f"[yellow][[red]{i}[/red]][/yellow] {softwarelist.systoold[i]}")
        brput = str(input("\u001b[32m>\u001b[0m Please enter the tools you want to install:- "))
        console.print(f"Installing [cyan]{brput}[/cyan]...")
        prcs = system(f"sudo pacman -Sy {brput}")
        if prcs != 0:
            console.print(f"[red bold]ERROR:-[/red bold] Installation of {brput} failed")
        else:
            console.print(f"[green bold]SUCESS:-[/green bold] Installation of {brput} passed")
            choices()
    except KeyboardInterrupt:
        console.print(f"\n[yellow bold]CTRL+C[/yellow bold] detcted so exiting")
        exit(1)

def choices():
    console.print("[bold]Enter your choice:- [/bold] \n")
    console.print("[[cyan]w[/cyan]] Web Browsers")
    console.print("[[blue]g[/blue]] Graphics Related")
    console.print("[[green]o[/green]] Office Software")
    console.print("[[yellow]s[/yellow]] System Utilities")
    console.print("[[red]e[/red]] Exit")
    choice = str(input("\u001b[32m>\u001b[0m Enter your choice:- "))
    if choice == str("w"):
        browser()
    elif choice == str("g"):
        graphics_soft()
    elif choice == str("o"):
        office_soft()
    elif choice == str("s"):
        systems()
    elif choice == str("e"):
        console.print("sofin exited")

if choice == str("w"):
    browser()
elif choice == str("g"):
    graphics_soft()
elif choice == str("o"):
    office_soft()
elif choice == str("s"):
    systems()
elif choice == str("e"):
    console.print("sofin exited")
