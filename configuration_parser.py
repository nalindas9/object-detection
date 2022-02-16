"""
"""
import json, yaml

class ConfigurationParser:
    """
    """
    def __init__(self, path=None, module_name=None):
        """
        """
        self.yaml_path = path
        self.yaml_config_dict = self.parseYamlFile()
        self.json_path = self.getJsonConfigPath(module_name)
        self.config_dict = self.parseJsonFile()

    def parseJsonFile(self):
        """
        """
        config_dict = {}
        file = open(self.json_path, 'r')
        config_dict = json.load(file)
        return config_dict

    def parseYamlFile(self):
        """
        """
        config_dict = {}
        file = open(self.yaml_path, 'r')
        config_dict = yaml.load(file, Loader=yaml.FullLoader)
        return config_dict

    def getJsonConfigPath(self, module_name):
        """
        """
        return self.parseYamlFile()[module_name]['config_path']

    def getConfigValue(self, key):
        """
        """
        return self.config_dict[key]