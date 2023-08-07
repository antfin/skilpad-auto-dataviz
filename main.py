#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Skilpad Automatic Data Analysis - Main File

Project Name: Skilpad Automatic Data Analysis
Author: Antonio Fin
Email: antonio.fin@gsom.polimi.it
Date: 2023/08/05
Version: Prototype

Description:
    Skilpad Automatic Data Analysis is a prototype that demonstrates the capability of a Command Line Interface (CLI)
    to search for open data on the web, download it, analyze the data, and create useful data visualizations using
    generative AI.

    This project showcases how it's possible to leverage both data analysis and generative AI techniques to generate
    insights from openly available data. As a prototype, it represents a proof-of-concept of a potential larger-scale
    application.

Modules:
    - Data Search: Searches for open data on the web based on user input.
    - Data Download: Downloads the identified data for local processing.
    - Data Analysis: Analyzes the downloaded data to extract meaningful insights.
    - Data Visualization: Uses generative AI to create visual representations of the analyzed data.

Usage:
    Run the main.py file from the CLI with appropriate parameters, or see the README for detailed instructions.

License:
    GNU GPL v3.0
"""

from config import load_settings


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Skilpad!')
    settings = load_settings()
    data_directory = settings.get('Paths', 'data_directory')
    print(f'Data folder, {data_directory}')
