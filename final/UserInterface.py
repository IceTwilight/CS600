from flask import Flask, jsonify, request, Response
from SearchEngine import SearchEngine
from flask import render_template
import json
import re

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def search():
#     print request.args.get('key')
    if request.args.get('key') == None:
        html = render_template("search.html", ol=False, key=False)
    else:
        rank = None
        regex = re.compile('\s+')
        keywords = request.args.get('key')
        keylist = []
        odict = []
        for key in regex.split(keywords):
            if len(key) <= 2:
                badkey = {"KeyString": key, "This key is too short to search!":1}
                odict.append(badkey)
                continue
            else:
                result = se.getRecommendWebsite(key)
                if result:
                    outputAddress = "./output/" + key + ".txt"
                    write1 = open(outputAddress, "w")
                    for r in result:
                        keylist.append(r.keys())
                        odict.append(r)
                        s = json.dumps(r)
                        s = str(r)
                        ####        print(s)
                        write1.write(s + '\n')
                    write1.close()

                    ####    writeResult.writelines(se.getRecommendWebsite(keyString))


                else:
                    continue
            
        output = odict    
        if output:
            rank = output
            html = render_template("search.html", ol = output, rank = rank, key = keywords)
        else:
            html = render_template("search.html", ol = None, rank = None, key = False)

    return html

if __name__ == '__main__':
    se = SearchEngine()
    se.createTrie()
    app.run(debug=True, port=5000)

