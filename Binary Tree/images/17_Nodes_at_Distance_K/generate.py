"""Build exact tree diagrams as PNG + editable SVG. Run with Python 3 and Pillow.

The supplied transparent AlgoZenith logo is embedded unchanged, then scaled
proportionally during rendering. Fonts match the neighboring course diagrams.
"""
from pathlib import Path
import base64
import html
import math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
W, H, SCALE = 1536, 1024, 2
CREAM, BLUE, TEAL, BROWN = '#EFEBDA', '#012B41', '#005C83', '#28190E'
FONT = '/System/Library/Fonts/Supplemental/Andale Mono.ttf'
NUM = '/System/Library/Fonts/Supplemental/Comic Sans MS.ttf'
LOGO = HERE / 'algozenith-original.png'


class Diagram:
    def __init__(self, description):
        self.im = Image.new('RGBA', (W*SCALE, H*SCALE))
        self.d = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img"><title>{html.escape(description)}</title>']
        self.d.rounded_rectangle((12*SCALE,12*SCALE,1524*SCALE,1012*SCALE), radius=34*SCALE, fill=CREAM, outline=BLUE, width=2*SCALE)
        self.svg.append(f'<rect x="12" y="12" width="1512" height="1000" rx="34" fill="{CREAM}" stroke="{BLUE}" stroke-width="2"/>')
        logo = Image.open(LOGO).convert('RGBA')
        logo = logo.resize((180*SCALE,180*SCALE), Image.Resampling.LANCZOS)
        self.im.alpha_composite(logo, (1220*SCALE,130*SCALE))
        data = base64.b64encode(LOGO.read_bytes()).decode()
        self.svg.append(f'<image x="1220" y="130" width="180" height="180" xlink:href="data:image/png;base64,{data}"/>')

    def text(self, x, y, value, size=24, anchor='middle', color=BLUE, numeral=False):
        value = str(value)
        font = ImageFont.truetype(NUM if numeral else FONT, size*SCALE)
        self.d.text((x*SCALE,y*SCALE),value,font=font,fill=color,anchor={'middle':'mm','start':'lm','end':'rm'}[anchor])
        family = 'Comic Sans MS' if numeral else 'Andale Mono'
        self.svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" dominant-baseline="central" font-family="{family}, monospace" font-size="{size}" fill="{color}">{html.escape(value)}</text>')

    def line(self, a, b, color=BROWN, width=4, dash=False):
        if dash:
            dx,dy=b[0]-a[0],b[1]-a[1]
            length=math.hypot(dx,dy)
            for i in range(0,int(length),12):
                end=min(i+4,length)
                self.d.line(((a[0]+dx*i/length)*SCALE,(a[1]+dy*i/length)*SCALE,(a[0]+dx*end/length)*SCALE,(a[1]+dy*end/length)*SCALE),fill=color,width=max(1,int(width*SCALE)))
        else:
            self.d.line(tuple(v*SCALE for p in (a,b) for v in p),fill=color,width=int(width*SCALE))
        self.svg.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="4 8"' if dash else '')+'/>')

    def arrow(self,a,b):
        self.line(a,b,BLUE,2)
        t=math.atan2(b[1]-a[1],b[0]-a[0])
        for dt in (-0.45,0.45):
            self.line(b,(b[0]-11*math.cos(t+dt),b[1]-11*math.sin(t+dt)),BLUE,2)

    def circle(self,x,y,r,fill,outline,width):
        self.d.ellipse(((x-r)*SCALE,(y-r)*SCALE,(x+r)*SCALE,(y+r)*SCALE),fill=fill,outline=outline,width=int(width*SCALE))
        self.svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill or "none"}" stroke="{outline}" stroke-width="{width}"/>')

    def node(self,x,y,value,selected=False,r=28):
        if selected:
            self.circle(x,y,r+10,None,BLUE,2)
        self.circle(x,y,r,TEAL,BROWN,5)
        self.text(x,y-1,value,26,color='white',numeral=True)

    def save(self,name):
        self.im.resize((W,H),Image.Resampling.LANCZOS).save(HERE/f'{name}.png')
        (HERE/f'{name}.svg').write_text('\n'.join(self.svg)+ '\n</svg>\n')


def tree(d, positions, values, edges, selected=()):
    for a, b in edges:
        d.line(positions[a], positions[b])
    for key, (x, y) in positions.items():
        d.node(x, y, values[key], selected=key in selected, r=32)


EDGES = [(3, 5), (3, 1), (5, 6), (5, 2), (1, 0), (1, 8), (2, 7), (2, 4)]


