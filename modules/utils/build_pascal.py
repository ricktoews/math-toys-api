def build_triangle(rows = 50):
    pascal = [[1]]

    i = len(pascal)
    
    while i <= rows:
        prev_row = pascal[i - 1]
        new_row = []
        new_row.append(1)
        j = 0
        while j < len(prev_row):
            a = prev_row[j]
            if j == len(prev_row) - 1:
                b = 0
            else:
                b = prev_row[j + 1]
            new_row.append(a + b)
            j += 1
        pascal.append(new_row)
        i += 1
        
    return pascal