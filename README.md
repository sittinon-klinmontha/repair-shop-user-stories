# RepairFlow — งานจำลองตามแบบฝึกหัด
เน้น User Stories ตั้งแต่เก็บความต้องการ ออกแบบ สร้างเว็บ ทดสอบ และเทียบผลกับแบบ

## ใช้งาน
เปิด index.html สำหรับลูกค้า / admin.html สำหรับ Admin ด้วยเบราว์เซอร์เดียวกัน
หรือรัน `python -m http.server 8766 --bind 127.0.0.1` จากโฟลเดอร์นี้ แล้วเปิด http://127.0.0.1:8766
Admin รับงานก่อน แจ้งเลขงานให้ลูกค้า ลูกค้ากรอกเลขงานและเบอร์โทรเพื่อดูความคืบหน้า

## ลำดับส่งงาน
1. [INTERVIEW.md](INTERVIEW.md) → [OWNER-ANSWERS.md](OWNER-ANSWERS.md) → [USER-STORIES.md](USER-STORIES.md) — บทสัมภาษณ์ คำตอบจำลอง และ acceptance criteria
2. DESIGN.md — FR/BR/NFR, architecture, model, flow และ sequence
3. TEST-DATA.md — ข้อมูลและค่าขอบ
4. BUILD-PROMPT.md — ข้อกำหนดสร้างระบบ
5. index.html / admin.html / styles.css — ตัวระบบ
6. CHARTERS.md — แผนสำรวจ
7. TEST-PLAN.md / PLAN-REVIEW.md — กรณีทดสอบและทบทวนข้อจำกัด
8. TEST-RESULTS.md / results.json — ผลรันจริง
9. DESIGN-CONFORMANCE.md — เปรียบเทียบผลกับแบบ

## รันทดสอบ
```powershell
python -m pip install playwright
python -m playwright install chromium
python tests/test_e2e.py
```
ภาพหลักฐาน: result-admin-mobile.png, result-admin-desktop.png, result-user.png, result-user-desktop.png
ทดสอบ Chromium; ข้อมูลสมมติทั้งหมด ยังไม่มี server database หรือ Admin login ใช้เฉพาะต้นแบบ
ขอบเขตปรับจากตัวอย่างสปา: buildless HTML/localStorage แทน Next.js/PostgreSQL/Docker ไม่มีผู้รีวิวอิสระหรือบั๊กที่ฝังโดยเจตนา

## เอกสารต้นทางแบบตัวอย่าง
- [INTERVIEW.md](INTERVIEW.md): บทสัมภาษณ์จำลองรอบแรก
- [OWNER-ANSWERS.md](OWNER-ANSWERS.md): คำตอบจำลอง กฎและขอบเขต MVP
- [USER-STORIES.md](USER-STORIES.md): เรื่องราวผู้ใช้ เกณฑ์ยอมรับ และตาราง K/Q/A
อ้างอิงรูปแบบจาก https://github.com/niphitphon8bit/repair-shop-user-stories — repo ตัวอย่างใช้ INTERVIEW.md และ OWNER-ANSWERS.md
โครงการนี้ใช้โจทย์จำลองของตนเอง ไม่อ้างว่าครอบคลุมกฎซ่อม ราคา ประกัน และงานตัวอย่างทั้งหมดของ repo ดังกล่าว

## พรอมต์ที่ใช้และพรอมต์ทำซ้ำ
ดู [prompts/README.md](prompts/README.md) สำหรับรายการเรียงเลขและที่มา แต่ละไฟล์ระบุชัดว่าเป็นข้อความผู้ใช้ที่คัดตรงบางช่วง หรือพรอมต์ทำซ้ำที่เรียบเรียงภายหลัง ไม่ใช่ประวัติ AI ครบทั้งเซสชัน
