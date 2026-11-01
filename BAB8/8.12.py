def make_sandwich(*items):
    """Print a summary of the sandwich that's being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
 
 
make_sandwich('turkey', 'lettuce')
make_sandwich('tuna', 'tomato', 'onion')
make_sandwich('ham', 'cheese', 'pickles', 'mustard')
 