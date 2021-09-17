# Try and Except Errors
[python try and except documentation](https://docs.python.org/3/tutorial/errors.html)

*Try* block is code you want to run

*Except* block is errors you are expecting if the code block doesn't work

**Syntax Example**
```
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print('This is an example error message')

    # For multiple errors 

    try:
        df = pd.read_csv(file_path)
        return df
    except (FileNotFoundError, ErrorNumberTwo):
        print('This is an example error message')      
```

