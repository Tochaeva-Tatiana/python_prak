import math
import sys

def main():
    # Читаем все строки из stdin
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            lines.append(line)
    
    commands = []
    labels = {}
    current_line = 0
    
    # Первый проход: разбор команд и сбор меток
    for line in lines:
        words = line.split()
        if not words:
            continue
            
        # Обработка меток
        if words[0].endswith(':'):
            label = words[0][:-1]
            labels[label] = current_line
            words = words[1:]
            if not words:
                continue
        
        # Разбор команд с помощью match case
        match words:
            case ["stop"]:
                commands.append(["stop"])
            case ["store", n, p]:
                commands.append(["store", n, p])
            case ["add" | "sub" | "div" | "mul", a, b, pr]:
                commands.append([words[0], a, b, pr])
            case ["ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle", a, op, m]:
                commands.append([words[0], a, op, m])
            case ["out", source]:
                commands.append(["out", source])
            case _:
                continue  # Игнорируем некоманды
                
        current_line += 1

    # Проверка существования всех меток, используемых в переходах
    for cmd in commands:
        match cmd:
            case ["ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle", _, _, m]:
                if m not in labels:
                    return  # Не начинаем выполнение, если есть неизвестная метка
            case _:
                pass

    # Второй проход: выполнение программы
    variables = {}
    pc = 0
    
    while pc < len(commands):
        cmd = commands[pc]
        
        match cmd:
            case ["stop"]:
                # Выходим из цикла выполнения при команде stop
                break
                
            case ["store", n, p]:
                try:
                    value = float(n)
                except ValueError:
                    value = 0.0
                variables[p] = value
                pc += 1
                
            case ["add", a, b, pr]:
                val_a = variables.get(a, 0.0)
                val_b = variables.get(b, 0.0)
                variables[pr] = val_a + val_b
                pc += 1
                
            case ["sub", a, b, pr]:
                val_a = variables.get(a, 0.0)
                val_b = variables.get(b, 0.0)
                variables[pr] = val_a - val_b
                pc += 1
                
            case ["div", a, b, pr]:
                val_a = variables.get(a, 0.0)
                val_b = variables.get(b, 0.0)
                if val_b == 0:
                    variables[pr] = math.inf
                else:
                    variables[pr] = val_a / val_b
                pc += 1
                    
            case ["mul", a, b, pr]:
                val_a = variables.get(a, 0.0)
                val_b = variables.get(b, 0.0)
                variables[pr] = val_a * val_b
                pc += 1
                
            case ["ifeq", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a == val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["ifne", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a != val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["ifgt", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a > val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["ifge", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a >= val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["iflt", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a < val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["ifle", a, op, m]:
                val_a = variables.get(a, 0.0)
                val_op = variables.get(op, 0.0)
                if val_a <= val_op:
                    pc = labels[m]
                else:
                    pc += 1
                    
            case ["out", source]:
                value = variables.get(source, 0.0)
                print(value)
                pc += 1
                
            case _:
                # Для неизвестных команд просто переходим к следующей
                pc += 1

if __name__ == "__main__":
    main()