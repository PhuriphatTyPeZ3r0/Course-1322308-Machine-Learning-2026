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
- **Brute-Force MAP Learning Algorithm** — วิธีหา $h_{MAP}$ โดยไล่คำนวณ Posterior Probability ของสมมติฐานทุกตัวใน $H$ แล้วเลือกตัวที่สูงสุด ถูกต้องเสมอแต่ใช้งานจริงไม่ได้เมื่อ $H$ ใหญ่
- **Learning a Real Valued Function** — การประยุกต์ ML Hypothesis กับเป้าหมายที่เป็นค่าต่อเนื่อง (Real-Valued Target) โดยอาศัยสมมติฐาน Gaussian Noise ซึ่งนำไปสู่การ Minimize Sum of Squared Error — รากฐานของ Linear Regression
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

### 3. ขั้นตอนวิธีหา MAP แบบไล่ตรวจทุกกรณี (Brute-Force MAP Learning Algorithm)

แนวคิดที่ตรงไปตรงมาที่สุดในการหา $h_{MAP}$ คือ **ไล่คำนวณทีละสมมติฐานจนครบทุกตัวใน $H$:**

> **Brute-Force MAP Learning Algorithm**
> 1. สำหรับสมมติฐาน $h$ แต่ละตัวใน $H$ ให้คำนวณ Posterior Probability:
>    $$P(h \mid D) = \frac{P(D \mid h)\,P(h)}{P(D)}$$
> 2. คืนค่าสมมติฐาน $h_{MAP}$ ที่มี $P(h \mid D)$ สูงที่สุด:
>    $$h_{MAP} = \arg\max_{h \in H} P(h \mid D)$$

อัลกอริทึมนี้ **รับประกันว่าได้ $h_{MAP}$ ที่ถูกต้องเสมอ** เพราะตรวจสอบทุกความเป็นไปได้จริง ๆ แต่ในทางปฏิบัติ **ใช้งานแทบไม่ได้** เพราะ:
- ปริภูมิสมมติฐาน $H$ ของปัญหาจริงมีขนาดใหญ่มาก หรือต่อเนื่องไม่จำกัด (เช่น ค่าน้ำหนักในโครงข่ายประสาทเทียม)
- ต้องคำนวณ $P(D \mid h)$ และ $P(h)$ ซ้ำสำหรับทุกสมมติฐาน ต้นทุนการคำนวณจึงสูงมาก

> [!tip] เชื่อมโยงกับตัวอย่างถัดไป
> ตัวอย่างวินิจฉัยมะเร็งด้านล่างคือการใช้ Brute-Force MAP กับ $H = \{\text{cancer}, \neg\text{cancer}\}$ ซึ่งมีสมาชิกแค่ 2 ตัวจึงคำนวณไหว แต่ถ้า $H$ ใหญ่ขึ้นวิธีนี้จะใช้ไม่ได้จริง จึงต้องอาศัยอัลกอริทึมเฉพาะทาง เช่น Naïve Bayes (ดู [[02-Naive-Bayes-Classifier-and-Text-Categorization]]) หรือ Decision Tree (ดู [[02-ID3-Algorithm-and-PlayTennis-Walkthrough|ID3 Algorithm]]) แทนการไล่ตรวจทุกสมมติฐาน

---

### 4. ตัวอย่างการคำนวณจริง: การวินิจฉัยทางการแพทย์ (Medical Diagnosis)

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

### 5. การเรียนรู้ฟังก์ชันค่าจริง (Learning a Real Valued Function) — จุดเชื่อมโยงสู่ Linear Regression

ตัวอย่างก่อนหน้านี้ล้วนมีเป้าหมาย (Target) เป็นค่าไม่ต่อเนื่อง (Discrete) เช่น cancer/¬cancer แต่ถ้าเป้าหมายเป็น **ค่าต่อเนื่อง (Real-Valued)** เช่น ความเข้มของพิกเซล ความถี่คลื่น หรือราคาบ้าน จะไม่สามารถ "นับความถี่" เพื่อประมาณความน่าจะเป็นได้แบบตัวอย่างที่ผ่านมา ต้องใช้ **สมมติฐานของสัญญาณรบกวน (Noise Model)** แทน

#### สมมติฐาน

- ให้ $f$ เป็นฟังก์ชันเป้าหมายค่าจริงที่ต้องการเรียนรู้ (unknown target function)
- ข้อมูลฝึกแต่ละตัวมีสัญญาณรบกวนปน: $d_i = f(x_i) + e_i$
- $e_i$ เป็นตัวแปรสุ่มที่สุ่มมาจาก **การแจกแจงแบบปกติ (Gaussian Distribution)** ที่มีค่าเฉลี่ยเป็นศูนย์: $e_i \sim \mathcal{N}(0, \sigma^2)$ และเป็นอิสระต่อกัน (i.i.d.)
- เป้าหมาย: หาสมมติฐาน $h$ (จากปริภูมิสมมติฐาน $H$ ของฟังก์ชันค่าจริง เช่น เส้นตรง, พหุนาม) ที่เป็น Maximum Likelihood Hypothesis $h_{ML}$

