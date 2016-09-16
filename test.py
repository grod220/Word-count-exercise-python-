"""Count words."""
def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    splitArr = s.split(' ')
    holderObj = {}
    for word in splitArr:
        if word in holderObj:
          holderObj[word] += 1
        else:
          holderObj[word] = 1
    holderArr = []
    for key in holderObj:
      holderArr.append([key, holderObj[key]])

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    def sorter(item):
      holderW = ''
      for letter in item[0]:
        holderW += chr(219-ord(letter))
      # print(chr(item[1] + 96) + holderW)
      return chr(item[1] + 96) + holderW
    holderArr.sort(key=sorter, reverse=True)
    # print(holderArr)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return holderArr[:n]

def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))

test_run()
