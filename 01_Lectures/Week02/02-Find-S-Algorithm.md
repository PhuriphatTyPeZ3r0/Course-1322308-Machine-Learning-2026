---
tags: [ml, week02, find-s, algorithm-trace, limitations]
course: 1322308
week: 2
date: 2026-09-13
---

# อัลกอริทึม Find-S และการค้นหาสมมติฐานเฉพาะเจาะจง (Find-S Algorithm)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week02-MOC|MOC สัปดาห์ 02]] | ก่อนหน้า: [[01-Concept-Learning-and-General-to-Specific-Ordering]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Find-S Algorithm** — อัลกอริทึมค้นหาสมมติฐานที่เน้นเริ่มจากสมมติฐานที่เฉพาะเจาะจงที่สุด แล้วค่อย ๆ ขยายขอบเขต (Generalize) ให้ครอบคลุมเฉพาะตัวอย่างบวก
- **Most Specific Hypothesis ($h_0$)** — สมมติฐานเริ่มต้นที่ไม่ยอมรับอินสแตนซ์ใดเลย ($\langle \varnothing, \varnothing, \varnothing, \varnothing, \varnothing, \varnothing \rangle$)
- **Generalization Step** — การผ่อนปรนเงื่อนไขในสมมติฐานจากค่าเฉพาะเจาะจงไปเป็นเครื่องหมาย `?` เมื่อพบตัวอย่างบวกที่ไม่ตรงกับเงื่อนไขเดิม
- **Negative Example Invariance** — คุณสมบัติของ Find-S ที่ไม่นำตัวอย่างลบ (Negative examples) มาใช้ในการปรับค่าสมมติฐานโดยตรง

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. กลไกการทำงานของอัลกอริทึม Find-S

อัลกอริทึม Find-S ทำงานโดยการสำรวจ Hypothesis Space จากล่างขึ้นบน (Specific-to-General):

```text
1. กำหนดค่าเริ่มต้น h = ⟨Ø, Ø, Ø, Ø, Ø, Ø⟩ (สมมติฐานเฉพาะเจาะจงที่สุด)
2. สำหรับแต่ละตัวอย่างฝึกฝนที่เป็นบวก (Positive instance x):
     สำหรับแต่ละแอตทริบิวต์ a_i ใน h:
       ถ้า a_i ใน h สอดคล้องกับค่าของ x -> ไม่ต้องแก้ไข
       ถ้า a_i ใน h ขัดแย้งกับค่าของ x -> แทนที่ a_i ด้วยเงื่อนไขที่ทั่วไปขึ้นขั้นต่ำสุด (แทนด้วยค่า x หรือ ?)
3. คืนค่าสมมติฐาน h สุดท้าย
```

> [!important] ข้อสังเกตสำคัญ
> ตัวอย่างลบ (Negative Examples, ป้ายกำกับ `-` หรือ `No`) จะถูก **ข้ามการทำงานทั้งหมด** ใน Find-S!

---

### 2. การแกะรอยการทำงานทีละขั้นตอน (Step-by-Step Trace)

ข้อมูลตัวอย่าง 4 วัน:
- $x_1 = \langle Sunny, Warm, Normal, Strong, Warm, Same \rangle \to \mathbf{+}$
- $x_2 = \langle Sunny, Warm, High, Strong, Warm, Same \rangle \to \mathbf{+}$
- $x_3 = \langle Rainy, Cold, High, Strong, Warm, Change \rangle \to \mathbf{-}$
- $x_4 = \langle Sunny, Warm, High, Strong, Cool, Change \rangle \to \mathbf{+}$

#### การอัปเดตสถานะสมมติฐาน:
1. **เริ่มต้น ($h_0$):**
   $$h_0 = \langle \varnothing, \varnothing, \varnothing, \varnothing, \varnothing, \varnothing \rangle$$
2. **ประมวลผล $x_1$ (Positive):**
   เนื่องจากเดิมเป็น $\varnothing$ ทั้งหมด จึงแทนที่ด้วยค่าจริงของ $x_1$:
   $$h_1 = \langle Sunny, Warm, Normal, Strong, Warm, Same \rangle$$
3. **ประมวลผล $x_2$ (Positive):**
   เปรียบเทียบ $h_1$ กับ $x_2$:
   - `Humidity`: เดิมคือ `Normal` แต่ $x_2$ คือ `High` $\implies$ ผ่อนปรนเป็น `?`
   - แอตทริบิวต์อื่นตรงกันหมด คงเดิมไว้:
   $$h_2 = \langle Sunny, Warm, \mathbf{?}, Strong, Warm, Same \rangle$$
