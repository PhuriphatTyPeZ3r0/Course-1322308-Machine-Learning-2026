---
tags: [ml, week08, naive-bayes, conditional-independence, play-tennis, text-classification, laplace-smoothing]
course: 1322308
week: 8
date: 2026-09-13
---

# ตัวจำแนกแบบนาอีฟเบย์สและการประยุกต์จำแนกข้อความ (Naïve Bayes & Text Classification)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week08-MOC|MOC สัปดาห์ 08]] | ก่อนหน้า: [[01-Bayes-Theorem-MAP-and-Bayes-Optimal-Classifier]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Naïve Bayes Classifier** — ตัวจำแนกความน่าจะเป็นที่ตั้งสมมติฐานแบบไร้เดียงสา (Naïve) ว่าทุกคุณลักษณะมีความเป็นอิสระต่อกันเมื่อทราบคลาสเป้าหมายแล้ว
- **Conditional Independence Assumption** — สมมติฐานว่าความน่าจะเป็นของแอตทริบิวต์หนึ่งจะไม่ส่งผลกระทบต่อแอตทริบิวต์อื่นเมื่อกำหนดคลาส $v_j$
- **Zero-Frequency Problem** — ปัญหาเมื่อพบแอตทริบิวต์ที่ไม่เคยปรากฏในข้อมูลฝึกฝนของคลาสนั้น ทำให้ความน่าจะเป็นรวมกลายเป็นศูนย์ทั้งหมด
- **$m$-estimate / Laplace Smoothing** — เทคนิคการปรับความเรียบเพื่อป้องกันความน่าจะเป็นศูนย์ โดยเพิ่มค่าน้ำหนักจำลองเข้าไปในตัวเศษและตัวส่วน
- **Bag-of-Words (BoW)** — รูปแบบการแทนเอกสารข้อความด้วยความถี่ของคำในคลังคำศัพท์ (Vocabulary) โดยไม่สนใจไวยากรณ์และลำดับคำ

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. สมมติฐานความอิสระแบบมีเงื่อนไข (The Naïve Bayes Assumption)

ในการทำนายคลาส $v_j \in V$ จากเวกเตอร์คุณลักษณะ $\mathbf{x} = \langle a_1, a_2, \dots, a_n \rangle$:
$$v_{MAP} = \arg\max_{v_j \in V} P(v_j) P(a_1, a_2, \dots, a_n \mid v_j)$$

เนื่องจากการประมาณค่าความน่าจะเป็นร่วม $P(a_1, \dots, a_n \mid v_j)$ ต้องใช้ข้อมูลจำนวนมหาศาลแบบก้าวกระโดด ($2^n$) นาอีฟเบย์สจึงตั้งสมมติฐานว่า:
> *"ทุกแอตทริบิวต์มีความเป็นอิสระต่อกันเชิงความน่าจะเป็น เมื่อทราบค่าคลาสเป้าหมาย $v_j$ แล้ว"*

ทำให้สามารถแยกเทอมความน่าจะเป็นร่วมออกเป็น **ผลคูณของความน่าจะเป็นเดี่ยว**:
$$P(a_1, a_2, \dots, a_n \mid v_j) = \prod_{i=1}^n P(a_i \mid v_j)$$

#### สูตรหลักของ Naïve Bayes Classifier:
$$\mathbf{v_{NB} = \arg\max_{v_j \in V} P(v_j) \prod_{i=1}^n P(a_i \mid v_j)}$$

---

### 2. ตัวอย่างการคำนวณจริงทีละสเต็ปบนชุดข้อมูล PlayTennis

ต้องการทำนายวันที่มีสภาพอากาศใหม่:
$$\mathbf{x} = \langle Outlook = Sunny,\; Temp = Cool,\; Humidity = High,\; Wind = Strong \rangle$$

ข้อมูลสอน 14 วัน มี $Play = Yes$ (9 วัน) และ $Play = No$ (5 วัน):
- $P(Yes) = \frac{9}{14} \approx 0.643$
- $P(No) = \frac{5}{14} \approx 0.357$

#### 1. คำนวณคะแนนสำหรับคลาส $Yes$:
- $P(Sunny \mid Yes) = 2/9$
- $P(Cool \mid Yes) = 3/9$
- $P(High \mid Yes) = 3/9$
- $P(Strong \mid Yes) = 3/9$
$$Score(Yes) = P(Yes) \prod P(a_i \mid Yes) = \frac{9}{14} \times \frac{2}{9} \times \frac{3}{9} \times \frac{3}{9} \times \frac{3}{9} \approx \mathbf{0.00529}$$