def directed_edge(d, a, b, radius=34, destination_radius=34):
    """Clip a traversal arrow to both node boundaries."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    start = (a[0] + radius*dx/length, a[1] + radius*dy/length)
    end = (b[0] - destination_radius*dx/length, b[1] - destination_radius*dy/length)
    d.line(start, end)
    angle = math.atan2(dy, dx)
    for delta in (-0.45, 0.45):
        d.line(end, (end[0]-14*math.cos(angle+delta), end[1]-14*math.sin(angle+delta)))


def example():
    d = Diagram('Target 5, K = 2. Ringed nodes 7, 4, and 1 are exactly two edges from 5; node 1 is outside its subtree.')
    pos = {3:(540,410), 5:(340,555), 1:(800,555), 6:(220,705),
           2:(460,705), 0:(680,705), 8:(920,705), 7:(390,850), 4:(530,850)}
    tree(d, pos, {n:n for n in pos}, EDGES, (7,4,1))
    d.text(450, 310, 'target = 5, K = 2', 26)
    d.text(540, 345, 'root', 22)
    d.text(270, 555, 'target', 23, anchor='end')
    d.text(1170, 435, 'Two-edge paths', 25)
    d.text(1170, 505, '5 → 2 → 7', 27)
    d.text(1170, 565, '5 → 2 → 4', 27)
    d.text(1170, 625, '5 → 3 → 1', 27)
    d.text(1170, 740, 'answer = [7, 4, 1]', 24)
    d.text(768, 945, 'Ringed nodes are exactly K edges from the target.', 24)
    d.save('01_target_and_answer')


def neighbors():
    d = Diagram('At current node 5, BFS can reach left child 6, right child 2, and parent 3. The parent map supplies upward access.')
    pos = {3:(460,410), 5:(460,600), 6:(280,790), 2:(640,790)}
    for neighbor in (3,6,2):
        directed_edge(d, pos[5], pos[neighbor])
    for node, (x,y) in pos.items():
        d.node(x,y,node,r=32)
    d.text(460, 340, 'parent', 24)
    d.text(510, 495, 'parent[cur]', 24, anchor='start')
    d.text(395, 600, 'cur', 25, anchor='end')
    d.text(280, 860, 'cur->left', 24)
    d.text(640, 860, 'cur->right', 24)
    d.text(1090, 425, 'DFS records', 25)
    d.text(1090, 495, 'parent[5] = 3', 25)
    d.text(1090, 555, 'parent[3] = nullptr', 23)
    d.text(1090, 675, 'BFS from 5 discovers', 24)
    d.text(1090, 735, '[6, 2, 3]', 28)
    d.text(768, 945, 'Arrows show possible moves from cur; the tree is unchanged.', 22)
    d.save('02_parent_access')


def layers():
    d = Diagram('BFS starts with [5], then [6,2,3], then [7,4,1]. Stop at distance 2 without expanding those nodes. Visited tracking skips reverse moves.')
    pos = {5:(300,610), 6:(740,450), 2:(740,610), 3:(740,770),
           7:(1180,450), 4:(1180,610), 1:(1180,770)}
    for a,b in [(5,6),(5,2),(5,3),(2,7),(2,4),(3,1)]:
        directed_edge(d,pos[a],pos[b],destination_radius=44 if b in (7,4,1) else 34)
    for node,(x,y) in pos.items():
        d.node(x,y,node,r=32,selected=node in (7,4,1))
    for x, dist in [(300,0),(740,1),(1180,2)]:
        d.text(x,340,f'distance = {dist}',25)
    d.text(300, 700, 'start', 24)
    d.text(300, 850, 'queue = [5]', 24)
    d.text(740, 850, '[6, 2, 3]', 24)
    d.text(1180, 850, '[7, 4, 1]', 24)
    d.text(1180, 900, 'K = 2: stop here', 23)
    d.text(768, 965, 'Enqueue only unvisited neighbors; each column is one complete layer.', 21)
    d.save('03_bfs_layers')


def opposite_subtree():
    d = Diagram('DFS at cur 3 receives leftDistance 0 from target 5. Reaching right child 1 uses two edges, leaving K-leftDistance-2 = 0, so collect node 1.')
    pos = {3:(440,430),5:(260,620),1:(620,620),0:(530,810),8:(710,810)}
    d.line(pos[1],pos[0])
    d.line(pos[1],pos[8])
    directed_edge(d,pos[5],pos[3])
    directed_edge(d,pos[3],pos[1],destination_radius=44)
    for node,(x,y) in pos.items():
        d.node(x,y,node,r=32,selected=node==1)
    d.text(440, 350, 'cur = 3', 25)
    d.text(260, 700, 'target', 24)
    d.text(260, 745, 'leftDistance = 0', 22)
    d.text(275, 490, '1 edge', 23)
    d.text(610, 490, '1 edge', 23)
    d.text(685, 620, 'cur->right', 22, anchor='start')
    d.text(1110, 425, 'K = 2', 28)
    d.text(1110, 515, 'remaining', 25)
    d.text(1110, 570, '= K - leftDistance - 2', 23)
    d.text(1110, 625, '= 2 - 0 - 2 = 0', 25)
    d.text(1110, 730, 'Collect node 1.', 25)
    d.text(1110, 785, 'Do not descend to 0 or 8.', 22)
    d.text(768, 925, 'Local view: descendants of target 5 are omitted.', 23)
    d.save('04_opposite_subtree_distance')


if __name__ == '__main__':
    example()
    neighbors()
    layers()
    opposite_subtree()

