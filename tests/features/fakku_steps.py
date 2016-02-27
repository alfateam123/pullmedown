#from lettuce import step, world, before
from aloe import step, world, before
import pexpect
import os
import six

def create_fakku_process(url):
    return pexpect.spawn("pullmedown", args=["fakku", url])


def retrieve_images(folder="."):
    _, _, files = six.next(os.walk(folder))
    return [file_ for file_ in files if os.path.splitext(file_)[-1] == ".jpg"]


def number_of_images(number, folder="."):
    return len(retrieve_images(folder)) == number


#@before.each_scenario
@before.each_example
def clean_images(scenario, outline, step):
    for image_ in retrieve_images():
        os.remove(image_)


@step(u'Given I want to download (.+)')
def given_i_want_to_download_(step, url):
    world.fakku_proc = create_fakku_process(url)


@step(u'When I download it')
def when_i_download_it(step):
    try:
        world.fakku_proc.expect(pexpect.EOF, timeout=30)
        assert True
    except pexpect.TIMEOUT:
        assert False, "pullmedown looped"


@step(u'Then pullmedown says it cannot find it')
def then_pullmedown_says_it_cannot_find_it(step):
    lines = world.fakku_proc.before.splitlines()
    assert (b"could not find enough information to download"
            b" the doujin you asked for." in lines[-1])

@step(u'Then pullmedown says it\'s a book')
def then_pullmedown_says_its_a_book(step):
    lines = world.fakku_proc.before.splitlines()
    print(lines)
    assert (b"this is a Fakku Book" in lines[-1])

@step(u'Then (\d+) images have been downloaded')
def then_at_least_one_image_have_been_downloaded(step, number):
    assert number_of_images(int(number)), "only {0} images were downloaded instead".format(len(retrieve_images()))

@step(u'Then pullmedown says you have to subscribe')
def then_pullmedown_says_you_have_to_subscribe(step):
    lines = world.fakku_proc.before.splitlines()
    assert (b"subscribe" in lines[-1])
