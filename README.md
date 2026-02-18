<h1 align="center">🏧 ATM Simulator (Python)</h1>

<p align="center">
A simple command-line ATM simulation built using Python.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🔐 PIN authentication with 3 attempts</li>
  <li>💰 Balance inquiry</li>
  <li>➕ Deposit money</li>
  <li>➖ Withdraw money with insufficient funds check</li>
  <li>🚫 Account blocking after failed PIN attempts</li>
  <li>🖥️ Menu-driven interface</li>
</ul>

<hr>

<h2>📋 How It Works</h2>
<ol>
  <li>User sets an initial balance and PIN.</li>
  <li>User must enter the correct PIN (max 3 attempts).</li>
  <li>After successful login, ATM menu appears.</li>
  <li>User can perform banking operations until choosing Exit.</li>
</ol>

<hr>

<h2>🧠 Concepts Used</h2>
<ul>
  <li><code>while</code> loops</li>
  <li><code>if-elif-else</code> conditions</li>
  <li>Nested loops</li>
  <li>User input handling</li>
  <li>Basic state management</li>
</ul>

<hr>

<h2>▶️ How to Run</h2>

<h3>✅ Requirements</h3>
<ul>
  <li>Python 3.x installed</li>
</ul>

<h3>🔧 Steps</h3>

<pre><code># Clone the repository (if using git)
git clone &lt;your-repo-link&gt;

# Navigate to project folder
cd atm-simulator

# Run the program
python atm_simulator.py
</code></pre>

<hr>

<h2>🖥️ Sample Output</h2>

<pre><code>Welcome to the ATM Simulator
Enter your initial balance: 5000
Set your PIN: 1234
Enter your PIN: 1234

*** ATM MENU ***
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
</code></pre>

<hr>

<h2>⚠️ Limitations</h2>
<ul>
  <li>❌ No data persistence (balance resets after program ends)</li>
  <li>❌ No input validation for non-numeric values</li>
  <li>❌ Single user only</li>
  <li>❌ PIN stored in plain variable (not secure for real systems)</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>✅ Add file/database storage</li>
  <li>✅ Add multiple user accounts</li>
  <li>✅ Add input validation</li>
  <li>✅ Mask PIN input</li>
  <li>✅ GUI version using Tkinter</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p><strong>Darshan</strong></p>
