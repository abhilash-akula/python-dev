def reverse_string(str):
    if str == "":
        return ""
    else:
        return reverse_string(str[1:]) + str[0]

def reverse_string_loop(str):
  rev_str = ""
  #max_index = len(str)-1
  for i in range(0, len(str)):
    rev_str += str[len(str)-1-i]
  return rev_str
    


print("reverse of string {} is {}" .format("hello.someone.you.are.great", reverse_string("hello.someone.you.are.great")))

print("reverse of string {} is {}" .format("hello.someone.you.are.great", reverse_string_loop("hello.someone.you.are.great")))
