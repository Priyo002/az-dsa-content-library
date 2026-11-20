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


def tree(d, positions, values, edges, labels=None):
    # Trim every edge at the object boundary; # denotes an empty position.
    for parent, child in edges:
        a, b = positions[parent], positions[child]
        dx, dy = b[0]-a[0], b[1]-a[1]
        length = math.hypot(dx, dy)
        ra = 28 if values[parent] is not None else 20
        rb = 28 if values[child] is not None else 20
        d.line((a[0]+ra*dx/length,a[1]+ra*dy/length),
               (b[0]-rb*dx/length,b[1]-rb*dy/length))
    for key, (x, y) in positions.items():
        if values[key] is None:
            d.text(x,y,'#',28)
        else:
            d.node(x,y,values[key])
    for key, (label, dx, dy) in (labels or {}).items():
        x,y=positions[key]
        d.text(x+dx,y+dy,label,22)


def bracket(d, x1, x2, y, label):
    d.line((x1,y-10),(x1,y),BLUE,2)
    d.line((x1,y),(x2,y),BLUE,2)
    d.line((x2,y),(x2,y-10),BLUE,2)
    d.text((x1+x2)/2,y+27,label,22)


VALUES={'r':1,'L':2,'R':3,'LL':None,'LR':-4,'RL':2,'RR':None,
        'LRL':None,'LRR':None,'RLL':None,'RLR':None}
EDGES=[('r','L'),('r','R'),('L','LL'),('L','LR'),('R','RL'),('R','RR'),
       ('LR','LRL'),('LR','LRR'),('RL','RLL'),('RL','RLR')]
BFS=['1','2','3','#','-4','2','#','#','#','#','#']
DFS=['1','2','#','-4','#','#','3','2','#','#','#']


def missing_positions():
    d=Diagram('Null markers distinguish a left child from a right child, even when preorder values are identical.')
    for cx,name,right in [(450,'Tree A',False),(1086,'Tree B',True)]:
        d.text(cx,355,name,26)
        pos={'r':(cx,445),'L':(cx-125,585),'R':(cx+125,585)}
        vals={'r':1,'L':None if right else 2,'R':2 if right else None}
        child='R' if right else 'L'
        x,y=pos[child]
        pos.update(a=(x-65,710),b=(x+65,710))
        vals.update(a=None,b=None)
        tree(d,pos,vals,[('r','L'),('r','R'),(child,'a'),(child,'b')])
        d.text(cx-125,535,'left',21)
        d.text(cx+125,535,'right',21)
        d.text(cx,805,'1,#,2,#,#' if right else '1,2,#,#,#',28)
    d.text(768,865,'Preorder values alone: 1,2 in both trees',24)
    d.text(768,915,'# preserves each missing child position',25)
    d.save('01_null_markers_preserve_structure')


def bfs_encoding():
    d=Diagram('BFS serialization of the running tree: 1,2,3,#,-4,2,#,#,#,#,#. Null positions have no children.')
    pos={'r':(768,365),'L':(480,490),'R':(1056,490),
         'LL':(350,615),'LR':(610,615),'RL':(926,615),'RR':(1186,615),
         'LRL':(545,725),'LRR':(675,725),'RLL':(861,725),'RLR':(991,725)}
    tree(d,pos,VALUES,EDGES)
    for y,label in [(365,'level 0'),(490,'level 1'),(615,'level 2'),(725,'level 3')]:
        d.text(155,y,label,22,anchor='start')
    xs=[238+106*i for i in range(11)]
    for x,t in zip(xs,BFS): d.text(x,820,t,28)
    for a,b,label in [(0,0,'level 0'),(1,2,'level 1'),(3,6,'level 2'),(7,10,'level 3')]:
        bracket(d,xs[a]-35,xs[b]+35,853,label)
    d.text(768,939,'Read each level left to right; # adds no children.',24)
    d.save('02_bfs_serialization')


def bfs_decoding():
    d=Diagram('BFS decoding: each queued real parent consumes its next two tokens, left then right. Repeated values identify distinct positions.')
    pos={'r':(390,435),'L':(235,565),'R':(545,565),
         'LL':(150,695),'LR':(320,695),'RL':(460,695),'RR':(630,695),
         'LRL':(265,805),'LRR':(375,805),'RLL':(420,805),'RLR':(530,805)}
    tree(d,pos,VALUES,EDGES,{'L':('2a',-65,0),'RL':('2b',65,0)})
    d.text(390,350,'Rebuilt tree',25)
    for x,t in [(865,'Parent'),(1070,'Left'),(1260,'Right')]:d.text(x,350,t,25)
    rows=[('1','2','3'),('2a','#','-4'),('3','2','#'),('-4','#','#'),('2b','#','#')]
    for i,(p,l,r) in enumerate(rows):
        y=435+i*86
        d.text(865,y,p,27)
        d.arrow((930,y),(995,y))
        d.text(1070,y,l,28)
        d.text(1260,y,r,28)
    d.text(768,888,'Queue order: 1 → 2a → 3 → -4 → 2b',25)
    d.text(768,938,'2a and 2b are labels; both store the value 2.',23)
    d.save('03_bfs_deserialization')


def dfs_subtrees():
    d=Diagram('DFS preorder consumes root, complete left subtree, then complete right subtree. Tokens 1–5 form the left subtree; tokens 6–10 form the right.')
    pos={'r':(768,360),'L':(470,490),'R':(1066,490),
         'LL':(330,615),'LR':(610,615),'RL':(926,615),'RR':(1206,615),
         'LRL':(545,720),'LRR':(675,720),'RLL':(861,720),'RLR':(991,720)}
    tree(d,pos,VALUES,EDGES)
    d.text(396,419,'left subtree',23)
    d.text(1110,419,'right subtree',23)
    xs=[238+106*i for i in range(11)]
    d.text(100,783,'index',20,anchor='start')
    for i,(x,t) in enumerate(zip(xs,DFS)):
        d.text(x,783,i,20)
        d.text(x,823,t,28)
    for a,b,label in [(0,0,'root'),(1,5,'complete left subtree'),(6,10,'complete right subtree')]:
        bracket(d,xs[a]-35,xs[b]+35,856,label)
    d.text(768,939,'After token 5, the next call starts at token 6.',24)
    d.save('04_dfs_subtree_boundaries')


if __name__=='__main__':
    missing_positions()
    bfs_encoding()
    bfs_decoding()
    dfs_subtrees()
