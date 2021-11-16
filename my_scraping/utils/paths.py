from pathlib import Path
import sys


ROOT_FOLDER = Path(__file__).parent.parent.parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'
FIREFOX_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'firefoxdriver.exe'
drivers = {
    'chrome': CHROME_DRIVER_PATH,
    'firefox': FIREFOX_DRIVER_PATH
}
