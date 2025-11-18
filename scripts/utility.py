import pycountry
import matplotlib.pyplot as plt
import seaborn as sns

def check_and_clean_dataset(df):
    """
    Performs a final data quality check and basic cleaning on a DataFrame.

    Steps performed:
    1. Checks for missing values in each column and prints a summary.
    2. Displays unique values for categorical columns:
       - experience_level
       - employment_type
       - company_size
       - remote_ratio
    3. Prints salary statistics and the min/max range for 'salary_in_usd'.
    4. Validates ISO country codes for 'employee_residence' and 'company_location',
       allowing 'Kosovo' as a special case.
    5. Identifies and prints any duplicate rows.
    6. Removes duplicate rows and prints the new dataset shape.
    7. Displays the final shape of the dataset and data types of each column.

    Parameters:
    df (pandas.DataFrame): Input dataset to be checked and cleaned.

    Returns:
    pandas.DataFrame: Cleaned dataset with duplicates removed.
    """

    print("\n" + "-" * 40)
    print("        FINAL DATA QUALITY CHECK")
    print("-" * 40 + "\n")

    # Missing values
    missing_summary = df.isnull().sum()
    if missing_summary.sum() > 0:
        print("✅ Missing values per column:")
        print(missing_summary[missing_summary > 0])
    else:
        print("✅ No missing values found in any column.")

    # Unique values for categorical columns
    print("\n✅ Unique values for categorical columns:")
    for col in ['experience_level', 'employment_type', 'company_size', 'remote_ratio']:
        print(f"🔹 {col}: {df[col].unique()}")

    # Salary ranges and stats
    print("\n✅ Salary (USD) statistics:")
    print(f"🔹 Range: {df['salary_in_usd'].min()} to {df['salary_in_usd'].max()}")
    print(f"🔹 Summary:\n{df['salary_in_usd'].describe()}")

    # Country code validation
    valid_codes = [c.alpha_2 for c in pycountry.countries]

    invalid_residences = [code for code in df['employee_residence'].unique()
                          if code not in valid_codes and code != 'Kosovo']
    invalid_locations = [code for code in df['company_location'].unique()
                         if code not in valid_codes and code != 'Kosovo']

    if invalid_residences:
        print("\n⚠️ Invalid employee residence codes:", invalid_residences)
    else:
        print("\n✅ All employee residence codes are valid.")

    if invalid_locations:
        print("⚠️ Invalid company location codes:", invalid_locations)
    else:
        print("✅ All company location codes are valid.")

    # Remove duplicates
    duplicates_count = df.duplicated().sum()
    print(f"\n✅ Total duplicates found: {duplicates_count}")

    df_cleaned = df.drop_duplicates()
    print(f"✅ Duplicates removed. New dataset shape: {df_cleaned.shape}")

    # Final shape & dtypes
    print("\n✅ Final dataset shape:", df_cleaned.shape)
    print("\n✅ Column data types:")
    print(df_cleaned.dtypes)

    return df_cleaned


def plot_top_countries_salary(df, top_n = 10):
    """
    Plots the top N countries by number of reported salaries and their average salary in USD.
    
    Parameters:
    - df: pandas DataFrame containing at least 'employee_residence' and 'salary_in_usd' columns
    - top_n: int, number of top countries to consider (default 10)

    Returns
    -------
    fig, (ax1, ax2) : tuple
        Figure and axes objects for optional further customization.
    """

    # Identify top N countries by number of reported salaries
    top_countries_counts = df['employee_residence'].value_counts().nlargest(top_n)
    top_countries = top_countries_counts.index.tolist()

    # Calculate average salary (USD) only for those top countries
    top_avg_salary = (
        df[df['employee_residence'].isin(top_countries)]
        .groupby('employee_residence', observed = True)['salary_in_usd']
        .mean()
        .loc[top_countries]
        .sort_values(ascending=False))

    # Print key insights
    print(f"🌍 Top {top_n} countries by number of reported salaries:")
    print(top_countries_counts)
    print(f"\n💵 Average salary (USD) for those top {top_n} countries:")
    print(top_avg_salary)

    # Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Bar plot: number of reports per country
    sns.barplot(
        x = top_countries_counts.values,
        y = top_countries_counts.index.astype(str),
     	hue = top_countries_counts.index,
        order = top_countries,
    	palette = "deep",  
        ax = ax1)

    # Set title and labels
    ax1.set_title(f"Top {top_n} Countries by Report Count", fontsize = 14, fontweight = 'bold')
    ax1.set_xlabel("Number of Reports")
    ax1.set_ylabel("Country")
    sns.despine(ax = ax1, top=True, right=True)

    # Bar plot: average salary (USD) per country
    sns.barplot(
        x = top_avg_salary.values,
        y = top_avg_salary.index,
    	hue = top_avg_salary.index.astype(str),
        order = top_avg_salary.index,
    	palette = "vlag",
        ax = ax2)

    # Set title and labels
    ax2.set_title(f"Average Salary (USD) in Top {top_n} Countries", fontsize = 14, fontweight = 'bold')
    ax2.set_xlabel("Average Salary (USD)")
    ax2.set_ylabel("Country")
    sns.despine(ax = ax2, top=True, right=True)

    return fig, (ax1, ax2)




def plot_yearly_salary_trends(df):
    """
    Plots two side-by-side line charts:
    1. Number of salary records per year.
    2. Average reported salary per year (USD).

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain 'work_year' and 'salary_in_usd' columns.

    Returns
    -------
    fig, (ax1, ax2) : tuple
        Figure and axes objects for optional further customization.
    """
    
    year_counts = df['work_year'].value_counts().sort_index()
    year_salary = df.groupby('work_year', observed=True)['salary_in_usd'].mean().sort_index()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 5))

    # --- Titles and labels ---
    ax1.set_title("Number of Salary Reports per Year", fontsize = 14, fontweight = 'bold')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Count of Records")
    ax1.grid(which = 'both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax1.minorticks_on()
    sns.despine(ax = ax1, top=True, right=True)
    
    ax2.set_title("Average Reported Salary (USD) per Year", fontsize = 16, fontweight = 'bold', pad = 15)
    ax2.set_xlabel("Year", fontsize = 12)
    ax2.set_ylabel("Average Salary (USD)", fontsize = 12)
    ax2.grid(which = 'both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax2.minorticks_on()
    sns.despine(ax = ax2, top=True, right=True)
    
    
    # Plot basic lines
    ax1.plot(year_counts.index, year_counts.values, marker = "o", linewidth = 2)
    ax2.plot(year_salary.index, year_salary.values, marker = "s", linewidth = 2)

    return fig, (ax1, ax2)