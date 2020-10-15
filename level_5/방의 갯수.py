def solution(arrows):
    # 기본적으로 이전에 방문한 점을 또다시 방문하면 방이 만들어짐.
    # 예외 : 이전에 갔던 선분을 다시 되돌아 가는 경우 arrow(0) 이동후 arrow(4)로 이동하는 경우

    # arrow 별 이동 경로
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]

    answer = 0
    # 방문 체크
    visit = {}
    # (시작점, 끝점), (끝점, 시작점) 점 두개가 연결된 선 체크
    dirs = {}
    que = [(0,0)]
    x, y = 0, 0
    for arrow in arrows:
        # 점에서 만나는 것 외에도 선분끼리 만날 때도 세어야 하기 때문에
        # 점과 점 사이에 점을 하나 더 추가한다.
        for i in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            visit[(nx,ny)] = 0
            dirs[(x,y,nx,ny)] = 0
            dirs[(nx,ny,x,y)] = 0
            que.append((nx,ny))
            x, y = nx,ny
    x, y = que.pop(0)
    visit[(x,y)] = 1
    while que:
        nx, ny = que.pop(0)
        # 이전에 방문한 적이 있는 점
        if visit[(nx,ny)]:
            # 이전에 이동한 선분이 아닌 경우
            if not dirs[(x,y,nx,ny)]:
                answer += 1
                dirs[(x,y,nx,ny)] = 1
                dirs[(nx,ny,x,y)] = 1
        else:
            visit[(nx,ny)] = 1
            dirs[(x,y,nx,ny)] = 1
            dirs[(nx,ny,x,y)] = 1
        x,y = nx,ny

    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))