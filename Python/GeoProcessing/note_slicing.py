# Sequence and string operations
'ab' * 3 == 'ababab'
'ab' + 'cd' == 'abcd'
(1,2) + (3,) == (1,2,3)
[1,2] in [0,1,2] == False
'bc' in 'abcd' == True
1 in (0,1) == True

'abc'[1] == 'b'
'abcd'[1,3] == 'bc'
'abcd'[1:] == 'bcd'
'abcdefgh'[1:7:2] == 'bdf' #start at [0], skip by 2, end before [7]
(1,2,3)[-1] == 3
[1,2][:] == [1,2]
[1,2][:] is not [1,2]
