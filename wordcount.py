def word_count(filename):
    """Takes in a text file and returns the count of each word's appearance."""

    word_dict = {}

    file_name = open(filename)

    for line in file_name:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

            # Alternative using if/else statements:

            # if word not in word_dict:
            #     word_dict[word] = 1
            # else:
            #     word_dict[word] += 1

    for word, count in word_dict.iteritems():
        print word, count

word_count("test.txt")
word_count("twain.txt")