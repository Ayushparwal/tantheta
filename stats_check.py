from tantheta.stats import (
    mean,
    median,
    variance,
    standard_deviation,
    mode,
    range_,
    quartiles,
    interquartile_range,
    covariance,
    correlation_coefficient,
    z_scores,
    skewness,
    kurtosis,
    coefficient_of_variation,
    sample_variance,
    sample_standard_deviation,
    percentile,
)

data1 = [1, 2, 2, 3, 4, 5, 6]
data2 = [2, 4, 4, 6, 8, 10, 12]

print("Mean:", mean(data1))
print("Median:", median(data1))
print("Variance:", variance(data1))
print("Standard Deviation:", standard_deviation(data1))
print("Mode:", mode(data1))
print("Range:", range_(data1))
print("Quartiles (Q1, Q2, Q3):", quartiles(data1))
print("Interquartile Range:", interquartile_range(data1))
print("Covariance:", covariance(data1, data2))
print("Correlation Coefficient:", correlation_coefficient(data1, data2))
print("Z-Scores:", z_scores(data1))
print("Skewness:", skewness(data1))
print("Kurtosis:", kurtosis(data1))
print("Coefficient of Variation:", coefficient_of_variation(data1))
print("Sample Variance:", sample_variance(data1))
print("Sample Standard Deviation:", sample_standard_deviation(data1))
print("25th Percentile:", percentile(data1, 25))
print("50th Percentile:", percentile(data1, 50))
print("75th Percentile:", percentile(data1, 75))
