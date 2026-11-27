from dash import Dash, dcc, html
import plotly.graph_objects as go

from main import build_market_snapshot


GRID_STYLE = {
    "display": "grid",
    "gridTemplateColumns": "repeat(auto-fit, minmax(min(100%, 180px), 1fr))",
    "gap": "1rem",
}
CARD_STYLE = {
    "backgroundColor": "#ffffff",
    "border": "1px solid #d7e0eb",
    "borderRadius": "0.75rem",
    "padding": "1rem",
    "minWidth": 0,
}


def comparison_figure(snapshot):
    figure = go.Figure()
    for role, color, dash_style in (
        ("instrument", "#096a72", "solid"),
        ("benchmark", "#6350a0", "dash"),
    ):
        series = snapshot[f"{role}_base_100"]
        ticker = snapshot[role]["ticker"]
        figure.add_trace(go.Scatter(
            x=[row["date"] for row in series],
            y=[row["value"] for row in series],
            mode="lines",
            name=ticker,
            line={"color": color, "width": 3, "dash": dash_style},
            hovertemplate="%{y:.2f}",
        ))
    figure.update_layout(
        template="plotly_white",
        font={"family": "system-ui, sans-serif", "color": "#15253b", "size": 14},
        xaxis={"title": "Date", "type": "date", "showgrid": False},
        yaxis={"title": "Base 100", "gridcolor": "#e3eaf2"},
        hovermode="x unified",
        legend={"orientation": "h", "y": 1.02, "yanchor": "bottom"},
        margin={"l": 60, "r": 20, "t": 52, "b": 60},
    )
    return figure


def performance_card(label, value):
    return html.Div([
        html.H2(label, style={"fontSize": "1rem", "margin": "0 0 0.5rem"}),
        html.P(value, style={"fontSize": "2rem", "fontWeight": 700, "margin": 0}),
    ], style=CARD_STYLE)


def dashboard_layout(snapshot):
    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]
    context = (
        ("Instrument", f"{instrument['ticker']} · {instrument['name']}"),
        ("Benchmark", f"{benchmark['ticker']} · {benchmark['name']}"),
        ("Lookback", snapshot["lookback"]),
        ("Interval", snapshot["interval"]),
    )
    return html.Main([
        html.Header([
            html.H1("MarketPulse", style={"margin": "0 0 0.3rem", "fontSize": "2.4rem"}),
            html.P(snapshot["provider"], style={"margin": 0, "color": "#d2e1f4"}),
            html.Dl([
                html.Div([
                    html.Dt(label, style={"color": "#d2e1f4", "fontSize": "0.9rem"}),
                    html.Dd(value, style={"margin": "0.25rem 0 0", "fontWeight": 600}),
                ])
                for label, value in context
            ], style={**GRID_STYLE, "margin": "1.4rem 0 0"}),
        ], style={
            "backgroundColor": "#142944", "color": "#ffffff",
            "padding": "1.5rem", "borderRadius": "0.75rem",
        }),
        html.Section([
            performance_card("Instrument return", f"{snapshot['instrument_return']:+.2f}%"),
            performance_card("Benchmark return", f"{snapshot['benchmark_return']:+.2f}%"),
            performance_card("Relative performance", f"{snapshot['relative_performance']:+.2f} pts"),
        ], style={**GRID_STYLE, "margin": "1rem 0"}),
        html.Section([
            html.H2("Instrument vs Benchmark · Base 100", style={"margin": "0 0 0.25rem"}),
            dcc.Graph(
                id="base-100-comparison",
                figure=comparison_figure(snapshot),
                config={"displaylogo": False},
                responsive=True,
                style={"height": "clamp(19rem, 45vh, 30rem)"},
            ),
        ], style=CARD_STYLE),
    ], style={
        "maxWidth": "70rem", "margin": "0 auto", "padding": "clamp(0.75rem, 3vw, 2rem)",
        "fontFamily": "system-ui, sans-serif", "color": "#15253b",
        "backgroundColor": "#f1f5fa", "borderRadius": "1rem",
    })


def create_app():
    app = Dash(__name__, title="MarketPulse")
    app.layout = dashboard_layout(build_market_snapshot())
    return app


if __name__ == "__main__":
    create_app().run(debug=False)
