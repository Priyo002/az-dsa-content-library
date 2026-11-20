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


VALUES = {'r': -10, 'a': 9, 'b': 20, 'c': 15, 'd': 7}
EDGES = [('r', 'a'), ('r', 'b'), ('b', 'c'), ('b', 'd')]


def optimal_path():
    d = Diagram('The maximum path is 15 → 20 → 7, with sum 42. It does not include root -10.')
    pos = {'r': (475, 405), 'a': (290, 560), 'b': (660, 560),
           'c': (550, 740), 'd': (770, 740)}
    tree(d, pos, VALUES, EDGES, ('b', 'c', 'd'))
    d.text(475, 340, 'root', 23)
    d.text(1110, 495, 'Best complete path', 25)
    d.text(1110, 555, '15 → 20 → 7', 30)
    d.text(1110, 615, '15 + 20 + 7 = 42', 25)
    d.text(1110, 720, 'The root is not required.', 22)
    d.text(768, 860, 'Ringed nodes form the maximum-sum path.', 25)
    d.save('01_optimal_path_below_root')


def gain_vs_candidate():
    d = Diagram('At node 20, save the complete candidate 42 but return only the branch gain 35 to the parent.')
    for cx, selected in [(420, ('r', 'a', 'b')), (1090, ('r', 'a'))]:
        pos = {'r': (cx, 520), 'a': (cx-130, 695), 'b': (cx+130, 695)}
        tree(d, pos, {'r': 20, 'a': 15, 'b': 7}, [('r','a'),('r','b')], selected)
    d.text(420, 350, 'Complete path at 20', 25)
    d.text(1090, 350, 'One branch to parent', 25)
    d.arrow((1090, 465), (1090, 395))
    d.text(1120, 427, '35', 25, anchor='start')
    d.text(420, 795, '15 → 20 → 7', 26)
    d.text(1090, 795, '20 → 15', 26)
    d.text(420, 855, '20 + 15 + 7 = 42', 25)
    d.text(1090, 855, '20 + max(15, 7) = 35', 25)
    d.text(768, 935, 'Save both sides in the answer; return only one side.', 24)
    d.save('02_return_gain_vs_complete_path')


def negative_connectors():
    d = Diagram('A negative node can have a positive gain or connect the optimal path. Judge the full branch sum, not just its first node.')
    pos = {'r': (510, 435), 'a': (420, 580), 'b': (330, 725)}
    tree(d, pos, {'r': 2, 'a': -5, 'b': 10}, [('r','a'),('a','b')])
    d.text(440, 350, 'A positive child gain', 25)
    d.text(490, 580, 'gain = 5', 23, anchor='start')
    d.text(400, 725, 'gain = 10', 23, anchor='start')
    d.text(440, 825, '-5 + 10 = 5 > 0', 25)
    d.text(440, 880, 'Keep this branch at node 2.', 22)
    d.text(440, 930, 'Best complete path: 10', 23)
    pos = {'r': (1100, 500), 'a': (970, 690), 'b': (1230, 690)}
    tree(d, pos, {'r': -5, 'a': 10, 'b': 10}, [('r','a'),('r','b')], ('r','a','b'))
    d.text(1100, 350, 'A negative connector', 25)
    d.text(1100, 825, '10 + (-5) + 10 = 15', 25)
    d.text(1100, 880, 'The path must include -5.', 22)
    d.text(1100, 930, 'Best complete path: 15', 23)
    d.save('03_negative_nodes_can_help')


def all_negative():
    d = Diagram('For -3 with children -2 and -5, child contributions become zero but the nonempty maximum path is the single node -2.')
    pos = {'r': (440, 445), 'a': (280, 650), 'b': (600, 650)}
    tree(d, pos, {'r': -3, 'a': -2, 'b': -5}, [('r','a'),('r','b')], ('a',))
    d.text(275, 525, 'take 0', 23)
    d.text(605, 525, 'take 0', 23)
    d.text(280, 725, 'gain = -2', 23)
    d.text(600, 725, 'gain = -5', 23)
    d.text(1060, 435, 'Candidate at the root', 25)
    d.text(1060, 495, '-3 + 0 + 0 = -3', 26)
    d.text(1060, 610, 'All local candidates', 25)
    d.text(1060, 670, '-2, -5, -3', 27)
    d.text(1060, 740, 'answer = -2', 28)
    d.text(768, 850, 'Zero means omit a child branch.', 25)
    d.text(768, 910, 'The complete path still contains at least one node.', 24)
    d.save('04_all_negative_nonempty_path')


def postorder_gains():
    d = Diagram('Postorder returns gains 9,15,7,35,25. Candidate 42 at node 20 remains the global answer after root candidate 34.')
    pos = {'r': (520, 410), 'a': (300, 590), 'b': (740, 590),
           'c': (615, 785), 'd': (865, 785)}
    tree(d, pos, VALUES, EDGES)
    d.text(520, 335, 'return 25', 24)
    d.text(260, 675, 'return 9', 23)
    d.text(800, 535, 'return 35', 23)
    d.text(585, 855, 'return 15', 23)
    d.text(895, 855, 'return 7', 23)
    d.text(1170, 440, 'At node 20', 25)
    d.text(1170, 495, 'candidate = 42', 24)
    d.text(1170, 610, 'At root -10', 25)
    d.text(1170, 665, 'candidate = 34', 24)
    d.text(1170, 770, 'answer stays 42', 25)
    d.text(768, 940, 'Postorder: 9 → 15 → 7 → 20 → -10', 25)
    d.save('05_postorder_gains')


if __name__ == '__main__':
    optimal_path()
    gain_vs_candidate()
    negative_connectors()
    all_negative()
    postorder_gains()

