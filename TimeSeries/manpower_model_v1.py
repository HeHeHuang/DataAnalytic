import streamlit as st
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from itertools import product
import warnings
plt.style.use('fivethirtyeight')


@st.cache()
def convert_df(df):
    return df.to_csv().encode('utf-8')


@st.cache()
def totaljabs_convert(BD_Poly, BM_Poly, MP_Poly, OU_Poly, PR_Poly, PG_Poly, SK_Poly, TP_Poly):
    # Empty list for weeks that overlap into another month
    week_col_lst = []

    # List of df for all polyclinics
    df_lst = [BD_Poly, BM_Poly, MP_Poly, OU_Poly,
              PR_Poly, PG_Poly, SK_Poly, TP_Poly]

    # Fill in values of NaN with 0
    for df in df_lst:
        df.drop(0, inplace=True)
        df.fillna(0, inplace=True)

    # Get all the overlap weeks that are available in Bedok Polyclinic
    for i in range(BD_Poly.shape[1]-1):
        if BD_Poly.iloc[1, i] == BD_Poly.iloc[1, i+1]:
            week_col_lst.append(
                str(BD_Poly.iloc[0, i]) + str(BD_Poly.iloc[0, i+1]))

    for i in range(2, BD_Poly.shape[1]-1):
        if (BD_Poly.iloc[0, i][-2:] != BD_Poly.iloc[0, i+1][-2:]) & (datetime.date(int('20' + BD_Poly.iloc[0, i+1][-2:]), 1, 1).isoweekday() != 7) & (BD_Poly.iloc[1, i+1] == 1):
            week_col_lst.append(
                str(BD_Poly.iloc[0, i]) + str(BD_Poly.iloc[0, i+1]))

    # Sum the columns of weeks that overlap
    for df in df_lst:
        for i in range(df.shape[1]-1):
            if df.iloc[1, i] == df.iloc[1, i+1]:
                df[df.columns[i]] = df[df.columns[i]] + df[df.columns[i+1]]

        for i in range(2, df.shape[1]-1):
            if (df.iloc[0, i][-2:] != df.iloc[0, i+1][-2:]) & (datetime.date(int('20' + df.iloc[0, i+1][-2:]), 1, 1).isoweekday() != 1) & (df.iloc[1, i+1] == 1):
                df[df.columns[i]] = df[df.columns[i]] + df[df.columns[i+1]]

        # Renaming all the column headers with the month and year
        df.rename(columns=df.iloc[0], inplace=True)

    # Getting the index for all needed columns for the different polyclinic
    com_lst = []

    for df in df_lst:
        test_lst = []
        for i in [i for i in week_col_lst if i in df]:
            test_lst.append(df.columns.get_loc(i)+1)

        column_numbers = [x for x in range(df.shape[1]) if x not in test_lst]
        com_lst.append(column_numbers)

    # Amend jabs per weeks based on index for all needed columns
    BD_Poly = pd.DataFrame(BD_Poly.iloc[:, com_lst[0]])
    BM_Poly = pd.DataFrame(BM_Poly.iloc[:, com_lst[1]])
    MP_Poly = pd.DataFrame(MP_Poly.iloc[:, com_lst[2]])
    OU_Poly = pd.DataFrame(OU_Poly.iloc[:, com_lst[3]])
    PR_Poly = pd.DataFrame(PR_Poly.iloc[:, com_lst[4]])
    PG_Poly = pd.DataFrame(PG_Poly.iloc[:, com_lst[5]])
    SK_Poly = pd.DataFrame(SK_Poly.iloc[:, com_lst[6]])
    TP_Poly = pd.DataFrame(TP_Poly.iloc[:, com_lst[7]])

    df_lst = [BD_Poly, BM_Poly, MP_Poly, OU_Poly,
              PR_Poly, PG_Poly, SK_Poly, TP_Poly]

    # Getting the year month and week for each polyclinic
    com_weeks = []

    for df in df_lst:
        weeks, date_lst = [], []
        weeks = df[0:2].transpose().iloc[2:, :]
        weeks[2] = np.where(((weeks[1].str.len() > 6) & (weeks[1].str.slice(
            4, 6) == weeks[1].str.slice(10, 12))), weeks[2]/2, weeks[2])
        weeks[2] = np.where(((weeks[1].str.len() > 6) & (weeks[1].str.slice(
            4, 6) != weeks[1].str.slice(10, 12))), weeks[2]-1, weeks[2])
        weeks[1] = np.where(weeks[1].str.len() > 6,
                            weeks[1].str[0:6], weeks[1])
        weeks[1] = weeks[1].str.split(" ").str[-1]
        weeks[1] = "20" + weeks[1]
        weeks[1] = weeks[1].astype(int)
        weeks[2] = weeks[2].astype(int)

        t_date = datetime.date(
            int(weeks.iloc[0, 0]), 1, 1) + relativedelta(weeks=+int(weeks.iloc[0, 1]))

        while t_date.isoweekday() != 1:
            t_date = t_date - relativedelta(days=+1)

        date_lst.append(t_date)

        for i in range(1, weeks.shape[0]):
            t_date += relativedelta(days=+7)
            date_lst.append(t_date)

        com_weeks.append(date_lst)

    # Amend jabs per weeks based on index for all needed columns
    BD_Poly = pd.DataFrame(BD_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'BD'})
    BM_Poly = pd.DataFrame(BM_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'BM'})
    MP_Poly = pd.DataFrame(MP_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'MP'})
    OU_Poly = pd.DataFrame(OU_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'OU'})
    PR_Poly = pd.DataFrame(PR_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'PR'})
    PG_Poly = pd.DataFrame(PG_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'PG'})
    SK_Poly = pd.DataFrame(SK_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'SK'})
    TP_Poly = pd.DataFrame(TP_Poly.iloc[2:, 2:].sum(axis=0)).reset_index(
        drop=True).rename(columns={0: 'TP'})

    BD_Poly.index = com_weeks[0]
    BM_Poly.index = com_weeks[1]
    MP_Poly.index = com_weeks[2]
    OU_Poly.index = com_weeks[3]
    PR_Poly.index = com_weeks[4]
    PG_Poly.index = com_weeks[5]
    SK_Poly.index = com_weeks[6]
    TP_Poly.index = com_weeks[7]

    totaljabs_perwk = pd.concat(
        [BD_Poly, BM_Poly, MP_Poly, OU_Poly, PR_Poly, PG_Poly, SK_Poly, TP_Poly], axis=1)
    totaljabs_perwk.fillna(0, inplace=True)
    totaljabs_perwk = totaljabs_perwk.astype(int)

    return totaljabs_perwk


