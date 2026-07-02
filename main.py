print(r"""
+----------------------------------------------------------+
|   ________   __ ____________  ___   _____ _____ _        |
|   | ___ \ \ / / | ___ \ ___ \/ _ \ /  ___|_   _| |       |
|   | |_/ /\ V /  | |_/ / |_/ / /_\ \\ `--.  | | | |       |
|   |  __/  \ /   | ___ \    /|  _  | `--. \ | | | |       |
|   | |     | |   | |_/ / |\ \| | | |/\__/ /_| |_| |____   |
|   \_|     \_/   \____/\_| \_\_| |_/\____/ \___/\_____/   |
+----------------------------------------------------------+
by Guilherme Sodré
""")

# ==========================================
# LOGIN 
# ==========================================

username = input("Nome de usuário: ")

while True:
    password = input("Crie sua senha: ")
    confirm = input("Confirmar senha: ")

    if password == confirm:
        break
    print("Erro: as senhas não são iguais.\n")

# ==========================================
# FILESYSTEM 
# ==========================================

filesystem = {
    "~": {
        "dirs": {
            "Desktop": {"dirs": {}, "files": {}},
            "Documents": {"dirs": {}, "files": {}},
            "Downloads": {"dirs": {}, "files": {}}
        },
        "files": {
            "Hello.txt": "Bem vindo ao PyBrasil!"
        }
    }
}

current_path = ["~"]

# ==========================================
# FUNÇÕES BASE
# ==========================================

def get_dir():
    node = filesystem["~"]

    for part in current_path[1:]:
        node = node["dirs"][part]

    return node


def pwd():
    print("/".join(current_path))


def ls():
    node = get_dir()

    print("\nDirectories:")
    for d in node["dirs"]:
        print("[DIR]", d)

    print("\nFiles:")
    for f in node["files"]:
        print("[FILE]", f)

    print()


def cd(path):
    global current_path

    if path == "..":
        if len(current_path) > 1:
            current_path.pop()
        return

    node = get_dir()

    if path in node["dirs"]:
        current_path.append(path)
    else:
        print("Diretório não encontrado.")


def mkdir(name):
    node = get_dir()

    if name in node["dirs"]:
        print("Diretório já existe.")
        return

    node["dirs"][name] = {"dirs": {}, "files": {}}
    print("Diretório criado.")


def rmdir(name):
    node = get_dir()

    if name in node["dirs"]:
        del node["dirs"][name]
        print("Diretório removido.")
    else:
        print("Diretório não encontrado.")


def touch(name):
    node = get_dir()

    if name in node["files"]:
        print("Arquivo já existe.")
        return

    node["files"][name] = ""
    print("Arquivo criado.")


def write(name):
    node = get_dir()

    if name not in node["files"]:
        print("Arquivo não encontrado.")
        return

    content = input("Escreva: ")
    node["files"][name] = content
    print("File saved.")


def read(name):
    node = get_dir()

    if name not in node["files"]:
        print("Arquivo não encontrado.")
        return

    print("\n" + node["files"][name] + "\n")


def rm(name):
    node = get_dir()

    if name in node["files"]:
        del node["files"][name]
        print("Arquivo removido.")
    else:
        print("Arquivo não encontrado.")


def clear():
    # simulação sem os
    print("\n" * 50)


# ==========================================
# LOOP PRINCIPAL
# ==========================================

print("\nLogado com sucesso!")
print("Digite 'help' para os comandos.\n")

while True:

    cmd = input(f"{username}@pybrasil:{'/'.join(current_path)}$ ").strip()

    if cmd == "exit":
        break

    elif cmd == "help":
        print("""
Commands:
help
exit
ls
pwd
cd <dir>
mkdir <name>
rmdir <name>
touch <file>
write <file>
read <file>
rm <file>
clear
whoami
""")

    elif cmd == "ls":
        ls()

    elif cmd == "pwd":
        pwd()

    elif cmd == "whoami":
        print(username)

    elif cmd == "clear":
        clear()

    elif cmd.startswith("cd "):
        cd(cmd.split(" ", 1)[1])

    elif cmd.startswith("mkdir "):
        mkdir(cmd.split(" ", 1)[1])

    elif cmd.startswith("rmdir "):
        rmdir(cmd.split(" ", 1)[1])

    elif cmd.startswith("touch "):
        touch(cmd.split(" ", 1)[1])

    elif cmd.startswith("write "):
        write(cmd.split(" ", 1)[1])

    elif cmd.startswith("read "):
        read(cmd.split(" ", 1)[1])

    elif cmd.startswith("rm "):
        rm(cmd.split(" ", 1)[1])

    else:
        print("Unknown command.")
