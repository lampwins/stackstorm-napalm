from lib.action import NapalmBaseAction


class NapalmCommit(NapalmBaseAction):
    """Commit the network device configuration via NAPALM
    """

    def run(self, **std_kwargs):

        try:
            with self.get_driver(**std_kwargs) as device:
                device.commit_config()

        except Exception, e:
            self.logger.error(str(e))
            return (False, str(e))

        return (True, "commit successful on {}".format(self.hostname))
