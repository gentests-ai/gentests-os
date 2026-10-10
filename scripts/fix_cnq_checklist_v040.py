"""Correção focal CNQ-VIS-006-01 para o PDF original v0.4.0.

Remove apenas o prefixo PDF literal \\22641 das sete linhas numeradas,
atualiza /Length do stream e reconstrói os offsets xref. Não reescreve
outros objetos, fontes, links, textos ou geometria. Rejeita outra fonte.
"""
from pathlib import Path
import hashlib,re,json,argparse
from pypdf import PdfReader

SOURCE_SHA256='7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b'

def correct(source,output,evidence):
    original=source.read_bytes()
    if hashlib.sha256(original).hexdigest()!=SOURCE_SHA256:
        raise ValueError('Fonte inesperada: SHA-256 não corresponde à v0.4.0 auditada')
    reader=PdfReader(source,strict=True)
    assert len(reader.pages)==5
    assert reader.pages[3].raw_get('/Contents').idnum==12
    assert len(reader.xref)==2 and set(reader.xref[0])==set(range(1,16))
    starts=[reader.xref[0][i] for i in range(1,16)]
    xref_start=int(re.search(rb'startxref\s+(\d+)\s+%%EOF',original).group(1))
    boundaries=starts+[xref_start]
    objects={i:original[boundaries[i-1]:boundaries[i]] for i in range(1,16)}
    obj=objects[12]
    prefix=b'\\22641 '
    assert obj.count(prefix)==7
    for n in range(1,8):
        assert obj.count(b'('+prefix+str(n).encode()+b'. ')==1
    assert original.count(prefix)==7
    old_stream=reader.pages[3].get_contents().get_data()
    new_obj=obj.replace(prefix,b'')
    length=re.search(rb'/Length\s+(\d+)',obj)
    assert length and b'/Filter' not in obj
    new_length=int(length.group(1))-7*len(prefix)
    new_obj=re.sub(rb'(/Length\s+)\d+',lambda m:m[1]+str(new_length).encode(),new_obj,count=1)
    objects[12]=new_obj
    body=bytearray(original[:starts[0]])
    offsets={}
    for i in range(1,16):
        offsets[i]=len(body);body.extend(objects[i])
    new_xref=len(body)
    trailer=original[xref_start:]
    assert trailer.startswith(b'xref\n0 16\n')
    lines=trailer.splitlines(keepends=True)
    for i in range(1,16):
        assert re.fullmatch(rb'\d{10} 00000 n \s*',lines[i+2])
        lines[i+2]=f'{offsets[i]:010d} 00000 n \n'.encode()
    trailer=b''.join(lines)
    trailer=re.sub(rb'(startxref\s+)\d+',lambda m:m[1]+str(new_xref).encode(),trailer,count=1)
    result=bytes(body)+trailer
    output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(result)
    corrected=PdfReader(output,strict=True)
    assert len(corrected.pages)==5
    for i in range(5):
        a=reader.pages[i];b=corrected.pages[i]
        if i==3:
            assert b.get_contents().get_data()==old_stream.replace(prefix,b'')
            assert b.extract_text()==a.extract_text().replace('–41 ','')
        else:
            assert a.get_contents().get_data()==b.get_contents().get_data()
            assert a.extract_text()==b.extract_text()
        assert a.mediabox==b.mediabox
    for i in range(1,16):
        end=corrected.xref[0][i+1] if i<15 else new_xref
        changed=result[corrected.xref[0][i]:end]!=original[boundaries[i-1]:boundaries[i]]
        assert changed==(i==12)
    report={'finding':'CNQ-VIS-006-01','source_sha256':SOURCE_SHA256,
      'corrected_sha256':hashlib.sha256(result).hexdigest(),'corrected_bytes':len(result),
      'removed_prefix_pdf_literal':'\\22641 ','removed_occurrences':7,
      'changed_objects':[12],'changed_pages':[4],'all_other_objects_byte_identical':True,
      'changes_infrastructure':['Length of page 4 content stream','xref offsets and startxref'],
      'all_text_unchanged_except_prefix':True,'original_generator_available':False,
      'method':'Surgical stream repair; rebuild xref; verify with strict pypdf parser'}
    evidence.parent.mkdir(parents=True,exist_ok=True)
    evidence.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('source',type=Path);parser.add_argument('output',type=Path);parser.add_argument('evidence',type=Path)
    args=parser.parse_args();correct(args.source,args.output,args.evidence)
