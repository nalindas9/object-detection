"""
# To-Do
"""
from configuration_parser import ConfigurationParser

class Detect:
    """
    Detect class
    """
    def __init__(self):
        """
        Detect class constructor
        """
        self.path = 'config/config.yaml'
        self.config_parser = ConfigurationParser(path=self.path,
                                                 module_name='detect')
        self.classes = self.config_parser.getConfigValue('classes')

    def detect(self):
        """
        Detects faces in an image
        """
        print('self.classes: {}'.format(self.classes))