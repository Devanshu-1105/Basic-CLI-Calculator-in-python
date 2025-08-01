

---

### ✅ `README.md`

````markdown
# 🧮 Basic CLI Calculator in Python

This is a simple command-line calculator built in Python that performs basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.

It uses the `match-case` construct (introduced in Python 3.10) to mimic switch-case behavior, along with proper exception handling for input errors.

---

## 🚀 Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Input validation with error handling
- Default case for unsupported operations

---

## 🛠 Requirements

- **Python 3.10+**  
  This project uses `match-case`, which is only available in Python 3.10 and above.

---

## 📦 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/calculator-cli.git
   cd calculator-cli
````

2. Run the script:

   ```bash
   python calculator.py
   ```

3. Follow the prompts in the terminal.

---

## 💻 Example Usage

```bash
Enter a number: 5
Enter a number: 3
What operation do you want to perform?: Addition + 
 Subtraction - 
 Division / 
 Multiplication * 
Enter the operation: *
The result is 15
```

---

## ⚠️ Error Handling

* Invalid numeric input (e.g., typing letters) will trigger an error message.
* Division by zero is not specifically handled but can be added easily.
* An unsupported operation symbol triggers the default case.

---

## 📁 File Structure

```
calculator-cli/
├── calculator.py
└── README.md
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Contributing

Feel free to fork the repo, make improvements, and submit a pull request! For major changes, please open an issue first to discuss what you'd like to change.

---

## ⭐️ Happy Coding!
