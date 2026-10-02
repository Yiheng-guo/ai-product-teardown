#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path

def audit(d):
    evidence={e['id']:e for e in d['evidence']}
    if len(evidence)!=len(d['evidence']):raise ValueError('duplicate evidence id')
    findings=[]
    for c in d['claims']:
        refs=c.get('evidence_ids',[])
        if not set(refs)<=set(evidence):findings.append({'claim':c['id'],'issue':'unknown evidence id'});continue
        if c['kind']=='confirmed':
            if not refs:findings.append({'claim':c['id'],'issue':'confirmed without evidence'})
            if c.get('behavior_claim') and not any(evidence[r]['type']=='observed_behavior' for r in refs):findings.append({'claim':c['id'],'issue':'marketing/docs cannot prove observed behavior'})
        if c['kind'] not in ('confirmed','inference','proposal','unknown'):raise ValueError('unknown claim kind')
    return {'status':'needs_review' if findings else 'linked','findings':findings,'limits':'Link/type audit only; does not semantically verify source support.'}
def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:
        result=audit(json.loads(a.input.read_text()))
        with a.output.open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
        return 0 if not result['findings'] else 2
    except (ValueError,KeyError,OSError) as e:print(e,file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
