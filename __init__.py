from compose.plugin import compose_command, compose_patch
import compose
from dockerdns import DockerDns


@compose_command(standalone=True)
def test_command(self, options):
    """
    Test command

    Usage: config [options]

    Options:
        -q, --quiet     Only validate the configuration, don't print
                        anything.
        --services      Print the service names, one per line.

    """
    # print('command')
    print(self, options)


'''
@compose_patch(compose.project.Project, "_labeled_containers")
def patched_ps_command(self, original_func, stopped=False, one_off=OneOffFilter.exclude):
    print('B1')
    return_value = original_func(self, stopped, one_off)
    print('E1')
    return return_value
'''


@compose_patch(compose.cli.main.TopLevelCommand, "ps")
def patched_ps_command(original_fnc, tlc, options):
    print('B2')
    original_fnc(tlc, options)
    print('E2')


@compose_patch(compose.cli.main, "get_version_info")
def get_version_info(original_fnc, scope):
    return 'brrr ' + original_fnc(scope)

plugin = DockerDns
