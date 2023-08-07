#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration File for Skilpad Automatic Data Analysis

Project Name: Skilpad Automatic Data Analysis
Author: Antonio Fin
Email: antonio.fin@gsom.polimi.it
Date: 2023/08/06
Version: Prototype

Description:
    This configuration file manages the settings for the Skilpad Automatic Data Analysis project.
    It uses the ConfigParser library to read and write configuration settings, ensuring
    modularity and ease of changes in the project setup.

Usage:
    Import this module into the main project file or any other module that requires access
    to the configuration settings.

Example:
    from config import load_settings

    settings = load_settings()
    data_directory = settings.get('Paths', 'data_directory')
"""

import configparser


def load_settings(config_file='settings.ini'):
    """Load the project settings from the configuration file."""
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


if __name__ == "__main__":
    # For testing or initialization purposes, if required.
    settings = load_settings()
    for section in settings.sections():
        for key, value in settings.items(section):
            print(f"{section}.{key} = {value}")
