# Laboratory Activity #3: Working with JSON

This activity involves integrating an external API (JSONPlaceholder) to retrieve and manipulate data. The goal is to familiarize yourself with JSON as a data format, parse JSON strings, and convert Python data structures into valid JSON.

---

## Objectives
- Familiarize and identify JSON as a primary data format for API development.
- Parse JSON strings and traverse data in the JSON string using Python.
- Convert Python data structures into a valid JSON format.

---

## Instructions
1. Clone the GitHub repository: [https://github.com/jpcanamaque/itec116_it4e_lab](https://github.com/jpcanamaque/itec116_it4e_lab).
2. Go to the `lab3` folder, create your `.venv`, and install the pip packages inside the folder.
3. Create a new API with the following specifications:
   - Endpoint: `/detailed_post/{userID}`
   - Method: `GET`
   - Given the `userID`, show all posts of that specific user and all comments per post.
   - Use appropriate key names based on the value to be outputted.

---

## Endpoints

### 1. GET /posts/
Retrieves all posts or a specific post by `postId`.

**Example Request:**