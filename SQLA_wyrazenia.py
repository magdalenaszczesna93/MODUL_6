from SQLA_tworzenie_tabel import students

ins=students.insert()
print(ins)
print(ins.compile().params)

ins=students.insert().values(name="Eric", lastname="Idle")
print(ins.compile().params)

up=students.update()
up=students.update().values(name="Ada")
print(up.compile().params)

dele=students.delete()
dele=students.delete().where(students.c.id==1)
print(dele.compile().params)