from pathlib import Path

all_names = ''
while True:
    asked_name = input("Please tell me your name(q for quit): ")
    if asked_name == 'q':
        break
    
    all_names += (asked_name.title() + '\n')
    

path = Path('guest_book.txt')
path.write_text(all_names)