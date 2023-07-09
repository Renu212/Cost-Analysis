import streamlit as st

import numpy as np
import pandas as pd


st.set_page_config(page_title='cost analysis')
original_title = '<p style="font-family:Inter; font-size: 60px;font-weight: bold;">Investment Cost Analysis</p>'
st.markdown(original_title, unsafe_allow_html=True)

page_bg_img1 = """
<style>
[data-testid="stAppViewContainer"]  {
 background-color: #b5d4ea;

}
[data-testid="stHeader"] {
 background-color: #b5d4ea ;
} 
</style>
"""

st.markdown(page_bg_img1,unsafe_allow_html=True)

box1,box2=st.columns(2)
with box1:
    st.subheader('Plant Equipment')
    machine,installation=st.columns(2)
    with machine:
        machine_equipment=st.text_input('enter Cost of Machinery and Equipment',value=0)
    with installation:
        installation_Setup=st.text_input('enter Cost of Installation and Setup',value=0)
    plant_equipment= float(machine_equipment) + float(installation_Setup)
    st.write('The total cost on Plant & Equipment is',plant_equipment)
with box2:
    st.subheader('Infrastructure')
    Construction_building,Utilities_services=st.columns(2)
    with Construction_building:
        construction=st.text_input('enter Cost of Construction and Building',value=0)
    with Utilities_services:
        utilities=st.text_input('enter Cost of Utilities and Services',value=0)
    Infrastructure= float(construction) + float(utilities)
    st.write('The total cost on Infrastructure is',Infrastructure)
box3,box4=st.columns(2)
with box3:
    st.subheader('Research and Development (R&D)')
    Laboratory,r_d =st.columns(2)
    with Laboratory:
        Laboratory_equipment=st.text_input('enter Cost of Laboratory Equipment',value=0)
    with r_d:
        r_d_expenses=st.text_input('enter the Cost of R&D Expenses',value=0)
    research= float(machine_equipment) + float(installation_Setup)
    st.write('The total cost on Plant & Equipment is',research)
with box4:
    st.subheader('Regulatory Compliance')
    st.write("")
    st.write("")
    Permits,Environmental =st.columns(2)
    with Permits:
        Permits_Licenses=st.text_input(' enter the  Cost of Permits and Licenses',value=0)
    with Environmental :
        Environmental_impact=st.text_input('enter  Cost of Environmental Impact Assessment',value=0)
    regulatory = float(Permits_Licenses) + float(Environmental_impact)
    st.write('The total cost on Plant & Equipment is',regulatory)
box5,box6=st.columns(2)
with box5:
    st.subheader('Raw Materials and Inventory')
    raw,storage =st.columns(2)
    with raw:
        raw_stock=st.text_input('enter the cost of Initial Raw Material Stock',value=0)
    with storage:
        storage_facilities=st.text_input('enter the Cost of Storage Facilities',value=0)
    inventory= float(raw_stock) + float(storage_facilities)
    st.write('The total cost on Plant & Equipment is',inventory)
with box6:
    st.subheader('Human Resources')
   

    Recruitment,salaries =st.columns(2)
    with Recruitment:
        Recruitment_Training=st.text_input(' enter the  Cost of Recruitment and Training',value=0)
    with salaries :
       Salaries_Benefits=st.text_input('enter  Cost of Salaries and Benefits (Year 1)',value=0)
    human_resources = float(Recruitment_Training) + float( Salaries_Benefits)
    st.write('The total cost on Plant & Equipment is',human_resources)
box7,box8=st.columns(2)
with box7:
    st.subheader('Marketing and Distribution')
    st.write("")
    st.write("")
    branding,sales=st.columns(2)
    
    with branding:
        brand_market=st.text_input('enter the cost of Branding and Marketing',value=0)
    with sales:
        sales_network=st.text_input('enter the Cost of Sales Network Development',value=0)
    st.write("")
    distribution=st.text_input('enter the Cost of Logistics and Distribution',value=0)
    marketing= float(brand_market) + float(sales_network)+float(distribution)
    st.write('The total cost on Plant & Equipment is',marketing)
with box8:
    st.subheader('Contingency and Miscellaneous Costs')
   
    Contingency,consulting=st.columns(2)
    insurance,capital=st.columns(2)
    with Contingency:
        Contingency_fund=st.text_input(' enter the  Cost of Contingency Fund',value=0)
    with consulting :
      consulting_fees=st.text_input('enter  Cost of Legal and Consulting Fees',value=0)
    with insurance:
        st.write("")
        insu=st.text_input(' enter the  Cost of Insurance',value=0)
    with capital :
       Working_Capital=st.text_input('enter  Cost of Working Capital',value=0)
    Contingency_Miscellaneous = float(Contingency_fund) + float( consulting_fees)+float(insu)+float(Working_Capital)
    st.write('The total cost on Plant & Equipment is',Contingency_Miscellaneous)


