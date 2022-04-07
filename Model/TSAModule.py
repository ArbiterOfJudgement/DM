from tsfresh import extract_features

class TSA:
    def TimeSeriesAnalyser(self, parameters):
        extractedFeatures = self.ExtractFeatures(parameters);

    def ExtractFeatures(self, timeSeries):
        return extract_features(timeSeries, column_id="id", column_sort="time");