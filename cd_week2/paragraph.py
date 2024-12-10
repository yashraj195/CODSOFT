p = input().strip()
if len(p) >1 and ' ' in p:
    if p[-1] in ['\t','\n','.']:
        print("Paragraph")
    else:
        print("not a paragraph")
