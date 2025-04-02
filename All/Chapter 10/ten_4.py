from pathlib import Path

asked_name = input("Please tell me your name: ").title()
path = Path('guest.txt')
path.write_text(asked_name)