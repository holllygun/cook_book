def record(name):
    with open(name, encoding='utf-8') as f:
        lines = f.readlines()
        return(len(lines))

def lines(name):
    with open(name, encoding='utf-8') as f:
        text = f.readlines()
        return(text)


final_lines = {'1.txt': lines('1.txt'), '2.txt': lines('2.txt'), '3.txt': lines('3.txt')}
res = {'1.txt': record('1.txt'), '2.txt': record('2.txt'), '3.txt': record('3.txt')}
sorted_res = dict(sorted(res.items(), key=lambda item: item[1]))
keys, values = list(sorted_res.keys()), list(sorted_res.values())


with open('final_text.txt', 'w', encoding='utf-8') as f:
    for i in range(len(keys)):
        f.write(keys[i] + '\n')
        f.write(str(values[i]) + '\n')
        f.writelines(final_lines.get(keys[i]))
        f.write('' + '\n')


