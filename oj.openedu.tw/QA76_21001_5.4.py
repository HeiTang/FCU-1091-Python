def get_day(m, d):
    
    # write your code here
    md = { 1:31, 2:29, 3:31, 4:30, 5:31, 6:30,
          7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

    result = 2
    d = d-1
    for i in range (1, m):
        result += md[i]
    result += d
    return result % 7 + 1

w = { 1: 'Mon', 2: 'Tue', 3:'Wed', 4:'Thu', 5:'Fri',
      6: 'Sat', 7: 'Sun' }
month, date = eval(input())
print (w[get_day(month, date)])