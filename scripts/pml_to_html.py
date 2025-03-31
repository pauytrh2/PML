import re

def pml_to_html(pml):
    # <pml> to <html>
    html = re.sub(r'<pml>', '<html>', pml)
    html = re.sub(r'</pml/>', '</html>', html)

    # <t1> to <h1>
    html = re.sub(r'<t1.*?>', '<h1>', html)
    html = re.sub(r'</t1/>', '</h1>', html)

    # <t2> to <h2>
    html = re.sub(r'<t2.*?>', '<h2>', html)
    html = re.sub(r'</t2/>', '</h2>', html)

    # <t3> to <h3>
    html = re.sub(r'<t3.*?>', '<h3>', html)
    html = re.sub(r'</t3/>', '</h3>', html)

    # <t4> to <h4>
    html = re.sub(r'<t4.*?>', '<h4>', html)
    html = re.sub(r'</t4/>', '</h4>', html)

    # <t5> to <h5>
    html = re.sub(r'<t5.*?>', '<h5>', html)
    html = re.sub(r'</t5/>', '</h5>', html)

    # <img> to <img> tag and handle src attributes
    html = re.sub(r'<img>(.*?)</img/>', r'<img src=\1/>', html)

    # <dropdown> to <select>
    html = re.sub(r'<dropdown>\s*({.*?})\s*</dropdown/>', lambda match: 
                  '<select>' + ''.join([f'<option>{item.strip().strip("\"")}</option>' for item in match.group(1).strip('{}').split(',')]) + '</select>', html)

    return html

if __name__ == "__main__":
    pml = """
    <pml>
        <t1>hi</t1/>
        <t2>hi</t2/>
        <t3>hi</t3/>
        <t4>hi</t4/>
        <t5>hi</t5/>

        <img> "https://example.com/test.png" </img/>
        <img> "images/logo.png" </img/>

        <dropdown> {"I'm option 1", "I'm option 2 hihi"} </dropdown/>
    </pml/>
    """

    html = pml_to_html(pml)

    print(html)