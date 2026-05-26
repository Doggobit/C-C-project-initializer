import os, subprocess

dir = input("Insert the directory of the C/C++ Project: ")

lang = int(input("Chose between C[1] / C++[2]: "))
if lang != 1  and lang != 2:
    print("You must put 1 or 2!\n")
    exit(1)

cppdemo = """#include <iostream>

int main(){
    std::cout << \"Hello world\" << std::endl;
    return 0;
}
"""

cdemo = """#include <stdio.h>

int main(int argc, char** argv){
printf(\"Hello world\");
}
"""

try:
    os.mkdir(dir)
except FileExistsError:
    print("You cannot initialize into a directory that already exsist!\n")
    exit()
print(f"making {dir}/src...")
os.makedirs(dir+"/src...")
print(f"making {dir}/bin...")
os.makedirs(dir+"/bin")
print(f"making {dir}/include...")
os.makedirs(dir+"/include")

print("Creating makefile...")
makefile = open(dir+"/makefile", "w")
makefile.close()

print("Creating README.md ...")
readme = open(dir+"/README.md", "w")
readme.close()

print("Creating LICENSE ...")
readme = open(dir+"/LICENSE", "w")
readme.close()

if lang == 1:
    print("Creating src/main.c ...")
    main = open(dir+"\\src\\main.c", "w")
    main.write(cdemo)
    main.close

else:
    print("Creating src/main.cpp ...")
    main = open(dir+"\\src\\main.cpp", "w")
    main.write(cppdemo)
    main.close

print("\nInitializing Git repository...")
subprocess.run(["git", "init"], cwd=dir)

print("Adding files...")
subprocess.run(["git", "add", "."], cwd=dir)

print("Checking status...")
subprocess.run(["git", "status"], cwd=dir)

print("Project sucsesfully initialized!")
