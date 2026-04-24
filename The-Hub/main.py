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
        filtered = assignments
    else:
        filtered = [a for a in assignments if a["class"] == selected_class]

    # COUNTER
    total = len(filtered)
    completed = len([a for a in filtered if a["done"]])

    return render_template(
        "assignments.html",
        assignments=filtered,
        total=total,
        completed=completed,
        selected_class=selected_class
    )


@app.route("/complete/<int:index>")
def complete(index):
    if 0 <= index < len(assignments):
        assignments[index]["done"] = True
    return redirect("/assignments")


@app.route("/internships", methods=["GET", "POST")
def internships():
    global internships
     if request.method == "POST":
    job = request.forms["job"]
    
    
        internships.append({
            "job": job,
            "applied":False
            "accepted": False
        })

        return redirect("/internships")

    return render_template("internships.html")


if __name__ == "__main__":
    app.run(debug=True)
