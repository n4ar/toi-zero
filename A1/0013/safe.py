char = input()
password = int(input())

correct_char = 'H'
correct_password = 4567

if char == correct_char and password == correct_password: # ถูกทั้งคู่
    print("safe unlocked")
elif char == correct_char and password != correct_password: # ถูกแค่ตัวอักษร
    print("safe locked - change digit")
elif char != correct_char and password == correct_password: # ถูกแค่รหัส
    print("safe locked - change char")
elif char != correct_char and password != correct_password: # ถูกแค่รหัส
    print("safe locked")
