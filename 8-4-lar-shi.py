def make_shirt(message="I love Python", size='large'):
    """Display the size of the shirt and the message printed on it."""
    print(f"The size of the shirt is {size.title()} and the message is '{message.title()}'.")

make_shirt()
make_shirt(size='medium')
make_shirt(message='I miss my mom', size='any')