---
tags: [ml, week08, bayesian-learning, bayes-theorem, map-hypothesis, bayes-optimal-classifier]
course: 1322308
week: 8
date: 2026-09-13
---

# ทฤษฎีบทของเบย์ส สมมติฐาน MAP และตัวจำแนกเบย์สที่เหมาะสมที่สุด (Bayes Theorem & MAP)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week08-MOC|MOC สัปดาห์ 08]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Bayes' Theorem** — ทฤษฎีบทพื้นฐานของทฤษฎีความน่าจะเป็นที่ใช้ปรับปรุงความน่าจะเป็นของสมมติฐานเมื่อได้รับหลักฐานหรือข้อมูลใหม่
- **Prior Probability ($P(h)$)** — ความน่าจะเป็นล่วงหน้าของสมมติฐาน $h$ ก่อนที่จะพบข้อมูลการสังเกตการณ์ $D$
- **Likelihood ($P(D \mid h)$)** — ภาวะน่าจะเป็น คือความน่าจะเป็นที่จะพบข้อมูล $D$ หากสมมติฐาน $h$ เป็นความจริง
- **Posterior Probability ($P(h \mid D)$)** — ความน่าจะเป็นภายหลัง คือความน่าจะเป็นของสมมติฐาน $h$ หลังจากได้สังเกตเห็นข้อมูล $D$ แล้ว
- **Maximum A Posteriori (MAP)** — สมมติฐานที่มีความน่าจะเป็นภายหลังสูงที่สุดในปริภูมิสมมติฐาน
- **Bayes Optimal Classifier** — ตัวจำแนกประเภทในอุดมคติที่ผสานผลการทำนายของทุกสมมติฐานถ่วงน้ำหนักด้วย Posterior Probability

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. ทฤษฎีบทของเบย์ส (Bayes' Theorem Formulation)

การเรียนรู้แบบเบย์ส (Bayesian Learning) อาศัยความน่าจะเป็นในการให้เหตุผลภายใต้ความไม่แน่นอน:

$$P(h \mid D) = \frac{P(D \mid h) \, P(h)}{P(D)}$$

โดยที่:
- **$P(h)$ (Prior):** ความรู้หรือความเชื่อตั้งต้นเกี่ยวกับสมมติฐาน $h$
- **$P(D \mid h)$ (Likelihood):** โอกาสที่ข้อมูล $D$ จะเกิดขึ้นถ้า $h$ เป็นจริง
- **$P(D)$ (Evidence / Marginal Likelihood):** ความน่าจะเป็นรวมของการเกิดข้อมูล $D$ ซึ่งทำหน้าที่เป็นตัวปรับสเกล (Normalizing Constant):
  $$P(D) = \sum_{h' \in H} P(D \mid h') P(h')$$
- **$P(h \mid D)$ (Posterior):** ความน่าเชื่อถือของ $h$ หลังประมวลผลข้อมูล $D$

---

### 2. การเลือกสมมติฐาน: MAP vs Maximum Likelihood (ML)

#### 1. Maximum A Posteriori (MAP Hypothesis):
ต้องการหาสมมติฐาน $h \in H$ ที่เป็นไปได้มากที่สุดเมื่อกำหนดข้อมูล $D$:
$$h_{MAP} = \arg\max_{h \in H} P(h \mid D) = \arg\max_{h \in H} \frac{P(D \mid h) P(h)}{P(D)}$$
เนื่องจาก $P(D)$ มีค่าคงที่สำหรับทุก $h$ จึงตัดทิ้งได้:
$$\mathbf{h_{MAP} = \arg\max_{h \in H} P(D \mid h) \, P(h)}$$

#### 2. Maximum Likelihood (ML Hypothesis):
หากเราไม่มีความรู้ตั้งต้น หรือสมมติว่าทุกสมมติฐานมีความน่าจะเป็นล่วงหน้าเท่ากันหมด ($P(h_i) = P(h_j)$):
$$\mathbf{h_{ML} = \arg\max_{h \in H} P(D \mid h)}$$

---

### 3. ตัวอย่างการคำนวณจริง: การวินิจฉัยทางการแพทย์ (Medical Diagnosis)

กำหนดให้:
- ประชากรทั่วไปมีโอกาสเป็นโรคมะเร็ง: $P(\text{cancer}) = 0.008$, ดังนั้น $P(\neg\text{cancer}) = 0.992$
- ชุดตรวจในห้องปฏิบัติการ:
  - ตรวจพบผลบวกเมื่อเป็นโรคจริง: $P(+ \mid \text{cancer}) = 0.98$
  - ผลบวกปลอม (False Positive): $P(+ \mid \neg\text{cancer}) = 0.03$

**คำถาม:** หากผู้ป่วยคนหนึ่งเข้ารับการตรวจแล้ว **ได้ผลตรวจเป็นบวก ($+$)** ผู้ป่วยคนนี้เป็นมะเร็งจริงด้วยความน่าจะเป็นเท่าใด?

#### ขั้นตอนการคำนวณ:
1. คำนวณเทอม $P(D \mid h) P(h)$:
   - กรณีเป็นมะเร็ง:
     $$P(+ \mid \text{cancer}) P(\text{cancer}) = 0.98 \times 0.008 = \mathbf{0.00784}$$
   - กรณีไม่เป็นมะเร็ง:
     $$P(+ \mid \neg\text{cancer}) P(\neg\text{cancer}) = 0.03 \times 0.992 = \mathbf{0.02976}$$
2. คำนวณ $h_{MAP}$:
   เปรียบเทียบ $0.02976 > 0.00784 \implies \mathbf{h_{MAP} = \neg\text{cancer}}$
3. คำนวณความน่าจะเป็นจริงโดย Normalize:
   $$P(\text{cancer} \mid +) = \frac{0.00784}{0.00784 + 0.02976} = \frac{0.00784}{0.0376} \approx \mathbf{0.2085 \ (20.85\%)}$$

> [!important] ข้อคิดสำคัญทางการแพทย์
> แม้ว่าชุดตรวจจะมีความไวถึง 98% แต่เมื่อผลออกมาเป็นบวก โอกาสที่ผู้ป่วยจะเป็นมะเร็งจริงมีเพียง **20.85%** เท่านั้น! สาเหตุเกิดจากโรคนี้มีอุบัติการณ์ต่ำมาก (Prior ต่ำเพียง 0.8%) ทำให้ผลบวกปลอมจากคนกลุ่มใหญ่กลืนผลบวกจริง

---

### 4. ตัวจำแนกเบย์สที่เหมาะสมที่สุด (Bayes Optimal Classifier)

ทำไม $h_{MAP}$ จึงไม่ใช่ตัวจำแนกที่ดีที่สุดเสมอไป?
- สมมติมี 3 สมมติฐาน: $P(h_1 \mid D) = 0.4, P(h_2 \mid D) = 0.3, P(h_3 \mid D) = 0.3$
- $h_{MAP}$ คือ $h_1$ ซึ่งทำนายผลลัพธ์เป็น `+`
- แต่ $h_2$ และ $h_3$ ทำนายผลลัพธ์เป็น `-`
- หากรวมคะแนนเสียง: ผลลัพธ์ `-` มีน้ำหนักรวม $0.3 + 0.3 = 0.6$ ซึ่งชนะผลลัพธ์ `+` ที่มีเพียง $0.4$!

**Bayes Optimal Classifier** แก้ปัญหานี้โดยการรวมผลทำนายของทุกสมมติฐาน:
$$v_{BOC} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) \, P(h_i \mid D)$$
ให้ความแม่นยำสูงสุดในเชิงทฤษฎี แต่ในทางปฏิบัติมักคำนวณไม่ได้โดยตรงเพราะขนาดของ $H$ มีมหาศาล

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart LR
    Start((●)) --> Inputs
    subgraph Inputs ["ความน่าจะเป็นเริ่มต้น (Probabilistic Inputs)"]
        Prior(["ความน่าจะเป็นล่วงหน้า<br>Prior: P(h)"])
        Likelihood(["ข้อมูลหลักฐานที่สังเกตพบ<br>Likelihood: P(D|h)"])
    end
    Inputs --> Bayes([ประมวลผลทฤษฎีบทเบย์ส<br>Bayes Theorem: P(h|D) ∝ P(D|h) · P(h)])
    Bayes --> Posterior([ความน่าจะเป็นภายหลัง<br>Posterior: P(h|D)])
    Posterior --> MAP([เลือกค่าสูงสุด<br>MAP Hypothesis: h_MAP])
    Posterior --> BOC([รวมถ่วงน้ำหนักทุกสมมติฐาน<br>Bayes Optimal Classifier])
    MAP --> EndNode(((●)))
    BOC --> EndNode
```

**ตัวอย่าง:** ผังกระบวนการปรับปรุงความเชื่อจาก Prior ผสาน Likelihood สู่ Posterior Probability

---
<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[02-Naive-Bayes-Classifier-and-Text-Categorization]]
