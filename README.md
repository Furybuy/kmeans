# 🛍️ Mall Customer Segmentation: K-Means Clustering Analysis

This project explores customer segmentation using an unsupervised machine learning approach via **K-Means Clustering** implemented in Python with `scikit-learn`. The primary objective is to group mall customers into distinct behavioral and demographic clusters based on their **Age** and **Spending Score (1-100)**.

---

## 📂 Project Structure & Workflow

The script (`kmeans.py`) performs the following standard machine learning and exploratory data workflow:
1. **Data Loading:** Imports the dataset from `Mall_Customers.csv`.
2. **Exploratory Data Analysis (EDA):** Generates an initial scatter plot visualizing the distribution of customer age versus spending score.
3. **Feature Selection:** Extracts relevant input dimensions (`Age` and `Spending Score (1-100)`) for cluster modeling.
4. **Model Initialization:** Configures the `KMeans` model with $k=5$ clusters using the `k-means++` initialization strategy for optimized centroid placement.
5. **Prediction & Grouping:** Fits the model and predicts cluster labels for every customer instance.
6. **Cluster Visualization:** Plots color-coded scatter charts displaying distinct customer segments, legends, and grid boundaries.

---

## ⚙️ Data Dimensions & Features

The model analyzes two primary attributes from the dataset:
* **`Age`**: Demographic dimension representing the age of the customer.
* **`Spending Score (1-100)`**: Behavioral/transactional dimension assigned by the shopping mall based on purchasing habits and customer spending nature.

---

## 🤖 Model Configuration & Training

### K-Means Unsupervised Model
* **Algorithm:** K-Means Clustering
* **Number of Clusters ($k$):** `5`
* **Initialization Method:** `k-means++` (ensures smarter initial centroid seeding to accelerate convergence and avoid local optima)
* **Features ($X$):** `Age`, `Spending Score (1-100)`

---

## 📊 Visualizations Included

The script generates sequential `matplotlib` charts to aid interpretation:
- **EDA Scatter Plot:** Raw distribution chart plotting customer age against spending score before segmentation.
- **Segmented Cluster Plot:** Color-coded multi-cluster visualization (`Cluster 0` to `Cluster 4`) displaying distinct customer groups, cluster centers, legends, and grid lines.
