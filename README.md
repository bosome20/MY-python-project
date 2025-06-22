 # 🎮 Gacha Simulator Project
 
 This project includes three Python simulators for exploring gacha pull mechanics and probabilities, covering basic pickup rate analysis, SSR performance comparisons, and off-banner SSR collection chances.
 
 ---
 
 ## 📦 Simulators Included
 
 ### 1. `gacha_simulator.py` — Basic Pickup Simulator
 
 - **Pickup Rate**: 0.7% per pull  
 - **Ceiling System**: 1 guaranteed pickup every 200 pulls  
 - **Outputs**:
   - Total pickups (natural vs. guaranteed)  
   - Percentile rank among simulated players
   - Input validation and retry loops  
 
 ---
 
 ### 2. `ssr_analyzer.py` — SSR Pull Analyzer
 
 - **SSR Rates**:
   - Normal gacha: 3%  
   - Festival gacha: 6%  
 - **Outputs**:
   - Percentile rank among simulated players   
   - Histogram of the results
   - Input validation and retry loops
 
 ---
 
 ### 3. `offbanner_analyzer.py` — Off-Banner SSR Analyzer
 
 - **SSR Rate**: Normal (3%) or Festival (6%), minus 0.7% pickup = off-banner rate  
 - **Pool Size**: 114 equally likely off-banner SSRs  
 - **Outputs**:
   - Probability of collecting **all** _k_ desired off-banners in _n_ pulls (simulated over 100,000 players)  
   - Expected number of pulls to complete the set (simulated)  
   - Progress bar via `tqdm` and input validation  
 
 ---
 
 ## 🧪 Key Features
 
 - **100,000-player simulations** for accurate probability estimates  
 - **`tqdm` progress bars** for long-running loops  
 - **Input validation** (non-negative integers, logical constraints)  
 - **Retry loops** on invalid input, clean exit options  
 - **Separate, focused scripts** for each analysis type  
 
 ---
 
 ## 📁 Folder Structure
 
 
 ```plaintext
 VS python project/
 ├── gacha_simulator.py
 ├── ssr_analyzer.py
 ├── offbanner_analyzer.py
 └── README.md
 ```
 
 
 ---
 
 
 ## 🔧 Installation
 
 1. Make sure **Python 3.7+** is installed.
 2. Install required packages:
 
    ```bash
    pip install tqdm matplotlib
    ```
 
 _No other dependencies required._
 
 **Notes:**
 - `tqdm` is used for progress bars during long simulations.  
 - `matplotlib` is required for the SSR histogram feature in `ssr_analyzer.py`.  
 - The standard library’s `random` module and built-in I/O require no additional installation.  
 
 ---
 
 ## 🕹️ Usage
 
 Run the desired script from your terminal:
 
 ```bash
 python gacha_simulator.py
 python ssr_analyzer.py
 python offbanner_analyzer.py
 ```
 
 Follow the on-screen prompts to enter:
 
 - Number of pulls  
 - Number of pickups/SSRs or desired off-banner count  
 
 Each tool will validate your input, simulate, and display results.
 
 ---
 
 ## 💡 Example Output
 
 ```plaintext
 🎲 Welcome to the Basic Gacha Luck Analyzer!
 
 🔢 Enter number of pulls you've done: 600
 ⭐ Enter total pickups you got (including guaranteed ones): 5
 
 📊 Simulating luck... please wait.
 🏅 You did better than or equal to 87.23% of players.
 
 🔁 Would you like to try another simulation? (y/n): n
 👋 Exiting Gacha Luck Analyzer. Goodbye!
 ```
 

 ```plaintext
 🎲 Welcome to the SSR Pull Analyzer!
 
 🎯 SSR Pull Analyzer
 Choose gacha mode - Normal (3% SSR) or Fes (6% SSR)? (normal/fes): fes
 🔢 Enter number of pulls you've done: 500
 ⭐ Enter number of SSRs you got: 12
 
 📊 Simulating luck... please wait.
 (100,000 simulations running)
 
 📈 Results:
 🎯 You got 12 SSRs out of 500 pulls.
 🏅 You did better than or equal to 91.32% of players in fes gacha.
 
 📉 Would you like to see a histogram of the results? (y/n): y

— A histogram window pops up showing the distribution of SSR counts, with a red dashed line at 12.

 🔁 Would you like to analyze another SSR pull? (y/n): n
 
 👋 Exiting SSR Pull Analyzer. Goodbye!
 ```
 
 
 ```plaintext
 🎯 Off-Banner SSR Collection Analyzer
 
 Choose gacha mode - Normal (3%) or Fes (6%)? fes
 🔢 Enter number of total pulls: 500
 ⭐ How many specific off-banner SSRs do you want to collect? (1-114): 3
 
 📊 Simulating 100,000 players... (this may take a few seconds)
 🎮 Running Simulations: 100%|████|100000/100000
 
 📈 Calculating expected pulls... (please wait)
 
 📈 Results:
 🎯 Probability of collecting all 3 off-banners in 500 pulls: 12.34%
 📉 Expected number of pulls to collect all 3 off-banners: 276 pulls
 ```
 
 ---
 
 
 ## 🙋 Author
 
 Created by **@bosome20**   (**Park jaemin**, a **second-year student** in the **Department of Mathematics** at **Yonsei University**.)

> “This project was developed with the assistance of ChatGPT and completed as the final project for the ‘MAT2014.01-00’ course.”