import math
import matplotlib.pyplot as plt

def orientacao(p, q, r):
    """
    Calcula a orientação dos pontos p, q e r.
    
    Retorna:
        0 se os pontos forem colineares,
        1 se os pontos estiverem no sentido anti-horário,
        2 se os pontos estiverem no sentido horário
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    
    if val == 0:
        return 0  # Colineares
    elif val > 0:
        return 1  # Anti-horário
    else:
        return 2  # Horário

def distancia(p):
    """
    Calcula a distância do ponto p da origem.
    
    Retorna:
        A distância do ponto p da origem.
    """
    return math.sqrt(p[0] ** 2 + p[1] ** 2)

def convex_hull(points):
    """
    Calcula a envoltória convexa de um conjunto de pontos.
    
    Parâmetros:
        points (lista): Lista de pontos no formato [(x, y), ...]
    
    Retorna:
        A lista de pontos que compõem a envoltória convexa.
    """
    n = len(points)
    if n < 3:
        raise ValueError("É necessário ao menos 3 pontos para calcular a envoltória convexa.")
    
    # Encontra o ponto mais baixo (ou com menor x se houver empate)
    ymin = min(points, key=lambda p: (p[1], p[0]))
    p0 = ymin
    
    # Ordena os pontos com base na orientação em relação a p0
    points.sort(key=lambda p: math.atan2(p[1] - p0[1], p[0] - p0[0]))
    
    # Inicializa a pilha com os dois primeiros pontos
    hull = [points[0], points[1]]
    
    # Itera sobre os demais pontos para calcular a envoltória convexa
    for i in range(2, n):
        while len(hull) > 1 and orientacao(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    
    return hull

# Exemplo de uso
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = convex_hull(points)

print("Pontos da envoltória convexa:")
for p in hull:
    print(p)

# Plotagem
plt.figure(figsize=(6, 6))
plt.scatter(*zip(*points), color='blue')
hull_x, hull_y = zip(*hull)
hull_x += (hull_x[0],)  # Fecha o polígono
hull_y += (hull_y[0],)
plt.plot(hull_x, hull_y, 'r-')
plt.gca().set_aspect('equal', adjustable='box')  # Mantém a proporção da figura
plt.show()
