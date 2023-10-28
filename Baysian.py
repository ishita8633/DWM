age = ['youth', 'youth', 'middle', 'senior', 'senior', 'senior', 'middle', 'youth', 'youth', 'senior', 'youth', 'middle', 'middle', 'senior']
income = ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium']
student = ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no']
credit_rating = ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent']
buys_computer = ['no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes']

p_y = buys_computer.count('yes') / 14
p_n = buys_computer.count('no') / 14

p_r_yes = 0
p_r_no = 0

for i in range(len(age)):
    if age[i] == 'youth' and buys_computer[i] == 'yes':
        p_r_yes += 1
    elif age[i] == 'youth' and buys_computer[i] == 'no':
        p_r_no += 1

p_s_yes = 0
p_s_no = 0

for i in range(14):
    if income[i] == 'medium' and buys_computer[i] == 'yes':
        p_s_yes += 1
    elif income[i] == 'medium' and buys_computer[i] == 'no':
        p_s_no += 1

p_d_yes = 0
p_d_no = 0

for i in range(14):
    if student[i] == 'yes' and buys_computer[i] == 'yes':
        p_d_yes += 1
    elif student[i] == 'yes' and buys_computer[i] == 'no':
        p_d_no += 1

p_x_yes = 0
p_x_no = 0

for i in range(14):
    if credit_rating[i] == 'fair' and buys_computer[i] == 'yes':
        p_x_yes += 1
    elif credit_rating[i] == 'fair' and buys_computer[i] == 'no':
        p_x_no += 1

prob_yes = (p_r_yes / buys_computer.count('yes')) * (p_s_yes / buys_computer.count('yes')) * (p_d_yes / buys_computer.count('yes')) * (p_x_yes / buys_computer.count('yes')) * p_y
prob_no = (p_r_no / buys_computer.count('no')) * (p_s_no / buys_computer.count('no')) * (p_d_no / buys_computer.count('no')) * (p_x_no / buys_computer.count('no')) * p_n

print(prob_yes, prob_no)

if prob_yes > prob_no:
    print("Hence it is classified as Yes")
else:
    print("Hence it is classified as No")
