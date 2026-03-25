# 📊 Integrated Autocorrelation Time

This repository provides a simple implementation to estimate the **integrated autocorrelation time** from a time series.

The method is particularly relevant in the analysis of correlated data, where successive measurements are not statistically independent.

---

## 📌 Overview

In many numerical simulations and stochastic processes, data points exhibit temporal correlations. This affects statistical estimates, especially error bars, since standard formulas assume independent samples.

The **integrated autocorrelation time** $\tau$ quantifies how many steps are effectively required for the system to produce an independent measurement.

---

## 🧠 What is the Integrated Autocorrelation Time?

Given a normalized autocorrelation function $A(k)$, the integrated autocorrelation time is defined as:

$$
\tau = \frac{1}{2} + \sum_{k=1}^{k_{\max}} A(k)
$$

It measures the persistence of correlations in the data:

- $\tau \approx 0.5$ → nearly uncorrelated data  
- large $\tau$ → strong correlations  
- effective number of independent samples is reduced by a factor $\sim 2\tau$  

---

## ⚙️ Method Description

The implementation follows these main steps:

### 1. Data Extraction

The input is assumed to be a two-column array:

- First column: time index (not used in calculations)  
- Second column: observable (time series)

Only the observable is used for the analysis.

---

### 2. Basic Statistics

The function computes:

- Sample mean of the series  
- Sample variance (with Bessel’s correction)

These quantities are required to normalize the autocorrelation function.

---

### 3. Autocorrelation Function

For each lag $k$, the autocorrelation is computed as:

- $k = 0$: variance of the series  
- $k > 0$: correlation between the series and a shifted version of itself  

The result is normalized by the variance, producing the **autocorrelation function** $A(k)$, with:

$$
A(0) = 1
$$

---

### 4. Integrated Autocorrelation Time

The integrated autocorrelation time is estimated by summing $A(k)$ up to a fixed cutoff $k_{\max}$:

$$
\tau = \frac{1}{2} + \sum_{k=0}^{k_{\max}} A(k)\left(1 - \frac{k_{\max}}{N}\right)
$$

where:

- $N$ is the length of the time series  
- $k_{\max}$ is the maximum lag considered  

---

## 📉 Finite-Size Effect Reduction

In practice, autocorrelation estimates at large lags become increasingly noisy due to the finite length of the time series.

To mitigate this, the implementation includes a correction factor:

$$
\left(1 - \frac{k_{\max}}{N}\right)
$$

This term reduces the contribution of the sum when the maximum lag becomes comparable to the total number of data points.

### Why this matters:

- For large $k$, fewer data pairs are available → higher statistical noise  
- The correction acts as a **finite-size damping factor**  
- It helps prevent overestimation of $ \tau $ due to noisy long-range correlations  

This is a simplified way to control truncation effects without implementing adaptive windowing schemes.

---

## ⚠️ Notes

- The method assumes the time series is **stationary**  
- The choice of $k_{\max}$ is fixed and may influence the estimate  
- For highly correlated systems, more sophisticated windowing procedures may be preferable  

---

## 📚 Reference

Wolfhard Janke, *Statistical Analysis of Simulations: Data Correlations and Error Estimation*, in:  
J. Grotendorst, D. Marx, A. Muramatsu (eds.),  
**Quantum Simulations of Complex Many-Body Systems: From Theory to Algorithms**,  
NIC Series, Vol. 10, pp. 423–445,  
John von Neumann Institute for Computing, Jülich (2002).
