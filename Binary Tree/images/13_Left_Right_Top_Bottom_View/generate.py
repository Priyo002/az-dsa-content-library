"""Rebuild the lesson's deterministic PNG and editable SVG diagrams (Pillow)."""
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


POS = {1:(768,400),2:(530,525),3:(1006,525),4:(410,650),5:(650,650),6:(886,650),7:(1126,650),8:(715,775),9:(821,775)}
EDGES = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(5,8),(6,9)]
HD = {1:0,2:-1,3:1,4:-2,5:0,6:0,7:2,8:1,9:-1}
DEPTH = {1:0,2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3}


def tree(d):
    for a,b in EDGES:
        d.line(POS[a],POS[b])
    for n,(x,y) in POS.items():
        d.node(x,y,n)


def side_views():
    d = Diagram('Left and right views select the first and last node at each level.')
    d.text(155,270,'One selection per level',26,anchor='start')
    d.text(185,340,'Left view')
    d.text(1350,340,'Right view')
    tree(d)
    for left,right in [(1,1),(2,3),(4,7),(8,9)]:
        x,y=POS[left]
        d.arrow((x-42,y),(260,y))
        d.text(185,y,left,28)
        x,y=POS[right]
        d.arrow((x+42,y),(1276,y))
        d.text(1350,y,right,28)
    d.text(185,850,'first in BFS',20)
    d.text(1350,850,'last in BFS',20)
    d.text(768,915,'At the deepest level, 8 and 9 remain visible.',24)
    d.save('01_side_views')


def coordinates():
    d=Diagram('Horizontal distances on the running tree. Left edges subtract one; right edges add one.')
    d.text(155,250,'Root: hd = 0',24,anchor='start')
    d.text(155,294,'Left child: hd - 1    Right child: hd + 1',24,anchor='start')
    tree(d)
    labels={1:(768,350),2:(415,525),3:(1121,525),4:(410,705),5:(570,697),6:(966,697),7:(1126,705),8:(675,830),9:(861,830)}
    for n,(x,y) in labels.items():
        hd=HD[n]
        d.text(x,y,f'hd = {hd:+d}' if hd else 'hd = 0',22)
    d.text(768,915,'5 and 6 share hd = 0 and depth = 2.',24)
    d.save('02_horizontal_distances')


def column_view(bottom=False):
    kind='Bottom' if bottom else 'Top'
    d=Diagram(f'{kind} view groups nodes by horizontal distance and selects '+('the last BFS node, with 6 winning the tie against 5.' if bottom else 'the first BFS node in each column.'))
    d.text(150,250,f'{kind} view: keep the '+('last' if bottom else 'first')+' BFS node per column',24,anchor='start')
    d.text(150,292,'Ring = selected node',21,anchor='start')
    xs={h:770+210*h for h in range(-2,3)}
    ys={depth:410+110*depth for depth in range(4)}
    selected={4,9,6,8,7} if bottom else {4,2,1,3,7}
    for h,x in xs.items():
        d.text(x,350,f'hd = {h:+d}' if h else 'hd = 0',22)
        d.line((x,375),(x,785),color='#A7B6B4',width=1,dash=True)
    for dep,y in ys.items():
        d.text(205,y,f'depth {dep}',21,anchor='end')
    for n in range(1,10):
        x=xs[HD[n]]+(-42 if n==5 else 42 if n==6 else 0)
        d.node(x,ys[DEPTH[n]],n,n in selected)
    if bottom:
        d.text(770,819,'hd = 0: 1 → 5 → 6; later equal-depth node 6 wins.',21)
    else:
        d.text(770,819,'At hd = 0, keep 1; later nodes 5 and 6 are hidden.',21)
    d.text(205,897,'View',22,anchor='end')
    result=[4,9,6,8,7] if bottom else [4,2,1,3,7]
    for h,n in zip(range(-2,3),result):
        d.text(xs[h],897,n,28)
    d.arrow((350,943),(1190,943))
    d.text(770,972,'Read columns from left to right',19)
    d.save('04_bottom_view' if bottom else '03_top_view')


if __name__ == '__main__':
    side_views()
    coordinates()
    column_view()
    column_view(bottom=True)
