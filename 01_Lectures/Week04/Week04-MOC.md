---
tags: [ml, week04, moc]
course: 1322308
course-name: Machine Learning (การเรียนรู้ของเครื่อง)
week: 4
date: 2026-09-13
instructor: รศ.ดร.ปริญญา สงวนสัตย์ (Assoc. Prof. Parinya Sanguansat, Ph.D.)
source: "04 k-Nearest Neighbor.pptx"
---

# Week 04 — k-Nearest Neighbors & Distance Metrics (MOC)

<span class="material-symbols-outlined">arrow_back</span> สัปดาห์ก่อนหน้า: [[Week03-MOC|MOC สัปดาห์ 03]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทำความเข้าใจแนวคิด Lazy Learning เปรียบเทียบกับ Eager Learning — ดู [[01-kNN-Algorithm-and-Distance-Metrics]]
- [ ] จำสูตรและความแตกต่างของ $L_1$ (Manhattan), $L_2$ (Euclidean), และ $L_\infty$ (Chebyshev) — ดู [[01-kNN-Algorithm-and-Distance-Metrics]]
- [ ] เข้าใจขั้นตอนอัลกอริทึม Condensed Nearest Neighbor (CNN) ในการคัดเลือก Prototype — ดู [[02-Instance-Reduction-and-Fast-Search-kdTree-LSH]]
- [ ] ทำความเข้าใจหลักการทำงานของ k-d Tree ในการแบ่งพื้นที่ค้นหา — ดู [[02-Instance-Reduction-and-Fast-Search-kdTree-LSH]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 04 (สรุปย่อ)

สัปดาห์ที่ 4 ศึกษาหนึ่งในอัลกอริทึมการเรียนรู้แบบไม่อิงพารามิเตอร์ (Non-parametric) ที่สำคัญที่สุด:
1. **หลักการของ k-NN (Instance-based Learning):** กลไกการจำแนกประเภทข้อมูลโดยอาศัยเพื่อนบ้านที่ใกล้ที่สุดจำนวน $k$ ตัว และการวิเคราะห์ผลกระทบของค่า $k$ ต่อเส้นแบ่งการตัดสินใจ (Decision Boundary)
2. **เรขาคณิตและมาตรวัดระยะทาง (Vector Norms):** คุณสมบัติของ Norm ในปริภูมิเวกเตอร์, รายละเอียดตระกูล $L_p$ Norm ($L_1, L_2, L_\infty$), และความสำคัญยิ่งยวดของการทำ Feature Normalization
3. **การเพิ่มความเร็วและลดขนาดข้อมูล (Efficiency & Indexing):** การบีบอัดข้อมูลด้วย Condensed Nearest Neighbor (CNN), โครงสร้างต้นไม้ดัชนี k-d Tree สำหรับมิติขนาดกลาง, และเทคนิค Locality-Sensitive Hashing (LSH) สำหรับข้อมูลมิติสูง

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 04

```mermaid
graph TD
    MOC["Week 04: k-Nearest Neighbor"] --> A[[01-kNN-Algorithm-and-Distance-Metrics]]
    MOC --> B[[02-Instance-Reduction-and-Fast-Search-kdTree-LSH]]

    A --> A1["หลักการ Lazy Learning & ผลของค่า k"]
    A --> A2["มาตรวัดระยะทาง L₁, L₂, L_∞ Norms"]
    A --> A3["Feature Normalization & ข้อดี-ข้อเสีย"]
    B --> B1["Condensed Nearest Neighbor (CNN)"]
    B --> B2["โครงสร้างดัชนี k-d Tree"]
    B --> B3["Locality-Sensitive Hashing (LSH)"]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
    style B fill:#dd6b20,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| :--- | :--- | :--- |
| [[01-kNN-Algorithm-and-Distance-Metrics]] | แนวคิด Lazy Learning, กลไก k-NN, อิทธิพลของค่า $k$, ตระกูล $L_p$ Norms ($L_1, L_2, L_\infty$), และข้อดี-ข้อจำกัด | สไลด์ 1–14 |
| [[02-Instance-Reduction-and-Fast-Search-kdTree-LSH]] | การเพิ่มประสิทธิภาพ k-NN: อัลกอริทึม CNN คัดเลือก Prototype, การแบ่งพื้นที่ด้วย k-d Tree, และการทำ LSH | สไลด์ 15–18 |

> [!tip] เคล็ดลับการจำสำหรับข้อสอบสัปดาห์ที่ 04
> - $L_1$ (Manhattan): นึกถึงการเดินตามตารางบล็อกถนนในนิวยอร์ก นำผลต่างสัมบูรณ์ของแต่ละแกนมารวมกัน ($|x_1 - y_1| + |x_2 - y_2|$)
> - $L_2$ (Euclidean): พีทาโกรัสเส้นตรง ($\sqrt{\Delta x^2 + \Delta y^2}$)
> - $L_\infty$ (Chebyshev): การเดินของ King ในหมากรุก (วัดที่ค่าความต่างสูงสุดแกนเดียว $\max |\Delta x_i|$)

---
<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week05-MOC|MOC สัปดาห์ 05]]
