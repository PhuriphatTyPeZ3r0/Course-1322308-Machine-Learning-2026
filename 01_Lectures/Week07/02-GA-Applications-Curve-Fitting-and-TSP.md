---
tags: [ml, week07, ga-applications, curve-fitting, tsp, cycle-crossover]
course: 1322308
week: 7
date: 2026-09-13
---

# การประยุกต์ใช้ GA ในการประมาณฟังก์ชันและปัญหาการเดินทางของพนักงานขาย (GA Applications: Curve Fitting & TSP)

<span class="material-symbols-outlined">arrow_back</span> กลับไปที่ [[Week07-MOC|MOC สัปดาห์ 07]] | ก่อนหน้า: [[01-Genetic-Algorithms-Foundations-and-Operators]]

## <span class="material-symbols-outlined">key</span> Keyword

- **Polynomial Curve Fitting** — การปรับจูนสัมประสิทธิ์ของฟังก์ชันพหุนามเพื่อให้กราฟลากผ่านจุดข้อมูลตัวอย่างได้อย่างแนบเนียนที่สุด
- **Traveling Salesperson Problem (TSP)** — ปัญหาการหาเส้นทางเดินทางเชื่อมต่อเมืองทุกเมืองให้ครบโดยผ่านแต่ละเมืองเพียงครั้งเดียวและมีระยะทางรวมสั้นที่สุด (NP-hard)
- **Permutation Chromosome** — โครโมโซมที่เก็บลำดับการเรียงสับเปลี่ยนของสมาชิกที่ไม่ซ้ำกัน
- **Cycle Crossover (CX)** — ตัวดำเนินการครอสโอเวอร์พิเศษสำหรับโครโมโซมแบบเรียงสับเปลี่ยน เพื่อป้องกันปัญหาเมืองซ้ำซ้อนหรือตกหล่น
- **Elitism** — กลยุทธ์การคัดลอกคำตอบที่ดีที่สุดในรุ่นปัจจุบันข้ามไปยังรุ่นถัดไปโดยตรง เพื่อป้องกันไม่ให้คำตอบที่ดีที่สุดสูญหายไปจากการผสมพันธุ์

## <span class="material-symbols-outlined">menu_book</span> Theory (เข้าใจง่าย)

### 1. การปรับจูนเส้นโค้งพหุนาม (Polynomial Curve Fitting with GA)

กำหนดให้มีจุดข้อมูลพิกัด $(x, y)$ ปริมาณมาก และต้องการหาฟังก์ชันพหุนามดีกรี 5:
$$y = c_5 x^5 + c_4 x^4 + c_3 x^3 + c_2 x^2 + c_1 x + c_0$$

#### การออกแบบองค์ประกอบ GA:
- **โครงสร้างโครโมโซม:** อาเรย์ของจำนวนจริง 6 ตัวแทนสัมประสิทธิ์:
  $$\mathbf{c} = [c_5, c_4, c_3, c_2, c_1, c_0]$$
- **ฟังก์ชันประเมินความผิดพลาด (Loss / Badness):**
  $$Badness(\mathbf{c}) = \sum_{i=1}^M |y_i - (c_5 x_i^5 + \dots + c_0)|$$
- **Fitness Function:** $Fitness(\mathbf{c}) = \frac{1}{1 + Badness(\mathbf{c})}$
- **กระบวนการทำงาน:**
  1. สร้างประชากรเริ่มต้น 100 โครโมโซม สุ่มค่าจำนวนจริง
  2. วนซ้ำ 500 เจเนอเรชัน:
     - คำนวณความคลาดเคลื่อนของทั้ง 100 โครโมโซม
     - เลือกเก็บ 10 อันดับที่ดีที่สุดไว้โดยตรง (**Elitism**)
     - สร้างอีก 90 โครโมโซมที่เหลือด้วยการ Crossover และ Mutation จากกลุ่มที่ดีที่สุด
  3. ได้ชุดสัมประสิทธิ์ที่ฟิตกับข้อมูลอย่างแม่นยำ

---

### 2. ปัญหาการเดินทางของพนักงานขาย (Traveling Salesperson Problem: TSP)

TSP เป็นโจทย์แบบ Combinatorial Optimization:
- **โครโมโซม:** ลำดับการแวะเยี่ยมเมือง เช่น มี 6 เมือง: $[2, 3, 1, 4, 5, 6]$
- **Fitness:** ระยะทางรวมของการเดินทางทั้งวงรอบ (ต้องการหาระยะทางสั้นที่สุด $\implies$ Fitness แปรผกผันกับผลรวมระยะทาง)

