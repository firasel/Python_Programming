exStr = "GATGGAACTTGACTACGTAAATT"


def DNAtoRNA(exStr):
    return str.replace(exStr, 'T', 'U')


print(DNAtoRNA(exStr))
