import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('university_student_data.csv')

st.title('Dashboard de Análisis de Estudiantes Universitarios')

  # Filtros
year_filter = st.sidebar.multiselect('Seleccionar Año', df['Year'].unique(), default=df['Year'].unique())
dept_filter = st.sidebar.multiselect('Seleccionar Departamento', df['Department'].unique(), default=df['Department'].unique())
term_filter = st.sidebar.multiselect('Seleccionar Término', df['Term'].unique(), default=df['Term'].unique())

  # Filtrar datos
filtered_df = df[(df['Year'].isin(year_filter)) & (df['Department'].isin(dept_filter)) & (df['Term'].isin(term_filter))]

  # KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Tasa de Retención Promedio', f"{filtered_df['Retention_Rate'].mean():.2f}%")
with col2:
    st.metric('Puntaje de Satisfacción Promedio', f"{filtered_df['Satisfaction_Score'].mean():.2f}")
with col3:
    st.metric('Total de Matrículas', int(filtered_df['Enrollments'].sum()))

  # Line Chart: Tendencias de Retención
st.subheader('Tendencias de Tasa de Retención')
retention_trend = filtered_df.groupby('Year')['Retention_Rate'].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(data=retention_trend, x='Year', y='Retention_Rate', ax=ax)
st.pyplot(fig)

  # Bar Chart: Satisfacción por Departamento
st.subheader('Satisfacción por Departamento')
satisfaction_dept = filtered_df.groupby('Department')['Satisfaction_Score'].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=satisfaction_dept, x='Department', y='Satisfaction_Score', ax=ax2)
st.pyplot(fig2)

  # Pie Chart: Distribución por Término
st.subheader('Matrículas por Término')
term_enroll = filtered_df.groupby('Term')['Enrollments'].sum()
fig3, ax3 = plt.subplots()
term_enroll.plot.pie(ax=ax3, autopct='%1.1f%%')
st.pyplot(fig3)
  