from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    with open("suspicious.log") as f:
        logs = f.readlines()
    logs = logs[-50:]  # Show last 50 alerts
    return render_template_string("""
        <html><body>
        <h2>Net Watchdog Alerts</h2>
        <pre>{{ logs }}</pre>
        </body></html>
    """, logs="".join(logs))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)