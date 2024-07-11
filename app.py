from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    todo = request.json
    todos.append(todo)
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id] = request.json
        return jsonify(todos[todo_id])
    return jsonify({"error": "Todo not found"}), 404


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todo = todos.pop(todo_id)
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
