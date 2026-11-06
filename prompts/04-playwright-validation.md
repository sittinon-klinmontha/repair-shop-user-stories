# พรอมต์ทำซ้ำ — เรียบเรียงภายหลัง
ไม่ใช่ transcript การทดสอบครั้งแรก

อ่าน USER-STORIES.md, DESIGN.md, TEST-DATA.md และ TEST-PLAN.md
รัน tests/test_e2e.py ด้วย Playwright Chromium ใน browser context ใหม่
ตรวจรับงาน ค่าขอบ ค้นหา กรอง สถานะ ประวัติ persistence และเลขงานต่อเนื่อง
ตรวจหน้าลูกค้า: เบอร์ผิดไม่แสดงรายละเอียด เบอร์ถูกดูประวัติได้ และไม่มีปุ่มเปลี่ยนสถานะ
ตรวจมือถือ 390×844 และเก็บภาพ desktop 1440×1000
รายงาน PASS/FAIL ตามผลรันจริงใน TEST-RESULTS.md และ results.json ระบุข้อจำกัด
เทียบผลกับแบบใน DESIGN-CONFORMANCE.md ห้ามสร้างผลผ่านโดยไม่ได้รันทดสอบ
