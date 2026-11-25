def verify_card_number(card_number:str) -> str:
    cleaned_number = card_number.replace(' ','').replace('-','')

    total_sum = 0
    reverse_digit = cleaned_number[::-1]

    for i,char in enumerate(reverse_digit):
        digit = int(char)

        if i%2 == 1:
            digit*=2
            if digit > 9:
                digit -= 9

        total_sum += digit

    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

print(verify_card_number('4111-1111-1111-1111'))