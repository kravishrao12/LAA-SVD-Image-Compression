# Image Compression using Singular Value Decomposition (SVD)

## 👥 Team Members
- K Ravish Rao (PES1UG24AM127)  
- K R Manoj (PES1UG24AM125)  
- Manjunatha H J (PES1UG24AM157)  
- Mohit S (PES1UG24AM166)

---

## 📌 Objective
To implement image compression using **Singular Value Decomposition (SVD)** and analyze the trade-off between compression ratio and reconstruction quality using Linear Algebra.

---

## 🧠 Background

An image can be represented as a matrix \( A \in \mathbb{R}^{m \times n} \).  
SVD factorizes the matrix as:

\[
A = U \Sigma V^T
\]

- \( U \): left singular vectors  
- \( \Sigma \): diagonal matrix of singular values (importance)  
- \( V^T \): right singular vectors  

By retaining only the top-**k** singular values, we form a **rank-k approximation**:

\[
A_k = U_k \Sigma_k V_k^T
\]

This reduces storage while preserving dominant information.

---

## ⚙️ Methodology

1. Read input image (RGB / grayscale)  
2. Convert image → matrix representation  
3. Apply SVD on:
   - Entire matrix (grayscale), or  
   - Each channel separately (RGB)  
4. Retain top-k singular values  
5. Reconstruct compressed image  
6. Evaluate:
   - Mean Squared Error (MSE)  
   - Compression Ratio  
7. Visualize outputs for different k values  

---

## 🚀 Features

- Supports **RGB and grayscale images**  
- Adjustable compression via **k parameter**  
- Computes **MSE (reconstruction error)**  
- Calculates **compression ratio**  
- Saves compressed images automatically  
- Visual comparison across compression levels  

---

## 📊 Results

| k Value | Compression Level | Observation |
|--------|------------------|------------|
| 5      | Very High        | Highly blurred, only coarse structure |
| 20     | High             | Object recognizable, noise present |
| 50     | Medium           | Good clarity, balanced compression |
| 100    | Low              | Near-original quality |

---

## 📈 Analysis

- Increasing **k** → retains more singular values → **better quality**
- Increasing **k** → increases stored data → **lower compression**
- Demonstrates **trade-off between compression and fidelity**

---

## 🧮 Mathematical Insight

- Image = matrix in vector space  
- Singular values represent **energy / importance**  
- Majority of energy is concentrated in top singular values  
- Rank reduction ≈ dimensionality reduction  

---

## 🛠️ Tech Stack

- **Python**  
- **NumPy** (linear algebra operations)  
- **OpenCV** (image processing)  
- **Matplotlib** (visualization)  

---

## 📁 Project Structure
MINIPROJECT/
│
├── main.py
├── images/
│ └── sample.jpg
├── output/
│ ├── compressed_k5.jpg
│ ├── compressed_k20.jpg
│ ├── compressed_k50.jpg
│ └── compressed_k100.jpg
