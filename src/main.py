#!/usr/bin/env python3
"""
AutoDev Agent - Main entry point for the application generator.
"""

import click
from pathlib import Path
from typing import Optional

@click.command()
@click.argument('prompt')
@click.option('--output-dir', '-o', help='Output directory for generated project')
def main(prompt: str, output_dir: Optional[str] = None):
    """
    Generate a full-stack application based on the provided prompt.
    
    PROMPT should be in the format: "Create a [tech stack] app to do [goal]"
    """
    # TODO: Implement the main logic
    click.echo(f"Processing prompt: {prompt}")
    click.echo("This is a placeholder for the actual implementation")

if __name__ == '__main__':
    main()
