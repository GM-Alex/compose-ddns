from compose.plugin import Plugin


class DockerDns(Plugin):
    def install(self):
        print('Installing {}'.format(self.name))
        return True

    def execute(self):
        pass