from lettuce import step, world
import pexpect


def create_fakku_process(url):
    return pexpect.spawn("pullmedown", args=["fakku", url])


@step(u'Given I want to download (.+)')
def given_i_want_to_download_(step, url):
    world.fakku_proc = create_fakku_process(url)


@step(u'When I download it')
def when_i_download_it(step):
    try:
        world.fakku_proc.expect(pexpect.EOF, timeout=8)
        assert True
    except pexpect.TIMEOUT:
        assert False, "pullmedown looped"


@step(u'Then pullmedown says it cannot find it')
def then_pullmedown_says_it_cannot_find_it(step):
    lines = [line for line in world.fakku_proc.before.splitlines()]
    assert ("could not find enough information to download"
            " the doujin you asked for." in lines[-1])
