import streamlit as st
import plotly.express as px
from calculators.class_emi import emi
from calculators.class_sip import sip

st.sidebar.title('Enter Required Fields')

option = st.sidebar.selectbox('Choose SIP or EMI Calculator',('EMI','SIP'))

if option == 'EMI':
    st.header('EMI Calculator')

    principal = st.sidebar.slider('Loan Amount (INR)', 100000, 10000000, step=50000)
    annual_rate = st.sidebar.slider('Rate of Interest (P.A.)', float(1), float(30), step=0.1)
    tenure_years = st.sidebar.slider('Loan Tenure (Yr)', 1, 25)

    emi_calculation = emi(principal,annual_rate,tenure_years)
    final_emi = emi_calculation.calculate_emi()

    months = tenure_years*12
    total_payment = final_emi*months
    interest = total_payment - principal

    st.markdown(f'Your Monthly EMI is: ₹ {final_emi}')
    st.markdown(f'Total Amount Paid: ₹ {total_payment:.2f}')
    st.markdown(f'Total Interest Paid: ₹ {interest:.2f}')

    st.markdown("### 📊 Loan Breakdown")

    data = {
    'Component': ['Principal', 'Interest'],
    'Amount': [principal, interest]
    }

    fig = px.pie(
        data,
        names='Component',
        values='Amount',
        color_discrete_sequence=['#2196F3', '#FFC107'],
        hole=0.3 
    )

    fig.update_traces(textfont_size=12)
    fig.update_layout(
        height=350, width=350,
        margin=dict(t=0, b=0, l=0, r=0),
        showlegend=True
    )

    chart_container = st.empty()
    with chart_container:
        st.plotly_chart(fig, use_container_width=False)

elif option == 'SIP':
    st.header('SIP Calculator')

    sip_amount = st.sidebar.slider("Monthly Investment (INR)", 500, 100000, step=500)
    rate = st.sidebar.slider("Expected Annual Return (%)", 1.0, 20.0, step=0.1)
    tenure = st.sidebar.slider("Investment Period (Years)", 1, 25)

    sip_calculation = sip(sip_amount,rate,tenure)
    final_amount = sip_calculation.calculate_sip()

    months = tenure*12
    total_invested = sip_amount*months
    returns = final_amount - total_invested

    st.markdown(f' Final Amount after {tenure} years is: ₹ {final_amount:.2f}')
    st.markdown(f'Total Invested amount is: ₹ {total_invested}')
    st.markdown(f'Estimated Returns: ₹ {returns:.2f}')

    st.subheader("📊 Investment Breakdown")

    data = {
        'Component': ['Invested Amount', 'Returns'],
        'Amount': [total_invested, returns]
    }

    fig = px.pie(
        data,
        names='Component',
        values='Amount',
        color_discrete_sequence=['#2196F3', '#FFC107'],
        hole=0.3
    )

    fig.update_traces(textfont_size=12)
    fig.update_layout(
        height=350, width=350,
        margin=dict(t=0, b=0, l=0, r=0),
        showlegend=True
    )

    chart_container = st.empty()
    with chart_container:
        st.plotly_chart(fig, use_container_width=False)

