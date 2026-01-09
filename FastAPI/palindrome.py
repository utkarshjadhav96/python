
def check_palindrome(palindrome: str):
    last = len(palindrome)-1
    first =0
    flag = True
    while first < (last ):
        if palindrome[first] != palindrome[last]:
            flag = False
            break
        else:
            flag = True
        first =+1
        last =-1

    if flag == True:
        result = "Palindrome string"
    else :
        result = "Not a palindrome string"

    return {"text" : palindrome, "result" :result}