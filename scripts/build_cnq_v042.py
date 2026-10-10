"""Typography-only reconstruction from approved v0.4.1. Python 3.12, reportlab 4.4.9, pypdf 6.10.0.
Usage: python scripts/build_cnq_v042.py comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf output.pdf
Fonts beside script in fonts/cnq/. All approved strings read from guarded historical PDF.
"""
import sys, hashlib, re, io, json
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
SOURCE_SHA='646554cfdba296457af7d0bdc4b50783f2fe44a2841970fce48692a989f5038a'
source,out=map(Path,sys.argv[1:3]); assert hashlib.sha256(source.read_bytes()).hexdigest()==SOURCE_SHA
fontdir=Path(__file__).parent/'fonts'/'cnq'
if not fontdir.exists(): fontdir=Path(__file__).parent/'fonts'
for name,file in [('CNQ','DejaVuSans.ttf'),('CNQBold','DejaVuSans-Bold.ttf')]: pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
r=PdfReader(source); buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=(595,842),invariant=1,pageCompression=1,initialFontName='CNQ')
c.setTitle('GenTests.ai — Guia Executivo de Custo da Não Qualidade de Software');c.setAuthor('GenTests.ai');c.setSubject('GT-MKT-CNQ-001 v0.4.2 — revisão interna; distribuição não autorizada')
plans=[]; linkrect=None
for pn,page in enumerate(r.pages):
    ops=ContentStream(page.get_contents(),r).operations; color=(0,0,0);font=None;size=0;x=y=0; entries=[]
    for args,op in ops:
        if op==b'rg': color=tuple(map(float,args))
        elif op==b'Tf': font=str(args[0]);size=float(args[1])
        elif op==b'Tm': x,y=map(float,args[-2:])
        elif op==b're':
            c._code.append('/Artifact BMC');c.setFillColorRGB(*color);c.rect(*map(float,args),stroke=0,fill=1);c._code.append('EMC')
        elif op==b'Tj':
            text=args[0].original_bytes.decode('cp1252'); newsize=12 if size==10.5 else size
            fname='CNQBold' if font=='/F2' else 'CNQ'
            # Preserve line breaks, margins, palette, page count. Align only whitespace-based financial columns.
            parts=[text];positions=[x];list_label=None
            if text.startswith('• ') or (pn==3 and re.match(r'^[1-7]\. ',text)):
                list_label=text[:2] if text.startswith('•') else text[:3]
                parts=[list_label,text[len(list_label):]];positions=[x,x+pdfmetrics.stringWidth(list_label,fname,newsize)]
            if pn==2 and size==10.5 and re.search(r'\s{2,}R\$',text):
                parts=re.split(r'\s{2,}',text.strip()); positions=([44,245,520-pdfmetrics.stringWidth(parts[-1],fname,newsize)] if len(parts)==3 else [44,520-pdfmetrics.stringWidth(parts[-1],fname,newsize)])
            role='Artifact' if y>806 or y<43 else ('H1' if size>=29 else 'H2' if size==11 else 'P')
            for t,px in zip(parts,positions):
                width=pdfmetrics.stringWidth(t,fname,newsize)
                assert px+width<582,(pn,t,px+width)
                entry={'text':t,'x':px,'y':y,'size':newsize,'role':role,'list_kind':('Lbl' if t==list_label else 'LBody') if list_label else None}
                mcid=len(entries);entries.append(entry)
                c._code.append('/Artifact BMC' if role=='Artifact' else f'/{role} <</MCID {mcid}>> BDC')
                c.setFillColorRGB(*color);c.setFont(fname,newsize);c.drawString(px,y,t);c._code.append('EMC')
                if t=='https://gentests-site.pages.dev/':
                    face=pdfmetrics.getFont(fname).face
                    linkrect=[px-0.5,y+face.descent*newsize/1000-0.5,px+width+0.5,y+face.ascent*newsize/1000+0.5]
                    c.linkURL(t,linkrect,relative=0,thickness=0)
    plans.append(entries);c.showPage()
c.save();w=PdfWriter();w.clone_document_from_reader(PdfReader(io.BytesIO(buf.getvalue())));w.pdf_header='%PDF-1.7'
# Meaningful reading-order tree: H1/H2, paragraphs, lists, financial rows; repeated furniture is artifact.
N=NameObject;D=DictionaryObject;A=ArrayObject;I=NumberObject;S=TextStringObject
root=D({N('/Type'):N('/StructTreeRoot')});rootref=w._add_object(root)
doc=D({N('/Type'):N('/StructElem'),N('/S'):N('/Document'),N('/P'):rootref,N('/K'):A()});docref=w._add_object(doc);root[N('/K')]=A([docref]); parentnums=A()
def elem(role,parent,kids=None,page=None):
    d=D({N('/Type'):N('/StructElem'),N('/S'):N('/'+role),N('/P'):parent,N('/K'):A(kids or [])})
    if page is not None:d[N('/Pg')]=page
    ref=w._add_object(d);parent.get_object()[N('/K')].append(ref);return ref
