# 🚗 Car Price Prediction using Machine Learning

This project predicts the **selling price of a used car** based on multiple factors such as the year of manufacture, present showroom price, kilometers driven, fuel type, transmission, seller type, and number of previous owners.

The goal of this project is to demonstrate how **regression-based machine learning models** can be used to estimate real-world prices and support better decision-making for buyers and sellers.

---

## 📊 Dataset Information

The dataset consists of historical records of used cars with their technical specifications and selling prices.

### Features Used:
- **Year** – Year in which the car was manufactured  
- **Present_Price** – Current showroom price of the car (in lakhs)  
- **Kms_Driven** – Total kilometers driven  
- **Fuel_Type** – Petrol / Diesel / CNG  
- **Seller_Type** – Dealer or Individual  
- **Transmission** – Manual or Automatic  
- **Owner** – Number of previous owners  

### Target Variable:
- **Selling_Price** – Actual selling price of the car (in lakhs)

---

## 🧩 Steps Involved

1. **Data Loading**
   - Loaded the dataset from an Excel file using Pandas.

2. **Data Preprocessing**
   - Handled categorical variables using encoding techniques.
   - Selected relevant features for prediction.

3. **Exploratory Data Analysis (EDA)**
   - Analyzed relationships between features and the target variable.
   - Identified important factors affecting car prices.

4. **Model Building**
   - Split the dataset into training and testing sets.
   - Trained a **Linear Regression model** to predict car prices.

5. **Model Evaluation**
   - Evaluated the model using:
     - R² Score
     - Mean Absolute Error (MAE)

6. **Prediction System**
   - Built a user-input-based prediction system.
   - Allowed real-time price prediction based on car details.

7. **Model Deployment**
   - Saved the trained model using Pickle.
   - Deployed the model using **Streamlit** for interactive usage.

---

## 📈 Model Performance

- **R² Score:** ~0.85  
- **Mean Absolute Error (MAE):** ~1.22  

These results indicate strong predictive performance and good generalization.

---

## 🛠️ Tools & Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Pickle**

---

## 👩‍💻 Author
**Pranshi**

   git clone https://github.com/your-username/car-price-prediction.git
