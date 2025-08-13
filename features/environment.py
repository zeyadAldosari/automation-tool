import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from src.utils.config import load_config

def before_all(context):
    context.cfg = load_config()
    context.base_url = context.cfg["ui"]["base_url"]

def before_feature(context, feature):
    if "features/ui/" in feature.filename.replace("\\", "/"):
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def before_scenario(context, driver):
    try:
        context.driver
    except Exception:
        return
    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    context.driver = webdriver.Chrome(options=options)
    context.wait = WebDriverWait(driver, 10)

def after_scenario(context, driver):
    try:
        context.driver.quit()
    except Exception:
        return

def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        os.makedirs("reports/screens", exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in step.name)
        context.driver.save_screenshot(f"reports/screens/{ts}-{safe}.png")

