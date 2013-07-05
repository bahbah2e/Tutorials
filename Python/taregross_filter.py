file_original = open('original.log')
file_filtered = open('filtered.log', 'w')
filter = 'TAREGROSS: '

try:
    for line in file_original:
        header = line[0:11]
        if header == filter:
            file_filtered.write(line)
finally:
    file_original.close()
    file_filtered.close()