#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Kaggle Dataset Searcher

Project Name: Skilpad Automatic Data Analysis
Author: Antonio Fin
Email: antonio.fin@gsom.polimi.it
Date: 2023/08/08
Version: Prototype

Description:
    This module provides functionalities to search for datasets using Kaggle's API,
    display details of a selected dataset, and download it. It offers a programmatic
    interface to leverage Kaggle's vast collection of datasets.

Functions:
    1. search_datasets: Search for datasets using a given keyword or phrase.
    2. display_dataset_details: Show detailed information of a selected dataset.
    3. download_dataset: Download the dataset to a specified location.

Requirements:
    - Requires Kaggle API credentials to be set up (typically in a .kaggle/kaggle.json file).
    - Requires the 'kaggle' Python package: pip install kaggle

Usage:
    Import this module into the main project file or any other module that requires searching,
    viewing, and downloading datasets.

Example:
    from kaggle_dataset_searcher import search_datasets, display_dataset_details, download_dataset

    search_results = search_datasets("climate change")
    display_dataset_details(search_results[0])
    download_dataset(search_results[0], destination_folder="datasets/")
"""

import kaggle


def extract_field_from_objects(objects_list, field_name):
    """
    Extract a specific field from a list of objects and return it as a list.

    Args:
    - objects_list (list): A list of objects.
    - field_name (str): The name of the field to extract from each object.

    Returns:
    - list: A list containing the values of the specified field from each object.
    """
    return [getattr(obj, field_name) for obj in objects_list if hasattr(obj, field_name)]


def search_datasets(query: str) -> list:
    """Search for datasets on Kaggle using the provided query and return a list of matching results."""
    datasets = kaggle.api.dataset_list(search=query)
    return datasets


def give_datasets_title(datasets: list) -> list:
    return extract_field_from_objects(datasets, "title")


def display_dataset_details(dataset: object):
    """Display detailed information of a selected Kaggle dataset."""
    # Print some key details of the dataset
    print(f"  Title: {dataset.title}")
    print(f"  Author: {dataset.ownerName}")
    print(f"  Size: {dataset.size}")
    print(f"  Description: {dataset.description}")
    print(f"  Rating: {dataset.usabilityRating}")


def download_dataset(dataset: object, destination_folder: str):
    """Download the specified Kaggle dataset to the given destination folder."""
    dataset_ref = f"{dataset.ownerName}/{dataset.slug}"
    kaggle.api.dataset_download_files(dataset_ref, path=destination_folder, unzip=True)


if __name__ == "__main__":
    # For testing or initialization purposes, if required.
    search_results = search_datasets("test")
    if search_results:
        display_dataset_details(search_results[0])
        #download_dataset(search_results[0], destination_folder="./datasets")
