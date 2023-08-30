counter = 0


def inception():
    global counter
    print(counter)
    if counter > 3:
        return "done"
    counter += 1
    # If I want to bubble up the "done" to the top then I have to return inception().
    # Without return the function
    # call stack look like this inception(inception(inception(inception("done")))) After popping the innermost
    # function call from stack, the function call stack looks like this inception(inception(inception(None))))
    # Continuous popping will return None without the return inception() statement.
    return inception()


# This inception() call is basically inception(inception(inception(inception(inception()))))
print(inception())
