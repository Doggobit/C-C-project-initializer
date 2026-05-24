# C/C++ Project Initializer

A Python script to quickly scaffold and initialize a C/C++ project with a standard directory structure and Git integration.

## Features

-  **Automated Directory Structure** - Creates a clean, organized project layout:
  - `src/` - Source files directory
  - `bin/` - Compiled binaries directory
  - `include/` - Header files directory
- **Boilerplate Files** - Automatically generates:
  - `makefile` - Empty Makefile for build configuration
  - `src/main.c` - Starter main source file
-  **Git Integration** - Initializes Git repository and stages all files automatically
-  **One-Command Setup** - Get a fully initialized project in seconds

## Prerequisites

- **Python 3.6+**
- **Git** - Must be installed and accessible from command line
- **Windows, macOS, or Linux**

## Installation

1. Clone or download this script
2. Save it as `InitCProj.py` (or your preferred name)
3. Ensure Python and Git are installed on your system

## Usage

Run the script:

```bash
python InitCProj.py
```

When prompted, enter the name/path of your new project:

```
Insert the directory of the C/C++ Project: my_awesome_project
```

The script will:
1.  Create the project directory
2.  Generate subdirectories (`src`, `bin`, `include`)
3.  Create template files (`makefile`, `src/main.c`)
4.  Initialize a Git repository
5.  Add all files to Git
6.  Display the Git status

### Example Output

```
Making my_awesome_project/src...
Making my_awesome_project/bin...
Making my_awesome_project/include...
Creating makefile...
Creating src/main.c...

Initializing Git repository...
Adding files...
Checking status...
On branch master

No commits yet

Changes to be committed:
  new file:   makefile
  new file:   src/main.c

Project successfully initialized!
```

## Project Structure

After running the script, your project will look like this:

```
my_awesome_project/
├── makefile
├── .git/
├── src/
│   └── main.c
├── bin/
└── include/
```

- **makefile** - Configure your build process here
- **src/** - Place all your `.c` and `.cpp` source files here
- **include/** - Place all your header files (`.h`) here
- **bin/** - Output directory for compiled binaries
- **.git/** - Git repository (automatically initialized)

## Configuration

You can easily customize the script to:

- Add more initial files (e.g., `.gitignore`, `README.md`)
- Modify the directory structure
- Pre-populate files with boilerplate code

### Example: Adding a .gitignore

Add this before Git initialization:

```python
print("Creating .gitignore...")
gitignore_content = """*.o
*.out
*.exe
bin/*
.DS_Store
"""
with open(dir + "/.gitignore", "w") as f:
    f.write(gitignore_content)
```

## Error Handling

- **Directory Already Exists** - The script will exit if the directory already exists (prevents overwriting)
- **Git Not Found** - Ensure Git is installed and added to your system PATH

## Tips

- Use relative paths: `./my_project` or just `my_project`
- Use absolute paths: `/home/user/projects/my_project`
- The script will create the directory if it doesn't exist
- All files are automatically staged in Git, ready for your first commit

## First Commit

After the script completes, you can make your first commit:

```bash
cd my_awesome_project
git commit -m "Initial project setup"
```

## Future Improvements

- [ ] Option to choose between C and C++ templates
- [ ] Support for CMake instead of Make
- [ ] Interactive configuration menu
- [ ] Pre-configured .gitignore for C/C++ projects

## License

MIT License - Feel free to modify and distribute this script.

## Contributing

Have improvements? Feel free to fork and submit a pull request!

## Author

Created to streamline C/C++ project initialization.

---

**Happy coding!** 
