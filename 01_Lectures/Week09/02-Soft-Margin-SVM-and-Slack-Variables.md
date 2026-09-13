---
tags: [ml, week09, svm, soft-margin, slack-variables, regularization, c-parameter]
course: 1322308
week: 9
date: 2026-09-13
---

# ซัพพอร์ตเวกเตอร์แมชชีนแบบซอฟต์มาร์จินและตัวแปรหย่อน (Soft-Margin SVM & Slack Variables)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week09-MOC|MOC สัปดาห์ 09]] | ก่อนหน้า: [[01-Maximal-Margin-and-Hard-Margin-SVM]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Soft-Margin SVM** — การขยายขีดความสามารถของ SVM ให้สามารถรับมือกับชุดข้อมูลที่มีสัญญาณรบกวน (Noise) หรือข้อมูลที่ไม่สามารถแบ่งแยกเชิงเส้นได้อย่างสมบูรณ์
- **Slack Variable ($\xi_i$)** — ตัวแปรหย่อนที่ยอมให้ข้อมูลบางจุดรุกล้ำเข้ามาในเขตมาร์จินหรือข้ามไปอยู่ผิดฝั่งของเส้นแบ่งเขตได้เล็กน้อย
- **Trade-off Parameter ($C$)** — พารามิเตอร์ควบคุมน้ำหนักระหว่างการขยายขนาดมาร์จินกับการลงโทษความผิดพลาดจากการจำแนกผิด
- **Box Constraint** — ขอบเขตเงื่อนไขบังคับบนตัวคูณลากรองจ์ในปัญหาทวิภาค ($0 \le \alpha_i \le C$) ซึ่งจำกัดอิทธิพลสูงสุดของข้อมูลแต่ละจุดไม่ให้ดึงเส้นแบ่งเพี้ยน

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. ทำไม Hard-Margin จึงไม่เพียงพอ?

ในข้อมูลจริง:
1. มักมี **สัญญาณรบกวน (Outliers / Noise)** ปนอยู่เสมอ จุดแปลกแยกเพียงจุดเดียวสามารถทำให้ Hard-Margin ไม่สามารถหาคำตอบได้ (Infeasible)
2. หากบังคับให้แบ่งแยกถูกต้อง 100% จะทำให้มาร์จินแคบลงอย่างรุนแรงและนำไปสู่ภาวะ **Overfitting**

---

### 2. สมการปัญหาปฐมภูมิของ Soft-Margin (Primal Formulation)

Cortes และ Vapnik (1995) ได้เสนอให้เพิ่มตัวแปรหย่อน $\xi_i \ge 0$ สำหรับข้อมูลแต่ละตัวอย่าง:

$$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i$$
ภายใต้เงื่อนไข:
$$y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i \quad \text{และ} \quad \xi_i \ge 0 \quad \forall i$$

#### ความหมายทางเรขาคณิตของค่า $\xi_i$:
- **$\xi_i = 0$:** ข้อมูลอยู่ถูกต้องนอกเขตมาร์จิน (ไม่มีการละเมิดเงื่อนไข)
- **$0 < \xi_i \le 1$:** ข้อมูลรุกล้ำเข้ามาในเขตมาร์จิน แต่อยู่ในฝั่งที่ถูกต้องของการตัดสินใจ
- **$\xi_i > 1$:** ข้อมูลข้ามเส้นระนาบไฮเปอร์เพลนไปอยู่อีกฝั่งหนึ่ง (เกิดการจำแนกประเภทผิดพลาด / Misclassification)

---

### 3. บทบาทของพารามิเตอร์ $C$ (การควบคุม Overfitting)

พารามิเตอร์ $C > 0$ ทำหน้าที่เป็นเครื่องมือปรับสมดุล (Regularization):

| ค่าพารามิเตอร์ $C$ | พฤติกรรมของโมเดล | ความกว้างมาร์จิน | ความเสี่ยง |
| :--- | :--- | :--- | :--- |
| **$C$ มีค่าสูงมาก ($C \to \infty$)** | ลงโทษความผิดพลาดหนักมาก บังคับให้ผิดน้อยที่สุด เข้าใกล้ Hard Margin | มาร์จินแคบ | เสี่ยงต่อ **Overfitting** สูง ไวต่อ Outliers |
| **$C$ มีค่าน้อย** | ผ่อนปรนให้เกิดความผิดพลาดได้เพื่อแลกกับเส้นแบ่งที่เรียบเนียน | มาร์จินกว้าง | ป้องกัน Overfitting ได้ดี แต่อาจเสี่ยง **Underfitting** หาก $C$ ต่ำเกินไป |

---

### 4. สมการปัญหาทวิภาค (Dual Formulation with Box Constraint)

เมื่อผ่านการอนุพันธ์ด้วย KKT Conditions ปัญหาทวิภาคของ Soft-Margin จะมีหน้าตาสมการวัตถุประสงค์ **เหมือนกับ Hard-Margin ทุกประการ**:

$$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j)$$

ข้อแตกต่างเพียงจุดเดียวที่เพิ่มเข้ามาคือ **Box Constraint**:
$$\mathbf{0 \le \alpha_i \le C} \quad \text{และ} \quad \sum_{i=1}^N \alpha_i y_i = 0$$

> [!important] ความหมายของ Box Constraint
> ค่า $C$ ทำหน้าที่เป็นเพดานกั้นบนตัวคูณลากรองจ์ ($\alpha_i \le C$) ซึ่งช่วยจำกัดให้อิทธิพลของจุดข้อมูล Outlier ไม่สามารถดึงให้ระนาบไฮเปอร์เพลนเอียงไปตามมันได้มากเกินไป

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart TD
    Start((●)) --> Data([รับชุดข้อมูลที่มีสัญญาณรบกวน<br>Data with Noise & Overlap])
    Data --> Choice{เลือกค่าพารามิเตอร์โทษ C<br>Select Penalty Parameter C?}
    Choice -->|C สูงมาก (High C)| Hard([เน้นห้ามผิดเด็ดขาด มาร์จินแคบ<br>Hard Margin: Risk of Overfitting])
    Choice -->|C เหมาะสม (Optimal C)| Soft([ยอมให้มีค่า Slack ξᵢ มาร์จินกว้าง<br>Soft Margin: Max Generalization])
    Choice -->|C ต่ำเกินไป (Low C)| Under([ละเลยความผิดพลาดมากเกินไป<br>Loose Margin: Risk of Underfitting])
    Hard --> EndNode(((●)))
    Soft --> EndNode
    Under --> EndNode
```

**ตัวอย่าง:** ผลกระทบของการปรับแต่งค่า Regularization Parameter $C$ ต่อความกว้างของมาร์จิน

---
<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[03-Kernel-Trick-and-Multiclass-SVM]]
