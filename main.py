from matplotlib import pyplot as plt
import sys


def main(args):
    # Collect Data
    name_dict = dict()
    time_dict = dict()
    text_list = ['']
    with open(args[1], 'r', encoding='utf-8') as f:
        [f.readline() for _ in range(3)]
        for line in f:
            if line[0] == '[':
                name = line[line.find('[') + 1:line.find(']')]
                time = line[line.find('[', line.find('[') + 1) + 1:line.find(']', line.find(']') + 1)][:-3]
                text = "".join(line.split()[3:])
                if "오전" in time or "오후" in time:
                    if name in name_dict:
                        name_dict[name] += 1
                    else:
                        name_dict[name] = 1
                    if time in time_dict:
                        time_dict[time] += 1
                    else:
                        time_dict[time] = 1
                text_list.append(text)

    # Reformat Time
    time_sorted = sorted(sorted(time_dict.items(), key=lambda x: int(x[0][3:])), key=lambda x: x[0][:2])
    time_sorted[10], time_sorted[-1] = time_sorted[-1], time_sorted[10]

    # Reformat Text
    text_dict = dict()
    for i in text_list:
        for j in i.split():
            if j in text_dict:
                text_dict[j] += 1
            else:
                text_dict[j] = 1
    top_n = int(args[2]) if len(args) == 3 else 20
    text_sorted = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]

    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(16, 9))
    plt.title("채팅 횟수")
    plt.bar(name_dict.keys(), name_dict.values())
    for idx, value in enumerate(name_dict.values()):
        plt.text(idx, value, str(value), ha='center', va='bottom')
    plt.show()
    plt.figure(figsize=(16, 9))
    plt.title("채팅 시간")
    plt.plot([i[0] for i in time_sorted], [i[1] for i in time_sorted])
    plt.xticks(rotation=45)
    plt.show()
    plt.figure(figsize=(16, 9))
    plt.title("Top {} 단어".format(top_n))
    plt.bar([i[0] for i in text_sorted], [i[1] for i in text_sorted])
    plt.xticks(rotation=90)
    for i in range(len(text_sorted)):
        plt.text(i, text_sorted[i][1], str(text_sorted[i][1]), ha='center', va='bottom')
    plt.show()

    for i in text_sorted:
        print(i)


if __name__ == '__main__':
    main(sys.argv)
