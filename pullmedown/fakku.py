#_._ coding:utf-8 _._
import re
from .utils import get_page, store
from collections import namedtuple
from . import main
import click

@main.command()
@click.argument("doujin-url")
def fakku(doujin_url):
    raise NotImplementedError("I need two hands to write it, and one is busy right now :^)")
