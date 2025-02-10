def test_grade_calculation():
    from src.grade_analyzer import analyze_grades
    df = analyze_grades('data/sample_grades.csv')
    assert 'avg_grade' in df.columns
    assert df.avg_grade.mean() > 0