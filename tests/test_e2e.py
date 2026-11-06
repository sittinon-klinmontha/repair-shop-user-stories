from playwright.sync_api import sync_playwright, expect
from pathlib import Path
import json, datetime
root=Path(__file__).resolve().parents[1]
results=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch()
 page=browser.new_page(viewport={"width":390,"height":844})
 page.goto((root/'admin.html').as_uri())
 def test(id,story,fn):
  try:
   fn(); results.append(dict(id=id,story=story,result='PASS'))
  except Exception as e:
   results.append(dict(id=id,story=story,result='FAIL',error=str(e)))
 def fill(phone='0812345678',name='สมชาย'):
  for key,value in dict(customer=name,phone=phone,device='Notebook',issue='เปิดไม่ติด').items(): page.locator('#'+key).fill(value)
 def submit(): page.get_by_role('button',name='บันทึกงานซ่อม',exact=True).click()
 def count(n): expect(page.locator('article')).to_have_count(n)
 test('TC01','US01',lambda:(submit(),count(0)))
 for id,phone in [('TC02','081234567'),('TC03','08123456789')]:
  test(id,'US01',lambda phone=phone:(fill(phone),submit(),count(0)))
 test('TC04','US01',lambda:(fill(name='   '),submit(),count(0)))
 test('TC05','US01',lambda:(fill(),submit(),expect(page.locator('#message')).to_contain_text('REP-0001'),count(1)))
 test('TC06','US02',lambda:(page.locator('#search').fill('REP-0001'),count(1)))
 test('TC07','US02',lambda:(page.locator('#search').fill('missing'),expect(page.locator('#list')).to_have_text('ไม่พบงานซ่อม')))
 page.locator('#search').fill('')
 test('TC08','US03',lambda:(page.get_by_role('button',name='เปลี่ยนเป็น กำลังซ่อม',exact=True).click(),expect(page.locator('article')).to_contain_text('สถานะ: กำลังซ่อม')))
 test('TC09','US04',lambda:(page.locator('#filter').select_option('รับเรื่อง'),count(0),page.locator('#filter').select_option('กำลังซ่อม'),count(1)))
 test('TC10','US05',lambda:(page.reload(),expect(page.locator('article')).to_contain_text('สถานะ: กำลังซ่อม')))
 test('TC11','US03',lambda:(page.get_by_role('button',name='เปลี่ยนเป็น ซ่อมเสร็จ',exact=True).click(),page.get_by_role('button',name='เปลี่ยนเป็น ส่งคืนแล้ว',exact=True).click(),expect(page.locator('article button')).to_have_count(0),expect(page.locator('article small')).to_have_text('รับเรื่อง → กำลังซ่อม → ซ่อมเสร็จ → ส่งคืนแล้ว')))
 test('TC12','US01',lambda:(fill(),submit(),expect(page.locator('#message')).to_contain_text('REP-0002'),count(2)))
 test('TC13','NFR01',lambda:(_ for _ in ()).throw(AssertionError('horizontal overflow')) if page.evaluate('document.documentElement.scrollWidth > innerWidth') else None)
 page.screenshot(path=str(root/'result-admin-mobile.png'),full_page=True)
 page.set_viewport_size({'width':1440,'height':1000})
 page.screenshot(path=str(root/'result-admin-desktop.png'),full_page=True)
 page.set_viewport_size({'width':390,'height':844})
 page.goto((root/'index.html').as_uri())
 def lookup(phone):
  page.get_by_label('เลขงานซ่อม',exact=True).fill('REP-0001')
  page.get_by_label('เบอร์โทรที่แจ้งซ่อม',exact=True).fill(phone)
  page.get_by_role('button',name='ติดตามงาน',exact=True).click()
 test('TC14','US06',lambda:(lookup('0899999999'),expect(page.locator('#result article')).to_have_count(0),expect(page.locator('#feedback')).to_contain_text('ไม่พบข้อมูล')))
 test('TC15','US06',lambda:(lookup('0812345678'),expect(page.locator('#result')).to_contain_text('สถานะล่าสุด: ส่งคืนแล้ว'),expect(page.locator('#result li')).to_have_count(4)))
 test('TC16','US07',lambda:expect(page.locator('#result button')).to_have_count(0))
 test('TC17','NFR01',lambda:(_ for _ in ()).throw(AssertionError('customer horizontal overflow')) if page.evaluate('document.documentElement.scrollWidth > innerWidth') else None)
 page.screenshot(path=str(root/'result-user.png'),full_page=True)
 page.set_viewport_size({'width':1440,'height':1000})
 test('TC18','US06',lambda:expect(page.locator('#result')).to_contain_text('สถานะล่าสุด: ส่งคืนแล้ว'))
 page.screenshot(path=str(root/'result-user-desktop.png'),full_page=True)
 page.screenshot(path=str(root/'result-mobile.png'),full_page=True)
 browser.close()
(root/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'TEST-RESULTS.md').write_text('# ผลทดสอบจริง Playwright Chromium\n\nรัน: '+datetime.datetime.now().isoformat()+'\n\n| Test | Story | ผล |\n|---|---|---|\n'+'\n'.join('|'+r['id']+'|'+r['story']+'|'+r['result']+'|' for r in results)+'\n\nหลักฐาน: result-admin-mobile.png, result-admin-desktop.png, result-user.png, result-user-desktop.png และ results.json\nขอบเขต: Chromium มือถือ 390×844 และภาพ desktop 1440×1000; ยังไม่ได้ตรวจหลายเบราว์เซอร์หรือระบบหลายผู้ใช้',encoding='utf-8')
print(json.dumps(results,ensure_ascii=False))
assert all(r['result']=='PASS' for r in results)
