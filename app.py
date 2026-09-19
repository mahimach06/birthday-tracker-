<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Birthdays</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Birthdays</h1>

    <!-- Table of birthdays -->
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Month</th>
            <th>Day</th>
        </tr>
        {% for birthday in birthdays %}
        <tr>
            <td>{{ birthday[0] }}</td>
            <td>{{ birthday[1] }}</td>
            <td>{{ birthday[2] }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>Add a Birthday</h2>
    <form action="/" method="post">
        <input type="text" name="name" placeholder="Name" required>
        <input type="number" name="month" placeholder="Month" min="1" max="12" required>
        <input type="number" name="day" placeholder="Day" min="1" max="31" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>


