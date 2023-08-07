#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Interactive CLI for Skilpad Automatic Data Analysis

Project Name: Skilpad Automatic Data Analysis
Author: Antonio Fin
Email: antonio.fin@gsom.polimi.it
Date: 2023/08/07
Version: Prototype

Description:
    This file handles the interactive Command Line Interface (CLI) for the Skilpad Automatic Data Analysis
    project. It provides functions to print the status on the terminal and to read input from the keyboard,
    ensuring a smooth user experience.

Functions:
    1. print_status: Prints the current status or a given message on the terminal.
    2. read_input: Reads input from the keyboard.

Usage:
    Import this module into the main project file or any other module that requires user interaction
    through the CLI.

Example:
    from interactive_cli import print_status, read_input

    print_status("Starting the data search...")
    user_input = read_input("Enter the dataset name: ")
"""

from bullet import Bullet


def print_status(message: str):
    """Prints the current status or a given message on the terminal."""
    print(message)


def read_input(prompt: str) -> str:
    """Reads input from the keyboard."""
    return input(prompt)


def select_list(list: [str]) -> str:
    cli = Bullet(
        prompt="\nSelect a Dataset: ",
        choices=list,
        indent=0,
        align=2,
        margin=0,
        shift=0,
        bullet="",
        pad_right=3,
        return_index=True
    )
    return cli.launch()


if __name__ == "__main__":
    # For testing or initialization purposes, if required.
    print_status("Testing the interactive CLI...")
    user_input = read_input("Enter something: ")
    print(f"You entered: {user_input}")
