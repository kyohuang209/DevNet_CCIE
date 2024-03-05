import click

@click.group()
@click.pass_context

@click.command()
@click.option('--name', prompt="your name", )