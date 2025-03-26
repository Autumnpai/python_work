def make_shirt(size, message):
    """Display the size of the shirt and the message printed on it."""
    print(
        f"The size of the shirt is {size.title()} "
        f"and the matiral is '{message.title()}'."
    )

make_shirt('L', 'muslin')
make_shirt(message='flanel', size='M')