> [!important] ทำไม Crossover แบบธรรมดาจึงใช้กับ TSP ไม่ได้?
> หากใช้ Single-point Crossover แบบทั่วไป เช่น ตัดท่อนสลับกัน จะทำให้เกิดปัญหา **เมืองบางเมืองซ้ำซ้อนกัน** และ **บางเมืองตกหล่นหายไป** ซึ่งผิดกฎกติกาของเส้นทางเดิน จึงต้องใช้เทคนิคครอสโอเวอร์แบบพิเศษ เช่น **Cycle Crossover (CX)**

---

### 3. ตัวดำเนินการ Cycle Crossover (CX) ทีละขั้นตอนตามสไลด์

กำหนดโครโมโซมพ่อแม่ 6 เมือง:
- **Parent 1:** `1   2   3   4   5   6`
- **Parent 2:** `6   4   3   2   1   5`

#### ขั้นตอนการสร้าง Cycle:
1. **เริ่มที่ตำแหน่งที่ 1:**  
   Parent 1 มีค่า `1` ตรงกับ Parent 2 ที่มีค่า `6`
2. **ตามหาค่า `6` ใน Parent 1:**  
   พบค่า `6` อยู่ที่ตำแหน่งที่ 6 ซึ่งใน Parent 2 ตำแหน่งนี้คือค่า `5`
3. **ตามหาค่า `5` ใน Parent 1:**  
   พบค่า `5` อยู่ที่ตำแหน่งที่ 5 ซึ่งใน Parent 2 ตำแหน่งนี้คือค่า `1`
4. **ครบรอบ Cycle:**  
   ค่า `1` วนกลับมาชนกับค่าเริ่มต้นที่ตำแหน่ง 1 $\implies$ **ได้วงรอบ Cycle ที่ 1 ประกอบด้วยตำแหน่ง index: {1, 5, 6}**

#### การสร้างโครโมโซมลูก (Offspring):
- **Child 1:**  
  - ตำแหน่งใน Cycle {1, 5, 6} ให้ดึงค่ามาจาก **Parent 1** โดยตรง:
    - ตำแหน่ง 1 $\to$ `1`
    - ตำแหน่ง 5 $\to$ `5`
    - ตำแหน่ง 6 $\to$ `6`
  - ตำแหน่งที่เหลือนอก Cycle {2, 3, 4} ให้ดึงค่ามาจาก **Parent 2**:
    - ตำแหน่ง 2 $\to$ `4`
    - ตำแหน่ง 3 $\to$ `3`
    - ตำแหน่ง 4 $\to$ `2`
  - **ผลลัพธ์ Child 1:** `1   4   3   2   5   6` (เป็น Permutation ที่สมบูรณ์ ไร้เมืองซ้ำ!)

- **Child 2:** ใช้วิธีตรงกันข้าม ได้ผลลัพธ์เป็น: `6   2   3   4   1   5`

## <span class="material-symbols-outlined">schema</span> Diagram

```mermaid
flowchart TD
    Start((●)) --> InputP([รับโครโมโซมคู่พ่อแม่<br>Input Parent Chromosomes])

    subgraph Parents ["โครโมโซมพ่อแม่ (Parent Chromosomes)"]
        P1(["Parent 1: [1, 2, 3, 4, 5, 6]"])
        P2(["Parent 2: [6, 4, 3, 2, 1, 5]"])
    end

    InputP --> Parents
    Parents --> TraceCycle([ตรวจจับวงรอบ Cycle 1<br>Trace Cycle: 1 ➔ 6 ➔ 5 ➔ 1])
    TraceCycle --> ConstructChild([สร้างโครโมโซมลูก Child 1<br>Fill Positions from Parents])
    ConstructChild --> Result([ได้ Child 1: [1, 4, 3, 2, 5, 6]<br>Valid Non-Repeating Permutation])
    Result --> EndNode(((●)))
```

**ตัวอย่าง:** ผังขั้นตอนการจับคู่และสลับข้อมูลด้วย Cycle Crossover (CX) สำหรับโจทย์ TSP

---
<span class="material-symbols-outlined">arrow_forward</span> กลับไปที่: [[Week07-MOC|MOC สัปดาห์ 07]]
