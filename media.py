# -*- coding: utf-8 -*-

import pandas as pd

df_semestre_01 = pd.read_csv('semestre_01.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_02 = pd.read_csv('semestre_02.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_03 = pd.read_csv('semestre_03.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_04 = pd.read_csv('semestre_04.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_05 = pd.read_csv('semestre_05.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_06 = pd.read_csv('semestre_06.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_07 = pd.read_csv('semestre_07.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])
df_semestre_08 = pd.read_csv('semestre_08.csv', sep=',', names=['Disciplina', 'Crédito', 'Nota'])

semestres = [df_semestre_01, df_semestre_02, df_semestre_03, df_semestre_04, df_semestre_05, df_semestre_06, df_semestre_07, df_semestre_08]
notas = 0.0
creditos = 0.0

for smt in semestres:
    print(smt)
    notas += (sum(smt['Crédito'] * smt['Nota']))
    creditos += sum(smt['Crédito'])
    print(round(notas/creditos, 2))
    print('\n')
