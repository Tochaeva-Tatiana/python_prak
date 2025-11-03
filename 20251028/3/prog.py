class Maze:
    def __init__(self, N):
        self.N = N
        # хранить будем проходы между комнатами как множество неориентированных рёбер
        self.passages = set()

    # -------------------------------
    #  Разбор ключа вида  M[x0,y0 : x1,y1]
    #  Python передаёт его как (x0, slice(y0, x1, None), y1)
    # -------------------------------
    @staticmethod
    def _parse_key(key):
        # key = (x0, slice(y0, x1), y1)
        if not isinstance(key, tuple) or len(key) != 3:
            raise TypeError("Bad index format for Maze")

        x0 = key[0]
        sl = key[1]
        y1 = key[2]

        if not isinstance(sl, slice):
            raise TypeError("Middle part must be slice")

        y0 = sl.start
        x1 = sl.stop

        return x0, y0, x1, y1

    # -------------------------------
    #  Проверка достижимости: M[x0,y0 : x1,y1]
    # -------------------------------
    def __getitem__(self, key):
        x0, y0, x1, y1 = Maze._parse_key(key)

        N = self.N
        start = (x0, y0)
        target = (x1, y1)

        # DFS / BFS — не важно, лишь бы реализован
        stack = [start]
        visited = set()

        while stack:
            x, y = stack.pop()
            if (x, y) == target:
                return True
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # соседние клетки
            for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= nx < N and 0 <= ny < N:
                    # если есть проход
                    if ((x,y),(nx,ny)) in self.passages or ((nx,ny),(x,y)) in self.passages:
                        stack.append((nx,ny))

        return False

    # -------------------------------
    #  Установка проходов (открытие/закрытие)
    # -------------------------------
    def __setitem__(self, key, value):
        x0, y0, x1, y1 = Maze._parse_key(key)

        if value not in ("·", "█"):
            return  # по условию ошибки не обрабатываем

        # перемещение по вертикали
        if x0 == x1:
            a, b = sorted((y0, y1))
            for y in range(a, b):
                edge = ((x0, y), (x0, y+1))
                if value == "·":
                    self.passages.add(edge)
                else:
                    self.passages.discard(edge)

        # перемещение по горизонтали
        elif y0 == y1:
            a, b = sorted((x0, x1))
            for x in range(a, b):
                edge = ((x, y0), (x+1, y0))
                if value == "·":
                    self.passages.add(edge)
                else:
                    self.passages.discard(edge)

        # иначе — ничего не делаем по условию

    # -------------------------------
    #  Красивый вывод лабиринта
    # -------------------------------
    def __str__(self):
        N = self.N
        out = []

        # верхняя стена
        out.append("█" * (2*N + 1))

        for y in range(N):
            row = ["█"]
            for x in range(N):
                row.append("·")   # сама комната
                
                # стена справа или проход
                if x < N-1 and (((x,y),(x+1,y)) in self.passages):
                    row.append("·")
                else:
                    row.append("█")
            out.append("".join(row))

            # линия снизу (горизонтальные стены)
            row2 = ["█"]
            for x in range(N):
                if y < N-1 and (((x,y),(x,y+1)) in self.passages):
                    row2.append("·")
                else:
                    row2.append("█")
                row2.append("█")
            out.append("".join(row2))

        return "\n".join(out)


import sys
exec(sys.stdin.read())