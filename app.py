import streamlit as st

def calculate_tax_new_regime(income, agri_income):
    total_income_for_rate = income + agri_income

    slabs = [
        (300000, 0.0),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    tax = 0
    prev_limit = 0

    for limit, rate in slabs:
        if total_income_for_rate <= limit:
            tax += max(0, income - prev_limit) * rate
            break
        else:
            slab_taxable = min(income, limit) - prev_limit
            if slab_taxable > 0:
                tax += slab_taxable * rate
            prev_limit = limit

    cess = tax * 0.04
    total_tax = tax + cess
    return income, tax, cess, total_tax

st.title("🧾 Indian Senior Citizen Income Tax Calculator (New Regime)")

st.markdown("""
Calculate your total taxable income including salary, mutual funds, shares (capital gains), interest income, and agricultural income.
Agricultural income is exempt but included for rate calculation.
""")

age = st.number_input("Enter your age (must be 60 or above)", min_value=60, max_value=120, value=65, step=1)

if age < 60:
    st.warning("This calculator is designed for senior citizens aged 60 or above.")
else:
    salary = st.number_input("Salary Income (₹)", min_value=0, value=0, step=1000)
    mutual_funds = st.number_input("Mutual Funds Income (₹)", min_value=0, value=0, step=1000,
                                   help="Include dividends or capital gains from mutual funds")
    shares = st.number_input("Shares/Capital Gains Income (₹)", min_value=0, value=0, step=1000,
                             help="Short-term and long-term capital gains from shares")
    interest = st.number_input("Interest Income (₹)", min_value=0, value=0, step=1000,
                               help="Interest from savings, fixed deposits, bonds etc.")
    agri_income = st.number_input("Agricultural Income (₹)", min_value=0, value=0, step=1000,
                                 help="Agricultural income is exempt but added for slab rate calculation")

    total_income = salary + mutual_funds + shares + interest

    taxable_income, tax, cess, total_tax = calculate_tax_new_regime(total_income, agri_income)

    st.subheader("Tax Calculation (New Regime)")
    st.write(f"Total Taxable Income (excluding agricultural income): ₹{taxable_income:,.2f}")
    st.write(f"Agricultural Income (exempt but included for rate calc): ₹{agri_income:,.2f}")
    st.write(f"Tax Before Cess: ₹{tax:,.2f}")
    st.write(f"Health & Education Cess (4%): ₹{cess:,.2f}")
    st.write(f"Total Tax Payable: ₹{total_tax:,.2f}")
