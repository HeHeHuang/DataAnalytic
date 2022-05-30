from itertools import product
from statsmodels.tsa.statespace.sarimax import SARIMAX
import streamlit as st
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('fivethirtyeight')


@st.cache()
def convert_df(df):
    return df.to_csv().encode('utf-8')


@st.cache()
def exporttable(df):
    df_T = df.transpose()
    df_T.columns = df_T. iloc[0]
    df_T.columns.values[1] = 'VisitD'
    influenzalist = ['VisitD', 'INFLUENZA (QUADRIVALENT)',  'INFLUENZA']
    df_influenza = df_T[influenzalist].iloc[2:]
    visitdate = []
    for row in df_influenza['VisitD']:
        visitdate.append(datetime.strptime(
            '20' + row.split()[1] + '-' + row.split()[0]+'-01', '%Y-%b-%d'))
    df_influenza = df_influenza.reset_index(drop=True)
    VisitDate = pd.DataFrame(visitdate)
    df_influenza_f = pd.concat([VisitDate, df_influenza], axis=1)
    df_influenza_f.columns.values[0] = 'VisitDate'
    df_influenza_f = df_influenza_f.fillna(0)
    df_influenza_f['Patient Count'] = df_influenza_f['INFLUENZA (QUADRIVALENT)'] + \
        df_influenza_f['INFLUENZA']
    df_influenza_f = df_influenza_f.drop(
        ['VisitD', 'INFLUENZA (QUADRIVALENT)', 'INFLUENZA'], axis=1)
    df_influenza_f = df_influenza_f.groupby("VisitDate").sum("Patient Count")
    return df_influenza_f


@st.cache(allow_output_mutation=(True))
def cleanweekdata(df):
    BD_Poly = pd.read_excel(uploaded_file, 'Bedok', engine='openpyxl')
    BM_Poly = pd.read_excel(uploaded_file, 'Bukit Merah', engine='openpyxl')
    MP_Poly = pd.read_excel(uploaded_file, 'Marine Parade', engine='openpyxl')
    OU_Poly = pd.read_excel(uploaded_file, 'Outram', engine='openpyxl')
    PR_Poly = pd.read_excel(uploaded_file, 'Pasir Ris', engine='openpyxl')
    PG_Poly = pd.read_excel(uploaded_file, 'Punggol', engine='openpyxl')
    SK_Poly = pd.read_excel(uploaded_file, 'Sengkang', engine='openpyxl')
    TP_Poly = pd.read_excel(uploaded_file, 'Tampines', engine='openpyxl')
    # Empty list for weeks that overlap into another month
    week_col_lst = []

    # List of df for all polyclinics
    df_lst = [BD_Poly, BM_Poly, MP_Poly, OU_Poly,
              PR_Poly, PG_Poly, SK_Poly, TP_Poly]
    dfl = []
    for df in df_lst:
        dfl.append(exporttable(df))
    Total = pd.concat(dfl, axis=1)
    Total = Total.fillna(0)
    Total['Total'] = Total.sum(axis=1)
    INFLUENZA = Total[['Total']].astype(int)
    INFLUENZA.columns = INFLUENZA.columns.str.replace('Total', 'Patient Count')
    return INFLUENZA


@st.cache(allow_output_mutation=(True))
def cleandata(df):
    df1 = df
    stat_df1 = df1['Patient Count']
    return df1, stat_df1  # , testset


@st.cache(allow_output_mutation=(True))
def splitdata(dataf):
    if 4 > dataf.index[-1].month > 0:
        traingset = dataf.iloc[(-dataf.index[-1].month)-3 -
                               36:(-dataf.index[-1].month)-3]
        testset = dataf.iloc[(-dataf.index[-1].month)-3:]

    elif 10 > dataf.index[-1].month >= 4:
        traingset = dataf.iloc[(3-dataf.index[-1].month) -
                               36:(3-dataf.index[-1].month)]
        testset = dataf.iloc[3-dataf.index[-1].month:]
    else:
        traingset = dataf.iloc[(9-dataf.index[-1].month) -
                               36:(9-dataf.index[-1].month)]
        testset = dataf.iloc[9-dataf.index[-1].month:]
    dataset = pd.concat([traingset, testset])
    return traingset, testset, dataset


