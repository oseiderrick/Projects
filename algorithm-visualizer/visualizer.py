import pygame, sys, math, heapq, random
W, H = 800, 600
GRID = 20
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

def grid_nodes(cols=30, rows=20):
    nodes = [(x,y) for y in range(rows) for x in range(cols)]
    walls = set(random.sample(nodes, k=len(nodes)//6))
    if (0,0) in walls: walls.remove((0,0))
    if (cols-1,rows-1) in walls: walls.remove((cols-1,rows-1))
    return nodes, walls, (0,0), (cols-1, rows-1)

def neighbors(p, cols=30, rows=20):
    x,y = p
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < cols and 0 <= ny < rows:
            yield (nx, ny)

def draw(nodes, walls, start, goal, open_set=set(), closed=set(), path=set(), title=""):
    screen.fill((30,30,30))
    cols = max(x for x,_ in nodes)+1
    rows = max(y for _,y in nodes)+1
    for x in range(cols):
        for y in range(rows):
            rect = pygame.Rect(x*GRID, y*GRID, GRID-1, GRID-1)
            color = (60,60,60)
            if (x,y) in walls: color = (40,0,0)
            if (x,y) in open_set: color = (0,40,0)
            if (x,y) in closed: color = (40,40,0)
            if (x,y) in path: color = (0,0,80)
            if (x,y) == start: color = (0,80,0)
            if (x,y) == goal: color = (80,0,0)
            pygame.draw.rect(screen, color, rect)
    txt = font.render(title, True, (200,200,200))
    screen.blit(txt, (10, H-30))
    pygame.display.flip()

def bfs(nodes, walls, start, goal):
    from collections import deque
    q = deque([start])
    parent = {start: None}
    open_set, closed = {start}, set()
    while q:
        cur = q.popleft()
        if cur == goal:
            break
        closed.add(cur)
        for nb in neighbors(cur):
            if nb in walls or nb in parent: continue
            parent[nb] = cur
            q.append(nb)
            open_set.add(nb)
            yield open_set, closed, set()
    # reconstruct
    path = set()
    cur = goal
    while cur and cur in parent:
        path.add(cur)
        cur = parent[cur]
        yield open_set, closed, path

def main():
    nodes, walls, start, goal = grid_nodes()
    stepper = None
    algo_name = "Press B/DFS(D)/Dijkstra(K)"
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    nodes, walls, start, goal = grid_nodes()
                    stepper = None
                    algo_name = "Reset"
                if e.key == pygame.K_b:
                    stepper = bfs(nodes, walls, start, goal)
                    algo_name = "BFS"
                if e.key == pygame.K_SPACE and stepper:
                    try:
                        open_set, closed, path = next(stepper)
                    except StopIteration:
                        stepper = None
        draw(nodes, walls, start, goal, open_set=set(), closed=set(), path=set(), title=algo_name)
        clock.tick(30)

if __name__ == "__main__":
    main()
