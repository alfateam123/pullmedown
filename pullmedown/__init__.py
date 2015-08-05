#_._ coding:utf-8 _._
from __future__ import print_function
import click
import sys
from .musicforprogramming import MusicForProgrammingDownloader as MFPDownloader

@click.group()
def main():
    """oh hi"""
    pass


@main.command()
@click.option("--list-albums", is_flag=True, help="lists all the albums")
@click.option("--number", default=0, help="download the specified song")
@click.option("--download-all", is_flag=True, help="use it if you want to download all the albums")
def musicforprogramming(list_albums, number, download_all):
    if list_albums:
        MFPDownloader().list_albums()
        return
    raise NotImplementedError("you still need to wait for --number and --download-all")
