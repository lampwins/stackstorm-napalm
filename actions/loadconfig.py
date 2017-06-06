from lib.action import NapalmBaseAction


class NapalmLoadConfig(NapalmBaseAction):
    """Load configuration into network device via NAPALM
    """

    def run(self, config_file, method, commit, **std_kwargs):

        try:
            if not method:
                method = 'merge'
            else:
                method = method.lower()
                if method not in ["merge", "replace"]:
                    raise ValueError(('{} is not a valid load method, use: '
                                      'merge or replace').format(method))

            with self.get_driver(**std_kwargs) as device:

                if method == "replace":
                    device.load_replace_candidate(filename=config_file)
                else:
                    device.load_merge_candidate(filename=config_file)

                if commit:
                    device.commit_config()

        except Exception, e:
            self.logger.error(str(e))
            return (False, str(e))

        return (True, "load ({}) successful on {}".format(method, self.hostname))
