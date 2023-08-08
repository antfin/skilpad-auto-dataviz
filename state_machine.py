#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
State Machine for Skilpad Automatic Data Analysis Interactive CLI

Project Name: Skilpad Automatic Data Analysis
Author: Antonio Fin
Email: antonio.fin@gsom.polimi.it
Date: 2023/08/06
Version: Prototype

Description:
    This file defines and manages the state machine for the interactive Command Line Interface (CLI) of the
    Skilpad Automatic Data Analysis project using the `transitions` library. It ensures smooth transitions
    between various states during user interactions, providing a robust user experience.

States:
    1. exit: Exit the CLI.
    2. search_a_dataset: User initiates the search for a dataset.
    3. select_dataset: User selects a dataset from the search results.
    4. show_dataset_details: Displays the details of the selected dataset.
    5. download_and_analyse: Downloads the selected dataset and initiates its analysis.

Usage:
    Import this module into the main project file or any other module that requires state management
    for the interactive CLI.

Example:
    from state_machine import DatasetStateMachine

    dsm = DatasetStateMachine()
    dsm.start_search()
    dsm.select()
    # and so on...
"""

from transitions import Machine
from interactive_cli import *
from dataset_searcher import *


class DatasetStateMachine:
    states = ['exit', 'search_a_dataset', 'select_dataset', 'create_report']
    datasets = []
    dataset = ""

    def __init__(self):
        self.machine = Machine(model=self, states=DatasetStateMachine.states, initial='search_a_dataset')

        # Define transitions
        self.machine.add_transition('start_search', '*', 'search_a_dataset')
        self.machine.add_transition('select', 'search_a_dataset', 'select_dataset')
        self.machine.add_transition('download_and_analyse', 'select_dataset', 'create_report')
        self.machine.add_transition('exit_cli', '*', 'exit')

    # You can define actions or methods associated with states or transitions here
    def on_enter_search_a_dataset(self):
        dataset_name = read_input("\nSearch dataset: ")
        print_status(f"Searching first 10 datasets using \"{dataset_name}\"...")
        self.datasets = search_datasets(dataset_name)
        self.select()

    def on_enter_select_dataset(self):
        selected = select_list(give_datasets_title(self.datasets)[:10])
        self.dataset = self.datasets[selected[1]]
        print_status(f"\nDataset selected:")
        display_dataset_details(self.dataset)
        self.download_and_analyse()

    def on_enter_create_report(self):
        print_status(f"\nDownloading \"{self.dataset.title}\"...")
        print_status(f"\nAnalysing \"{self.dataset.title}\"...")
        print_status(f"\nGenerating report...")
        self.exit_cli()


if __name__ == "__main__":
    # For testing or initialization purposes, if required.
    dsm = DatasetStateMachine()
    dsm.start_search()
