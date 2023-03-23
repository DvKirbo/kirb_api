from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

kirb_lore = [{
    'code':200,
    'status':'ok👌'
},
{
    'characters':[{
        'kirby':{
            'about':'bola rosa',
            '1ra aparicion':'Kirby adventure 1993 NES',
            'img_url':'https://static.wikia.nocookie.net/kirby/images/8/86/KRtDLD_Kirby.png/revision/latest?cb=20230214153003',
            'song': 'https://www.youtube.com/watch?v=3CS93CdMv_E'
            },
            },
        {
        'metal knight':{
            'about':'proveniente del mismo planeta de kirby busca acabar con la bola rosa',
            '1ra aparicion':'Kirby adventure 1993 NES',
            'img_url':'https://www.smashbros.com/assets_v2/img/fighter/meta_knight/main.png'
        }        
        }]
}
    ]

@app.route('/kirb_api')
def status():
    return jsonify (kirb_lore[0])

@app.route('/kirb_api/<ru>')
def rutas(ru):
    if ru == 'main':
        return jsonify(kirb_lore[1])
#if __name__ == '__name__':
app.run(debug=True)    