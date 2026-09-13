---
tags: [ml, week05, moc]
course: 1322308
course-name: Machine Learning (การเรียนรู้ของเครื่อง)
week: 5
date: 2026-09-13
instructor: รศ.ดร.ปริญญา สงวนสัตย์ (Assoc. Prof. Parinya Sanguansat, Ph.D.)
source: "05 Artificial Neural Networks.pptx"
---

# Week 05 — Artificial Neural Networks & Backpropagation (MOC)

<span class="material-symbols-outlined">arrow_back</span> สัปดาห์ก่อนหน้า: [[Week04-MOC|MOC สัปดาห์ 04]]

## <span class="material-symbols-outlined">check_circle</span> เช็คลิสต์ก่อนเข้าเรียน

- [ ] ทำความเข้าใจการทำงานของ Single-layer Perceptron และสาเหตุที่ล้มเหลวในปัญหา XOR — ดู [[01-Biological-Foundations-and-Single-Layer-Perceptron]]
- [ ] ไล่การพิสูจน์ทางคณิตศาสตร์ของการหาเกรเดียนต์บน Mean Square Error (Delta Rule) — ดู [[02-Gradient-Descent-and-Linear-Units]]
- [ ] จำอนุพันธ์ของฟังก์ชัน Sigmoid: $\sigma'(y) = \sigma(y)(1 - \sigma(y))$ — ดู [[03-Multilayer-Perceptrons-and-Backpropagation]]
- [ ] เข้าใจสมการ Backpropagation ทั้งในชั้นเอาต์พุต ($\delta_k$) และชั้นซ่อน ($\delta_h$) — ดู [[03-Multilayer-Perceptrons-and-Backpropagation]]

## <span class="material-symbols-outlined">assignment</span> ภาพรวมสัปดาห์ 05 (สรุปย่อ)

สัปดาห์ที่ 5 สำรวจหัวใจของโครงข่ายประสาทเทียม (Artificial Neural Networks) ซึ่งเป็นรากฐานของ Deep Learning ยุคปัจจุบัน:
1. **รากฐานเซลล์ประสาทและเพอร์เซปตรอน (Biological to Artificial):** แบบจำลอง McCulloch-Pitts, กฎการเรียนรู้ของ Perceptron, ความสามารถในการแบ่งแยกเชิงเส้น (Linear Separability), และวิกฤตความล้มเหลวในการแก้ฟังก์ชัน XOR
2. **การเรียนรู้ด้วยการลดระดับตามความชัน (Gradient Descent):** เซลล์ประสาทเชิงเส้น (Linear Units), การคำนวณและหาอนุพันธ์ของฟังก์ชัน MSE Loss, ความแตกต่างระหว่าง Batch Gradient Descent กับ Stochastic Gradient Descent (SGD), และข้อแตกต่างระหว่าง Perceptron Rule กับ Delta Rule
3. **โครงข่ายหลายชั้นและการแพร่ย้อนกลับ (MLP & Backpropagation):** กลไกของ Hidden Units ในการแปลงพิกัดเพื่อพิชิต XOR, คุณสมบัติของฟังก์ชัน Sigmoid, การพิสูจน์สมการ Backpropagation ด้วยกฎลูกโซ่อย่างละเอียด, การเสริม Momentum เพื่อหนี Local Minima, และการประยุกต์ใช้ในระบบจริง เช่น ALVINN

## <span class="material-symbols-outlined">map</span> แผนที่หัวข้อสัปดาห์ 05

```mermaid
graph TD
    MOC["Week 05: Artificial Neural Networks"] --> A[[01-Biological-Foundations-and-Single-Layer-Perceptron]]
    MOC --> B[[02-Gradient-Descent-and-Linear-Units]]
    MOC --> C[[03-Multilayer-Perceptrons-and-Backpropagation]]

    A --> A1["เซลล์ประสาทชีววิทยา vs เทียม"]
    A --> A2["Perceptron Rule & Linear Separability"]
    A --> A3["ปัญหา XOR ที่เพอร์เซปตรอนแก้ไม่ได้"]
    B --> B1["Linear Unit & ฟังก์ชัน MSE Loss"]
    B --> B2["การพิสูจน์ Gradient Descent"]
    B --> B3["Batch vs Stochastic Mode (SGD)"]
    C --> C1["Hidden Layers แก้ปัญหา XOR"]
    C --> C2["อนุพันธ์ Sigmoid & สมการ Backpropagation"]
    C --> C3["Momentum & Early Stopping"]

    style MOC fill:#2b6cb0,color:#fff
    style A fill:#38a169,color:#fff
    style B fill:#dd6b20,color:#fff
    style C fill:#805ad5,color:#fff
```

## <span class="material-symbols-outlined">collections_bookmark</span> โน้ตรายหัวข้อ

| หัวข้อ | เนื้อหาหลัก | หน้าสไลด์ |
| :--- | :--- | :--- |
| [[01-Biological-Foundations-and-Single-Layer-Perceptron]] | โครงสร้างเซลล์ประสาท, แบบจำลองเพอร์เซปตรอน, กฎการอัปเดตน้ำหนัก, การแก้ปัญหา AND/OR, และข้อจำกัดในปัญหา XOR | สไลด์ 1–19 |
| [[02-Gradient-Descent-and-Linear-Units]] | เซลล์ประสาทเชิงเส้น, การหาอนุพันธ์ MSE Loss, กฎเดลต้า (Delta Rule), การเปรียบเทียบ Batch vs SGD, และความแตกต่างระหว่าง Perceptron vs Gradient Descent | สไลด์ 29–37 |
| [[03-Multilayer-Perceptrons-and-Backpropagation]] | การแทนค่าในชั้นซ่อน, ฟังก์ชันซิกมอยด์, การพิสูจน์กฎ Backpropagation สำหรับชั้น $\delta_k$ และ $\delta_h$, พจน์โมเมนตัม, และการป้องกัน Overfitting | สไลด์ 20–28, 38–56 |

> [!tip] เคล็ดลับการจำสูตรในห้องสอบสัปดาห์ที่ 05
> สังเกตความสอดคล้องของพจน์ Error $\delta$:
> - **ชั้นเอาต์พุต ($\delta_k$):** รู้ผลต่างจริงทันที $\implies (t_k - o_k) \cdot o_k(1 - o_k)$
> - **ชั้นซ่อน ($\delta_h$):** ไม่รู้ค่า $t$ จริง ต้องดึง Error สะท้อนกลับมาจากชั้นถัดไป $\implies \left[\sum w_{hk} \delta_k\right] \cdot o_h(1 - o_h)$
> ส่วนการปรับน้ำหนักจำรูปแบบเดียวเสมอ: $\Delta w = \eta \times \delta \times \text{Input ของเส้นเชื่อมนั้น}$

---
<span class="material-symbols-outlined">arrow_forward</span> สัปดาห์ถัดไป: [[Week06-MOC|MOC สัปดาห์ 06]]
