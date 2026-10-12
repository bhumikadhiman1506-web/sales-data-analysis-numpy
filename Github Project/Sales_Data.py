import numpy as np
np.random.seed(20)
sales=np.random.randint(10000,60000,size=12)

print("Sales:\n",sales,"\n")

months=np.array(["January","February","March","April","May","June","July","August","September","October","November","December"])
print("Months:\n",months,"\n")

total_sales=sales.sum()
print("Total Annual Sales:",total_sales,"\n")
avg_sales=sales.mean()
print("Average Sales:",avg_sales.round(2),"\n")

print("----------Highest and Lowest Sales----------")
print("\n")
highest_sales_index=np.argmax(sales)
Highest_sales_month=months[highest_sales_index]
Highest_sales=sales[highest_sales_index]
print("Highest Sales:",Highest_sales)
print("Highest Sales Month:",Highest_sales_month)

Lowest_sales_index=np.argmin(sales)
Lowest_sales_month=months[Lowest_sales_index]
Lowest_sales=sales[Lowest_sales_index]
print("Lowest Sales:",Lowest_sales)
print("Lowest Sales Month:",Lowest_sales_month)

median_sales=np.median(sales)
print("Median Monthly Sales:",median_sales.round(2))

range_of_sales=sales.max()-sales.min()
print("Range of Sales:",range_of_sales)

Percentage_sales=(sales/total_sales)*100
print("Sales Percentage(%):",Percentage_sales.round(2),"\n")

growth_sales=(sales[1:]-sales[:-1])/sales[:-1]*100


print("Growth Sales:\n")
for i,growth in enumerate(growth_sales):
    print(f"{months[i+1]}:{growth_sales[i]:.2f}%")

quarters=["Q1","Q2","Q3","Q4"]
reshaped_sales=sales.reshape((4,3))
print("\n")
print("Quarterly Sales:\n",reshaped_sales)


sum_per_quarter=reshaped_sales.sum(axis=1)
print("Total Sales per Quarter:",sum_per_quarter)


highest_sales_quarter=sum_per_quarter.argmax()
print("Highest Quarter Sales:",sum_per_quarter[highest_sales_quarter])
print("Highest Quarter:",quarters[highest_sales_quarter])

lowest_sales_quarter=sum_per_quarter.argmin()
print("Lowest Qaurter Sales:",sum_per_quarter[lowest_sales_quarter])
print("Lowest Quarter:",quarters[lowest_sales_quarter])

print("\n")
print("----------Sales Greater Than Average----------\n")
sales_greater_than_avg=sales>avg_sales
sales_more=sales[sales_greater_than_avg]
months_more=months[sales_greater_than_avg]


for i,more_sale in enumerate(sales_more):
    print(f"{months_more[i]}:{sales_more[i]}")

print("\n")
print("----------Sales Less Than Average----------\n")
sales_less_than_avg=sales<avg_sales

sales_less=sales[sales_less_than_avg]
months_less=months[sales_less_than_avg]


for i,less_sale in enumerate(sales_less):
    print(f"{months_less[i]}:{sales_less[i]}")

print("\n")
print("------------Standard Deviation of Sales------------")
print("\n")
standard=sales.std()
print(standard.round(2))

print("\n")
print("------------Classification of Sales------------")
sales_classification=np.where(sales>avg_sales,"Above Average",np.where(sales<avg_sales,"Below Average","Equal To Average"))
print("Sales Calssification:\n",sales_classification,"\n")

categories,counts=np.unique(sales_classification,return_counts=True)
for category,count in zip(categories,counts):
    print(f"{category}:{count} months")
print("\n")

upper_threshold=avg_sales+standard
lower_threshold=avg_sales-standard


print("---------Unusually High Sales----------")
print("\n")
condition1=sales>upper_threshold
sales_above_upper=sales[condition1]
months_above_upper=months[condition1]


for i,upper in enumerate(sales_above_upper):
    print(f"{months_above_upper[i]}:{sales_above_upper[i]}")

print("\n")

print("----------Unusually Low Sales----------")
print("\n")
condition2=sales<lower_threshold
sales_below_lower=sales[condition2]
months_below_lower=months[condition2]

for i,lower in enumerate(sales_below_lower):
    print(f"{months_below_lower[i]}:{sales_below_lower[i]}")
print("\n")

print("---------------Months with Highest Positive Growth Rate--------------\n")

highest_rate=np.argmax(growth_sales)
print(f"Highest Growth-{months[highest_rate+1]}:{growth_sales[highest_rate]:.2f}%\n")


lowest_rate=np.argmin(growth_sales)
print(f"Largest Decline-{months[lowest_rate+1]}:{growth_sales[lowest_rate]:.2f}%\n")


print("----------Sales Summary----------\n")
sales_summary=np.array([total_sales,avg_sales,median_sales,Highest_sales,Lowest_sales])


summary_labels=np.array(["Total Sales","Average Sales","Median Sales","Highest Sales","Lowest Sales"])

for i,summary in enumerate(sales_summary):
    print(f"{summary_labels[i]}:{sales_summary[i]:.2f}")
