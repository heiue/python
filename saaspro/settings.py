
class Settings:
    setting_dict = {}

    def __init__(self, setting_dict):
        self.setting_dict = setting_dict

    def set(self, key, value):
        self.setting_dict[key] = value

    def get(self, key):
        test_key = "%s_%s" % (key, 'test')
        if self.setting_dict['env'] == 'DEV' and test_key in self.setting_dict:
            return self.setting_dict[test_key]
        return self.setting_dict[key]
