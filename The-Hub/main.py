from flask import Flask, render_template, request, redirect

app = Flask(__name__)

assignments = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/assignments", methods=["GET", "POST"])
def assignments_page():
    global assignments

    # ADD assignment
    if request.method == "POST":
        title = request.form["title"]
        class_name = request.form["class_name"]

        assignments.append({
            "title": title,
            "class": class_name,
            "done": False
        })

        return redirect("/assignments")

    # FILTER
    selected_class = request.args.get("class", "all")

    if selected_class == "all":
        # Pass enumerate to template to keep track of original indices
        filtered = list(enumerate(assignments))
    else:
        filtered = [(i, a) for i, a in enumerate(assignments) if a["class"] == selected_class]

    # COUNTER
    total = len(assignments)
    completed = len([a for a in assignments if a["done"]])

    return render_template(
        "assignments.html",
        assignments=filtered,
        total=total,
        completed=completed,
        selected_class=selected_class
    )
@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(assignments):
        assignments[index]["done"] = not assignments[index]["done"]
    return redirect("/assignments")

@app.route("/complete/<int:index>")
def complete(index):
    if 0 <= index < len(assignments):
        assignments[index]["done"] = True
    return redirect("/assignments")


internships_list = []

@app.route("/internships", methods=["GET", "POST"])
def internships():
    global internships_list

    if request.method == "POST":
        job = request.form["job"]

        internships_list.append({
            "job": job,
            "applied": False,
            "accepted": False
        })

        return redirect("/internships")

    return render_template("internships.html", internships=internships_list)

@app.route("/apply/<int:index>")
def apply(index):
    if 0 <= index < len(internships_list):
        internships_list[index]["applied"] = True
    return redirect("/internships")

@app.route("/accept/<int:index>")
def accept(index):
    if 0 <= index < len(internships_list):
        internships_list[index]["accepted"] = True
    return redirect("/internships")

if __name__ == "__main__":
    app.run(debug=True, port=5007)
