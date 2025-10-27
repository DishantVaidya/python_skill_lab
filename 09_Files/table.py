# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 


folder_name = "Tables" 

for i in range(2, 21):
    file_path = folder_name + f"/Table_{i}.txt" 
    with open(file_path, "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

print("✅ Multiplication tables from 2 to 20 created successfully!")