4. **ประมวลผล $x_3$ (Negative):**
   เนื่องจากเป็นตัวอย่างลบ Find-S จะไม่ทำอะไร:
   $$h_3 = h_2 = \langle Sunny, Warm, ?, Strong, Warm, Same \rangle$$
5. **ประมวลผล $x_4$ (Positive):**
   เปรียบเทียบ $h_3$ กับ $x_4$:
   - `Water`: เดิมคือ `Warm` แต่ $x_4$ คือ `Cool` $\implies$ เปลี่ยนเป็น `?`
   - `Forecast`: เดิมคือ `Same` แต่ $x_4$ คือ `Change` $\implies$ เปลี่ยนเป็น `?`
   $$h_4 = \langle Sunny, Warm, ?, Strong, \mathbf{?}, \mathbf{?} \rangle$$

---

### 3. คุณสมบัติและข้อจำกัดของ Find-S (Properties & Limitations)

- **จุดเด่น:** Find-S รับประกันว่าจะได้สมมติฐานที่แคบที่สุด (Most Specific) ที่ครอบคลุมตัวอย่างบวกทั้งหมดเสมอ
- **ข้อจำกัด 4 ประการ (มักเป็นข้อสอบข้อเขียน):**
  1. **ไม่รู้ว่าลู่เข้าสู่คำตอบแท้จริงหรือยัง (Convergence uncertainty):** ไม่สามารถทราบได้ว่าสมมติฐานที่ได้เป็นคำตอบเดียวที่สอดคล้อง หรือยังมีสมมติฐานอื่นอีกในระบบ
  2. **ทนทานต่อสัญญาณรบกวนไม่ได้ (No tolerance to noise):** หากมีข้อมูลผิดพลาด (Error/Noise) ปนมาแม้แต่จุดเดียว จะทำให้ขอบเขตของ $h$ ขยายกว้างเกินจริงอย่างถาวร
  3. **ละเลยตัวอย่างลบ (Ignores negative examples):** ไม่สามารถตรวจสอบความขัดแย้ง (Inconsistency) ของข้อมูลได้
  4. **อคติในการเลือกเฉพาะเจาะจง (Arbitrary bias):** หากมีสมมติฐานเฉพาะเจาะจงสูงสุดหลายตัว Find-S จะเลือกมาเพียงตัวเดียวโดยไม่มีเกณฑ์ทางทฤษฎีสนับสนุน

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart TD
    Start((●)) --> Init([เริ่มต้นสมมติฐานจำเพาะสูงสุด<br>Initialize: h₀ = ⟨Ø, Ø, Ø, Ø, Ø, Ø⟩])
    Init --> Read([อ่านตัวอย่างฝึกฝนถัดไป<br>Read Next Instance: ⟨x, c(x)⟩])
    Read --> CheckPos{เป็นตัวอย่างบวกหรือไม่?<br>Positive Instance: c(x) == + ?}
    CheckPos -- ไม่ใช่ (-) --> Skip([เพิกเฉยตัวอย่างลบ<br>Ignore Negative Example])
    CheckPos -- ใช่ (+) --> CheckMatch{ค่าแอตทริบิวต์ตรงกับ h หรือไม่?<br>Attribute Matches h_i?}
    CheckMatch -- ตรงกัน --> Keep([คงค่าเดิมไว้<br>Retain Constraint])
    CheckMatch -- ไม่ตรงกัน --> Gen([ผ่อนปรนเป็นเครื่องหมาย ?<br>Generalize Constraint: ?])
    Keep --> More{ยังมีข้อมูลเหลือหรือไม่?<br>Has More Data?}
    Gen --> More
    Skip --> More
    More -- มีข้อมูล --> Read
    More -- หมดแล้ว --> Done([ส่งออกสมมติฐานสุดท้าย h<br>Output Final Hypothesis])
    Done --> EndNode(((●)))
```

**ตัวอย่าง:** ผังขั้นตอนการทำงานของ Find-S ที่เน้นขยายขอบเขตจากล่างขึ้นบนเฉพาะเมื่อพบตัวอย่างบวก

---
<span class="material-symbols-outlined">arrow_forward</span> ต่อไป: [[03-Candidate-Elimination-and-Inductive-Bias]]
