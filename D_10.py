a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


def create_new_string():
    output = s.replace(',', "")
    output = output.replace('.', "")
    output = output.split(' ')
    output.reverse()
    result = []

    for i in output:
        for j in a:
            if i.capitalize() == j.capitalize():
                index = output.index(i)
                if output[index-1] not in result:
                    result.append(output[index-1])

    result.reverse()

    with open("out.txt", "w") as out:
        for word in result:
            out.write(word)
            out.write(' ')
        out.close()


create_new_string()
