from app import app, server
from layout.time_viz.time_viz_callbacks import update_cumulative_count


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost")