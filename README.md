# 1322308 Machine Learning (การเรียนรู้ของเครื่อง)

คลังสรุปเนื้อหา แบบฝึกหัด และโปรเจกต์รายวิชา **1322308 การเรียนรู้ของเครื่อง (Machine Learning)**
สถาบันการจัดการปัญญาภิวัฒน์ (PIM) — ภาคการศึกษา 1/2569, กลุ่มเรียน 1.2-1 (3 หน่วยกิต)

---

## <span class="material-symbols-outlined">push_pin</span> ข้อมูลรายวิชาเบื้องต้น

- **รหัสวิชา:** 1322308
- **หน่วยกิต:** 3
- **กลุ่มเรียน:** 1.2-1

---

## <span class="material-symbols-outlined">folder_copy</span> โครงสร้าง Repository (Project Structure)

```text
02_1322308_Machine-Learning/
├── 00_Templates/          # Template โน้ตและคู่มือ format
├── 01_Lectures/
│   ├── 01_Docs/           # เอกสารและตำราประกอบการสอน (Ignored in Git)
│   ├── 02_Teaching_Slides/ # สไลด์ประกอบการสอนประจำสัปดาห์ (Ignored in Git)
│   └── Week*/              # โน้ตสรุปเนื้อหาบรรยายประจำสัปดาห์ (Markdown / Obsidian)
├── 02_Labs_Assignments/  # ใบงาน แบบฝึกหัด และโค้ดแล็บ
├── 03_Projects/          # โครงงานและโปรเจกต์ประจำวิชา
├── 04_Exams_Review/      # แนวข้อสอบ สรุปทบทวนก่อนสอบกลางภาคและปลายภาค
└── README.md             # เอกสารแนะนำและสารบัญหลัก
```

---

## <span class="material-symbols-outlined">menu_book</span> สารบัญเนื้อหาบรรยาย (Lecture Notes Index)

| สัปดาห์ | หัวข้อการบรรยาย | MOC (สารบัญประจำสัปดาห์) | หัวข้อย่อยเด่น |
| :---: | :--- | :--- | :--- |
| **Week 01** | Introduction to Machine Learning | [[Week01-MOC\|Week 01 MOC]] | นิยาม $T, P, E$, 4 ขั้นตอนการออกแบบระบบ, กฎการปรับน้ำหนัก LMS |
| **Week 02** | Concept Learning | [[Week02-MOC\|Week 02 MOC]] | ลำดับ General-to-Specific, อัลกอริทึม Find-S, Version Space, Inductive Bias |
| **Week 03** | Decision Tree Learning | [[Week03-MOC\|Week 03 MOC]] | Shannon Entropy, Information Gain, อัลกอริทึม ID3, Pruning, C4.5 |
| **Week 04** | k-Nearest Neighbor | [[Week04-MOC\|Week 04 MOC]] | Lazy Learning, $L_p$ Norms ($L_1, L_2, L_\infty$), CNN Prototype, kd-Tree, LSH |
| **Week 05** | Artificial Neural Networks | [[Week05-MOC\|Week 05 MOC]] | Perceptron, ปัญหา XOR, Gradient Descent, Delta Rule, Sigmoid, Backpropagation |
| **Week 06** | Clustering & Unsupervised Learning | [[Week06-MOC\|Week 06 MOC]] | Self-Organizing Maps (SOM), K-Means, Fuzzy C-Means, GMM, อัลกอริทึม EM |
| **Week 07** | Genetic Algorithms | [[Week07-MOC\|Week 07 MOC]] | Roulette Wheel, Crossover, Mutation, Curve Fitting, TSP & Cycle Crossover |
| **Week 08** | Bayesian Learning | [[Week08-MOC\|Week 08 MOC]] | ทฤษฎีบทของเบย์ส, MAP, Bayes Optimal, Naïve Bayes, Bayesian Belief Networks |
| **Week 09** | Support Vector Machine | [[Week09-MOC\|Week 09 MOC]] | Maximal Margin, Hard/Soft Margin, ตัวแปรหย่อน $\xi$, Kernel Trick (RBF), Multiclass |

---

## <span class="material-symbols-outlined">lightbulb</span> วิธีการใช้งาน (How to Use)

- **เปิดอ่านผ่าน GitHub:** สามารถคลิกลิงก์ Markdown เพื่ออ่านเนื้อหาผ่าน GitHub ได้ทันที
- **เปิดผ่าน Obsidian:** สามารถเปิดโฟลเดอร์นี้เป็น Obsidian Vault ได้ทันที รองรับ Wikilinks, MathJax ($...$), Callouts (`> [!info]`), และ Mermaid Diagrams
