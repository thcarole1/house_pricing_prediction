# house_pricing_prediction

# Housing price prediction : The big picture
Welcome to the Machine Learning Housing Corporation!

Our task is to build a model using California census data to predict housing prices.

The data includes details like population, median income, and housing prices for small areas called block groups (or "districts"), which usually have 600–3,000 people.

Our model will use this data **to predict the median housing price** in a district based on other metrics.

## Framing the problem
### What is the business objective is?
The goal isn’t just to build a model but to understand how the company plans to use it and benefit from it.


Knowing the objective helps **define the problem**, **choose algorithms**, **select a performance measure**, and **decide how much effort to spend improving the model**.


In our current project, our model’s predictions (median housing prices) will be used by another system, alongside other data, to decide if investing in an area is worthwhile. <br>

**This decision is crucial as it impacts revenue.**

### What is the current solution (if it exists) ?
Understanding it can provide a **performance baseline** and **ideas for solving the problem**.

In our corporation, housing prices are **<span style="font-family:Comic Sans MS; color:red">currently estimated manually</span>** by experts who gather district data and use complex rules when the median price isn’t available. This process is **<span style="font-family:Comic Sans MS; color:red">expensive</span>**, **<span style="font-family:Comic Sans MS; color:red">slow</span>**, and **<span style="font-family:Comic Sans MS; color:red">often inaccurate—estimates</span> are <span style="font-family:Comic Sans MS; color:red"> frequently off by over 30%</span>**.


The company wants <ins>to train a model to predict median housing prices using district data</ins>. <br>

Census data, which includes prices and other district information for thousands of areas, is ideal for this task.

### What is the type of learning ?
With the gathered information, we are ready to design our system.

- This is a **supervised learning task** because the model can train on labeled examples (districts with their median housing prices).

- It’s a **regression task** since the goal is to predict a value. Specifically, it’s a **multiple regression** problem because the prediction uses several features (like population and median income).

- It’s **univariate regression** because only one value (median price) is predicted for each district. If multiple values were predicted, it would be multivariate regression.
- Since the data is not continuously flowing, doesn’t require rapid updates, and fits in memory, **batch learning** is sufficient.

## Selecting a performance measure
The next step is to choose a performance measure. <br>

For regression problems, a common choice is the **root mean square error (RMSE)**.<br>

It shows how much error the model typically makes, giving more weight to larger errors.

# Let's go !
