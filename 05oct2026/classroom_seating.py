total_students=int(input("enter the no.on students: "))
students_per_bench=int(input("enter the no.of students_per_bench: "))
occupied_benches=total_students//students_per_bench
leftover_students=total_students%students_per_bench
print(f"completely occupied benches: {occupied_benches}")
print(f"students left without a complete group: {leftover_students}")