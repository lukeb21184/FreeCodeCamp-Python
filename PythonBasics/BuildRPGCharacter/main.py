


elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
        str_bar = (full_dot * strength) + (empty_dot * (10 - strength))
        int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        cha_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))

        return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"
