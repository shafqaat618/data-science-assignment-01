import pandas as pd

data = {
    'Name': ['Shafqaat Ahmad', 'Ahmed', 'Sana', 'Bilal', 'Hira', 'Usman'],
    'Section': ['A', 'A', 'B', 'B', 'A', 'B'],
    'City': ['Kamra', 'Attock', 'Kamra', 'Attock', 'Rawalpindi', 'Kamra'],
    'Marks': [85, 72, 91, 58, 79, 66],
}
dfOrbit = pd.DataFrame(data)
print('\nOriginal DataFrame:\n', dfOrbit)
print('\nMarks above 70:\n', dfOrbit[dfOrbit['Marks'] > 70])
print('\nMean marks per section:\n', dfOrbit.groupby('Section')['Marks'].mean())
dfOrbit['Grade'] = dfOrbit['Marks'].apply(lambda m: 'A' if m >= 80 else ('B' if m >= 60 else 'C'))
print('\nWith Grade:\n', dfOrbit)
print('\nSorted by marks:\n', dfOrbit.sort_values('Marks', ascending=False))
