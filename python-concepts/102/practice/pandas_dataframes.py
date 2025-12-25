import pandas as pd


def create_dataframe():
    """
    Dataframes can represent data sql style with manipulations
    Here we represent the scores of 3 students on 3 subjects
    :return: None
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(df)


def print_dataframe_stats():
    """
    Dataframe describe is more descriptive than numpy and Series describe methods
    It automatically provides formatted data with count, mean, median over 25, 50 and 75th quartiles
    :return: None
    """
    grades_dict = get_student_grades()
    # Set Option method is used for setting the precision
    pd.set_option("display.precision", 2)
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(df)
    print(df.describe())


def find_grade_by_student(student: str):
    """
    The default dataframe access is by column name, in this case student name is given to find matching results.
    :param student:
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Grades of given student: {df[student]}")
    print("*" * 25)
    print(f"Grades of student 3 : {df.stu3}")


def find_grade_by_index_value(subject: str):
    """
    The LOC attribute gets grades by index
    :param subject:
    :return: None
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Print {subject} scores for all available student data: \n {df.loc[subject]}")


def get_student_grades() -> dict[str, list[int]]:
    grades_dict = {
        "stu1": [86, 78, 89],
        "stu2": [56, 68, 79],
        "stu3": [87, 92, 100],
    }
    return grades_dict


def find_grade_by_index_position(position: int):
    """
    Integer Location(iloc) helps get data by position without knowing its custom value defined
    :param position: of the index
    :return: None
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Print position {position} scores for all available student data: \n {df.iloc[position]}")


def slice_by_row_select_specific_columns():
    """
    Slicing can be done to find subset of rows and columns. Comma in this example represents specific columns, and
    slice is by row to choose specific rows we are interested in. Here 3 rows Science, math, language will be
    returned.
    :return:
    """
    grades_dict = {
        "stu1": [86, 78, 89, 55],
        "stu2": [56, 68, 79, 67],
        "stu3": [87, 92, 100, 78],
        "stu4": [76, 88, 89, 76],
        "stu5": [97, 62, 78, 89],
    }
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language", "Coding"])
    print(df)
    selected_data = df.loc["Science":"Language", ['stu2', 'stu3']]
    print(selected_data)


def slice_by_column_select_specific_rows():
    """
    Slicing can be done to find subset of rows and columns. Comma represents non-contiguous rows, and slice
    for column to filter only columns we are interested in
    :return:
    """
    grades_dict = {
        "stu1": [86, 78, 89, 55],
        "stu2": [56, 68, 79, 67],
        "stu3": [87, 92, 100, 78],
        "stu4": [76, 88, 89, 76],
        "stu5": [97, 62, 78, 89],
    }
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language", "Coding"])
    print(df)
    selected_data = df.iloc[[0, 3], 1:2]
    print(selected_data)


def find_by_boolean_indexing():
    """
    We can also create custom dataframes by custom boolean conditions
    Any non-matching cells are filled with NaN
    Bitwise and (&) ampersand is used for dataframe conditions over python 'and', similarly | is used for OR condition.
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(df[(df >= 60) & (df <= 90)])


def find_by_cell_row_and_column():
    """
    The at and iat attributes help find specific cell values by row and column
    The `at` accepts custom indexes, and `iat` stands for integer-at, hence `iat` takes in integer row column positions.
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(df)
    cell_value = df.at['Science', 'stu2']
    print(f"The Cell Value for Science Score for student 2 is : {cell_value}")
    another_cell_value = df.iat[2, 2]
    print(f"The cell value for row 3 and column 3 is : {another_cell_value}")


def transpose_dataframe():
    """
    Transpose can be through T property on the dataframe or using transpose() method. Both are identical for basic
    2D use cases. However, for advanced usage where memory optimization or multidimensional operation is needed then
    transpose() offers more control. For simple Swap operations, T is the right choice.

    The attribute T creates a view on the data. Any change made on the view affects the parent dataframe.
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Before transpose: {df}")
    transposed_df = df.T
    print(f"After transpose: {transposed_df}")
    pd.set_option("display.precision", 2)
    print(transposed_df.describe())

def sorting_dataframe_by_index():
    """
    Dataframes can be sorted by index or by value
    Sorting by index is a simpler option to just order by ascending or descending
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Before sorting{df}")
    sorted_data = df.sort_index()
    print(f"After sorting{sorted_data}")

def sort_dataframes_by_values():
    """
    Sorting dataframes by value is a powerful option where we can identify patterns on data, and sort them
    For example, who performed the best on a specific test and order by that column
    :return:
    """
    grades_dict = get_student_grades()
    df = pd.DataFrame(grades_dict, index=["Science", "Math", "Language"])
    print(f"Before sorting{df}")
    df.sort_values(by=["Math", "Language"], axis=1, ascending=False, inplace=True)
    print(f"After sorting{df}")

    # Sort values by index and condition
    math_df=df.loc['Math'].sort_values(ascending=False, inplace=False)
    print(f"Sorted by Math: {math_df}")

    # Transposed values can also be sorted
    transposed_sorted_df = df.T.loc['stu1'].sort_values(ascending=False, inplace=False)
    print(f"Sorted by Student Scores: {transposed_sorted_df}")



def final_practice():
    temps = {
        'Mon': [68, 89],
        'Tue': [71, 93],
        'Wed': [66, 82],
        'Thu': [75, 97],
        'Fri': [62, 79],
    }
    temperatures = pd.DataFrame(temps, index=["Low", "High"])
    print(temperatures)
    print("Only select columns from monday to wednesday")
    print(temperatures.loc[:, "Mon":"Wed"]) # slice notation specifies all rows
    print("Using row index Low, select only low temperatures for each day")
    lowest_temp = temperatures.loc["Low"].sort_values(ascending=True, inplace=False)
    print(lowest_temp)
    print("Stats for temperatures")
    pd.set_option("display.precision", 2)
    print(temperatures.describe())
    print("Average of low and high temperatures")
    print(temperatures.mean(axis=1))

if __name__ == '__main__':
    create_dataframe()
    print_dataframe_stats()
    find_grade_by_student("stu1")
    find_grade_by_index_value("Math")
    find_grade_by_index_position(2)
    slice_by_row_select_specific_columns()
    slice_by_column_select_specific_rows()
    find_by_boolean_indexing()
    find_by_cell_row_and_column()
    transpose_dataframe()
    sorting_dataframe_by_index()
    sort_dataframes_by_values()
    print("*"*25)
    final_practice()