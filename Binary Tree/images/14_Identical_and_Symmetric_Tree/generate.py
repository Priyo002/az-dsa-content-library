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


def draw_tree(d, positions, values, edges, labels=None):
    for a, b in edges:
        d.line(positions[a], positions[b])
    for key, (x, y) in positions.items():
        if values[key] is None:
            # Null is an empty pointer position, never a filled tree node.
            d.d.rectangle(((x-43)*SCALE, (y-24)*SCALE,
                           (x+43)*SCALE, (y+24)*SCALE), fill=CREAM)
            d.svg.append(f'<rect x="{x-43}" y="{y-24}" width="86" height="48" fill="{CREAM}"/>')
            d.text(x, y, 'null', 24)
        else:
            d.node(x, y, values[key])
    for key, value in (labels or {}).items():
        x, y = positions[key]
        d.text(x, y+54, value, 22)


def identical(mismatch=False):
    d = Diagram('Trees with the same values are '+
                ('not identical when node 4 changes from right child to left child.'
                 if mismatch else 'identical when every left and right position matches.'))
    for cx, name, flipped in [(450, 'Tree A', False), (1086, 'Tree B', mismatch)]:
        d.text(cx, 360, name, 26)
        pos = {'root': (cx, 460), 'L': (cx-145, 605), 'R': (cx+145, 605),
               'LR': (cx-65, 750)}
        vals = {'root': 1, 'L': 2, 'R': 3, 'LR': 4}
        edges = [('root', 'L'), ('root', 'R'), ('L', 'LR')]
        labels = {}
        if mismatch:
            pos['LL'] = (cx-225, 750)
            vals['LL'] = 4 if flipped else None
            vals['LR'] = None if flipped else 4
            edges.append(('L', 'LL'))
            labels = {'LL': 'left', 'LR': 'right'}
        draw_tree(d, pos, vals, edges, labels)
    if mismatch:
        d.text(768, 875, 'Compare the left children of 2: (null, 4)', 25)
        d.text(768, 927, 'Same values, different positions → false', 25)
    else:
        d.text(768, 865, 'Compare left with left, and right with right.', 25)
        d.text(768, 922, 'Same structure + same values → true', 25)
    d.save('03_identical_structure_mismatch' if mismatch else '01_identical_trees')


def symmetry(mismatch=False):
    d = Diagram('Identical subtrees need not be mirrors: LL is null but RR contains 3.'
                if mismatch else 'Symmetry compares L with R, LL with RR, and LR with RL.')
    pos = {'root': (768, 400), 'L': (520, 565), 'R': (1016, 565),
           'LL': (385, 730), 'LR': (655, 730),
           'RL': (881, 730), 'RR': (1151, 730)}
    vals = {'root': 1, 'L': 2, 'R': 2, 'LL': 3, 'LR': 4, 'RL': 4, 'RR': 3}
    if mismatch:
        vals.update(LL=None, LR=3, RL=None)
    edges = [('root', 'L'), ('root', 'R'), ('L', 'LL'), ('L', 'LR'),
             ('R', 'RL'), ('R', 'RR')]
    # An annotation line marks the reflection axis; tree edges stay solid brown.
    d.line((768, 452), (768, 817), BLUE, 2, dash=True)
    draw_tree(d, pos, vals, edges, {k:k for k in ('LL', 'LR', 'RL', 'RR')})
    d.text(458, 556, 'L', 23)
    d.text(1078, 556, 'R', 23)
    if mismatch:
        d.text(768, 868, 'Outer pair: (LL, RR) = (null, 3)', 25)
        d.text(768, 922, 'Identical subtrees, but no mirror → false', 25)
    else:
        d.text(445, 870, 'Outer: (LL, RR) = (3, 3)', 23)
        d.text(1080, 870, 'Inner: (LR, RL) = (4, 4)', 23)
        d.text(768, 928, 'Opposite directions at every depth → true', 25)
    d.save('04_identical_but_not_symmetric' if mismatch else '02_symmetric_mirror_pairs')


if __name__ == '__main__':
    identical()
    symmetry()
    identical(mismatch=True)
    symmetry(mismatch=True)
