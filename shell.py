import codebee

while True:
    text = input("Codebee >> ")
    result,err = codebee.run("<<shell>>",text)
    if err:
        print(err.as_string())
    else:
        print(result)