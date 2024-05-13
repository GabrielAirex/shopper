from flask import Flask, jsonify

app = Flask(__name__)

events = [
    {
        "id": "evt-888999000",
        "timestamp": "2024-04-30T12:15:00Z",
        "text": "A bicicleta é perfeita para trilhas, muito resistente e bem equipada. Recomendo!",
        "sentiment": {"score": 0.92, "label": "positivo"},
        "product": {"id": "prod-667788990", "name": "Bicicleta Mountain Bike"},
        "user": {"id": "usr-123456789", "username": "trailblazer"},
        "source": "Facebook"
    },
    {
        "id": "evt-999000111",
        "timestamp": "2024-05-01T08:00:00Z",
        "text": "Incrível como essa luminária mudou o ambiente do meu escritório, iluminação perfeita para leitura!",
        "sentiment": {"score": 0.97, "label": "positivo"},
        "product": {"id": "prod-223344556", "name": "Luminária de Mesa LED"},
        "user": {"id": "usr-234567890", "username": "bookworm"},
        "source": "Instagram"
    },
    {
        "id": "evt-000111222",
        "timestamp": "2024-05-02T18:45:00Z",
        "text": "A mesa de vidro chegou com um arranhão visível. Esperava mais cuidado no transporte.",
        "sentiment": {"score": 0.40, "label": "negativo"},
        "product": {"id": "prod-112233445", "name": "Mesa de Centro Moderna"},
        "user": {"id": "usr-345678901", "username": "designlover"},
        "source": "Twitter"
    },
    {
        "id": "evt-111222333",
        "timestamp": "2024-05-03T17:30:00Z",
        "text": "Excelente jaqueta, resistente à água como prometido e muito confortável para caminhadas longas.",
        "sentiment": {"score": 0.89, "label": "positivo"},
        "product": {"id": "prod-778899001", "name": "Jaqueta Impermeável"},
        "user": {"id": "usr-456789012", "username": "hikemaster"},
        "source": "Instagram"
    },
    {
        "id": "evt-222333444",
        "timestamp": "2024-05-04T14:00:00Z",
        "text": "A mochila é bem espaçosa, mas as alças não são tão confortáveis para carregar peso.",
        "sentiment": {"score": 0.65, "label": "neutro"},
        "product": {"id": "prod-990011223", "name": "Mochila de Viagem"},
        "user": {"id": "usr-567890123", "username": "traveljunkie"},
        "source": "Reddit"
    }
]


@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
