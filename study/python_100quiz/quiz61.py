

def str_list(input_str):
    count = 1
    format_list = []
    for idx, char in enumerate(input_str):
        if idx == len(input_str) - 2:
            if input_str[idx] != input_str[idx +1]:
                format_list.append(input_str[idx])
                format_list.append(str(count))
                format_list.append(input_str[idx +1])
                format_list.append('1')
                break
            else:
                format_list.append(input_str[idx])
                format_list.append(str(count+1))
                break
        elif input_str[idx] != input_str[idx+1]:
                format_list.append(input_str[idx])
                format_list.append(str(count))
                count = 1
        else:
                count += 1
    return format_list


str1 = input()
print(str_list(str1))