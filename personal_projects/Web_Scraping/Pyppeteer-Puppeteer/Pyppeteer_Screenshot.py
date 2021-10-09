# Example: open web page and take a screenshot.

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'Pyppeteer_example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())