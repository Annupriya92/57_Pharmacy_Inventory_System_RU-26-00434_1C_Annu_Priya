# Documentation - Pharmacy Inventory System - PS No. 57

## 1. Introduction
This project is a console application to manage pharmacy stock.

## 2. Problem Statement
Manage medicines - Add, View, Sell, Delete, Low Stock Report.

## 3. Tools Used
Language: Python 3
File: medicines.csv
Concepts: List, Dictionary, Functions, CSV File Handling

## 4. How System Works
- Data is loaded from medicines.csv into list of dictionaries
- ID is auto generated as M1, M2, M3...
- After every Add/Sell/Delete, file is updated
- Sell: Bill = Quantity x Price
- Low Stock: Quantity < 10

## 5. Test Cases
1. Normal - Add Paracetamol - Passed
2. Boundary - Sell full stock 50 - Passed, Stock 0, Bill 125.00
3. Invalid - Sell 8 when stock 5 - Passed, Shows Insufficient stock

## 6. Conclusion
All 3 test cases passed. System meets all bare minimum requirements.
