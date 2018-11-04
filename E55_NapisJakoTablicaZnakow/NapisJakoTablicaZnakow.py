q = 'THE EYES'
print('2:')
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])
print('3:')
q = 'a gentleman'
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])
print('4:')
q = 'THE MORSE CODE'
 #   HERE COME DOTS
print(q[1:3] + q[6] + q[8]  + q[9:12] + q[4] + q[-1] + q[-5] + q[-2] + q[-3] + q[0] + q[-7])
print('5:')
line = "'Program \"Kropka nad i\" nadamy o: 22:00'"
time = line[line.find(':') + 2:line.rfind("'")]
title = line[line.find('"') + 1:line.rfind('"')]
print(title)
print(time)
