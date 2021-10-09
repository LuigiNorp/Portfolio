import asyncio
from pyppeteer import launch
import CREDS

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 720})
    await page.goto('https://www.reddit.com/login/', {'waitUntil': 'networkidle0'}) # wait until page load
    await page.type('#id', CREDS.username)
    await page.type('#loginPw', CREDS.password)

    # click and wait for navigation
    navigationPromise = await asyncio.ensure_future(page.waitForNavigation())
    await page.click('#loginSubmit')

main()
