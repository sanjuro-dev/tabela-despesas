# Spending's Table

A desktop application designed to track and visualize personal expenses. This tool provides a user-friendly GUI to log expenditures and generates insightful charts to analyze spending habits over time.

## Features

* **Graphical User Interface (GUI)**: Built with `tkinter`, featuring a clean layout and high-readability fonts.
* **Persistent Storage**: Automatically manages an Excel database (`data.xlsx`) to save your records.
* **Smart Input**:
    * **Categories**: Pre-defined dropdown menu (Energy, Wi-Fi, Transport, Food, Leisure).
    * **Formatting**: Automatically handles decimal commas/dots for financial values.
* **Data Visualization**:
    * **Distribution**: A pie chart showing the percentage of spending per category for the current month.
    * **Trends**: A bar chart displaying total spending for every month of the current year.
* **Automated Initialization**: The system detects if the database exists on startup and creates it if necessary.

##Project Structure

The project is divided into two main modules:

1.  **`main.py`**: Handles the UI logic, window rendering, and widget placement using a custom `Field` class for consistent styling.
2.  **`dataframe.py`**: Contains the backend logic, including Excel manipulation via `pandas` and chart generation via `matplotlib`.

## ## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install pandas matplotlib openpyxl
```

*Note: `tkinter` is usually included with standard Python installations.*

##How to Use

1.  **Launch the App**: Run the main script:
    ```bash
    python main.py
    ```
2.  **Log an Expense**:
    * Select a **Category** from the dropdown.
    * Enter a **Description** (e.g., "Grocery Store").
    * Input the **Value** (numbers only).
    * Click **Add**.
3.  **Analyze Data**:
    * Click **Generate Data** to open a window with the Pie and Bar charts.

## ## Technical Details

* **Backend**: `pandas` for data framing and `openpyxl` for Excel engine support.
* **Charts**: `matplotlib` with a dual-subplot configuration (1x2).
* **Styling**: Uses the `clam` theme for `ttk` widgets and custom high-resolution font settings (Helvetica 25) for accessibility.

---
