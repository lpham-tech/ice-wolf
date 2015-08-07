__author__ = 'bluzky'
import json

user_settings = "settings.ini"
class Settings(object):
    """
    Singleton class used to store all application setting
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.initialized = False
        return cls.__instance

    def __init__(self):
        if self.initialized:
            return
        self.initialized = True

        self.require_activation = False

    def to_json(self):
        return json.dumps(self.__dict__)

    def load_config(self):
        """
        load user config from file. If getting exception, use default setting
        :return:
        """
        try:
            with open(user_settings) as config_file:
                conf_string = config_file.read()
                config = json.loads(conf_string)
                for key, value in config.iteritems():
                    if key in self.__dict__:
                        setattr(self, key, value)
        except Exception as e:
            print "Use default config"

    def save_config(self):
        """
        write setting to config file
        :return:
        """
        with open(user_settings, mode="w") as config_file:
            config_str = self.to_json()
            config_file.write(config_str)

settings = Settings()