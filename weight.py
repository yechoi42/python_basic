def std_weight(height, gender):
    if gender == "male":
        print("키 {0} 남자의 표준 체중은 {1}입니다.".format(height * 100, round(height * height * 22, 2)))
    else:
        print("키 {0} 여자의 표준 체중은 {1}입니다.".format(height * 100, round(height * height * 21, 2)))

std_weight(1.74, "female")
