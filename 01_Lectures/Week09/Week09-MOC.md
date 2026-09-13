---
tags: [ml, week09, moc]
course: 1322308
course-name: Machine Learning (การเรียนรู้ของเครื่อง)
week: 9
date: 2026-09-13
instructor: รศ.ดร.ปริญญา สงวนสัตย์ (Assoc. Prof. Parinya Sanguansat, Ph.D.)
source: "09 Support Vector Machine.pptx"
---

# Week 09 — Support Vector Machine & Kernel Methods (MOC)

<span class="material-symbols-outlined">arrow_back</span> สัปดาห์ก่อนหน้า: [[Week08-MOC|MOC สัปดาห์ 08]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทำความเข้าใจแนวคิด Maximal Margin และที่มาของสูตรระยะห่าง $\frac{2}{\|\mathbf{w}\|}$ — ดู [[01-Maximal-Margin-and-Hard-Margin-SVM]]
- [ ] ไล่สมการปัญหาปฐมภูมิ (Primal) สู่ปัญหาทวิภาค (Dual) และบทบาทของ Support Vectors — ดู [[01-Maximal-Margin-and-Hard-Margin-SVM]]
- [ ] เข้าใจหน้าที่ของตัวแปรหย่อน ($\xi_i$) และการจูนพารามิเตอร์ $C$ ใน Soft-Margin — ดู [[02-Soft-Margin-SVM-and-Slack-Variables]]
- [ ] ทำความเข้าใจหลักการ Kernel Trick (Mercer's Theorem) และการประยุกต์ใช้ RBF Kernel — ดู [[03-Kernel-Trick-and-Multiclass-SVM]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 09 (สรุปย่อ)

สัปดาห์ที่ 9 ศึกษาโมเดลการจำแนกประเภทที่มีรากฐานทฤษฎีการเรียนรู้เชิงสถิติ (Statistical Learning Theory) แข็งแกร่งที่สุด:
1. **การหาขอบเขตสูงสุด (Maximal Margin & Hard-Margin):** ทฤษฎีมิติ VC, การกำหนดสมการระนาบมาตรฐาน (Canonical Hyperplane), การลดทอนขนาด $\|\mathbf{w}\|$, การแก้ปัญหา Quadratic Programming ด้วยตัวคูณลากรองจ์, และเงื่อนไข KKT ที่พิสูจน์ว่ามีเพียง Support Vectors เท่านั้นที่มีผลต่อระนาบ
2. **การผ่อนปรนด้วยซอฟต์มาร์จิน (Soft-Margin SVM):** การรับมือกับสัญญาณรบกวนด้วยตัวแปรหย่อน (Slack Variables $\xi_i$), การควบคุม Overfitting ด้วยพารามิเตอร์ $C$, และเงื่อนไข Box Constraint บนตัวแปรทวิภาค
3. **เคล็ดวิธีเคอร์เนลและการจำแนกหลายคลาส (Kernels & Multiclass):** การแปลงพิกัดสู่มิติสูงโดยไม่ต้องคำนวณเวกเตอร์จริงด้วย Kernel Trick, การใช้งานเคอร์เนล Polynomial และ Gaussian RBF, กลยุทธ์ One-vs-Rest / One-vs-One / DAG-SVM, และอัลกอริทึมการคำนวณความเร็วสูง SMO

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 09

```mermaid
graph TD
    MOC["Week 09: Support Vector Machine"] --> A[[01-Maximal-Margin-and-Hard-Margin-SVM]]
    MOC --> B[[02-Soft-Margin-SVM-and-Slack-Variables]]
    MOC --> C[[03-Kernel-Trick-and-Multiclass-SVM]]

    A --> A1["ทฤษฎี VC Dimension & มาร์จิน M = 2/||w||"]
    A --> A2["สมการปัญหาปฐมภูมิ (Primal QP)"]
    A --> A3["สมการปัญหาทวิภาค (Dual QP) & KKT"]
    B --> B1["ตัวแปรหย่อน (Slack Variables ξ)"]
    B --> B2["พารามิเตอร์ C ควบคุม Overfitting"]
    B --> B3["เงื่อนไข Box Constraint (0 ≤ α ≤ C)"]
    C --> C1["Kernel Trick & ทฤษฎีบทของเมอร์เซอร์"]
    C --> C2["ตระกูลเคอร์เนล Linear, Poly, RBF"]
    C --> C3["Multiclass SVM (OvR, OvO) & SMO"]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
    style B fill:#dd6b20,color:#fff
    style C fill:#805ad5,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| :--- | :--- | :--- |
| [[01-Maximal-Margin-and-Hard-Margin-SVM]] | ทฤษฎีมาร์จินสูงสุด, การพิสูจน์สูตรระยะห่าง $\frac{2}{\|\mathbf{w}\|}$, ฟังก์ชันลากรองเจียน, ปัญหาทวิภาค, และบทบาทของ Support Vectors | สไลด์ 1–18 |
| [[02-Soft-Margin-SVM-and-Slack-Variables]] | การจัดการข้อมูลที่มี Noise, ตัวแปรหย่อน $\xi_i$, การควบคุมความกว้างมาร์จินด้วยพารามิเตอร์ $C$, และเงื่อนไข Box Constraint | สไลด์ 19–24 |
| [[03-Kernel-Trick-and-Multiclass-SVM]] | การแปลงพิกัดไม่เป็นเชิงเส้น, ทฤษฎีบทของเมอร์เซอร์, สูตรเคอร์เนลยอดนิยม (Polynomial, RBF), การจัดการหลายคลาส (OvR, OvO, DAG), และอัลกอริทึม SMO | สไลด์ 25–40 |

> [!tip] เคล็ดลับการจำสำหรับข้อสอบสัปดาห์ที่ 09
> - **ทำไมต้องกลับด้านจาก $\max \frac{2}{\|\mathbf{w}\|}$ เป็น $\min \frac{1}{2}\|\mathbf{w}\|^2$?** เพราะฟังก์ชัน $\frac{1}{2}\|\mathbf{w}\|^2$ เป็นฟังก์ชันคอนเวกซ์ (Convex Quadratic) ที่มีจุดต่ำสุดสัมบูรณ์เพียงจุดเดียว ทำให้สามารถใช้ตัวแก้ Quadratic Programming หาคำตอบที่ดีที่สุดได้เสมอโดยไม่ติด Local Optima
> - **ความหมายของ Support Vectors:** จุดที่มีค่า $\alpha_i > 0$ มีเพียง Support Vectors เท่านั้น จุดอื่น ๆ จะมี $\alpha_i = 0$ ทั้งสิ้น

<!-- สัปดาห์ที่ 9 เป็นสัปดาห์สุดท้ายของชุดสไลด์บรรยายในรอบนี้ -->