# SARIMA Model Creation
@st.cache(allow_output_mutation=True)
def arima_model(dataf):
    # choose the best aic 3, check with test data for rmse and then choose the best model to predict
    if 4 > dataf.index[-1].month > 0:
        traingset = dataf.iloc[(-dataf.index[-1].month)-3 -
                               36:(-dataf.index[-1].month)-3]
        testset = dataf.iloc[(-dataf.index[-1].month)-3:]
    elif 10 > dataf.index[-1].month >= 4:
        traingset = dataf.iloc[(3-dataf.index[-1].month) -
                               36:(3-dataf.index[-1].month)]
        testset = dataf.iloc[3-dataf.index[-1].month:]
    else:
        traingset = dataf.iloc[(9-dataf.index[-1].month) -
                               36:(9-dataf.index[-1].month)]
        testset = dataf.iloc[9-dataf.index[-1].month:]
    # Define the p, d and q parameters to take any value between 0 and 2
    p = d = q = range(0, 2)
    # Generate all different combinations of p, q and q triplets
    pdq = list(product(p, d, q))
    # Generate all different combinations of seasonal p, q and q triplets
    seasonal_pdq = [(1, 1, 0, 12) for x in list(product(p, d, q))]

    warnings.filterwarnings("ignore")  # specify to ignore warning messages

    # Model Selection
    best_aic = float("inf")
    best_rmse = float("inf")
    aiclist = []
    predictlist = []
    rmselist = []
    modeldic = {}
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                model = SARIMAX(traingset,
                                order=param,
                                seasonal_order=param_seasonal,
                                enforce_invertibility=False)

                model1 = model.fit()
            except:
                continue
            aic = model1.aic
            # get_forecast(len(testset))
            predictions = pd.DataFrame(model1.forecast(steps=len(testset)))
            len(testset)

            rmse = mean_squared_error(testset, predictions, squared=False)
            mae = mean_absolute_error(testset, predictions)
            mape = mean_absolute_percentage_error(testset, predictions)
            info = str(param) + str(param_seasonal) + "aic:" + str(aic) + \
                "rmse:" + str(rmse) + "mae:" + str(mae) + "mape:" + str(mape)
            aiclist.append(info)
            sorted(aiclist[0:9])
            predictlist.append({"parameter": str(param) + str(param_seasonal),
                               "aic": aic, "rmse": rmse, "mae": mae, "mape": mape})
            rmselist.append(rmse)
            # in sorted(aiclist[0:33]) and (rmse < best_rmse)):
            if (mape < best_rmse):
                best_model = model1
                best_aic = aic
                best_rmse = mape
                best_param = param
                best_sparam = param_seasonal
    return best_model, best_param, best_sparam, round(best_aic, 2), aiclist, rmselist,  predictlist, round(best_rmse, 3)


# SARIMA Model Creation
@st.cache(allow_output_mutation=True)
def run_arima_model(dataf, best_param, best_sparam):

    # Generate   p, q and q
    pdq = best_param
    # Generate   seasonal p, q and q
    seasonal_pdq = best_sparam

    warnings.filterwarnings("ignore")  # specify to ignore warning messages

    try:
        model = SARIMAX(dataf,
                        order=best_param,
                        seasonal_order=best_sparam,
                        enforce_invertibility=False)
        model1 = model.fit()
        return model1
    except:
        print("exception")


@st.cache(allow_output_mutation=True)
def check_empty_value(df):
    state = df.eq(0).any().any()
    return state


