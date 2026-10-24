import asyncio, base64,re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).parent

def renderable(path):
 s=path.read_text()
 css=(ROOT/'styles.css').read_text()
 css=css.split("\n",1)[1]
 if path.parent==ROOT:
  s=s.replace('<link rel="stylesheet" href="styles.css">',f'<style>{css}</style>')
  s=s.replace('<script defer src="main.js"></script>','').replace('</body>',f'<script>{(ROOT/"main.js").read_text()}</script></body>')
 else:
  s=s.replace('<link rel="stylesheet" href="../styles.css">',f'<style>{css}</style>')
  s=s.replace('<script defer src="../main.js"></script>','').replace('</body>',f'<script>{(ROOT/"main.js").read_text()}</script></body>')
 for asset in (ROOT/'assets').glob('*.svg'):
  data=base64.b64encode(asset.read_bytes()).decode()
  s=s.replace('src="assets/'+asset.name+'"',f'src="data:image/svg+xml;base64,{data}"')
  s=s.replace('src="../assets/'+asset.name+'"',f'src="data:image/svg+xml;base64,{data}"')
 return s
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for width,height,device in [(1440,900,'desktop'),(390,844,'mobile')]:
   page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1,reduced_motion='reduce')
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   await page.set_content(renderable(ROOT/'index.html'),wait_until='load')
   await page.eval_on_selector_all('img[loading=lazy]','elements => elements.forEach(e => e.loading = "eager")')
   await page.wait_for_timeout(700)
   await page.screenshot(path=str(ROOT/f'{device}-preview.png'),full_page=True)
   await page.screenshot(path=str(ROOT/f'{device}-above-fold.png'))
   print(device,'title:',await page.title(),'height:',await page.evaluate('document.documentElement.scrollHeight'),'overflow:',await page.evaluate('document.documentElement.scrollWidth>innerWidth'),'errors:',errors)
   if device=='mobile':
    await page.locator('[data-menu-button]').click()
    print('mobile menu visible:',await page.locator('[data-mobile-panel]').is_visible(),'aria',await page.locator('[data-menu-button]').get_attribute('aria-expanded'))
    await page.locator('[data-mobile-panel] a').first.click()
    print('mobile menu after navigation:',await page.locator('[data-mobile-panel]').is_visible())
   if device=='desktop':
    await page.locator('[data-filter="video"]').click()
    print('filter video count:',await page.locator('[data-project-category]:visible').count())
    await page.locator('[data-filter="all"]').click()
    print('filter all count:',await page.locator('[data-project-category]:visible').count())
    await page.set_content(renderable(ROOT/'work'/'gloria-cup.html'))
    print('case study heading:',await page.locator('h1').inner_text())
    await page.screenshot(path=str(ROOT/'case-desktop.png'))
   await page.close()
  await browser.close()
asyncio.run(main())
