# Sales Data Analysis Using NumPy
## Project Overview

### Technologies Used
• Python
• NumPy

## Dataset

The dataset contains sales values for 12 months, from January to December. The sales data is randomly generated using NumPy, with a fixed random seed to make the results reproducible.

## Analysis Performed
• Calculated total, average, and median sales.

• Identified the months with the highest and lowest sales.

• Calculated the range and standard deviation of sales.

• Calculated each month's percentage contribution to annual sales.

• Analyzed month-over-month sales growth and decline.

• Reshaped monthly sales data into quarterly data and compared quarterly totals.

• Filtered months with sales above and below the annual average.

• Classified monthly sales as above average, below average, or equal to average.

• Identified months with unusually high or low sales using the average and standard deviation.

• Created a summary of the key sales statistics.

## Key Findings

• Total annual sales: 411,290

• Average monthly sales: 34,274.17

• Median monthly sales: 33,613.50

• Highest sales: 58,483 in January

• Lowest sales: 11,607 in October

• Standard deviation of monthly sales: 14,754.12

## NumPy Concepts Practiced

• Array creation and indexing

• Array slicing and Boolean filtering

• Aggregation methods such as sum(), mean(), median(), and std()

• argmax() and argmin()

• Array reshaping and axis-based operations

• np.where()

• np.unique() with return_counts=True

• np.any() and conditional checks

## How to Run

1. Install Python if it is not already installed.

2. Install NumPy by running:
    pip install numpy

4. Run the Python script:
    python sales_analysis.py

Replace sales_analysis.py with the actual name of your Python file if it is different.

##Learning Outcome

This project helped me practice NumPy arrays, statistical calculations, Boolean indexing, conditional classification, growth-rate calculations, and quarterly sales analysis.