if __name__ == '__main__':
    st.sidebar.title('Please Select Forecast Period')

    uploaded_file = st.file_uploader('Choose a xlsx file', type='xlsx')
    if uploaded_file:
        st.markdown('---')

        df = cleanweekdata(uploaded_file)
        st.dataframe(df)

        if check_empty_value(df):
            st.warning('There is 0 consumption in file, Please Check ')

        traingset, testset, dataset = splitdata(df)
        best_mod, best_param, best_sparam, best_aic, aic_list, rmselist, predictlist, best_rmse = arima_model(
            dataset)
        st.write(
            f'ARIMA{best_param}x{best_sparam} - AIC:{best_aic}, MAPE:{best_rmse}')
        if st.button('Advance'):
            st.write('Training Set')
            st.dataframe(traingset)
            st.write('Testing Set')
            st.dataframe(testset)
            st.write('Check whether Test data is in confidence interval')
            fc_int1 = int(6)
            ci_int1 = 1-(70/100)

        # Plotting of model
            fig1, ax1 = plt.subplots()
            pred_uc1 = best_mod.get_forecast(steps=fc_int1)
            pred_ci1 = pred_uc1.conf_int(alpha=0.05)
            pred_ciinput = pred_uc1.conf_int(alpha=ci_int1)
            ax = dataset['Patient Count'].plot(
                label='Observed', figsize=(12, 5))
            pred_uc1.predicted_mean.plot(ax=ax, label='Forecast')
            ax1.fill_between(pred_ci1.index,
                             pred_ci1.iloc[:, 0],
                             pred_ci1.iloc[:, 1], color='k', alpha=.25)
            ax1.fill_between(pred_ciinput.index,
                             pred_ciinput.iloc[:, 0],
                             pred_ciinput.iloc[:, 1], color='k', alpha=.4)
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Number of Influenza Vaccines')
            plt.legend()
            st.pyplot(fig1)

    # User entered values
    with st.form(key='form'):
        with st.sidebar:
            fc_period = st.slider(
                'Forecast Period (months)',
                min_value=1, max_value=13, value=1)

            ci_1 = st.selectbox(
                'Confidence Interval',
                ('90%', '85%', '80%', '75%', '70%'))

            proceed_submission = st.form_submit_button("SUBMIT HERE")

    # Once user submit entered values
    if proceed_submission:
        # Converting string variables into integers
        fc_int = int(fc_period)
        ci_int = 1-(int(ci_1.split('%')[0])/100)

        # Plotting of model
        fig, ax = plt.subplots()
        forecast_model = run_arima_model(dataset, best_param, best_sparam)
        pred_uc = forecast_model.get_forecast(steps=fc_int)
        pred_ci = pred_uc.conf_int(alpha=0.05)
        pred_ciinput = pred_uc.conf_int(alpha=ci_int)
        ax = dataset['Patient Count'].plot(
            label='Observed', figsize=(12, 5))
        pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
        ax.fill_between(pred_ci.index,
                        pred_ci.iloc[:, 0],
                        pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.fill_between(pred_ciinput.index,
                        pred_ciinput.iloc[:, 0],
                        pred_ciinput.iloc[:, 1], color='k', alpha=.4)
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Influenza Vaccines')
        plt.legend()
        st.pyplot(fig)

        # Merging of forecast df with CI df
        predict = pred_uc.predicted_mean.to_frame()
        predict.reset_index(inplace=True)
        predict.rename(
            columns={'index': 'Date', 'predicted_mean': 'Vaccine Forecast'}, inplace=True)
        predict['Vaccine Forecast'] = predict['Vaccine Forecast'].astype(int)

        pred_ci = pred_ci.astype(int)
        pred_ci.reset_index(inplace=True)
        pred_ci['lower Patient Count'] = np.where(
            pred_ci['lower Patient Count'] < 0, 0, pred_ci['lower Patient Count'])
        pred_ci.rename(columns={'index': 'Date', 'lower Patient Count': '95% CI Lower',
                       'upper Patient Count': '95% CI Upper'}, inplace=True)
        predict1 = predict.merge(pred_ci, how='inner', on=['Date'])

        new1 = ci_1 + " CI Lower"
        new2 = ci_1 + " CI Upper"
        pred_ciinput = pred_ciinput.astype(int)
        pred_ciinput.reset_index(inplace=True)

        pred_ciinput['lower Patient Count'] = np.where(
            pred_ciinput['lower Patient Count'] < 0, 0, pred_ciinput['lower Patient Count'])

        pred_ciinput.rename(columns={
                            'index': 'Date', 'lower Patient Count': new1, 'upper Patient Count': new2}, inplace=True)

        predict2 = predict1.merge(pred_ciinput, how='inner', on=['Date'])

       # predict2['Date'] = predict2['Date'].dt.date
      #  predict2.set_index(['Date'])

        predict2['Year'] = predict['Date'].dt.year
        predict2['Month'] = predict['Date'].dt.month
        predict2['Date'] = predict2['Date'].dt.date
        predict2 = predict2.set_index(['Date'])

        # Viewing of the entire forecasted df
        st.dataframe(predict2)
        predict2 = predict2.reset_index()

        predict2['95% CI Lower'] = np.where(
            predict2['95% CI Lower'] < 0, 0, predict2['95% CI Lower'])

        # Download forecasted df
        forecast_csv = convert_df(predict2)
        st.download_button(
            "Click to Download Forecasted Data (By Months)",
            forecast_csv,
            "Influenza_Forecast.csv",
            "text/csv",
            key="download-csv")

        # Southern Hemisphere forcasted df
        SH = predict2[(predict2['Month'] > 3) & (predict2['Month'] < 10)]
        SH1 = SH.groupby('Year').sum()
        SH2 = SH.groupby('Year')['Date'].count()

        SH['Date'] = SH['Date'].astype(str)
        SH_month = SH.groupby('Year')['Date'].transform(lambda x: ", ".join(x))
        SH_month.drop_duplicates(inplace=True)
        SH_month = SH_month.reset_index().drop(columns=['index'])

        SH3 = pd.merge(SH1, SH2, left_index=True, right_index=True)
        SH3.drop(columns=['Month'], inplace=True)
        SH3.rename(columns={'Date': 'Month Count'}, inplace=True)

        # Viewing of Southern Hemisphere forecasted df
        st.subheader('Southern Hemisphere Winter')

        if SH3.shape[0] == 0:
            st.write('No Forecasted Data Available')
        else:
            for i in range(SH3.shape[0]):
                # st.write(i)
                if SH3.iloc[i, 5] == 6:
                    st.success(
                        f'{SH3.index.values[i]} SH is COMPLETE with Months: {SH_month.iloc[i,:].values}')
                else:
                    st.warning(
                        f'{SH3.index.values[i]} SH is INCOMPLETE with Months: {SH_month.iloc[i,:].values}')
            st.dataframe(SH3)

            # Download forecasted Southern Hemisphere Influenza Vaccines
            SHforecast_csv = convert_df(SH3)
            st.download_button(
                "Click to Download Forecasted Data (Southern Hemisphere)",
                SHforecast_csv,
                "InfluenzaSH_Forecast.csv",
                "text/csv",
                key="download-csv")

        # Northern Hemisphere forecasted df
        NH = predict2[((predict2['Month'] > 0) & (predict2['Month'] < 4))]
        NH1 = NH.groupby('Year').sum()
        NH4 = NH.groupby('Year')['Date'].count()

        NH1 = NH1.reset_index()
        NH4 = NH4.reset_index()
        NH1['Year'] = (NH1['Year']-1).astype(str) + \
            "/" + (NH1['Year']).astype(str)
        NH4['Year'] = (NH4['Year']-1).astype(str) + \
            "/" + (NH4['Year']).astype(str)

        NH2 = predict2[predict2['Month'] > 9]
        NH3 = NH2.groupby('Year').sum()
        NH5 = NH2.groupby('Year')['Date'].count()

        NH3 = NH3.reset_index()
        NH5 = NH5.reset_index()
        NH3['Year'] = (NH3['Year']).astype(str) + \
            "/" + (NH3['Year']+1).astype(str)
        NH5['Year'] = (NH5['Year']).astype(str) + \
            "/" + (NH5['Year']+1).astype(str)

        NH6 = NH4.append(NH5)
        NH6 = NH6.groupby('Year')['Date'].sum()

        NH7 = NH1.append(NH3)
        NH7 = NH7.groupby('Year').sum()

        NH8 = pd.merge(NH7, NH6, left_index=True, right_index=True)
        NH8.drop(columns=['Month'], inplace=True)
        NH8.rename(columns={'Date': 'Month Count'}, inplace=True)

        # Months df from forecasted Northern Hemisphere data
        NH['Date'] = NH['Date'].astype(str)
        NH_JFM = NH.groupby('Year')['Date'].transform(lambda x: ", ".join(x))
        NH_JFM.drop_duplicates(inplace=True)
        NH_JFM = NH_JFM.reset_index().drop(columns=['index'])

        NH2['Date'] = NH2['Date'].astype(str)
        NH_OND = NH2.groupby('Year')['Date'].transform(lambda x: ", ".join(x))
        NH_OND.drop_duplicates(inplace=True)
        NH_OND = NH_OND.reset_index().drop(columns=['index'])

        if NH_JFM.shape[0] > 1:
            NH_OND['Date'] = NH_OND['Date'] + ", " + NH_JFM.iloc[1, 0]
            NH_JFM.drop([0], inplace=True)
            NH_JFM = NH_JFM.reset_index().drop(columns=['index'])

        elif NH_OND.shape[0] > 1:
            NH_JFM['Date'] = NH_OND.iloc[0, 0] + ", " + NH_JFM['Date']
            NH_OND.drop([0], inplace=True)
            NH_OND = NH_OND.reset_index().drop(columns=['index'])

        # Viewing of Northern Hemisphere forecasted df
        st.subheader('Northern Hemisphere Winter')
        if NH8.shape[0] == 0:
            st.write('No Forecasted Data Available')
        else:
            if NH8.shape[0] == 1:
                if NH_JFM.empty or NH_OND.empty:
                    month_lst = [NH_JFM, NH_OND]
                    for df in month_lst:
                        if not df.empty:
                            NH_months_final = df
                else:
                    NH_months_final = pd.DataFrame()
                    NH_months_final['Date'] = NH_OND['Date'] + \
                        ", " + NH_JFM['Date']

                if NH8.iloc[0, 5] == 6:
                    st.success(
                        f'{NH8.index.values[0]} is COMPLETE with Months: {NH_months_final.iloc[0,:].values}')
                else:
                    st.warning(
                        f'{NH8.index.values[0]} is INCOMPLETE with Months: {NH_months_final.iloc[0,:].values}')

            else:
                for i in range(NH8.shape[0]):
                    if NH8.iloc[i, 5] == 6:
                        NH_JFM['Date'] = NH_JFM['Date'] + NH_OND['Date']
                        st.success(
                            f'{NH8.index.values[i]} is COMPLETE with Months: {NH_JFM.iloc[i,:].values}')
                    elif i == 1:
                        st.warning(
                            f'{NH8.index.values[i]} is INCOMPLETE with Months: {NH_OND.iloc[0,:].values}')
                    else:
                        st.warning(
                            f'{NH8.index.values[i]} is INCOMPLETE with Months: {NH_JFM.iloc[0,:].values}')

            st.write(NH8)

            # Download forecasted Northern Hemisphere Influenza Vaccines
            NHforecast_csv = convert_df(NH8)
            st.download_button(
                "Click to Download Forecasted Data (Northern Hemisphere)",
                NHforecast_csv,
                "InfluenzaNH_Forecast.csv",
                "text/csv",
                key="download-csv")
