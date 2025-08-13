import os, time
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.config import load_config

def before_all(context):
    context.cfg = load_config()
    context.base_url = context.cfg["ui"]["base_url"]

@fixture
def browser_fixture(context):
    remote_url = os.getenv("SELENIUM_REMOTE_URL")
    opts = Options()
    if os.getenv("HEADLESS", "1") == "1":
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    if remote_url:
        context.browser = webdriver.Remote(command_executor=remote_url, options=opts)
    else:
        service = Service(ChromeDriverManager().install())
        context.browser = webdriver.Chrome(service=service, options=opts)
    context.browser.set_window_size(1280, 900)
    try:
        yield context.browser
    finally:
        context.browser.quit()
        del context.browser

def before_feature(context, feature):
    if "features/ui/" in feature.filename.replace("\\", "/"):
        use_fixture(browser_fixture, context)

def after_step(context, step):
    if step.status == "failed" and hasattr(context, "browser"):
        os.makedirs("reports/screens", exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in step.name)
        context.browser.save_screenshot(f"reports/screens/{ts}-{safe}.png")