original_title = '<p style="font-family:Inter; font-size: 30px;font-weight: bold;">Total Investment</p>'
st.markdown(original_title, unsafe_allow_html=True)
total_investment = float(plant_equipment) + float(Infrastructure)+float(research)+float(regulatory)+float(inventory) + float(human_resources)+float(marketing)+float(Contingency_Miscellaneous)
st.write('The total Investment in dollars',total_investment)

box9,box10=st.columns(2)
with box9:
    
    st.subheader('Revenue')
    st.write("")

    
    sales_volume,selling_price=st.columns(2)
    with sales_volume:
        volume=st.text_input('enter Sales Volume',value=0)
    with selling_price:
        sellprice=st.text_input('enter selling price per ton',value=0)
    revenue= float(volume)*float(sellprice)
    st.write('The total revenue',revenue)
with box10:
    st.subheader('Cost Of Goods Sold(COGS)')
    raw_material,labor,manufacturing=st.columns(3)
    with raw_material:
        rawcost=st.text_input('enter Raw material Cost per ton',value=0)
    with labor:
        laborcost=st.text_input('enter Direct Labor Cost per ton',value=0)
    with manufacturing:
        overhead=st.text_input('enter Manufacturing Overhead per ton',value=0)

    cogs= float(volume)*(float(rawcost) + float(laborcost)+float(overhead))
    st.write('The total Cost Of Goods Sold',cogs)
st.subheader('Operating Expenses')
salaries_wages,rent,repairs,advertising,admin=st.columns(5)
with salaries_wages:
    wage=st.text_input('enter Salaries and Wages',value=0)
with rent:
    utilities=st.text_input('enter Rent and Utilities',value=0)
with repairs:
    maintenance=st.text_input('enter Maintenance and Repairs',value=0)
with advertising:
    market_advert=st.text_input('enter Marketing and Advertising',value=0)
with admin:
    admin_expense=st.text_input('enter Administrative Expenses',value=0)
operative= float(wage)+float(utilities) + float(market_advert)+float(admin_expense)
st.write('The total Operating Expenses',operative)
box11,box12=st.columns(2)
with box11:
    st.subheader('Depreciation and Amortization')
    depreciation,amortization=st.columns(2)
    with depreciation:
        depreciation_expense=st.text_input('enter Cost of Depreciation Expense',value=0)
    with amortization:
        amortization_expense=st.text_input('enter Cost of Amortization expense',value=0)
    depreciation_amortization= float(depreciation_expense) + float(amortization_expense)
    st.write('The total Depreciation and Amortization',depreciation_amortization)
with box12:
    st.subheader('Interest and Taxes')
    interest,tax=st.columns(2)
    with interest:
        interest_expense=st.text_input('enter Cost of Interest Expenses',value=0)
    with tax:
        st.write("")
        taxes=st.text_input('enter the Cost of Taxes',value=0)
        
    interest_taxes= float(interest_expense) + float(taxes)
    st.write('The total cost of Interest and Taxes',interest_taxes)

gross_profit=  revenue-cogs
st.write("The Gross Profit is",gross_profit)
operating_profit=  float(gross_profit)-float(operative)-float(depreciation_expense)
st.write("The Gross Profit is",operating_profit)
net_profit= float(operating_profit)-float(interest_taxes)
st.write("The Gross Profit is",net_profit)
st.write('Initial Investment cost',total_investment)
st.write('Expected Annual Net Profit',net_profit)
rate_return=0
if total_investment!=0:
    rate_return=(float(net_profit)/float(st.write('please enter how much total investment calculated before',value=10)))*100
else:
    st.write('Please enter the total investment to calculate the rate of return.')
st.write('Rate of Return'+'%',rate_return)
service_life=st.text_input('enter Service Life',value=0)
capital_recovery=0
if rate_return!=0:
    capital_recovery= ((float(rate_return)/100)*(1+(float(rate_return)/100))**(float(service_life)))/(((1+(float(rate_return)/100))**(float(service_life)))-1)
st.write('Capital recovery Factor',capital_recovery)
annual_cost=(float(plant_equipment)+float(research))*float(capital_recovery)
st.write("Annual_cost",annual_cost)
dlc=float(st.text_input('enter direct labor cost per ton',value=0))
hrs=float(st.text_input('enter number of hours per year',value=0))
fohc=float(st.text_input('enter Manufacturing overhead cost',value=0))
fohr=0
if dlc!=0:
    fohr=fohc/dlc
c=0
c_l=0
if hrs!=0:
    c=annual_cost/hrs
    c_l=(dlc*float(volume))/hrs

machine_cost=c*(1+fohr)

st.text_input('enter factory overhead rate on labor ibn percent',value=0)
labor_cost=c_l*(1+fohr)
total_cost=machine_cost+labor_cost
st.write('Total cost rate for the machine',total_cost)

data={'Results':['Gross Profit','Operating Profit','Net Profit','Capital Recovery Factor','Uniform Annual Cost','Total Cost rate for the Machine'],
        'Values':[gross_profit,operating_profit,net_profit,capital_recovery,annual_cost,machine_cost]}
df=pd.DataFrame(data)
st.dataframe(df)
st.download_button('Downlaod CSV',df.to_csv(),file_name='results.csv',mime='text/csv')








