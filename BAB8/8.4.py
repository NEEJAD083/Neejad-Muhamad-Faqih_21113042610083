def make_shirt(size='large', text='I love Python'):
    """Display a summary of the shirt that's going to be made."""
    print(f"I'll make a {size} shirt with the text '{text}' on it.")
 
 
# A large shirt with the default message.
make_shirt()
 
# A medium shirt with the default message.
make_shirt(size='medium')
 
# A shirt of any size with a different message.
make_shirt('small', 'Keep calm and code on')
 