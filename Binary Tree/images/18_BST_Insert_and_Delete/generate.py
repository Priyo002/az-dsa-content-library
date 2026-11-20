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


# Stable node identifiers preserve object identity in the copy-key stage.
BASE = {50: (30, 70), 30: (20, 40), 70: (60, 80),
        20: (None, None), 40: (None, None), 60: (None, 65),
        80: (None, None), 65: (None, None)}
OFFSETS = {50:(0,0),30:(-180,130),70:(180,130),20:(-270,260),
           40:(-90,260),60:(90,260),80:(270,260),65:(150,390)}


def state_without(key):
    state = dict(BASE)
    del state[key]
    if key == 20:
        state[30] = (None, 40)
    elif key == 60:
        state[70] = (65, 80)
    elif key == 40:
        state[30] = (20, None)
    return state


def draw_tree(d, center, state, values=None, selected=(), compact=False):
    values = values or {key:key for key in state}
    factor = .64 if compact else 1
    pos = {key:(center+OFFSETS[key][0]*factor,450+OFFSETS[key][1]*(.87 if compact else 1))
           for key in state}
    if 65 in state and 60 not in state:
        pos[65] = (center+90*factor,450+260*(.87 if compact else 1))
    for parent, children in state.items():
        for child in children:
            if child is not None:
                d.line(pos[parent],pos[child])
    for key,(x,y) in pos.items():
        d.node(x,y,values[key],selected=key in selected,r=28 if compact else 31)
    return pos


def check_state(state, expected, values=None):
    values = values or {key:key for key in state}
    seen = set()
    def visit(key, lo=float('-inf'), hi=float('inf')):
        if key is None:
            return []
        assert key not in seen
        seen.add(key)
        value = values[key]
        assert lo < value < hi
        left,right = state[key]
        return visit(left,lo,value)+[value]+visit(right,value,hi)
    assert visit(50) == sorted(expected)
    assert seen == set(state)


def insertion():
    d=Diagram('Insert 65: compare with 50, 70, and 60; attach a new leaf as the right child of 60.')
    before=dict(BASE)
    del before[65]
    before[60]=(None,None)
    d.text(410,345,'Before: insert 65',26)
    d.text(1126,345,'After',26)
    p=draw_tree(d,410,before)
    draw_tree(d,1126,BASE,selected=(65,))
    d.arrow((735,610),(800,610))
    d.text(410,835,'50 → 70 → 60 → nullptr',24)
    d.text(410,885,'right, left, right',24)
    d.text(1126,910,'60->right = new Node(65)',23)
    d.text(768,967,'50 < 65 < 70, and 65 > 60: every ancestor constraint holds.',22)
    check_state(before,[20,30,40,50,60,70,80])
    check_state(BASE,[20,30,40,50,60,65,70,80])
    d.save('01_insert_65')


def leaf():
    d=Diagram('Delete leaf 20. Release node 20 and reconnect 30->left to nullptr; all other nodes remain.')
    d.text(410,345,'Before: delete 20',26)
    d.text(1126,345,'After',26)
    p=draw_tree(d,410,BASE,selected=(20,))
    after=state_without(20)
    q=draw_tree(d,1126,after)
    d.text(p[20][0],790,'leaf',24)
    # A null child is notation, not an allocated blue node.
    dx,dy = 856-q[30][0],690-q[30][1]
    length = math.hypot(dx,dy)
    d.line((q[30][0]+32*dx/length,q[30][1]+32*dy/length),(856,690))
    d.text(856,720,'nullptr',23)
    d.arrow((735,610),(800,610))
    d.text(410,915,'delete 20; return nullptr',23)
    d.text(1126,915,'30->left = nullptr',24)
    check_state(after,[30,40,50,60,65,70,80])
    d.save('02_delete_leaf')


def one_child():
    d=Diagram('Delete 60, which has only right child 65. Save 65, free 60, return 65, and reconnect 70->left.')
    d.text(410,345,'Before: delete 60',26)
    d.text(1126,345,'After',26)
    draw_tree(d,410,BASE,selected=(60,))
    after=state_without(60)
    draw_tree(d,1126,after,selected=(65,))
    d.arrow((735,610),(800,610))
    d.text(410,915,'save 65; delete 60; return 65',22)
    d.text(1126,835,'70->left = 65',25)
    d.text(1126,890,'50 < 65 < 70',24)
    check_state(after,[20,30,40,50,65,70,80])
    d.save('03_delete_one_child')


def successor():
    d=Diagram('Delete key 50 in three stages: find successor 60, copy 60 into the existing root, then delete the original successor and promote 65. The middle state temporarily has two keys equal to 60.')
    centers=(275,768,1261)
    for x,label in zip(centers,('1. Find successor','2. Copy its key','3. Remove original')):
        d.text(x,345,label,24)
    draw_tree(d,centers[0],BASE,selected=(60,),compact=True)
    copied={key:key for key in BASE}
    copied[50]=60
    draw_tree(d,centers[1],BASE,values=copied,selected=(50,60),compact=True)
    after=state_without(60)
    final={key:copied[key] for key in after}
    draw_tree(d,centers[2],after,values=final,selected=(65,),compact=True)
    d.arrow((482,570),(543,570))
    d.arrow((977,570),(1038,570))
    d.text(275,860,'right, then left',23)
    d.text(275,905,'70 → 60',25)
    d.text(768,860,'same root object',23)
    d.text(768,905,'temporary duplicate',22)
    d.text(1261,860,'delete original 60',22)
    d.text(1261,905,'70->left = 65',23)
    d.text(768,967,'The successor has no left child; its right child 65 is preserved.',22)
    check_state(after,[20,30,40,60,65,70,80],final)
    assert copied[50] == copied[60] == 60  # Deliberate intermediate state.
    d.save('04_delete_two_children')


def alternatives():
    d=Diagram('Two valid results of deleting 50 from the original tree: successor replacement uses 60 and promotes 65; predecessor replacement uses 40 and removes its original leaf. Both preserve the same remaining keys.')
    d.text(410,345,'Use successor 60',26)
    d.text(1126,345,'Use predecessor 40',26)
    succ=state_without(60)
    pred=state_without(40)
    sv={key:(60 if key==50 else key) for key in succ}
    pv={key:(40 if key==50 else key) for key in pred}
    draw_tree(d,410,succ,sv)
    draw_tree(d,1126,pred,pv)
    d.text(410,835,'minimum of right subtree',23)
    d.text(410,885,'promote 65 into 60\'s place',22)
    d.text(1126,900,'maximum of left subtree',23)
    d.text(768,967,'Same inorder: 20 30 40 60 65 70 80',25)
    check_state(succ,[20,30,40,60,65,70,80],sv)
    check_state(pred,[20,30,40,60,65,70,80],pv)
    d.save('05_successor_vs_predecessor')


if __name__ == '__main__':
    insertion()
    leaf()
    one_child()
    successor()
    alternatives()

