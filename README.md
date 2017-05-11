# Bug-Tracker
This includes all the sub files of the product
----------------------------------------------
CONSTRAINTS:
----------------------------------------------
1. Only registered users can login
2. To register, the users should provide the following:
        *EmployeeID (used as key and loginID) || 1<= len(EmployeeID) <=5 || only digits allowed
        *Username (Unique) ||  1<= len(Username) <=10 || Should begin with alphabets || only alphanumeric characters allowed
        *Password || 5<= len(EmployeeID) <=12 || only alphanumeric characters allowed
3. To login, the user should have her/his EmployeeID and Password.
4. In a bug entry,
        *ProductName || 1<= len(EmployeeID) <=50
        *ProductVersion || [digit][.][digit]
        *BugTitle ||  1<= len(Username) <=50 || only alphanumeric characters allowed
        *Description ||  1<= len(Username) <=500
        
