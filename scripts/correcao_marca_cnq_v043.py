from pathlib import Path
import io, hashlib, json, re, subprocess, sys
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import fitz
src,logo,out,ev=map(Path,sys.argv[1:5]); ev.mkdir(parents=True,exist_ok=True)
assert hashlib.sha256(src.read_bytes()).hexdigest()=='44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e'
r=PdfReader(src); w=PdfWriter(); w.clone_document_from_reader(r)
buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=(595,842),invariant=1)
c._code.append('/Artifact BMC')
im=Image.open(logo); width=210; height=width*im.height/im.width
c.drawImage(ImageReader(im),44,170,width=width,height=height,mask='auto')
c._code.append('EMC'); c.save()
w.pages[0].merge_page(PdfReader(buf).pages[0])
w.add_metadata({'/Subject':'GT-MKT-CNQ-001 v0.4.3 - correção focal de marca; distribuição não autorizada'})
with out.open('wb') as f: w.write(f)
new=PdfReader(out)
norm=lambda t:re.sub(r'\s+',' ',t).strip()
for a,b in zip(r.pages,new.pages): assert norm(a.extract_text())==norm(b.extract_text())
assert len(new.pages)==len(r.pages)==5
assert str(new.trailer['/Root']['/Lang'])=='pt-BR'
assert len(new.outline)==len(r.outline)
def annotations(reader):
    return [[{key:str(ref.get_object().get(key)) for key in ['/Subtype','/Rect','/A','/StructParent']} for ref in p.get('/Annots',[])] for p in reader.pages]
assert annotations(r)==annotations(new)
old=fitz.open(src); d=fitz.open(out)
checks=[]
for i,(a,b) in enumerate(zip(old,d)):
    pa=a.get_pixmap(); pb=b.get_pixmap()
    if i: assert pa.samples==pb.samples
    assert a.get_links()==b.get_links()
    checks.append({'page':i+1,'normalized_text_equal':True,'links_equal':True,'pixels_equal':pa.samples==pb.samples})
    if i==0:
        b.get_pixmap(matrix=fitz.Matrix(2,2)).save(ev/'depois-mupdf-1.png')
subprocess.run(['pdftoppm','-f','1','-l','1','-r','150','-png',str(out),str(ev/'depois-poppler')],check=True)
result={'version':'0.4.3','sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'logo_sha256':hashlib.sha256(logo.read_bytes()).hexdigest(),'logo_pixels':[im.width,im.height],'logo_rect_pdf':[44,170,width,height],'logo_marked_artifact':True,'pages':checks,'practical_tests':{'TP-01':'NÃO EXECUTADO','TP-02':'NÃO EXECUTADO','TP-03':'NÃO EXECUTADO'},'limitations':'Inspeção estrutural e renderização não substituem teste assistivo, clique em leitor ou telefone físico; sem certificação PDF/UA.'}
(ev/'checks-v0.4.3.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False))
