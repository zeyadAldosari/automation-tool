import os, yaml
from dotenv import load_dotenv
load_dotenv()

def load_config():
    with open("configs/config.yaml", "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["ui"]["base_url"] = os.getenv("UI_BASE_URL", cfg["ui"]["base_url"])
    cfg["api"]["base_url"] = os.getenv("API_BASE_URL", cfg["api"]["base_url"])
    return cfg
