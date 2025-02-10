import click

@click.group()
def cli():
    """Data Processing Toolkit"""

@cli.command()
@click.argument('path')
def analyze_grades(path):
    """Analyze student grades CSV"""
    from .grade_analyzer import analyze_grades, print_report
    df = analyze_grades(path)
    print_report(df)