# Source: https://2dengine.com/doc/intersections.html


def point_in_circle(px, py, cx, cy, r):
    dx = px - cx
    dy = py - cy

    return dx * dx + dy * dy <= r * r


def dot(ax, ay, bx, by):
    return ax * bx + ay * by


def point_on_triangle(px, py, ax, ay, bx, by, cx, cy):
    abx = bx - ax
    aby = by - ay

    acx = cx - ax
    acy = cy - ay

    apx = px - ax
    apy = py - ay

    # Vertex region outside a
    d1 = dot(abx, aby, apx, apy)
    d2 = dot(acx, acy, apx, apy)

    if d1 <= 0 and d2 <= 0:
        return ax, ay

    # Vertex region outside b
    bpx = px - bx
    bpy = py - by

    d3 = dot(abx, aby, bpx, bpy)
    d4 = dot(acx, acy, bpx, bpy)
    if d3 >= 0 and d4 <= d3:
        return bx, by

    # Edge region ab
    if d1 >= 0 and d3 <= 0 and d1 * d4 - d3 * d2 <= 0:
        v = d1 / (d1 - d3)
        return ax + abx * v, ay + aby * v

    # Vertex region outside c
    cpx = px - cx
    cpy = py - cy
    d5 = dot(abx, aby, cpx, cpy)
    d6 = dot(acx, acy, cpx, cpy)
    if d6 >= 0 and d5 <= d6:
        return cx, cy

    # Edge region ac
    if d2 >= 0 and d6 <= 0 and d5 * d2 - d1 * d6 <= 0:
        w = d2 / (d2 - d6)
        return ax + acx * w, ay + acy * w

    # Edge region bc
    if d3 * d6 - d5 * d4 <= 0:
        d43 = d4 - d3
        d56 = d5 - d6

        if d43 >= 0 and d56 >= 0:
            w = d43 / (d43 + d56)
            return bx + (cx - bx) * w, by + (cy - by) * w

    # Inside face region
    return px, py


def triangle_vs_circle(ax, ay, bx, by, cx, cy, sx, sy, r):
    qx, qy = point_on_triangle(sx, sy, ax, ay, bx, by, cx, cy)
    return point_in_circle(qx, qy, sx, sy, r)
