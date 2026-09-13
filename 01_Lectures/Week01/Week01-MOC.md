---
tags: [ml, week01, moc]
course: 1322308
course-name: Machine Learning (การเรียนรู้ของเครื่อง)
week: 1
date: 2026-09-13
instructor: รศ.ดร.ปริญญา สงวนสัตย์ (Assoc. Prof. Parinya Sanguansat, Ph.D.)
source: "01 Introduction to Machine Learning.pptx"
---

# Week 01 — Introduction to Machine Learning (MOC)

<!-- สัปดาห์แรกของรายวิชา (ไม่มีสัปดาห์ก่อนหน้า) -->

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทำความเข้าใจความแตกต่างระหว่างการเขียนโปรแกรมแบบดั้งเดิม (Rule-based) กับ Machine Learning — ดู [[01-Introduction-and-Well-Posed-Learning-Problems]]
- [ ] ฝึกจำแนกและระบุองค์ประกอบ $T, P, E$ จากโจทย์ปัญหาจริง — ดู [[01-Introduction-and-Well-Posed-Learning-Problems]]
- [ ] ทบทวนแนวคิด 4 ขั้นตอนการออกแบบระบบการเรียนรู้ (Mitchell's Framework) — ดู [[02-Designing-a-Learning-System]]
- [ ] เตรียมความพร้อมเรื่องแคลคูลัสพื้นฐานและการปรับค่าน้ำหนักเกรเดียนต์ (LMS Algorithm) — ดู [[03-LMS-Weight-Update-and-Checkers-Example]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 01 (สรุปย่อ)

สัปดาห์แรกเป็นการปูพื้นฐานแนวคิดสำคัญที่สุดของการเรียนรู้ของเครื่อง (Machine Learning Foundation):
1. **นิยามและการกำหนดกรอบปัญหา (Well-Posed Learning Problems):** นิยามตามทฤษฎีของ Tom M. Mitchell ที่ระบุว่าการเรียนรู้ต้องวัดผลได้ผ่าน 3 เสาหลัก คือ Task ($T$), Performance Measure ($P$), และ Training Experience ($E$)
2. **พิมพ์เขียวการออกแบบระบบการเรียนรู้ (Designing a Learning System):** เจาะลึก 4 การตัดสินใจเชิงวิศวกรรม ได้แก่ การเลือกประสบการณ์ (Direct vs Indirect), การเลือกฟังก์ชันเป้าหมาย ($ChooseMove$ vs $Evaluate$), การเลือกรูปแบบแทนฟังก์ชัน (Linear Representation), และการเลือกอัลกอริทึมประมาณค่า (LMS Rule)
3. **การทำงานเชิงปฏิบัติและการคำนวณจริง (LMS Walkthrough):** การแกะรอยการคำนวณปรับค่าน้ำหนักหมากฮอส ($w_0, w_1, w_2$) ทีละสถานะ ($b_0 \to b_1 \to b_3 \to b_4 \to b_5 \to b_6$) จนกระทั่งจบเกม พร้อมแนวทางการประยุกต์ใช้กับเกม Tic-Tac-Toe

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 01

```mermaid
graph TD
    MOC["Week 01: Introduction to Machine Learning"] --> A[[01-Introduction-and-Well-Posed-Learning-Problems]]
    MOC --> B[[02-Designing-a-Learning-System]]
    MOC --> C[[03-LMS-Weight-Update-and-Checkers-Example]]

    A --> A1["นิยาม ML & เมื่อไหร่ควรใช้"]
    A --> A2["การกำหนดกรอบ T, P, E"]
    B --> B1["4 ขั้นตอนการออกแบบระบบ"]
    B --> B2["ฟังก์ชันเป้าหมาย & Representation Trade-off"]
    C --> C1["กฎการปรับค่าน้ำหนัก LMS"]
    C --> C2["ตัวอย่างคำนวณหมากฮอสทีละสเต็ป"]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
    style B fill:#dd6b20,color:#fff
    style C fill:#805ad5,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| :--- | :--- | :--- |
| [[01-Introduction-and-Well-Posed-Learning-Problems]] | นิยามทางการของ ML, ทำไม/เมื่อไหร่ที่ควรใช้ ML, โครงสร้าง Well-Posed Problems ($T, P, E$) พร้อมตัวอย่างจริง | สไลด์ 1–10 |
| [[02-Designing-a-Learning-System]] | สถาปัตยกรรมการออกแบบ 4 ขั้นตอน, Direct vs Indirect Experience, ฟังก์ชันเป้าหมาย $V(b)$, Linear Representation และ Trade-off | สไลด์ 11–26 |
| [[03-LMS-Weight-Update-and-Checkers-Example]] | กฎ Least Mean Square (LMS), การแกะรอยคำนวณค่าน้ำหนัก $w_0, w_1, w_2$ สดทีละกระดาน, การทดสอบโมเดล, และโจทย์ Tic-Tac-Toe | สไลด์ 27–35 |

> [!tip] เคล็ดลับการเตรียมสอบสัปดาห์ที่ 01
> ข้อสอบกลางภาคมักออก 2 ประเด็นหลักเสมอ:
> 1. **การเขียนแจกแจง $T, P, E$:** ระวังอย่าเขียน $T$ และ $P$ สลับกัน ($T$ คืองานที่ทำ ส่วน $P$ คือตัวชี้วัดที่เป็นเกณฑ์ประเมิน)
> 2. **การคำนวณปรับค่าน้ำหนัก LMS:** ต้องเช็คเครื่องหมาย Error ให้ดีว่านำสถานะใดลบด้วยสถานะใด ($V_{train}(b) - \hat{V}(b)$) และอย่าลืมว่าค่า Bias $w_0$ จะมีตัวคูณ $f_0 = 1$ เสมอ

---
<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week02-MOC|MOC สัปดาห์ 02]]