#### 2. คำนวณคะแนนสำหรับคลาส $No$:
- $P(Sunny \mid No) = 3/5$
- $P(Cool \mid No) = 1/5$
- $P(High \mid No) = 4/5$
- $P(Strong \mid No) = 3/5$
$$Score(No) = P(No) \prod P(a_i \mid No) = \frac{5}{14} \times \frac{3}{5} \times \frac{1}{5} \times \frac{4}{5} \times \frac{3}{5} \approx \mathbf{0.02057}$$

#### 3. สรุปผลการตัดสินใจ:
เนื่องจาก $Score(No) = 0.02057 > Score(Yes) = 0.00529$:
$$\mathbf{v_{NB} = No \text{ (ไม่ไปเล่นเทนนิส)}}$$
เมื่อ Normalize ให้เป็นความน่าจะเป็น:
$$P(No \mid \mathbf{x}) = \frac{0.02057}{0.02057 + 0.00529} \approx \mathbf{79.5\%}, \quad P(Yes \mid \mathbf{x}) \approx \mathbf{20.5\%}$$

---

### 3. ปัญหาความถี่ศูนย์และการแก้ด้วย $m$-estimate (Laplace Smoothing)

หากในข้อมูลสอนไม่เคยมีตัวอย่างที่ $Outlook=Overcast$ ในวันที่ $Play=No$ เลย ($n_c = 0$):
$$P(Overcast \mid No) = \frac{0}{5} = 0$$
ค่า $0$ นี้จะทำให้ผลคูณทั้งหมดกลายเป็น $0$ ทันที แม้ว่าฟีเจอร์อื่น ๆ จะบ่งชี้ว่าเป็น $No$ อย่างท่วมท้นก็ตาม

#### การแก้ปัญหาด้วย $m$-estimate of probability:
$$P(a_i \mid v_j) = \frac{n_c + m \cdot p}{n + m}$$
โดย:
- $n$ = จำนวนตัวอย่างทั้งหมดในคลาส $v_j$
- $n_c$ = จำนวนตัวอย่างในคลาส $v_j$ ที่มีฟีเจอร์ $a_i$
- $p$ = ค่าประมาณการล่วงหน้า เช่น $\frac{1}{k}$ (เมื่อมี $k$ ค่าที่เป็นไปได้)
- $m$ = น้ำหนักความเชื่อมั่นเสมือน (Equivalent sample size)

ในกรณีพิเศษของ **Laplace Smoothing (Add-1)** กำหนดให้ $m = k$ และ $p = \frac{1}{k}$:
$$P(a_i \mid v_j) = \frac{n_c + 1}{n + k}$$

---

### 4. การประยุกต์ใช้ในการจำแนกประเภทเอกสารข้อความ (Text Classification)

ในการจำแนกหัวข้อข่าวหรือกรองสแปมอีเมล (Spam Filter):
- แทนเอกสารด้วยคลังคำศัพท์ $Vocabulary$ ทั้งหมดที่มีในคลัง
- ความน่าจะเป็นของแต่ละคำ $w_k$ ในหมวดหมู่ $v_j$:
  $$P(w_k \mid v_j) = \frac{n_k + 1}{n + |Vocabulary|}$$
  โดย $n_k$ คือจำนวนครั้งที่คำว่า $w_k$ ปรากฏในเอกสารหมวด $v_j$ และ $n$ คือจำนวนคำทั้งหมดในหมวดนั้น

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart TD
    Start((●)) --> InputDoc([รับข้อมูลตัวอย่างนำเข้า<br>Input Vector x = ⟨a₁, a₂, ..., aₙ⟩])
    InputDoc --> SplitFeat([แยกคุณลักษณะเดี่ยวอิสระ<br>Conditional Independence Split])
    SplitFeat --> ProbYes([คำนวณคะแนนคลาสบวก<br>P(Yes) · ∏ P(aᵢ|Yes)])
    SplitFeat --> ProbNo([คำนวณคะแนนคลาสลบ<br>P(No) · ∏ P(aᵢ|No)])
    ProbYes --> Compare{เปรียบเทียบคะแนนความน่าจะเป็น<br>Argmax Class Scores?}
    ProbNo --> Compare
    Compare -- คะแนน Yes สูงกว่า --> PredYes([ทำนายผลลัพธ์เป็น Yes<br>Classify: Positive])
    Compare -- คะแนน No สูงกว่า --> PredNo([ทำนายผลลัพธ์เป็น No<br>Classify: Negative])
    PredYes --> EndNode(((●)))
    PredNo --> EndNode
```

**ตัวอย่าง:** ผังขั้นตอนการคำนวณผลคูณความน่าจะเป็นแยกตามคลาสใน Naïve Bayes

---
<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[03-Bayesian-Belief-Networks]]