@st.cache()
def holi_count(holiday_excel, totaljabs_perwk, fc_period):
    # Obtain columns with Year label
    x = [i for i in holiday_excel.columns if i.startswith('20')]
    hol_lst1 = holiday_excel[x]

    # Unstack list of dates to a single column
    holis = pd.DataFrame(hol_lst1.unstack().reset_index(drop=True))
    for i in range(holis.shape[0]):
        if holis.iloc[i, 0].isoweekday() == 7:
            holis.iloc[i, 0] = holis.iloc[i, 0] + relativedelta(days=+1)

    # Obtain list of holidays ended and holiday count
    holi_idx, holi_ended = [], []
    testholi = [1, 2]

    for i in holis[0]:
        for j in totaljabs_perwk.index:
            if i >= j and i <= j + relativedelta(days=+6):
                holi_idx.append(j)
                holi_ended.append(i)

    # Format df for holiday count
    overholi_count = pd.DataFrame(pd.DataFrame(
        holi_idx).value_counts()).rename(columns={0: 'Holiday_Count'})
    overholi_count = overholi_count.reset_index().set_index(0)

    # Get list of holidays that are upcoming for exogenous variable for upcoming forecast

    forecast_dates, fc_holi_exgo = [], []

    # Obtain dates of holidays that are upcoming from excel file provided
    holi_uc = holis[~holis[0].isin(holi_ended)].astype(str)

    # Get all upcoming dates (weeks) from forecasted no of weeks provided
    # Change the range to the number of weeks of forecast keyed by user
    for i in range(1, fc_period+2):
        forecast_dates.append(
            str(totaljabs_perwk.index[-1] + relativedelta(days=+(i*7))))

    # Format of upcoming dates forecasted weeks df
    forecast_dates1 = pd.DataFrame(forecast_dates).set_index(0)
    forecast_dates1.drop(
        forecast_dates1.index[len(forecast_dates1)-1], inplace=True)

    # Get the dates of weeks with holiday and count number of holiday in the weeks
    for j in range(len(forecast_dates)-1):
        for i in holi_uc[0]:
            if (i >= forecast_dates[j]) and (i < forecast_dates[j+1]):
                fc_holi_exgo.append(forecast_dates[j])

    if len(fc_holi_exgo) > 0:
        # Format of weeks with holiday and count of holiday df
        fc_holi_exgo1 = pd.DataFrame(pd.DataFrame(fc_holi_exgo).value_counts()).rename(
            columns={0: 'Holiday_Count'})
        fc_holi_exgo1 = fc_holi_exgo1.reset_index().set_index(0)

        # Merging both df to obtain final df for the forecast exogenous variable of holiday count
        fc_holi_final = pd.merge(
            forecast_dates1, fc_holi_exgo1, how='outer', left_index=True, right_index=True)
        fc_holi_final['Holiday_Count'] = fc_holi_final['Holiday_Count'].fillna(
            0).astype(int)

    else:
        fc_holi_final = forecast_dates1
        fc_holi_final['Holiday_Count'] = 0

    return overholi_count, fc_holi_final


