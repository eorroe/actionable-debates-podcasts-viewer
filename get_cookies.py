import asyncio
import json
from playwright.async_api import async_playwright

async def get_youtube_cookies():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            ignore_https_errors=True,
        )
        page = await context.new_page()
        await page.goto("https://www.youtube.com/watch?v=Lx8lrn-cytc", wait_until="networkidle", timeout=120000)
        await page.wait_for_timeout(5000)
        cookies = await context.cookies()
        with open("yt_cookies.json", "w") as f:
            json.dump(cookies, f)
        print(f"Saved {len(cookies)} cookies to yt_cookies.json")
        await browser.close()

asyncio.run(get_youtube_cookies())
