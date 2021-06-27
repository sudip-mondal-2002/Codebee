import Classes.Run as codebee

while True:
    text = input('CodeBee >> ')
    if text.strip() == "":
        continue
    result, error = codebee.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