def run_arima_model(dataf):

    # Define the p, d and q parameters to take any value between 0 and 2
    p = d = q = range(0, 3)
    # Generate all different combinations of p, q and q triplets
    pdq = list(product(p, d, q))

    warnings.filterwarnings("ignore")  # specify to ignore warning messages

    best_aic = float("inf")

    for param in pdq:
        try:
            model = ARIMA(dataf.iloc[:, 0], exog=dataf['Holiday_Count'],
                          order=param,
                          enforce_invertibility=False)

            model1 = model.fit()
            #st.write('ARIMA{} - AIC:{}'.format(param, model1.aic))
        except:
            continue
        aic = model1.aic
        if (aic < best_aic):
            best_model = model1
            best_aic = aic
            best_param = param

    return best_model


if __name__ == '__main__':
    st.title('Nursing Manpower Forecast')
    st.sidebar.title('Please Select Forecast Period (Weeks)')

    file1, file2 = st.columns(2)

    with file1:
        uploaded_file = st.file_uploader(
            'Choose an Immunization Clinic Per Week Excel file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            jabs_file = pd.read_excel(uploaded_file,  engine='openpyxl')

            BD_Poly = jabs_file.get('Bedok')
            BM_Poly = jabs_file.get('Bukit Merah')
            MP_Poly = jabs_file.get('Marine Parade')
            OU_Poly = jabs_file.get('Outram')
            PR_Poly = jabs_file.get('Pasir Ris')
            PG_Poly = jabs_file.get('Punggol')
            SK_Poly = jabs_file.get('Sengkang')
            TP_Poly = jabs_file.get('Tampines')

            totaljabs_perwk = totaljabs_convert(
                BD_Poly, BM_Poly, MP_Poly, OU_Poly, PR_Poly, PG_Poly, SK_Poly, TP_Poly)

    with file2:
        # Loading of holiday list
        uploaded_file = st.file_uploader(
            'Choose the Holiday Excel file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            hol_lst = pd.read_excel(uploaded_file)

    # User entered values
    with st.form(key='form'):
        with st.sidebar:

            fc_period = st.slider(
                'Manpower Forecast Period (Weeks)',
                min_value=2, max_value=20, value=2)

            time_perjab = st.slider(
                'Average Time Per Jab (Minutes)',
                min_value=15, max_value=30, value=20)

            ci_1 = st.selectbox(
                'Confidence Interval',
                ('90%', '85%', '80%', '75%', '70%'))

            proceed_submission = st.form_submit_button("SUBMIT HERE")

    # Once user submit entered values
    if proceed_submission:
        poly_abb = ['BD', 'BM', 'MP', 'OU', 'PR', 'PG', 'SK', 'TP']

        # Converting string variables into integers
        fc_int = int(fc_period)
        ci_int = 1-(int(ci_1.split('%')[0])/100)
        time_perjab = int(time_perjab)

        holi_train, holi_fc = holi_count(hol_lst, totaljabs_perwk, fc_int)

        holi_fc.index.name = None
        holi_fc.astype(int)
        manhours = 44-(holi_fc['Holiday_Count']*8)
        manhours = manhours.reset_index(drop=True)

        totaljabs_perwk1 = pd.merge(
            totaljabs_perwk, holi_train, how='outer', left_index=True, right_index=True)
        totaljabs_perwk1['Holiday_Count'].fillna(0, inplace=True)
        totaljabs_perwk1['Holiday_Count'] = totaljabs_perwk1['Holiday_Count'].astype(
            int)

        st.write(totaljabs_perwk1)

        com_df = pd.DataFrame()

        for i in totaljabs_perwk1.columns:
            if i in poly_abb:

                df_per_clinic = totaljabs_perwk1[totaljabs_perwk1[i] != 0][[
                    i, 'Holiday_Count']][-160:]

                fc_model = run_arima_model(df_per_clinic)
                # st.write(fc_model.summary())

                pred_uc = fc_model.get_forecast(steps=fc_period, exog=holi_fc)
                pred_ci = pred_uc.conf_int(alpha=0.05)
                pred_ciinput = pred_uc.conf_int(alpha=ci_int)

                # Merging of forecast df with CI df
                predict = pred_uc.predicted_mean.to_frame()
                predict.reset_index(inplace=True)
                predict['Polyclinic'] = i

                if fc_int == 1:
                    predict = predict.reindex(
                        columns=['index', 'Polyclinic', 0])
                    predict.rename(
                        columns={'index': 'Date', 0: 'Manpower'}, inplace=True)
                else:
                    predict = predict.reindex(
                        columns=['index', 'Polyclinic', 'predicted_mean'])
                    predict.rename(
                        columns={'index': 'Date', 'predicted_mean': 'Manpower'}, inplace=True)

                predict['Manpower'] = round(
                    predict['Manpower'].astype(int)/manhours*(time_perjab/60), 2)
                predict['Manpower Rounded'] = predict['Manpower'].apply(
                    np.ceil)

                pred_ci[f'lower {i}'] = round(pred_ci[f'lower {i}'].div(
                    manhours.values, axis=0)*(time_perjab/60), 2)
                #pred_ci[f'lower {i}']
                pred_ci[f'upper {i}'] = round(pred_ci[f'upper {i}'].div(
                    manhours.values, axis=0)*(time_perjab/60), 2)
                #pred_ci[f'upper {i}']

                #pred_ci = round((pred_ci.astype(int))/44*(time_perjab/60),2)
                pred_ci.reset_index(inplace=True)
                pred_ci[f'lower {i}'] = np.where(
                    pred_ci[f'lower {i}'] < 0, 0, pred_ci[f'lower {i}'])
                pred_ci.rename(columns={'index': 'Date', f'lower {i}': '95% CI Lower',
                               f'upper {i}': '95% CI Upper'}, inplace=True)
                predict1 = predict.merge(pred_ci, how='inner', on=['Date'])

                new1 = ci_1 + " CI Lower"
                new2 = ci_1 + " CI Upper"

                pred_ciinput[f'lower {i}'] = round(pred_ciinput[f'lower {i}'].div(
                    manhours.values, axis=0)*(time_perjab/60), 2)
                #pred_ciinput[f'lower {i}']
                pred_ciinput[f'upper {i}'] = round(pred_ciinput[f'upper {i}'].div(
                    manhours.values, axis=0)*(time_perjab/60), 2)
                #pred_ciinput[f'upper {i}']
                #pred_ciinput = round((pred_ciinput.astype(int))/44*(time_perjab/60),2)
                pred_ciinput.reset_index(inplace=True)

                pred_ciinput[f'lower {i}'] = np.where(
                    pred_ciinput[f'lower {i}'] < 0, 0, pred_ciinput[f'lower {i}'])

                pred_ciinput.rename(columns={
                                    'index': 'Date', f'lower {i}': new1, f'upper {i}': new2}, inplace=True)

                fig1, ax1 = plt.subplots()
                ax = (df_per_clinic[i]/44*(20/60)).plot(
                    label='Observed', figsize=(12, 5))
                ((pred_uc.predicted_mean)/manhours.values *
                 (time_perjab/60)).plot(ax=ax, label='Forecast')

                ax1.fill_between(pred_ciinput.iloc[:, 0],
                                 pred_ciinput.iloc[:, 1],
                                 pred_ciinput.iloc[:, 2], color='k', alpha=.4)
                ax1.set_xlabel('Date')
                ax1.set_ylabel('Number of Nurse')
                ax1.set_ylim(ymin=0)
                plt.legend()
                plt.title(f'Manpower Forecast for {i}')
                st.pyplot(fig1)

                predict2 = predict1.merge(
                    pred_ciinput, how='inner', on=['Date'])

                predict2['Date'] = predict2['Date'].dt.date
                predict2 = predict2.set_index(['Date'])

                com_df = pd.concat([com_df, predict2])

        com_df['Manpower Rounded'] = com_df['Manpower Rounded'].astype(int)
        st.dataframe(com_df.style.format({'Manpower': '{:.2f}', '95% CI Lower': '{:.2f}', '95% CI Upper': '{:.2f}',
                                          f"{ci_1} CI Lower": '{:.2f}', f"{ci_1} CI Upper": '{:.2f}'}))

        com_df1 = convert_df(com_df)
        st.download_button(
            "Click to Download All Forecasted Manpower",
            com_df1,
            f"Manpower_Forecast_{time_perjab}mins.csv",
            "text/csv",
            key="download-csv")

        for i in holi_fc.index:
            st.subheader(f'Week with Monday on {i}')
            download_df = com_df[com_df.index.astype(str) == i]
            download_df1 = convert_df(download_df)
            st.dataframe(com_df[com_df.index.astype(str) == i].style.format({'Manpower': '{:.2f}', '95% CI Lower': '{:.2f}',
                                                                             '95% CI Upper': '{:.2f}', f"{ci_1} CI Lower": '{:.2f}',
                                                                             f"{ci_1} CI Upper": '{:.2f}'}))
            st.success(
                f'Total Manpower = {download_df["Manpower"].sum().round(2)} , Rounded Manpower = {download_df["Manpower Rounded"].sum()}')
            st.download_button(
                f"Click to Download Forecasted Manpower {i}_{time_perjab}mins",
                download_df1,
                f"{i}_Manpower_Forecast_{time_perjab}mins.csv",
                "text/csv",
                key="download-csv")