for pn,(p,entries) in enumerate(zip(w.pages,plans)):
    p[N('/StructParents')]=I(pn);p[N('/Tabs')]=N('/S'); mappings=A([NullObject() for e in entries]); sect=elem('Sect',docref,page=p.indirect_reference);last=None;li=None;lst=None;table=None;row=None;lasty=None
    for idx,e in enumerate(entries):
        if e['role']=='Artifact':continue
        txt=e['text'];y=e['y'];role=e['role'];ref=None
        if role=='H1' and last and last.get_object()['/S']=='/H1':ref=last
        elif role in ('H1','H2'):
            ref=elem(role,sect,page=p.indirect_reference);lst=table=row=li=None
        elif pn==2 and ((490<=y<=543) or (360<=y<=395)):
            if table is None:table=elem('Table',sect,page=p.indirect_reference)
            if y!=lasty:row=elem('TR',table,page=p.indirect_reference)
            ref=elem('TD',row,page=p.indirect_reference)
            if txt=='Subtotal de recursos':ref.get_object()[N('/A')]=D({N('/O'):N('/Table'),N('/ColSpan'):I(2)})
        elif e.get('list_kind') or (pn==3 and 403<=y<=543):
            if lst is None:
                lst=elem('L',sect,page=p.indirect_reference)
                lst.get_object()[N('/A')]=D({N('/O'):N('/List'),N('/ListNumbering'):N('/Decimal' if pn==3 else '/Disc')})
            if e.get('list_kind')=='Lbl':
                li=elem('LI',lst,page=p.indirect_reference);ref=elem('Lbl',li,page=p.indirect_reference)
            elif last and last.get_object()['/S']=='/LBody':ref=last
            else:ref=elem('LBody',li,page=p.indirect_reference)
        elif txt.startswith('https://'):
            ref=elem('Link',sect,page=p.indirect_reference)
        else:
            if last and last.get_object()['/S']=='/P' and lasty and 0<lasty-y<=18:ref=last
            else:ref=elem('P',sect,page=p.indirect_reference)
        ref.get_object()['/K'].append(I(idx));mappings[idx]=ref;last=ref;lasty=y
    parentnums.extend([I(pn),w._add_object(mappings)])
    # Associate the actionable link annotation with its semantic Link element.
    if pn==4:
        for ann in p.get('/Annots',[]):
            a=ann.get_object();a[N('/StructParent')]=I(5)
            lr=next(mappings[i] for i,e in enumerate(entries) if e['text'].startswith('https://'))
            lr.get_object()['/K'].append(D({N('/Type'):N('/OBJR'),N('/Obj'):ann,N('/Pg'):p.indirect_reference}));parentnums.extend([I(5),lr])
root[N('/ParentTree')]=w._add_object(D({N('/Nums'):parentnums}));root[N('/ParentTreeNextKey')]=I(6)
w.root_object[N('/StructTreeRoot')]=rootref;w.root_object[N('/MarkInfo')]=D({N('/Marked'):BooleanObject(True)});w.root_object[N('/Lang')]=S('pt-BR')
w.root_object[N('/ViewerPreferences')]=D({N('/DisplayDocTitle'):BooleanObject(True)})
for i,title in enumerate(['Quanto custa um incidente de software?','Entenda o impacto','Exemplo financeiro','Checklist prático','Próximos passos e fontes']):w.add_outline_item(title,i)
with open(out,'wb') as f:w.write(f)
# Preserve every approved word, numeral, punctuation and ordering (only layout whitespace may change).
norm=lambda s:re.sub(r'\s+',' ',s).strip()
new=PdfReader(out)
for i,(a,b) in enumerate(zip(r.pages,new.pages)):
    assert norm(a.extract_text())==norm(b.extract_text()),('text regression',i)
assert len(new.pages)==5
assert [m.group() for m in re.finditer(r'(?m)^[1-7]\.',new.pages[3].extract_text(extraction_mode='layout'))]==[f'{i}.' for i in range(1,8)]
print(json.dumps({'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'pages':5,'text_equal_ignoring_whitespace':True,'numbering_1_to_7':True,'link_rect':linkrect},indent=2))
