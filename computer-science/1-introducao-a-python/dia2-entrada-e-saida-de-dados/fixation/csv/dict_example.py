import csv

with open("graduacao_unb.csv", encoding="utf-8") as file:
    graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1

with open("new_department_report.csv", "w", encoding="utf-8") as file:
    headers = [
        "Departamento",
        "Total de cursos",
    ]

    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    for department, grades in group_by_department.items():
        row = {"Departamento": department, "Total de cursos": grades}
        writer.writerow(row)
