
for i in range(1, 51):
    name = str(i) + "주차.txt"
    with open(name, "w", encoding="utf8") as report_file:
        report_file.write("""-X 주차 주간보고-
부서:
이름:
업무요약:
""")
