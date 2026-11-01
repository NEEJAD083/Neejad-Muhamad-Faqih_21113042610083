def make_shirt(size, text):
    """Display a summary of the shirt that's going to be made."""
    print(f"I'll make a {size} shirt with the text '{text}' on it.")
 
 
# Positional arguments.
make_shirt('large', 'I love Python')
 
# Keyword arguments.
make_shirt(text='Hello, world!', size='medium')
 