# 💙 Job Salaries in 2025

Analyze **global salary trends in Data Science, Machine Learning, and AI jobs** from 2020 to 2025.  

In this notebook, we perform exploratory data analysis (EDA) on a global salary dataset for roles in AI, Machine Learning, and Data Science, covering the years 2020–2025. We will examine key trends such as:

- How salaries varies by experience level
- Geographic patterns in pay
- The impact of remote work ratio
- Company size effects on salaries

---

## 💡 About the Dataset

This dataset contains real-world salary data for Data Science, AI, and ML roles, collected from kaggle.com

**Key columns:**

| Column               | Description |
|---------------------|-------------|
| `work_year`          | Year salary was reported (2020–2025) |
| `experience_level`   | Seniority level: EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type`    | Contract type: FT (Full-time), PT (Part-time), CT (Contract), FL (Freelance) |
| `job_title`          | Specific role title (e.g., Data Scientist, ML Engineer, AI Specialist |
| `salary`             | Gross annual salary in the original currency (before taxes) |
| `salary_currency`    | Original currency (e.g., USD, EUR, INR) |
| `salary_in_usd`      | Salary converted to USD using 2025 exchange rates |
| `employee_residence` | Employee’s country (ISO 3166-1 alpha-2 code) |
| `remote_ratio`       | Remote work percentage: 0 = On-site, 50 = Hybrid, 100 = Fully remote |
| `company_location`   | Company headquarters country (ISO 3166-1 alpha-2 code)|
| `company_size`       | Company size: S (1–50), M (51–500), L (501+ employees) |


##  📊 Exploratory Data Analysis (EDA)

In this section, we dive into the Exploratory Data Analysis (EDA) of our global AI / Data Science salaries dataset. Our goal is to uncover patterns, trends, and anomalies in compensation — by experience level, geography, remote work, and more.

What we will explore:

- **Univariate analysis**:
  - `salary` → examine distribution and detect outliers
  - `experience_level` → analyze frequency and trends
  - `company_size` → check distributions across company sizes
  - `employment_type` → explore distribution of employment types

- **Outlier detection**:
  - `salary` → identify unusually high/low values and investigate validity

- **Bivariate relationships**:
  - `salary` vs `experience_level` → explore correlations
  - `salary` vs `remote_ratio` → analyze impact of remote work
  - `salary` vs `company_size` → check pay differences across company sizes

- **Geographic insights**:
  - `employee_residence` → map average salaries by country/region
  - `company_location` → compare pay across company locations

- **Time trends**:
  - `year` → track evolution of salaries and number of salary reports over time

## Project Structure

- `notebooks/` - Jupyter Notebook(s) for analysis
- `data/` - raw or sample datasets

- `scripts/` - helper Python scripts
