لديك قائمة تحتوي على درجات طلاب في مادة معينة، وتريد ترتيبها تنازليًا (من الأعلى إلى الأدنى) باستخدام خوارزمية الإدراج (Insertion Sort).

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):  
        key = arr[i]  
        j = i - 1  
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  
            j -= 1  
        
        arr[j + 1] = key  

grades = [85, 92, 78, 90, 88]
insertion_sort_desc(grades)
print("degree after sorting", grades)
'degree after sorting: [92, 90, 88, 85, 78]'