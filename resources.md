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

# Testing Code
* [Getting Started Testing Slide Deck](https://speakerdeck.com/pycon2014/getting-started-testing-by-ned-batchelder)

* [Getting Started Testing Video](https://www.youtube.com/watch?v=FxSsnHeWQBY)

* [Getting started with integration testing](https://www.fullstackpython.com/integration-testing.html)

* [Using the cloud for machine learning unit tests](https://developers.google.com/machine-learning/testing-debugging/pipeline/deploying)

* [Pytest documentation](https://docs.pytest.org/en/6.2.x/)


[Data Science TDD](https://www.linkedin.com/pulse/data-science-test-driven-development-sam-savage/)

[TDD is Essential for Good Data Science: Here's Why](https://medium.com/@karijdempsey/test-driven-development-is-essential-for-good-data-science-heres-why-db7975a03a44)

[Testing Your Code (general python TDD)](http://docs.python-guide.org/en/latest/writing/tests/)
