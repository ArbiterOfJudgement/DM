from tsfresh import extract_features
from sklearn import linear_model
import numpy as np
from tsfresh.utilities.dataframe_functions import roll_time_series
import pandas as pd


class TSA:

    defects = [] #raw defect
    rolleddef =[] #rolled defect
    dfy = [] #target vector y
    timeseries = [] #raw data
    rolledts = [] #rolled time series
    extractedFeatures = [] #features on raw data
    filteredfeatures = [] #features after fittin using lasso regression

    def TimeSeriesAnalyser(self, parameters, defects):
        self.defects = defects
        self.timeseries = parameters
        self.rolledts = self.RollTimeSeries(parameters)
        self.rolleddef = self.RollTimeSeries(defects)
        self.dfy = self.rolleddef.groupby("id", sort=False)[self.defects.columns.values[0]].max() >= 75.0 #Подсасывать из базы
        self.extractedFeatures = self.ExtractFeatures(self.rolledts)
        self.filteredfeatures = self.FitFeatures()
        print("SS")

    def RollTimeSeries(self, timeSeries):
        return roll_time_series(timeSeries, column_id="id", column_sort="time", max_timeshift=10, min_timeshift=10) #Из окна разработчика

    def ExtractFeatures(self, timeSeries):
        return extract_features(timeSeries, column_id="id", column_sort="time", n_jobs=6);

    def FitFeatures(self):
        clf = linear_model.Lasso()
        self.extractedFeatures.replace([np.inf, -np.inf], np.nan, inplace=True)
        fitted = clf.fit(self.extractedFeatures.fillna(0), self.dfy)
        fitted = np.ma.masked_equal(fitted.coef_, 0)
        fittedcoef = fitted.mask
        final = pd.DataFrame({"name": self.extractedFeatures.columns.values, "features": fitted})
        return final