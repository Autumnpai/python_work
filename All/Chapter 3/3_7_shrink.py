guest_name = ['Autumn Pai', 'Xueqin Cao', 'Xun Lu', 'Dixue Tang']
msg = 'please come to have dinner with me!'
print(f'{guest_name[0]},',msg)
print(f'{guest_name[1]},',msg)
print(f'{guest_name[2]},',msg)
print(f'{guest_name[3]},',msg)
print ()
print(f"{guest_name[2]} couldn't come this time.")
guest_name[2] = 'Elon Musk'
print(f'{guest_name[0]},',msg)
print(f'{guest_name[1]},',msg)
print(f'{guest_name[2]},',msg)
print(f'{guest_name[3]},',msg)
print()
guest_name.insert(0, 'Biaomei Guangxi')
guest_name.insert(2, 'Xiaojun Yunmen')
guest_name.append('Aijun Tang')
print(f'{guest_name[0]},',msg)
print(f'{guest_name[1]},',msg)
print(f'{guest_name[2]},',msg)
print(f'{guest_name[3]},',msg)
print(f'{guest_name[4]},',msg)
print(f'{guest_name[5]},',msg)
print(f'{guest_name[6]},',msg)
print()
removed_guest = guest_name.pop()
sorry_msg = "sorry, I can't invite you for this time, let's do it next time."
print(f"{removed_guest}, {sorry_msg}")
removed_guest = guest_name.pop()
sorry_msg = "sorry, I can't invite you for this time, let's do it next time."
print(f"{removed_guest}, {sorry_msg}")
removed_guest = guest_name.pop()
sorry_msg = "sorry, I can't invite you for this time, let's do it next time."
print(f"{removed_guest}, {sorry_msg}")
removed_guest = guest_name.pop()
sorry_msg = "sorry, I can't invite you for this time, let's do it next time."
print(f"{removed_guest}, {sorry_msg}")
removed_guest = guest_name.pop()
sorry_msg = "sorry, I can't invite you for this time, let's do it next time."
print(f"{removed_guest}, {sorry_msg}")
still_msg = 'you are still invited.'
print(f"{guest_name[0]}, {still_msg}")
print(f"{guest_name[1]}, {still_msg}")
print()
del guest_name[0]
del guest_name[0]
print(guest_name)