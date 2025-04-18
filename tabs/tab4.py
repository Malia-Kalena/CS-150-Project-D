from dash import html
import dash_bootstrap_components as dbc

def tab4_layout():
    faqs = [
        {
            "question": "Is this real science? 🔬🧪",
            "answer": "Yes. Next question.",
        },
        {
            "question": "What if I'm sad even after 12 hours of screen time?",
            "answer": "Turn your brightness up! 🔆",
        },
        {
            "question": "Did you even account for confounding variables? 👀",
            "answer": "No, but the vibes are ✨statistically significant✨",
        },
        {
            "question": "How accurate is your prediction model?",
            "answer": "It's emotionally accurate, which what truly matters. 🤷‍♀️",
        },
        {
            "question": "Was this peer-reviewed? 👥",
            "answer": "Yes, by our group chat 💬",
        }
    ]

    cards = []
    for faq in faqs:
        card = dbc.Card(
            [
                dbc.CardHeader(html.H5(f"Q: {faq['question']}")),
                dbc.CardBody(html.P(f"A: {faq['answer']}"))
            ],
            className="mb-3"
        )
        cards.append(card)

    return dbc.Container(
        [
            html.H3("🧾 FAQ (For Academic Integrity)"),
            html.P("Because transparency is key!",
                style={"fontStyle": "italic", "color": "gray"}
            ),
            *cards
        ],
        fluid=True,
        className="mt-4"
    )

