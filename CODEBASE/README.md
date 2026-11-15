# Pharmacy Inventory System

**University:** Rungta International Skills University
**School:** School of Computer Science and Engineering
**Course:** Bachelor of Technology - Computer Science and Engineering, First Semester
**PS No:** 57

## Problem Statement
Develop a console application to manage a pharmacy's medicine stock. The user can add medicines, view stock, sell medicines (reducing stock and generating a bill), delete medicines and see a low-stock report. Data is stored in a CSV file.

**Language:** Python 3
**Concepts:** Dictionaries, Lists, CSV, CRUD

**Note:** Medicines are stored in medicines.csv with columns ID, Name, Quantity, Price. IDs start from M1. A medicine is 'Low stock' when quantity is below 10.

## Features
1. Add Medicine - Menu Option 1
2. View Stock - View all medicines
3. Sell Medicine - Menu Option 3, Bill = Quantity x Price, stock updates automatically
4. Delete Medicine - Menu Option 4
5. Low Stock Report - Menu Option 5, shows medicines with Quantity < 10
6. Inventory Value - Menu Option 6, shows total value of all stock

## Project Structure
Pharmacy-Inventory-System/
├── CODEBASE/
│   ├── pharmacy_inventory.py
│   └── medicines.csv
├── TESTCASES/
│   ├── Test Case 1 - Normal Input
│   ├── Test Case 2 - Boundary / Minimum Input
│   ├── Test Case 3 - Invalid Input
│   └── Test Case 4 - Different Valid Scenario
└── README.md

## How to Run
1. Download CODEBASE folder
2. Open terminal / CMD in that folder
3. Run: python pharmacy_inventory.py

## Test Cases
| Test Case | Input | Expected Output |
|---|---|---|
| 1. Normal Input | Add Paracetamol, Qty 50, Price 2.50 | Medicine added. ID: M1 \| Paracetamol \| Qty: 50 \| Price: 2.50 |
| 2. Boundary Input | Sell 50 units of M1 | Sold 50 units. Bill: 125.00, Stock left: 0 \| Out of stock! |
| 3. Invalid Input | Stock 5, Try to sell 8 | Insufficient stock. Available: 5 |
| 4. Different Scenario | Low stock report, Delete M3, Inventory value | (a) M2 Cetirizine Low stock, (b) Medicine M3 deleted, (c) Total inventory value 165.00 |

## Bare Minimum Requirements Covered
- Python 3 single .py file
- Load medicines from medicines.csv into list of dictionaries and write back after every change
- Add, View, Sell, Delete, Low-stock report and Inventory value using functions
- Reject negative quantity/price and selling more than available stock
- Calculate bill for every sale and update stock
