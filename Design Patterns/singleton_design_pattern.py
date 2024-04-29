'''
[Singleton Design Pattern] Implement a configuration manager using the Singleton Design Pattern. 
The configuration manager should read configuration settings from a file and provide access to these settings
throughout the application. Demonstrate how the Singleton Design Pattern ensures that there is only one instance 
of the configuration manager, preventing unnecessary multiple reads of the configuration file.
'''

class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config = cls._instance._read_config_file()
        return cls._instance

    def _read_config_file(self):
        config = {}
        with open("config.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config

    def get_config(self, key):
        return self._config.get(key)

if __name__ == "__main__":

    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager() #Creating again
    print("Should print True if both config_manager1 and config_manager2 points to same instance: ")
    print(config_manager1 is config_manager2)  # Output should be True for (Singleton instance)

    
    print(config_manager1.get_config("server_ip"))  # Example config key
    print(config_manager2.get_config("port"))       # Example config key
