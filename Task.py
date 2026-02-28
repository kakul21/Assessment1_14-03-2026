'''Problem Statement
An electricity board charges consumers based on units consumed:
First 100 units → ₹5 per unit
Next 200 units → ₹7 per unit
Above 300 units → ₹10 per unit
Calculate total bill amount.'''
 
def calculate_bill(self, units):
    if(units<=100):
        bill = units*5
    elif(units<=300):
        bill=(100*5)+((units-100)*7)
    else:
        bill=(100*5)+(200*7)+((units-300)*10)
    return bill

# Shopping Cart Stock Checker
    
def process_items(self, items):
    result = []
    for i in items:
        if i>10:
            result.append("Stock Limit Exceeded")
            break
        elif(i<=0):
            break
        else:
            result.append(f"Item Accepted: {i}")
    return result
        
#Multi Subject Result System
    
def evaluate_result(self, marks_list):
    for i in marks_list:
        if(i<35):
            result = "fail"
        avg = sum(marks_list)/5
        if(avg>=75):
            result = "Distinction"
        elif(avg>=60):
            result="First Class"
        elif(avg>=50):
            result="Second Class"
        else:
            result="pass"
    return result
    
#City-wise Revenue Calculation Using Lists and Dictionaries

def city_revenue(self, orders):
    revenue_dict = {}
    for i in orders:
        city = i["city"]
        amount = i["amount"]
        if city in revenue_dict:
            revenue_dict[city]+=amount
        else:
            revenue_dict[city]=amount
    highest_city = max(revenue_dict,key=revenue_dict.get)
    return { "Revenue per City" :revenue_dict, "Highest Revenue City" : highest_city }

#Subject-wise Average Marks Calculator
    
def subject_average(self, students):
    subject_total = {}
    subject_count = {}
    for student in students:
        marks = student["marks"]
        for subject, score in marks.items():
            if subject in subject_total:
                subject_total[subject]+=score
                subject_count[subject]+=1
            else:
                subject_total[subject]=score
                subject_count[subject]=1
    subject_average={}
    for subject in subject_total:
        subject_average[subject]=subject_total[subject]/subject_count[subject]
    highest_subject = max(subject_average,key=subject_average.get)
    return {
        "Subject Averages":subject_average,
        "Highest Average Subject": highest_subject
    }

# Department-wise Patient Count System
   
def department_patient_count(self, visits):
    dept_count = {}
    for record in visits:
        department = record["department"]
        if department in dept_count:
            dept_count[department]+=1
        else:
            dept_count[department]=1
    max_department = max(dept_count,key = dept_count.get)
    return {
        "Department Patient Count": dept_count,
        "Department with Maximum Patients": max_department
    }


