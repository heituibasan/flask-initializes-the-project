import os


def generate_project_structure(root_dir, indent=""):
    project_structure = ""
    items = sorted(os.listdir(root_dir))

    for i, item in enumerate(items):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            project_structure += f"{indent}├── {item}/\n"
            project_structure += generate_project_structure(path, indent + "│   ")
        else:
            project_structure += f"{indent}├── {item}\n"

    return project_structure


def main():
    root_dir = input("请输入要生成结构的项目根目录路径：")
    if not os.path.isdir(root_dir):
        print("提供的路径不是一个有效的目录。")
        return

    project_structure = generate_project_structure(root_dir)
    print("项目结构如下：")
    file = open(file="project_structure.txt", mode="w", encoding="utf-8")
    file.write(project_structure)
    file.close()
    print(project_structure)


if __name__ == "__main__":
    main()