#### การอนุพันธ์ (Derivation)

เนื่องจาก $d_i = f(x_i) + e_i$ และ $e_i$ มีการแจกแจงแบบ $\mathcal{N}(0, \sigma^2)$ ดังนั้น $d_i$ ก็มีการแจกแจงแบบปกติที่มีค่าเฉลี่ยอยู่ที่ $h(x_i)$:
$$p(d_i \mid h) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(d_i - h(x_i))^2}{2\sigma^2}\right)$$

เพราะข้อมูลแต่ละตัวเป็นอิสระต่อกัน (i.i.d.):
$$h_{ML} = \arg\max_{h \in H} \prod_{i=1}^{m} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(d_i - h(x_i))^2}{2\sigma^2}\right)$$

ถอด log ทั้งสองข้าง (การหา $\arg\max$ ไม่เปลี่ยนเมื่อผ่านฟังก์ชันเพิ่มขึ้นแบบ monotonic อย่าง $\ln$):
$$h_{ML} = \arg\max_{h \in H} \sum_{i=1}^{m} \left[ \ln \frac{1}{\sqrt{2\pi\sigma^2}} - \frac{1}{2\sigma^2}(d_i - h(x_i))^2 \right]$$

เทอมแรก $\ln \frac{1}{\sqrt{2\pi\sigma^2}}$ เป็นค่าคงที่ไม่ขึ้นกับ $h$ จึงตัดทิ้งได้ และเครื่องหมายลบหน้าเทอมที่สองทำให้ **maximize** กลายเป็น **minimize**:
$$\mathbf{h_{ML} = \arg\min_{h \in H} \sum_{i=1}^{m} (d_i - h(x_i))^2}$$

> [!important] ทำไมเรื่องนี้ถึงสำคัญมาก
> สมการสุดท้ายนี้คือ **Sum of Squared Error (SSE)** ซึ่งเป็นฟังก์ชันเป้าหมาย (Objective Function) เดียวกันกับที่ **Linear Regression** ใช้ในการหาค่าพารามิเตอร์ที่ดีที่สุด! นี่คือการพิสูจน์เชิงทฤษฎีความน่าจะเป็นว่า **"ทำไมการ Fit เส้นตรงด้วยวิธี Least Squares จึงสมเหตุสมผลทางสถิติ"** — เพราะภายใต้สมมติฐานว่าสัญญาณรบกวนเป็น Gaussian Noise ที่มีค่าเฉลี่ยศูนย์ สมมติฐาน Maximum Likelihood จะตรงกับสมมติฐานที่ Minimize SSE พอดี ซึ่งเป็นหลักการเดียวกับที่ใช้ในการหา Weight ของ Linear Unit ด้วย Gradient Descent ใน [[02-Gradient-Descent-and-Linear-Units|สัปดาห์ 05: Gradient Descent and Linear Units]]

---

### 6. ตัวจำแนกเบย์สที่เหมาะสมที่สุด (Bayes Optimal Classifier)

ทำไม $h_{MAP}$ จึงไม่ใช่ตัวจำแนกที่ดีที่สุดเสมอไป?
- สมมติมี 3 สมมติฐาน: $P(h_1 \mid D) = 0.4, P(h_2 \mid D) = 0.3, P(h_3 \mid D) = 0.3$
- $h_{MAP}$ คือ $h_1$ ซึ่งทำนายผลลัพธ์เป็น `+`
- แต่ $h_2$ และ $h_3$ ทำนายผลลัพธ์เป็น `-`
- หากรวมคะแนนเสียง: ผลลัพธ์ `-` มีน้ำหนักรวม $0.3 + 0.3 = 0.6$ ซึ่งชนะผลลัพธ์ `+` ที่มีเพียง $0.4$!

**Bayes Optimal Classifier** แก้ปัญหานี้โดยการรวมผลทำนายของทุกสมมติฐาน:
$$v_{BOC} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) \, P(h_i \mid D)$$
ให้ความแม่นยำสูงสุดในเชิงทฤษฎี แต่ในทางปฏิบัติมักคำนวณไม่ได้โดยตรงเพราะขนาดของ $H$ มีมหาศาล

> [!tip] MAP vs ML vs Bayes Optimal Classifier
> - $h_{MAP}$ และ $h_{ML}$ ประมาณค่าออกมาเป็น **สมมติฐานเดียว** ที่ดีที่สุดใน $H$
> - **Bayes Optimal Classifier** ไม่ได้เลือกสมมติฐานเดียว แต่ใช้ **การแจกแจงความน่าจะเป็นทั้งหมด** $P(h \mid D)$ ในการทำนาย
> - ความแตกต่างนี้จะเห็นชัดตอนทำนายข้อมูลใหม่ (Inference) — Bayes Optimal Classifier สามารถให้ผลทำนายที่ **ไม่ตรงกับสมมติฐานใดใน $H$ เลยสักตัว** ได้ เพราะเป็นผลรวมถ่วงน้ำหนักของทุกสมมติฐาน ไม่ใช่การเลือกใช้สมมติฐานใดสมมติฐานหนึ่ง

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
