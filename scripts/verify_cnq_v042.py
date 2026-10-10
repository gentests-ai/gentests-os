"""Reproducible local evidence; no publication and no claim of a physical-device/UI click test.
python scripts/verify_cnq_v042.py comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf 05-Evidencias/GT-MKT-CNQ-001/v0.4.2
"""
import sys,fitz,json,hashlib,re,datetime,urllib.request,subprocess
from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw
pdf,previous,ev=map(Path,sys.argv[1:4]);ev.mkdir(parents=True,exist_ok=True)
subprocess.run(['pdftoppm','-r','150','-png',str(pdf),str(ev/'page')],check=True)
d=fitz.open(pdf);old=fitz.open(previous);r=PdfReader(pdf)
checks={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':[]}
for i,p in enumerate(d):
 p.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(str(ev/f'mupdf-{i+1}.png'))
 pix=p.get_pixmap(matrix=fitz.Matrix(390/595,390/595));small=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 pix=p.get_pixmap(matrix=fitz.Matrix(780/595,780/595));zoom=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 sheet=Image.new('RGB',(1190,zoom.height+50),'#edf1f3');draw=ImageDraw.Draw(sheet)
 for x,label in [(8,'390 px / ajustar largura'),(408,'390 px / zoom 200% / esquerda'),(808,'390 px / zoom 200% / direita')]:draw.text((x,10),label,fill='black')
 sheet.paste(small,(0,40));sheet.paste(zoom.crop((0,0,390,zoom.height)),(400,40));sheet.paste(zoom.crop((390,0,780,zoom.height)),(800,40));sheet.save(ev/f'mobile-simulation-{i+1}.png')
 spans=[s for b in p.get_text('dict')['blocks'] if 'lines'in b for l in b['lines'] for s in l['spans']]
 clipped=[s['text'] for s in spans if not p.rect.contains(fitz.Rect(s['bbox']))];assert not clipped
 overlaps=[]
 for a in range(len(spans)):
  for b in range(a+1,len(spans)):
   box=fitz.Rect(spans[a]['bbox'])&fitz.Rect(spans[b]['bbox'])
   if box.width>0.3 and box.height>0.3:overlaps.append([spans[a]['text'],spans[b]['text']])
 assert not overlaps,overlaps
 norm=lambda s:re.sub(r'\s+',' ',s).strip()
 same=norm(old[i].get_text())==norm(p.get_text());assert same
 checks['pages'].append({'page':i+1,'clipped_text':clipped,'overlapping_text_spans':overlaps,'normalized_approved_text_preserved':same,'body_font_pt':12,'mobile_fit_width_body_css_px':12*390/595,'mobile_200_percent_body_css_px':24*390/595})
link=d[4].get_links()[0];txt=d[4].search_for(link['uri'])[0];assert link['from'].contains(txt)
request=urllib.request.Request(link['uri'],headers={'User-Agent':'GenTests-CNQ-link-check'})
with urllib.request.urlopen(request,timeout=25) as res:
 body=res.read().decode('utf-8',errors='replace');http={'status':res.status,'url':res.url,'title':re.search(r'<title>(.*?)</title>',body,re.S).group(1),'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
checks['hyperlink']={'annotation_rect_top_origin':list(link['from']),'text_rect_top_origin':list(txt),'fully_contains_visible_text_bbox':True,'uri':link['uri'],'http':http,'native_reader_click':'NOT_TESTED: cloud browser rejected file:// protocol; no workaround attempted'}
root=r.trailer['/Root'];roles={}
def walk(ref):
 obj=ref.get_object()
 if not isinstance(obj,dict):return
 if '/S' in obj: roles[str(obj['/S'])]=roles.get(str(obj['/S']),0)+1
 for k in obj.get('/K',[]):
  if isinstance(k,dict) or hasattr(k,'get_object'):walk(k)
walk(root['/StructTreeRoot'])
assert roles['/Lbl']==11 and roles['/LI']==11 and roles['/H1']==5
checks['accessibility']={'lang':str(root['/Lang']),'marked':bool(root['/MarkInfo']['/Marked']),'structure_roles':roles,'outline_count':len(r.outline),'pdf_ua_certified':False,'screen_reader_tested':False,'residuals':['Financial tables use TD without added column headers, preserving approved content; assistive reading must be validated.','Fixed A4 layout needs zoom/pan at 390 px; no responsive reflow claim.','PDF/UA validator and screen-reader user testing remain necessary before any compliance claim.']}
checks['font_resources']=[{'resource':k,'font':str(v.get_object()['/BaseFont']),'font_file2':bool(v.get_object()['/FontDescriptor'].get('/FontFile2')),'to_unicode':bool(v.get_object().get('/ToUnicode'))}for k,v in r.pages[0]['/Resources']['/Font'].items()];assert all(f['font_file2'] and f['to_unicode'] for f in checks['font_resources'])
checks['numbering_1_to_7']=bool(re.search(r'1\. Registre.*2\. Some.*3\. Registre.*4\. Identifique.*5\. Separe.*6\. Considere.*7\. Concilie',norm(d[3].get_text())));assert checks['numbering_1_to_7']
(ev/'checks-v0.4.2.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False))
print(json.dumps({'sha256':checks['pdf_sha256'],'checks':'passed','http':http,'roles':roles},indent=2,ensure_ascii=False))
