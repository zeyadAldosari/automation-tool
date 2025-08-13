import os
import yaml

def load_config():
    """Load configuration from YAML and override with environment variables if set."""
    config_path = os.path.join("configs", "config.yaml")
    
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg

config = load_config()
