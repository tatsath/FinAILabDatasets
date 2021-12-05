.. _YahooFinance:

Yahoo Finance
=========

A callback is a set of functions that will be called at given stages of the training procedure.
You can use callbacks to access internal state of the RL model during training.
It allows one to do monitoring, auto saving, model manipulation, progress bars, ...


Custom Callback
---------------

To build a custom callback, you need to create a class that derives from ``BaseCallback``.
This will give you access to events (``_on_training_start``, ``_on_step``) and useful variables (like `self.model` for the RL model).


You can find two examples of custom callbacks in the documentation: one for saving the best model according to the training reward (see :ref:`Examples <examples>`), and one for logging additional values with Tensorboard (see :ref:`Tensorboard section <tensorboard>`).


-  `1. Historical Price and Volume for 1 Stock. <#1>`__
-  `2. Time Periods <#2>`__
-  `3. Frequency <#3>`__
-  `4. Split and Dividends <#4>`__
-  `5. Many Stocks <#5>`__
-  `6. Finanical Indices <#6>`__
-  `7. Currencies <#7>`__ `8. Crypto <#8>`__ `9. Mutual Funds <#9>`__
   `10. Treasury <#10>`__ `11. Stock Fundamentals <#11>`__ `12.
   Financials <#12>`__ `13. Put Call Options <#13>`__ `14. Stream Real
   Time Data <#14>`__

.. code:: ipython3

    import numpy as np
    import yfinance as yf

 ### Historical Price and Volume for 1 Stock.

.. code:: ipython3

    ticker = 'GE'

.. code:: ipython3

    yf.download(ticker)


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1962-01-02</th>
          <td>6.009615</td>
          <td>6.109776</td>
          <td>5.949519</td>
          <td>5.989583</td>
          <td>1.012673</td>
          <td>269568</td>
        </tr>
        <tr>
          <th>1962-01-03</th>
          <td>5.959535</td>
          <td>5.959535</td>
          <td>5.909455</td>
          <td>5.929487</td>
          <td>1.002512</td>
          <td>184704</td>
        </tr>
        <tr>
          <th>1962-01-04</th>
          <td>5.929487</td>
          <td>5.979567</td>
          <td>5.809295</td>
          <td>5.859375</td>
          <td>0.990659</td>
          <td>229632</td>
        </tr>
        <tr>
          <th>1962-01-05</th>
          <td>5.859375</td>
          <td>5.869391</td>
          <td>5.608974</td>
          <td>5.709135</td>
          <td>0.965257</td>
          <td>340704</td>
        </tr>
        <tr>
          <th>1962-01-08</th>
          <td>5.709135</td>
          <td>5.709135</td>
          <td>5.528846</td>
          <td>5.699119</td>
          <td>0.963564</td>
          <td>386880</td>
        </tr>
        <tr>
          <th>1962-01-09</th>
          <td>5.699119</td>
          <td>5.779247</td>
          <td>5.659054</td>
          <td>5.729167</td>
          <td>0.968643</td>
          <td>290784</td>
        </tr>
        <tr>
          <th>1962-01-10</th>
          <td>5.729167</td>
          <td>5.789263</td>
          <td>5.709135</td>
          <td>5.759215</td>
          <td>0.973724</td>
          <td>244608</td>
        </tr>
        <tr>
          <th>1962-01-11</th>
          <td>5.759215</td>
          <td>5.769231</td>
          <td>5.659054</td>
          <td>5.769231</td>
          <td>0.975417</td>
          <td>203424</td>
        </tr>
        <tr>
          <th>1962-01-12</th>
          <td>5.769231</td>
          <td>5.779247</td>
          <td>5.669071</td>
          <td>5.689103</td>
          <td>0.961870</td>
          <td>210912</td>
        </tr>
        <tr>
          <th>1962-01-15</th>
          <td>5.699119</td>
          <td>5.769231</td>
          <td>5.699119</td>
          <td>5.749199</td>
          <td>0.972031</td>
          <td>264576</td>
        </tr>
        <tr>
          <th>1962-01-16</th>
          <td>5.749199</td>
          <td>5.819311</td>
          <td>5.709135</td>
          <td>5.799279</td>
          <td>0.980498</td>
          <td>173472</td>
        </tr>
        <tr>
          <th>1962-01-17</th>
          <td>5.789263</td>
          <td>5.789263</td>
          <td>5.629006</td>
          <td>5.669071</td>
          <td>0.958484</td>
          <td>267072</td>
        </tr>
        <tr>
          <th>1962-01-18</th>
          <td>5.669071</td>
          <td>5.729167</td>
          <td>5.659054</td>
          <td>5.729167</td>
          <td>0.968643</td>
          <td>184704</td>
        </tr>
        <tr>
          <th>1962-01-19</th>
          <td>5.729167</td>
          <td>5.779247</td>
          <td>5.729167</td>
          <td>5.779247</td>
          <td>0.977112</td>
          <td>165984</td>
        </tr>
        <tr>
          <th>1962-01-22</th>
          <td>5.789263</td>
          <td>5.869391</td>
          <td>5.789263</td>
          <td>5.799279</td>
          <td>0.980498</td>
          <td>177216</td>
        </tr>
        <tr>
          <th>1962-01-23</th>
          <td>5.779247</td>
          <td>5.779247</td>
          <td>5.669071</td>
          <td>5.689103</td>
          <td>0.961870</td>
          <td>284544</td>
        </tr>
        <tr>
          <th>1962-01-24</th>
          <td>5.689103</td>
          <td>5.819311</td>
          <td>5.669071</td>
          <td>5.799279</td>
          <td>0.980498</td>
          <td>199680</td>
        </tr>
        <tr>
          <th>1962-01-25</th>
          <td>5.799279</td>
          <td>5.839343</td>
          <td>5.699119</td>
          <td>5.739183</td>
          <td>0.970338</td>
          <td>198432</td>
        </tr>
        <tr>
          <th>1962-01-26</th>
          <td>5.739183</td>
          <td>5.749199</td>
          <td>5.699119</td>
          <td>5.719151</td>
          <td>0.966951</td>
          <td>126048</td>
        </tr>
        <tr>
          <th>1962-01-29</th>
          <td>5.719151</td>
          <td>5.749199</td>
          <td>5.709135</td>
          <td>5.729167</td>
          <td>0.968643</td>
          <td>127296</td>
        </tr>
        <tr>
          <th>1962-01-30</th>
          <td>5.799279</td>
          <td>5.889423</td>
          <td>5.799279</td>
          <td>5.829327</td>
          <td>0.985579</td>
          <td>222144</td>
        </tr>
        <tr>
          <th>1962-01-31</th>
          <td>5.829327</td>
          <td>6.009615</td>
          <td>5.819311</td>
          <td>6.009615</td>
          <td>1.016061</td>
          <td>234624</td>
        </tr>
        <tr>
          <th>1962-02-01</th>
          <td>6.009615</td>
          <td>6.039663</td>
          <td>5.909455</td>
          <td>5.969551</td>
          <td>1.009287</td>
          <td>320736</td>
        </tr>
        <tr>
          <th>1962-02-02</th>
          <td>5.969551</td>
          <td>5.999599</td>
          <td>5.929487</td>
          <td>5.999599</td>
          <td>1.014367</td>
          <td>184704</td>
        </tr>
        <tr>
          <th>1962-02-05</th>
          <td>5.989583</td>
          <td>5.989583</td>
          <td>5.889423</td>
          <td>5.889423</td>
          <td>0.995740</td>
          <td>175968</td>
        </tr>
        <tr>
          <th>1962-02-06</th>
          <td>5.909455</td>
          <td>5.969551</td>
          <td>5.909455</td>
          <td>5.949519</td>
          <td>1.005900</td>
          <td>129792</td>
        </tr>
        <tr>
          <th>1962-02-07</th>
          <td>5.949519</td>
          <td>6.009615</td>
          <td>5.929487</td>
          <td>6.009615</td>
          <td>1.016061</td>
          <td>210912</td>
        </tr>
        <tr>
          <th>1962-02-08</th>
          <td>6.009615</td>
          <td>6.049679</td>
          <td>5.999599</td>
          <td>6.049679</td>
          <td>1.022834</td>
          <td>219648</td>
        </tr>
        <tr>
          <th>1962-02-09</th>
          <td>6.049679</td>
          <td>6.049679</td>
          <td>5.939503</td>
          <td>6.019631</td>
          <td>1.017754</td>
          <td>188448</td>
        </tr>
        <tr>
          <th>1962-02-12</th>
          <td>6.019631</td>
          <td>6.039663</td>
          <td>5.989583</td>
          <td>6.019631</td>
          <td>1.017754</td>
          <td>102336</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-22</th>
          <td>103.050003</td>
          <td>104.510002</td>
          <td>102.550003</td>
          <td>104.050003</td>
          <td>104.050003</td>
          <td>5355000</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>103.639999</td>
          <td>105.989998</td>
          <td>103.330002</td>
          <td>105.300003</td>
          <td>105.300003</td>
          <td>6496200</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>105.760002</td>
          <td>110.970001</td>
          <td>105.220001</td>
          <td>107.440002</td>
          <td>107.440002</td>
          <td>11701000</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>107.879997</td>
          <td>108.279999</td>
          <td>103.690002</td>
          <td>103.849998</td>
          <td>103.849998</td>
          <td>8984300</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>103.389999</td>
          <td>105.379997</td>
          <td>103.099998</td>
          <td>105.260002</td>
          <td>105.260002</td>
          <td>5910800</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>104.949997</td>
          <td>105.239998</td>
          <td>104.120003</td>
          <td>104.870003</td>
          <td>104.870003</td>
          <td>5617100</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>105.760002</td>
          <td>106.769997</td>
          <td>105.279999</td>
          <td>106.230003</td>
          <td>106.230003</td>
          <td>4887100</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>106.339996</td>
          <td>107.139999</td>
          <td>105.300003</td>
          <td>106.690002</td>
          <td>106.690002</td>
          <td>4480800</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>106.160004</td>
          <td>106.339996</td>
          <td>104.820000</td>
          <td>105.970001</td>
          <td>105.970001</td>
          <td>4111700</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>105.870003</td>
          <td>106.400002</td>
          <td>104.290001</td>
          <td>105.209999</td>
          <td>105.209999</td>
          <td>4675800</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>106.930000</td>
          <td>109.650002</td>
          <td>106.849998</td>
          <td>108.739998</td>
          <td>108.739998</td>
          <td>7600000</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>109.400002</td>
          <td>110.309998</td>
          <td>108.320000</td>
          <td>108.419998</td>
          <td>108.419998</td>
          <td>5174500</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>114.730003</td>
          <td>116.169998</td>
          <td>110.480003</td>
          <td>111.290001</td>
          <td>111.290001</td>
          <td>25123700</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>112.500000</td>
          <td>112.680000</td>
          <td>108.110001</td>
          <td>108.959999</td>
          <td>108.959999</td>
          <td>8692600</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>108.550003</td>
          <td>109.599998</td>
          <td>106.779999</td>
          <td>107.000000</td>
          <td>107.000000</td>
          <td>5512800</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>107.400002</td>
          <td>107.930000</td>
          <td>106.459999</td>
          <td>107.589996</td>
          <td>107.589996</td>
          <td>7621900</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>108.029999</td>
          <td>108.669998</td>
          <td>106.199997</td>
          <td>106.669998</td>
          <td>106.669998</td>
          <td>6124900</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>106.150002</td>
          <td>106.209999</td>
          <td>102.820000</td>
          <td>103.349998</td>
          <td>103.349998</td>
          <td>11997700</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>103.699997</td>
          <td>103.879997</td>
          <td>101.419998</td>
          <td>101.989998</td>
          <td>101.989998</td>
          <td>8307600</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>101.430000</td>
          <td>101.800003</td>
          <td>99.180000</td>
          <td>100.669998</td>
          <td>100.669998</td>
          <td>8530900</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>99.800003</td>
          <td>100.739998</td>
          <td>99.300003</td>
          <td>99.959999</td>
          <td>99.959999</td>
          <td>6603300</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>100.470001</td>
          <td>101.970001</td>
          <td>100.279999</td>
          <td>101.040001</td>
          <td>101.040001</td>
          <td>6206600</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>101.779999</td>
          <td>102.209999</td>
          <td>101.150002</td>
          <td>102.080002</td>
          <td>102.080002</td>
          <td>6011400</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>101.860001</td>
          <td>102.320000</td>
          <td>101.309998</td>
          <td>102.230003</td>
          <td>102.230003</td>
          <td>5572100</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>96.660004</td>
          <td>98.099998</td>
          <td>95.510002</td>
          <td>97.839996</td>
          <td>97.839996</td>
          <td>8607600</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    <p>15086 rows × 6 columns</p>
    </div>



.. code:: ipython3

    GE = yf.download(ticker)


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed


.. code:: ipython3

    GE.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1962-01-02</th>
          <td>6.009615</td>
          <td>6.109776</td>
          <td>5.949519</td>
          <td>5.989583</td>
          <td>1.012674</td>
          <td>269568</td>
        </tr>
        <tr>
          <th>1962-01-03</th>
          <td>5.959535</td>
          <td>5.959535</td>
          <td>5.909455</td>
          <td>5.929487</td>
          <td>1.002513</td>
          <td>184704</td>
        </tr>
        <tr>
          <th>1962-01-04</th>
          <td>5.929487</td>
          <td>5.979567</td>
          <td>5.809295</td>
          <td>5.859375</td>
          <td>0.990659</td>
          <td>229632</td>
        </tr>
        <tr>
          <th>1962-01-05</th>
          <td>5.859375</td>
          <td>5.869391</td>
          <td>5.608974</td>
          <td>5.709135</td>
          <td>0.965257</td>
          <td>340704</td>
        </tr>
        <tr>
          <th>1962-01-08</th>
          <td>5.709135</td>
          <td>5.709135</td>
          <td>5.528846</td>
          <td>5.699119</td>
          <td>0.963564</td>
          <td>386880</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    GE.tail()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    </div>



 ### Adding Time Periods

.. code:: ipython3

    yf.download(ticker, start = "2014-01-01", end = "2018-12-31")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-01-02</th>
          <td>214.307693</td>
          <td>214.923080</td>
          <td>210.846161</td>
          <td>211.538467</td>
          <td>178.125061</td>
          <td>5388981</td>
        </tr>
        <tr>
          <th>2014-01-03</th>
          <td>211.692307</td>
          <td>212.307693</td>
          <td>210.846161</td>
          <td>211.384613</td>
          <td>177.995529</td>
          <td>3584204</td>
        </tr>
        <tr>
          <th>2014-01-06</th>
          <td>212.769226</td>
          <td>213.307693</td>
          <td>208.846161</td>
          <td>209.692307</td>
          <td>176.570511</td>
          <td>3816358</td>
        </tr>
        <tr>
          <th>2014-01-07</th>
          <td>211.384613</td>
          <td>211.461533</td>
          <td>209.307693</td>
          <td>209.923080</td>
          <td>176.764862</td>
          <td>3214640</td>
        </tr>
        <tr>
          <th>2014-01-08</th>
          <td>210.384613</td>
          <td>210.461533</td>
          <td>208.615387</td>
          <td>209.307693</td>
          <td>176.246704</td>
          <td>3362957</td>
        </tr>
        <tr>
          <th>2014-01-09</th>
          <td>210.230774</td>
          <td>210.461533</td>
          <td>207.153839</td>
          <td>209.384613</td>
          <td>176.311432</td>
          <td>4070482</td>
        </tr>
        <tr>
          <th>2014-01-10</th>
          <td>209.153839</td>
          <td>209.461533</td>
          <td>206.615387</td>
          <td>207.384613</td>
          <td>174.627335</td>
          <td>5047718</td>
        </tr>
        <tr>
          <th>2014-01-13</th>
          <td>207.538467</td>
          <td>208.461533</td>
          <td>205.230774</td>
          <td>205.615387</td>
          <td>173.137604</td>
          <td>4474496</td>
        </tr>
        <tr>
          <th>2014-01-14</th>
          <td>206.461533</td>
          <td>207.692307</td>
          <td>205.692307</td>
          <td>207.461533</td>
          <td>174.692108</td>
          <td>3242967</td>
        </tr>
        <tr>
          <th>2014-01-15</th>
          <td>208.846161</td>
          <td>210.769226</td>
          <td>207.769226</td>
          <td>210.307693</td>
          <td>177.088745</td>
          <td>4142229</td>
        </tr>
        <tr>
          <th>2014-01-16</th>
          <td>209.384613</td>
          <td>209.769226</td>
          <td>208.307693</td>
          <td>209.230774</td>
          <td>176.181900</td>
          <td>4244279</td>
        </tr>
        <tr>
          <th>2014-01-17</th>
          <td>206.769226</td>
          <td>207.076920</td>
          <td>202.153839</td>
          <td>204.461533</td>
          <td>172.165955</td>
          <td>12641278</td>
        </tr>
        <tr>
          <th>2014-01-21</th>
          <td>205.615387</td>
          <td>205.692307</td>
          <td>200.307693</td>
          <td>202.230774</td>
          <td>170.287552</td>
          <td>7792031</td>
        </tr>
        <tr>
          <th>2014-01-22</th>
          <td>202.307693</td>
          <td>202.384613</td>
          <td>199.923080</td>
          <td>199.923080</td>
          <td>168.344376</td>
          <td>6327529</td>
        </tr>
        <tr>
          <th>2014-01-23</th>
          <td>199.846161</td>
          <td>199.846161</td>
          <td>196.384613</td>
          <td>198.615387</td>
          <td>167.243286</td>
          <td>7546162</td>
        </tr>
        <tr>
          <th>2014-01-24</th>
          <td>196.692307</td>
          <td>196.846161</td>
          <td>191.923080</td>
          <td>191.923080</td>
          <td>161.608017</td>
          <td>12428650</td>
        </tr>
        <tr>
          <th>2014-01-27</th>
          <td>194.307693</td>
          <td>194.538467</td>
          <td>191.538467</td>
          <td>192.846161</td>
          <td>162.385315</td>
          <td>7871240</td>
        </tr>
        <tr>
          <th>2014-01-28</th>
          <td>194.846161</td>
          <td>197.076920</td>
          <td>194.615387</td>
          <td>195.846161</td>
          <td>164.911469</td>
          <td>6555354</td>
        </tr>
        <tr>
          <th>2014-01-29</th>
          <td>194.923080</td>
          <td>196.307693</td>
          <td>193.538467</td>
          <td>194.538467</td>
          <td>163.810287</td>
          <td>5151861</td>
        </tr>
        <tr>
          <th>2014-01-30</th>
          <td>196.153839</td>
          <td>196.846161</td>
          <td>194.846161</td>
          <td>196.153839</td>
          <td>165.170486</td>
          <td>3912246</td>
        </tr>
        <tr>
          <th>2014-01-31</th>
          <td>193.923080</td>
          <td>195.230774</td>
          <td>192.923080</td>
          <td>193.307693</td>
          <td>162.773956</td>
          <td>5243420</td>
        </tr>
        <tr>
          <th>2014-02-03</th>
          <td>193.307693</td>
          <td>193.923080</td>
          <td>187.076920</td>
          <td>187.307693</td>
          <td>157.721619</td>
          <td>9808682</td>
        </tr>
        <tr>
          <th>2014-02-04</th>
          <td>188.692307</td>
          <td>190.615387</td>
          <td>187.692307</td>
          <td>189.000000</td>
          <td>159.146652</td>
          <td>5961280</td>
        </tr>
        <tr>
          <th>2014-02-05</th>
          <td>188.153839</td>
          <td>189.538467</td>
          <td>187.076920</td>
          <td>188.615387</td>
          <td>158.822800</td>
          <td>5233761</td>
        </tr>
        <tr>
          <th>2014-02-06</th>
          <td>190.769226</td>
          <td>193.076920</td>
          <td>189.384613</td>
          <td>191.923080</td>
          <td>161.608017</td>
          <td>5814172</td>
        </tr>
        <tr>
          <th>2014-02-07</th>
          <td>193.846161</td>
          <td>194.461533</td>
          <td>192.307693</td>
          <td>193.769226</td>
          <td>163.162582</td>
          <td>4513717</td>
        </tr>
        <tr>
          <th>2014-02-10</th>
          <td>195.307693</td>
          <td>195.307693</td>
          <td>191.769226</td>
          <td>192.692307</td>
          <td>162.255753</td>
          <td>4290572</td>
        </tr>
        <tr>
          <th>2014-02-11</th>
          <td>193.923080</td>
          <td>196.307693</td>
          <td>193.538467</td>
          <td>195.615387</td>
          <td>164.717087</td>
          <td>4236362</td>
        </tr>
        <tr>
          <th>2014-02-12</th>
          <td>196.692307</td>
          <td>197.153839</td>
          <td>195.000000</td>
          <td>195.307693</td>
          <td>164.458023</td>
          <td>3279627</td>
        </tr>
        <tr>
          <th>2014-02-13</th>
          <td>194.076920</td>
          <td>195.692307</td>
          <td>193.153839</td>
          <td>195.692307</td>
          <td>164.781876</td>
          <td>4206436</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2018-11-14</th>
          <td>67.384613</td>
          <td>68.076920</td>
          <td>63.000000</td>
          <td>64.000000</td>
          <td>63.191135</td>
          <td>22122074</td>
        </tr>
        <tr>
          <th>2018-11-15</th>
          <td>63.384617</td>
          <td>66.153847</td>
          <td>62.000000</td>
          <td>62.846153</td>
          <td>62.051872</td>
          <td>16701737</td>
        </tr>
        <tr>
          <th>2018-11-16</th>
          <td>62.153847</td>
          <td>63.076923</td>
          <td>59.461536</td>
          <td>61.692307</td>
          <td>60.912609</td>
          <td>22959157</td>
        </tr>
        <tr>
          <th>2018-11-19</th>
          <td>61.461536</td>
          <td>63.384617</td>
          <td>59.923077</td>
          <td>60.307693</td>
          <td>59.545494</td>
          <td>19250049</td>
        </tr>
        <tr>
          <th>2018-11-20</th>
          <td>59.000000</td>
          <td>60.461536</td>
          <td>57.923077</td>
          <td>58.846153</td>
          <td>58.102425</td>
          <td>18630235</td>
        </tr>
        <tr>
          <th>2018-11-21</th>
          <td>59.923077</td>
          <td>61.000000</td>
          <td>59.461536</td>
          <td>60.076923</td>
          <td>59.317650</td>
          <td>10977564</td>
        </tr>
        <tr>
          <th>2018-11-23</th>
          <td>59.846153</td>
          <td>60.461536</td>
          <td>58.076923</td>
          <td>58.230770</td>
          <td>57.494827</td>
          <td>5651243</td>
        </tr>
        <tr>
          <th>2018-11-26</th>
          <td>58.538464</td>
          <td>59.538464</td>
          <td>55.846153</td>
          <td>58.307693</td>
          <td>57.570770</td>
          <td>20624214</td>
        </tr>
        <tr>
          <th>2018-11-27</th>
          <td>57.615383</td>
          <td>58.692307</td>
          <td>56.692307</td>
          <td>57.230770</td>
          <td>56.507458</td>
          <td>14352910</td>
        </tr>
        <tr>
          <th>2018-11-28</th>
          <td>56.846153</td>
          <td>59.769230</td>
          <td>56.692307</td>
          <td>59.538464</td>
          <td>58.785984</td>
          <td>16159936</td>
        </tr>
        <tr>
          <th>2018-11-29</th>
          <td>58.846153</td>
          <td>61.538464</td>
          <td>57.615383</td>
          <td>61.076923</td>
          <td>60.305000</td>
          <td>16039829</td>
        </tr>
        <tr>
          <th>2018-11-30</th>
          <td>58.923077</td>
          <td>59.076923</td>
          <td>56.923077</td>
          <td>57.692307</td>
          <td>56.963165</td>
          <td>24320777</td>
        </tr>
        <tr>
          <th>2018-12-03</th>
          <td>58.000000</td>
          <td>61.153847</td>
          <td>57.923077</td>
          <td>60.076923</td>
          <td>59.317650</td>
          <td>16988725</td>
        </tr>
        <tr>
          <th>2018-12-04</th>
          <td>59.615383</td>
          <td>60.076923</td>
          <td>56.000000</td>
          <td>56.000000</td>
          <td>55.292244</td>
          <td>17332874</td>
        </tr>
        <tr>
          <th>2018-12-06</th>
          <td>55.384617</td>
          <td>56.846153</td>
          <td>55.000000</td>
          <td>56.538464</td>
          <td>55.823910</td>
          <td>14685541</td>
        </tr>
        <tr>
          <th>2018-12-07</th>
          <td>56.153847</td>
          <td>56.769230</td>
          <td>53.769230</td>
          <td>53.923077</td>
          <td>53.241570</td>
          <td>14882413</td>
        </tr>
        <tr>
          <th>2018-12-10</th>
          <td>53.615383</td>
          <td>54.769230</td>
          <td>51.923077</td>
          <td>53.307693</td>
          <td>52.633961</td>
          <td>14669434</td>
        </tr>
        <tr>
          <th>2018-12-11</th>
          <td>54.153847</td>
          <td>54.846153</td>
          <td>51.230770</td>
          <td>52.000000</td>
          <td>51.342793</td>
          <td>16195478</td>
        </tr>
        <tr>
          <th>2018-12-12</th>
          <td>52.615383</td>
          <td>54.076923</td>
          <td>51.538464</td>
          <td>51.615383</td>
          <td>50.963039</td>
          <td>13756600</td>
        </tr>
        <tr>
          <th>2018-12-13</th>
          <td>57.615383</td>
          <td>57.692307</td>
          <td>54.769230</td>
          <td>55.384617</td>
          <td>54.684647</td>
          <td>26946660</td>
        </tr>
        <tr>
          <th>2018-12-14</th>
          <td>54.461536</td>
          <td>55.769230</td>
          <td>53.846153</td>
          <td>54.615383</td>
          <td>53.925125</td>
          <td>16744091</td>
        </tr>
        <tr>
          <th>2018-12-17</th>
          <td>54.538464</td>
          <td>55.615383</td>
          <td>53.923077</td>
          <td>55.000000</td>
          <td>54.304890</td>
          <td>16865043</td>
        </tr>
        <tr>
          <th>2018-12-18</th>
          <td>55.230770</td>
          <td>58.692307</td>
          <td>55.076923</td>
          <td>56.000000</td>
          <td>55.292244</td>
          <td>19080555</td>
        </tr>
        <tr>
          <th>2018-12-19</th>
          <td>58.769230</td>
          <td>61.153847</td>
          <td>58.076923</td>
          <td>58.923077</td>
          <td>58.258404</td>
          <td>28531646</td>
        </tr>
        <tr>
          <th>2018-12-20</th>
          <td>58.846153</td>
          <td>60.153847</td>
          <td>56.615383</td>
          <td>57.230770</td>
          <td>56.585190</td>
          <td>23705968</td>
        </tr>
        <tr>
          <th>2018-12-21</th>
          <td>56.307693</td>
          <td>57.307693</td>
          <td>54.615383</td>
          <td>55.000000</td>
          <td>54.379585</td>
          <td>24134669</td>
        </tr>
        <tr>
          <th>2018-12-24</th>
          <td>54.307693</td>
          <td>54.846153</td>
          <td>53.076923</td>
          <td>53.230770</td>
          <td>52.630310</td>
          <td>9101352</td>
        </tr>
        <tr>
          <th>2018-12-26</th>
          <td>53.769230</td>
          <td>57.000000</td>
          <td>52.076923</td>
          <td>56.846153</td>
          <td>56.204914</td>
          <td>16879018</td>
        </tr>
        <tr>
          <th>2018-12-27</th>
          <td>55.230770</td>
          <td>55.923077</td>
          <td>53.461536</td>
          <td>55.923077</td>
          <td>55.292244</td>
          <td>15571218</td>
        </tr>
        <tr>
          <th>2018-12-28</th>
          <td>55.307693</td>
          <td>58.846153</td>
          <td>55.307693</td>
          <td>57.769230</td>
          <td>57.117569</td>
          <td>15817204</td>
        </tr>
      </tbody>
    </table>
    <p>1257 rows × 6 columns</p>
    </div>



.. code:: ipython3

    GE = yf.download(ticker, start = "2014-01-01", end = "2018-12-31")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed


.. code:: ipython3

    GE.info()


.. parsed-literal::

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 1257 entries, 2014-01-02 to 2018-12-28
    Data columns (total 6 columns):
    Open         1257 non-null float64
    High         1257 non-null float64
    Low          1257 non-null float64
    Close        1257 non-null float64
    Adj Close    1257 non-null float64
    Volume       1257 non-null int64
    dtypes: float64(5), int64(1)
    memory usage: 68.7 KB


.. code:: ipython3

    yf.download(ticker, period = "ytd")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-01-04</th>
          <td>87.120003</td>
          <td>87.199997</td>
          <td>83.199997</td>
          <td>83.760002</td>
          <td>83.569649</td>
          <td>9993688</td>
        </tr>
        <tr>
          <th>2021-01-05</th>
          <td>83.440002</td>
          <td>87.040001</td>
          <td>83.360001</td>
          <td>86.160004</td>
          <td>85.964195</td>
          <td>10462538</td>
        </tr>
        <tr>
          <th>2021-01-06</th>
          <td>86.639999</td>
          <td>92.959999</td>
          <td>86.639999</td>
          <td>90.879997</td>
          <td>90.673462</td>
          <td>16448075</td>
        </tr>
        <tr>
          <th>2021-01-07</th>
          <td>92.480003</td>
          <td>92.559998</td>
          <td>89.919998</td>
          <td>90.160004</td>
          <td>89.955109</td>
          <td>9411225</td>
        </tr>
        <tr>
          <th>2021-01-08</th>
          <td>90.320000</td>
          <td>91.519997</td>
          <td>89.279999</td>
          <td>90.720001</td>
          <td>90.513832</td>
          <td>9089963</td>
        </tr>
        <tr>
          <th>2021-01-11</th>
          <td>88.879997</td>
          <td>92.239998</td>
          <td>88.480003</td>
          <td>91.599998</td>
          <td>91.391830</td>
          <td>8406700</td>
        </tr>
        <tr>
          <th>2021-01-12</th>
          <td>92.080002</td>
          <td>95.279999</td>
          <td>91.279999</td>
          <td>94.239998</td>
          <td>94.025826</td>
          <td>11429913</td>
        </tr>
        <tr>
          <th>2021-01-13</th>
          <td>94.239998</td>
          <td>94.559998</td>
          <td>92.160004</td>
          <td>92.559998</td>
          <td>92.349640</td>
          <td>6714200</td>
        </tr>
        <tr>
          <th>2021-01-14</th>
          <td>92.879997</td>
          <td>93.839996</td>
          <td>92.639999</td>
          <td>93.279999</td>
          <td>93.068008</td>
          <td>7401188</td>
        </tr>
        <tr>
          <th>2021-01-15</th>
          <td>92.800003</td>
          <td>92.800003</td>
          <td>90.000000</td>
          <td>90.639999</td>
          <td>90.434006</td>
          <td>9201188</td>
        </tr>
        <tr>
          <th>2021-01-19</th>
          <td>91.839996</td>
          <td>93.199997</td>
          <td>91.199997</td>
          <td>91.440002</td>
          <td>91.232193</td>
          <td>7937425</td>
        </tr>
        <tr>
          <th>2021-01-20</th>
          <td>92.000000</td>
          <td>92.000000</td>
          <td>90.400002</td>
          <td>91.120003</td>
          <td>90.912926</td>
          <td>7376988</td>
        </tr>
        <tr>
          <th>2021-01-21</th>
          <td>91.199997</td>
          <td>91.440002</td>
          <td>88.559998</td>
          <td>88.559998</td>
          <td>88.358727</td>
          <td>8200338</td>
        </tr>
        <tr>
          <th>2021-01-22</th>
          <td>87.760002</td>
          <td>89.440002</td>
          <td>87.199997</td>
          <td>88.879997</td>
          <td>88.678009</td>
          <td>6614925</td>
        </tr>
        <tr>
          <th>2021-01-25</th>
          <td>89.120003</td>
          <td>89.199997</td>
          <td>86.160004</td>
          <td>87.919998</td>
          <td>87.720184</td>
          <td>11502613</td>
        </tr>
        <tr>
          <th>2021-01-26</th>
          <td>96.239998</td>
          <td>97.839996</td>
          <td>89.599998</td>
          <td>90.320000</td>
          <td>90.114731</td>
          <td>26475425</td>
        </tr>
        <tr>
          <th>2021-01-27</th>
          <td>88.639999</td>
          <td>92.480003</td>
          <td>85.120003</td>
          <td>91.040001</td>
          <td>90.833107</td>
          <td>18679988</td>
        </tr>
        <tr>
          <th>2021-01-28</th>
          <td>91.279999</td>
          <td>91.760002</td>
          <td>88.559998</td>
          <td>88.720001</td>
          <td>88.518372</td>
          <td>11762413</td>
        </tr>
        <tr>
          <th>2021-01-29</th>
          <td>88.000000</td>
          <td>89.919998</td>
          <td>85.360001</td>
          <td>85.440002</td>
          <td>85.245834</td>
          <td>13657350</td>
        </tr>
        <tr>
          <th>2021-02-01</th>
          <td>86.879997</td>
          <td>88.000000</td>
          <td>85.120003</td>
          <td>85.919998</td>
          <td>85.724731</td>
          <td>8335725</td>
        </tr>
        <tr>
          <th>2021-02-02</th>
          <td>87.040001</td>
          <td>90.800003</td>
          <td>86.720001</td>
          <td>89.919998</td>
          <td>89.715645</td>
          <td>10558238</td>
        </tr>
        <tr>
          <th>2021-02-03</th>
          <td>89.919998</td>
          <td>90.400002</td>
          <td>88.559998</td>
          <td>89.599998</td>
          <td>89.396378</td>
          <td>6776850</td>
        </tr>
        <tr>
          <th>2021-02-04</th>
          <td>89.839996</td>
          <td>92.000000</td>
          <td>89.519997</td>
          <td>91.599998</td>
          <td>91.391830</td>
          <td>8345975</td>
        </tr>
        <tr>
          <th>2021-02-05</th>
          <td>92.080002</td>
          <td>92.400002</td>
          <td>90.559998</td>
          <td>91.199997</td>
          <td>90.992737</td>
          <td>6477300</td>
        </tr>
        <tr>
          <th>2021-02-08</th>
          <td>91.760002</td>
          <td>93.199997</td>
          <td>91.279999</td>
          <td>92.879997</td>
          <td>92.668915</td>
          <td>5306813</td>
        </tr>
        <tr>
          <th>2021-02-09</th>
          <td>92.480003</td>
          <td>92.800003</td>
          <td>91.279999</td>
          <td>92.320000</td>
          <td>92.110191</td>
          <td>6592288</td>
        </tr>
        <tr>
          <th>2021-02-10</th>
          <td>92.720001</td>
          <td>92.720001</td>
          <td>91.040001</td>
          <td>91.199997</td>
          <td>90.992737</td>
          <td>5694988</td>
        </tr>
        <tr>
          <th>2021-02-11</th>
          <td>91.120003</td>
          <td>91.760002</td>
          <td>89.519997</td>
          <td>91.680000</td>
          <td>91.471649</td>
          <td>6478650</td>
        </tr>
        <tr>
          <th>2021-02-12</th>
          <td>91.279999</td>
          <td>93.919998</td>
          <td>91.040001</td>
          <td>93.839996</td>
          <td>93.626732</td>
          <td>7304963</td>
        </tr>
        <tr>
          <th>2021-02-16</th>
          <td>94.559998</td>
          <td>95.839996</td>
          <td>94.239998</td>
          <td>95.760002</td>
          <td>95.542381</td>
          <td>7539000</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-22</th>
          <td>103.050003</td>
          <td>104.510002</td>
          <td>102.550003</td>
          <td>104.050003</td>
          <td>104.050003</td>
          <td>5355000</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>103.639999</td>
          <td>105.989998</td>
          <td>103.330002</td>
          <td>105.300003</td>
          <td>105.300003</td>
          <td>6496200</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>105.760002</td>
          <td>110.970001</td>
          <td>105.220001</td>
          <td>107.440002</td>
          <td>107.440002</td>
          <td>11701000</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>107.879997</td>
          <td>108.279999</td>
          <td>103.690002</td>
          <td>103.849998</td>
          <td>103.849998</td>
          <td>8984300</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>103.389999</td>
          <td>105.379997</td>
          <td>103.099998</td>
          <td>105.260002</td>
          <td>105.260002</td>
          <td>5910800</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>104.949997</td>
          <td>105.239998</td>
          <td>104.120003</td>
          <td>104.870003</td>
          <td>104.870003</td>
          <td>5617100</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>105.760002</td>
          <td>106.769997</td>
          <td>105.279999</td>
          <td>106.230003</td>
          <td>106.230003</td>
          <td>4887100</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>106.339996</td>
          <td>107.139999</td>
          <td>105.300003</td>
          <td>106.690002</td>
          <td>106.690002</td>
          <td>4480800</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>106.160004</td>
          <td>106.339996</td>
          <td>104.820000</td>
          <td>105.970001</td>
          <td>105.970001</td>
          <td>4111700</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>105.870003</td>
          <td>106.400002</td>
          <td>104.290001</td>
          <td>105.209999</td>
          <td>105.209999</td>
          <td>4675800</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>106.930000</td>
          <td>109.650002</td>
          <td>106.849998</td>
          <td>108.739998</td>
          <td>108.739998</td>
          <td>7600000</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>109.400002</td>
          <td>110.309998</td>
          <td>108.320000</td>
          <td>108.419998</td>
          <td>108.419998</td>
          <td>5174500</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>114.730003</td>
          <td>116.169998</td>
          <td>110.480003</td>
          <td>111.290001</td>
          <td>111.290001</td>
          <td>25123700</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>112.500000</td>
          <td>112.680000</td>
          <td>108.110001</td>
          <td>108.959999</td>
          <td>108.959999</td>
          <td>8692600</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>108.550003</td>
          <td>109.599998</td>
          <td>106.779999</td>
          <td>107.000000</td>
          <td>107.000000</td>
          <td>5512800</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>107.400002</td>
          <td>107.930000</td>
          <td>106.459999</td>
          <td>107.589996</td>
          <td>107.589996</td>
          <td>7621900</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>108.029999</td>
          <td>108.669998</td>
          <td>106.199997</td>
          <td>106.669998</td>
          <td>106.669998</td>
          <td>6124900</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>106.150002</td>
          <td>106.209999</td>
          <td>102.820000</td>
          <td>103.349998</td>
          <td>103.349998</td>
          <td>11997700</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>103.699997</td>
          <td>103.879997</td>
          <td>101.419998</td>
          <td>101.989998</td>
          <td>101.989998</td>
          <td>8307600</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>101.430000</td>
          <td>101.800003</td>
          <td>99.180000</td>
          <td>100.669998</td>
          <td>100.669998</td>
          <td>8530900</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>99.800003</td>
          <td>100.739998</td>
          <td>99.300003</td>
          <td>99.959999</td>
          <td>99.959999</td>
          <td>6603300</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>100.470001</td>
          <td>101.970001</td>
          <td>100.279999</td>
          <td>101.040001</td>
          <td>101.040001</td>
          <td>6206600</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>101.779999</td>
          <td>102.209999</td>
          <td>101.150002</td>
          <td>102.080002</td>
          <td>102.080002</td>
          <td>6011400</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>101.860001</td>
          <td>102.320000</td>
          <td>101.309998</td>
          <td>102.230003</td>
          <td>102.230003</td>
          <td>5572100</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>96.660004</td>
          <td>98.099998</td>
          <td>95.510002</td>
          <td>97.839996</td>
          <td>97.839996</td>
          <td>8607600</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    <p>233 rows × 6 columns</p>
    </div>



.. code:: ipython3

    yf.download(ticker, period = "1mo")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-04</th>
          <td>105.870003</td>
          <td>106.400002</td>
          <td>104.290001</td>
          <td>105.209999</td>
          <td>105.209999</td>
          <td>4675800</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>106.930000</td>
          <td>109.650002</td>
          <td>106.849998</td>
          <td>108.739998</td>
          <td>108.739998</td>
          <td>7600000</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>109.400002</td>
          <td>110.309998</td>
          <td>108.320000</td>
          <td>108.419998</td>
          <td>108.419998</td>
          <td>5174500</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>114.730003</td>
          <td>116.169998</td>
          <td>110.480003</td>
          <td>111.290001</td>
          <td>111.290001</td>
          <td>25123700</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>112.500000</td>
          <td>112.680000</td>
          <td>108.110001</td>
          <td>108.959999</td>
          <td>108.959999</td>
          <td>8692600</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>108.550003</td>
          <td>109.599998</td>
          <td>106.779999</td>
          <td>107.000000</td>
          <td>107.000000</td>
          <td>5512800</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>107.400002</td>
          <td>107.930000</td>
          <td>106.459999</td>
          <td>107.589996</td>
          <td>107.589996</td>
          <td>7621900</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>108.029999</td>
          <td>108.669998</td>
          <td>106.199997</td>
          <td>106.669998</td>
          <td>106.669998</td>
          <td>6124900</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>106.150002</td>
          <td>106.209999</td>
          <td>102.820000</td>
          <td>103.349998</td>
          <td>103.349998</td>
          <td>11997700</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>103.699997</td>
          <td>103.879997</td>
          <td>101.419998</td>
          <td>101.989998</td>
          <td>101.989998</td>
          <td>8307600</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>101.430000</td>
          <td>101.800003</td>
          <td>99.180000</td>
          <td>100.669998</td>
          <td>100.669998</td>
          <td>8530900</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>99.800003</td>
          <td>100.739998</td>
          <td>99.300003</td>
          <td>99.959999</td>
          <td>99.959999</td>
          <td>6603300</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>100.470001</td>
          <td>101.970001</td>
          <td>100.279999</td>
          <td>101.040001</td>
          <td>101.040001</td>
          <td>6206600</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>101.779999</td>
          <td>102.209999</td>
          <td>101.150002</td>
          <td>102.080002</td>
          <td>102.080002</td>
          <td>6011400</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>101.860001</td>
          <td>102.320000</td>
          <td>101.309998</td>
          <td>102.230003</td>
          <td>102.230003</td>
          <td>5572100</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>96.660004</td>
          <td>98.099998</td>
          <td>95.510002</td>
          <td>97.839996</td>
          <td>97.839996</td>
          <td>8607600</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    yf.download(ticker, period = "5d")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    yf.download(ticker, period = "10y")


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2011-12-05</th>
          <td>125.769234</td>
          <td>126.923080</td>
          <td>124.461540</td>
          <td>125.615387</td>
          <td>97.810074</td>
          <td>8006050</td>
        </tr>
        <tr>
          <th>2011-12-06</th>
          <td>126.923080</td>
          <td>130.153839</td>
          <td>126.692307</td>
          <td>128.615387</td>
          <td>100.145996</td>
          <td>10792249</td>
        </tr>
        <tr>
          <th>2011-12-07</th>
          <td>128.307693</td>
          <td>129.461533</td>
          <td>127.153847</td>
          <td>128.769226</td>
          <td>100.265793</td>
          <td>8491054</td>
        </tr>
        <tr>
          <th>2011-12-08</th>
          <td>127.538460</td>
          <td>128.076920</td>
          <td>125.000000</td>
          <td>125.461540</td>
          <td>97.690247</td>
          <td>10364263</td>
        </tr>
        <tr>
          <th>2011-12-09</th>
          <td>126.000000</td>
          <td>130.615387</td>
          <td>125.846153</td>
          <td>129.538467</td>
          <td>100.864769</td>
          <td>11145940</td>
        </tr>
        <tr>
          <th>2011-12-12</th>
          <td>128.538467</td>
          <td>129.692307</td>
          <td>125.538460</td>
          <td>126.615387</td>
          <td>98.588707</td>
          <td>23322715</td>
        </tr>
        <tr>
          <th>2011-12-13</th>
          <td>127.384613</td>
          <td>128.615387</td>
          <td>125.384613</td>
          <td>126.307693</td>
          <td>98.349113</td>
          <td>9602632</td>
        </tr>
        <tr>
          <th>2011-12-14</th>
          <td>125.692307</td>
          <td>129.000000</td>
          <td>125.384613</td>
          <td>127.769234</td>
          <td>99.487129</td>
          <td>11581466</td>
        </tr>
        <tr>
          <th>2011-12-15</th>
          <td>129.384613</td>
          <td>129.769226</td>
          <td>127.615387</td>
          <td>129.153839</td>
          <td>100.565247</td>
          <td>7985822</td>
        </tr>
        <tr>
          <th>2011-12-16</th>
          <td>130.307693</td>
          <td>131.461533</td>
          <td>130.076920</td>
          <td>130.846161</td>
          <td>101.882957</td>
          <td>12543440</td>
        </tr>
        <tr>
          <th>2011-12-19</th>
          <td>130.538467</td>
          <td>131.538467</td>
          <td>129.153839</td>
          <td>129.692307</td>
          <td>100.984566</td>
          <td>8619377</td>
        </tr>
        <tr>
          <th>2011-12-20</th>
          <td>131.153839</td>
          <td>133.769226</td>
          <td>131.076920</td>
          <td>132.923080</td>
          <td>103.500153</td>
          <td>7991269</td>
        </tr>
        <tr>
          <th>2011-12-21</th>
          <td>133.230774</td>
          <td>136.692307</td>
          <td>131.923080</td>
          <td>136.076920</td>
          <td>105.955887</td>
          <td>10436738</td>
        </tr>
        <tr>
          <th>2011-12-22</th>
          <td>136.153839</td>
          <td>139.538467</td>
          <td>135.769226</td>
          <td>138.846161</td>
          <td>109.161209</td>
          <td>12432238</td>
        </tr>
        <tr>
          <th>2011-12-23</th>
          <td>138.615387</td>
          <td>140.615387</td>
          <td>138.076920</td>
          <td>140.230774</td>
          <td>110.249771</td>
          <td>6121726</td>
        </tr>
        <tr>
          <th>2011-12-27</th>
          <td>139.846161</td>
          <td>140.000000</td>
          <td>138.538467</td>
          <td>138.538467</td>
          <td>108.919304</td>
          <td>5493475</td>
        </tr>
        <tr>
          <th>2011-12-28</th>
          <td>138.461533</td>
          <td>138.615387</td>
          <td>136.307693</td>
          <td>137.153839</td>
          <td>107.830681</td>
          <td>5105438</td>
        </tr>
        <tr>
          <th>2011-12-29</th>
          <td>137.000000</td>
          <td>139.384613</td>
          <td>136.846161</td>
          <td>139.000000</td>
          <td>109.282135</td>
          <td>5624710</td>
        </tr>
        <tr>
          <th>2011-12-30</th>
          <td>138.692307</td>
          <td>139.076920</td>
          <td>137.538467</td>
          <td>137.769226</td>
          <td>108.314499</td>
          <td>4083014</td>
        </tr>
        <tr>
          <th>2012-01-03</th>
          <td>140.230774</td>
          <td>142.307693</td>
          <td>140.230774</td>
          <td>141.230774</td>
          <td>111.036011</td>
          <td>7631858</td>
        </tr>
        <tr>
          <th>2012-01-04</th>
          <td>140.846161</td>
          <td>143.076920</td>
          <td>140.615387</td>
          <td>142.769226</td>
          <td>112.245483</td>
          <td>5558111</td>
        </tr>
        <tr>
          <th>2012-01-05</th>
          <td>142.000000</td>
          <td>143.076920</td>
          <td>140.692307</td>
          <td>142.692307</td>
          <td>112.185036</td>
          <td>5956496</td>
        </tr>
        <tr>
          <th>2012-01-06</th>
          <td>144.076920</td>
          <td>144.538467</td>
          <td>142.769226</td>
          <td>143.461533</td>
          <td>112.789803</td>
          <td>6639022</td>
        </tr>
        <tr>
          <th>2012-01-09</th>
          <td>144.153839</td>
          <td>145.230774</td>
          <td>142.769226</td>
          <td>145.076920</td>
          <td>114.059845</td>
          <td>6108362</td>
        </tr>
        <tr>
          <th>2012-01-10</th>
          <td>146.230774</td>
          <td>146.538467</td>
          <td>143.230774</td>
          <td>144.000000</td>
          <td>113.213127</td>
          <td>7714772</td>
        </tr>
        <tr>
          <th>2012-01-11</th>
          <td>142.692307</td>
          <td>145.769226</td>
          <td>142.307693</td>
          <td>145.230774</td>
          <td>114.180794</td>
          <td>6222879</td>
        </tr>
        <tr>
          <th>2012-01-12</th>
          <td>145.846161</td>
          <td>146.153839</td>
          <td>144.307693</td>
          <td>145.615387</td>
          <td>114.483177</td>
          <td>5064514</td>
        </tr>
        <tr>
          <th>2012-01-13</th>
          <td>144.461533</td>
          <td>144.923080</td>
          <td>143.076920</td>
          <td>144.923080</td>
          <td>113.938889</td>
          <td>5464849</td>
        </tr>
        <tr>
          <th>2012-01-17</th>
          <td>146.076920</td>
          <td>146.923080</td>
          <td>143.692307</td>
          <td>144.153839</td>
          <td>113.334076</td>
          <td>6396884</td>
        </tr>
        <tr>
          <th>2012-01-18</th>
          <td>142.923080</td>
          <td>146.538467</td>
          <td>142.769226</td>
          <td>146.307693</td>
          <td>115.027473</td>
          <td>6878638</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-22</th>
          <td>103.050003</td>
          <td>104.510002</td>
          <td>102.550003</td>
          <td>104.050003</td>
          <td>104.050003</td>
          <td>5355000</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>103.639999</td>
          <td>105.989998</td>
          <td>103.330002</td>
          <td>105.300003</td>
          <td>105.300003</td>
          <td>6496200</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>105.760002</td>
          <td>110.970001</td>
          <td>105.220001</td>
          <td>107.440002</td>
          <td>107.440002</td>
          <td>11701000</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>107.879997</td>
          <td>108.279999</td>
          <td>103.690002</td>
          <td>103.849998</td>
          <td>103.849998</td>
          <td>8984300</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>103.389999</td>
          <td>105.379997</td>
          <td>103.099998</td>
          <td>105.260002</td>
          <td>105.260002</td>
          <td>5910800</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>104.949997</td>
          <td>105.239998</td>
          <td>104.120003</td>
          <td>104.870003</td>
          <td>104.870003</td>
          <td>5617100</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>105.760002</td>
          <td>106.769997</td>
          <td>105.279999</td>
          <td>106.230003</td>
          <td>106.230003</td>
          <td>4887100</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>106.339996</td>
          <td>107.139999</td>
          <td>105.300003</td>
          <td>106.690002</td>
          <td>106.690002</td>
          <td>4480800</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>106.160004</td>
          <td>106.339996</td>
          <td>104.820000</td>
          <td>105.970001</td>
          <td>105.970001</td>
          <td>4111700</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>105.870003</td>
          <td>106.400002</td>
          <td>104.290001</td>
          <td>105.209999</td>
          <td>105.209999</td>
          <td>4675800</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>106.930000</td>
          <td>109.650002</td>
          <td>106.849998</td>
          <td>108.739998</td>
          <td>108.739998</td>
          <td>7600000</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>109.400002</td>
          <td>110.309998</td>
          <td>108.320000</td>
          <td>108.419998</td>
          <td>108.419998</td>
          <td>5174500</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>114.730003</td>
          <td>116.169998</td>
          <td>110.480003</td>
          <td>111.290001</td>
          <td>111.290001</td>
          <td>25123700</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>112.500000</td>
          <td>112.680000</td>
          <td>108.110001</td>
          <td>108.959999</td>
          <td>108.959999</td>
          <td>8692600</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>108.550003</td>
          <td>109.599998</td>
          <td>106.779999</td>
          <td>107.000000</td>
          <td>107.000000</td>
          <td>5512800</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>107.400002</td>
          <td>107.930000</td>
          <td>106.459999</td>
          <td>107.589996</td>
          <td>107.589996</td>
          <td>7621900</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>108.029999</td>
          <td>108.669998</td>
          <td>106.199997</td>
          <td>106.669998</td>
          <td>106.669998</td>
          <td>6124900</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>106.150002</td>
          <td>106.209999</td>
          <td>102.820000</td>
          <td>103.349998</td>
          <td>103.349998</td>
          <td>11997700</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>103.699997</td>
          <td>103.879997</td>
          <td>101.419998</td>
          <td>101.989998</td>
          <td>101.989998</td>
          <td>8307600</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>101.430000</td>
          <td>101.800003</td>
          <td>99.180000</td>
          <td>100.669998</td>
          <td>100.669998</td>
          <td>8530900</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>99.800003</td>
          <td>100.739998</td>
          <td>99.300003</td>
          <td>99.959999</td>
          <td>99.959999</td>
          <td>6603300</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>100.470001</td>
          <td>101.970001</td>
          <td>100.279999</td>
          <td>101.040001</td>
          <td>101.040001</td>
          <td>6206600</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>101.779999</td>
          <td>102.209999</td>
          <td>101.150002</td>
          <td>102.080002</td>
          <td>102.080002</td>
          <td>6011400</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>101.860001</td>
          <td>102.320000</td>
          <td>101.309998</td>
          <td>102.230003</td>
          <td>102.230003</td>
          <td>5572100</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>96.660004</td>
          <td>98.099998</td>
          <td>95.510002</td>
          <td>97.839996</td>
          <td>97.839996</td>
          <td>8607600</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>96.830002</td>
          <td>98.400002</td>
          <td>98.400002</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>94.470001</td>
          <td>94.989998</td>
          <td>94.989998</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>94.199997</td>
          <td>95.779999</td>
          <td>92.809998</td>
          <td>95.230003</td>
          <td>95.230003</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>91.730003</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    <p>2517 rows × 6 columns</p>
    </div>



 ### Frequency Setting

.. code:: ipython3

    yf.download('GE',period='1mo',interval='1h')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-04 09:30:00-04:00</th>
          <td>105.870003</td>
          <td>106.330002</td>
          <td>104.910004</td>
          <td>104.930000</td>
          <td>104.930000</td>
          <td>724501</td>
        </tr>
        <tr>
          <th>2021-11-04 10:30:00-04:00</th>
          <td>104.955002</td>
          <td>105.029999</td>
          <td>104.290001</td>
          <td>104.324997</td>
          <td>104.324997</td>
          <td>785864</td>
        </tr>
        <tr>
          <th>2021-11-04 11:30:00-04:00</th>
          <td>104.309998</td>
          <td>104.989998</td>
          <td>104.309998</td>
          <td>104.989998</td>
          <td>104.989998</td>
          <td>714845</td>
        </tr>
        <tr>
          <th>2021-11-04 12:30:00-04:00</th>
          <td>105.000000</td>
          <td>105.379997</td>
          <td>104.610001</td>
          <td>104.889999</td>
          <td>104.889999</td>
          <td>566135</td>
        </tr>
        <tr>
          <th>2021-11-04 13:30:00-04:00</th>
          <td>104.900002</td>
          <td>105.019997</td>
          <td>104.500000</td>
          <td>104.614998</td>
          <td>104.614998</td>
          <td>409374</td>
        </tr>
        <tr>
          <th>2021-11-04 14:30:00-04:00</th>
          <td>104.620003</td>
          <td>104.790001</td>
          <td>104.519997</td>
          <td>104.773598</td>
          <td>104.773598</td>
          <td>454197</td>
        </tr>
        <tr>
          <th>2021-11-04 15:30:00-04:00</th>
          <td>104.779999</td>
          <td>105.260002</td>
          <td>104.779999</td>
          <td>105.260002</td>
          <td>105.260002</td>
          <td>536806</td>
        </tr>
        <tr>
          <th>2021-11-05 09:30:00-04:00</th>
          <td>106.930000</td>
          <td>108.589897</td>
          <td>106.849998</td>
          <td>108.030899</td>
          <td>108.030899</td>
          <td>2238735</td>
        </tr>
        <tr>
          <th>2021-11-05 10:30:00-04:00</th>
          <td>108.029999</td>
          <td>108.949997</td>
          <td>107.870003</td>
          <td>108.900002</td>
          <td>108.900002</td>
          <td>1088494</td>
        </tr>
        <tr>
          <th>2021-11-05 11:30:00-04:00</th>
          <td>108.915001</td>
          <td>109.264999</td>
          <td>108.570999</td>
          <td>109.070000</td>
          <td>109.070000</td>
          <td>881378</td>
        </tr>
        <tr>
          <th>2021-11-05 12:30:00-04:00</th>
          <td>109.029999</td>
          <td>109.650002</td>
          <td>108.860001</td>
          <td>109.065002</td>
          <td>109.065002</td>
          <td>999005</td>
        </tr>
        <tr>
          <th>2021-11-05 13:30:00-04:00</th>
          <td>109.050003</td>
          <td>109.320000</td>
          <td>108.669998</td>
          <td>109.199997</td>
          <td>109.199997</td>
          <td>619767</td>
        </tr>
        <tr>
          <th>2021-11-05 14:30:00-04:00</th>
          <td>109.199997</td>
          <td>109.220001</td>
          <td>108.610001</td>
          <td>108.766899</td>
          <td>108.766899</td>
          <td>613486</td>
        </tr>
        <tr>
          <th>2021-11-05 15:30:00-04:00</th>
          <td>108.779999</td>
          <td>108.900002</td>
          <td>108.599998</td>
          <td>108.745003</td>
          <td>108.745003</td>
          <td>718363</td>
        </tr>
        <tr>
          <th>2021-11-08 09:30:00-05:00</th>
          <td>109.400002</td>
          <td>110.309998</td>
          <td>108.820000</td>
          <td>110.010002</td>
          <td>110.010002</td>
          <td>1317712</td>
        </tr>
        <tr>
          <th>2021-11-08 10:30:00-05:00</th>
          <td>110.029999</td>
          <td>110.300003</td>
          <td>109.029999</td>
          <td>109.339996</td>
          <td>109.339996</td>
          <td>776933</td>
        </tr>
        <tr>
          <th>2021-11-08 11:30:00-05:00</th>
          <td>109.349998</td>
          <td>109.360001</td>
          <td>108.665001</td>
          <td>108.900002</td>
          <td>108.900002</td>
          <td>437123</td>
        </tr>
        <tr>
          <th>2021-11-08 12:30:00-05:00</th>
          <td>108.911797</td>
          <td>108.970001</td>
          <td>108.480003</td>
          <td>108.750000</td>
          <td>108.750000</td>
          <td>368035</td>
        </tr>
        <tr>
          <th>2021-11-08 13:30:00-05:00</th>
          <td>108.724998</td>
          <td>109.250000</td>
          <td>108.650002</td>
          <td>108.919998</td>
          <td>108.919998</td>
          <td>340864</td>
        </tr>
        <tr>
          <th>2021-11-08 14:30:00-05:00</th>
          <td>108.930000</td>
          <td>109.089996</td>
          <td>108.320000</td>
          <td>108.714996</td>
          <td>108.714996</td>
          <td>530117</td>
        </tr>
        <tr>
          <th>2021-11-08 15:30:00-05:00</th>
          <td>108.699997</td>
          <td>108.860001</td>
          <td>108.315002</td>
          <td>108.410004</td>
          <td>108.410004</td>
          <td>584033</td>
        </tr>
        <tr>
          <th>2021-11-09 09:30:00-05:00</th>
          <td>114.730003</td>
          <td>116.165001</td>
          <td>113.410004</td>
          <td>114.627098</td>
          <td>114.627098</td>
          <td>12338637</td>
        </tr>
        <tr>
          <th>2021-11-09 10:30:00-05:00</th>
          <td>114.623596</td>
          <td>115.269997</td>
          <td>112.900002</td>
          <td>113.009102</td>
          <td>113.009102</td>
          <td>3553528</td>
        </tr>
        <tr>
          <th>2021-11-09 11:30:00-05:00</th>
          <td>113.010002</td>
          <td>113.419998</td>
          <td>112.000000</td>
          <td>112.129997</td>
          <td>112.129997</td>
          <td>2528214</td>
        </tr>
        <tr>
          <th>2021-11-09 12:30:00-05:00</th>
          <td>112.120003</td>
          <td>112.529999</td>
          <td>111.910004</td>
          <td>112.059998</td>
          <td>112.059998</td>
          <td>1366079</td>
        </tr>
        <tr>
          <th>2021-11-09 13:30:00-05:00</th>
          <td>112.055099</td>
          <td>112.169998</td>
          <td>110.480003</td>
          <td>111.379997</td>
          <td>111.379997</td>
          <td>1722090</td>
        </tr>
        <tr>
          <th>2021-11-09 14:30:00-05:00</th>
          <td>111.370003</td>
          <td>111.629997</td>
          <td>111.070000</td>
          <td>111.529999</td>
          <td>111.529999</td>
          <td>1050639</td>
        </tr>
        <tr>
          <th>2021-11-09 15:30:00-05:00</th>
          <td>111.550003</td>
          <td>111.669998</td>
          <td>111.220001</td>
          <td>111.290001</td>
          <td>111.290001</td>
          <td>1602187</td>
        </tr>
        <tr>
          <th>2021-11-10 09:30:00-05:00</th>
          <td>112.500000</td>
          <td>112.680000</td>
          <td>109.570000</td>
          <td>110.070000</td>
          <td>110.070000</td>
          <td>2957543</td>
        </tr>
        <tr>
          <th>2021-11-10 10:30:00-05:00</th>
          <td>110.040001</td>
          <td>111.010002</td>
          <td>109.625702</td>
          <td>110.860001</td>
          <td>110.860001</td>
          <td>1114726</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-11-29 14:30:00-05:00</th>
          <td>98.730003</td>
          <td>99.110001</td>
          <td>98.510002</td>
          <td>98.720001</td>
          <td>98.720001</td>
          <td>969572</td>
        </tr>
        <tr>
          <th>2021-11-29 15:30:00-05:00</th>
          <td>98.720001</td>
          <td>98.820000</td>
          <td>98.309998</td>
          <td>98.360001</td>
          <td>98.360001</td>
          <td>1066469</td>
        </tr>
        <tr>
          <th>2021-11-30 09:30:00-05:00</th>
          <td>96.639999</td>
          <td>97.430000</td>
          <td>95.959999</td>
          <td>96.059998</td>
          <td>96.059998</td>
          <td>1875592</td>
        </tr>
        <tr>
          <th>2021-11-30 10:30:00-05:00</th>
          <td>96.059998</td>
          <td>96.610001</td>
          <td>95.370003</td>
          <td>95.610001</td>
          <td>95.610001</td>
          <td>1237491</td>
        </tr>
        <tr>
          <th>2021-11-30 11:30:00-05:00</th>
          <td>95.595001</td>
          <td>95.699997</td>
          <td>94.709999</td>
          <td>95.180000</td>
          <td>95.180000</td>
          <td>959147</td>
        </tr>
        <tr>
          <th>2021-11-30 12:30:00-05:00</th>
          <td>95.129997</td>
          <td>95.300003</td>
          <td>94.470001</td>
          <td>94.864799</td>
          <td>94.864799</td>
          <td>860893</td>
        </tr>
        <tr>
          <th>2021-11-30 13:30:00-05:00</th>
          <td>94.870003</td>
          <td>95.739998</td>
          <td>94.830002</td>
          <td>95.360001</td>
          <td>95.360001</td>
          <td>764238</td>
        </tr>
        <tr>
          <th>2021-11-30 14:30:00-05:00</th>
          <td>95.339996</td>
          <td>95.489998</td>
          <td>95.205200</td>
          <td>95.379997</td>
          <td>95.379997</td>
          <td>843077</td>
        </tr>
        <tr>
          <th>2021-11-30 15:30:00-05:00</th>
          <td>95.371002</td>
          <td>95.650002</td>
          <td>94.779999</td>
          <td>94.900002</td>
          <td>94.900002</td>
          <td>1692138</td>
        </tr>
        <tr>
          <th>2021-12-01 09:30:00-05:00</th>
          <td>96.550003</td>
          <td>96.889999</td>
          <td>95.940002</td>
          <td>96.386803</td>
          <td>96.386803</td>
          <td>1196768</td>
        </tr>
        <tr>
          <th>2021-12-01 10:30:00-05:00</th>
          <td>96.379997</td>
          <td>96.470001</td>
          <td>95.480003</td>
          <td>95.919998</td>
          <td>95.919998</td>
          <td>882856</td>
        </tr>
        <tr>
          <th>2021-12-01 11:30:00-05:00</th>
          <td>95.919998</td>
          <td>96.428299</td>
          <td>95.660004</td>
          <td>95.920502</td>
          <td>95.920502</td>
          <td>1272531</td>
        </tr>
        <tr>
          <th>2021-12-01 12:30:00-05:00</th>
          <td>95.930000</td>
          <td>96.010002</td>
          <td>95.000000</td>
          <td>95.495003</td>
          <td>95.495003</td>
          <td>947462</td>
        </tr>
        <tr>
          <th>2021-12-01 13:30:00-05:00</th>
          <td>95.495003</td>
          <td>95.510002</td>
          <td>94.470001</td>
          <td>95.099998</td>
          <td>95.099998</td>
          <td>1041330</td>
        </tr>
        <tr>
          <th>2021-12-01 14:30:00-05:00</th>
          <td>95.089996</td>
          <td>95.209900</td>
          <td>93.709999</td>
          <td>94.010002</td>
          <td>94.010002</td>
          <td>1262890</td>
        </tr>
        <tr>
          <th>2021-12-01 15:30:00-05:00</th>
          <td>94.019997</td>
          <td>94.234497</td>
          <td>92.940002</td>
          <td>93.000000</td>
          <td>93.000000</td>
          <td>1346447</td>
        </tr>
        <tr>
          <th>2021-12-02 09:30:00-05:00</th>
          <td>94.199997</td>
          <td>94.910004</td>
          <td>92.809998</td>
          <td>94.339996</td>
          <td>94.339996</td>
          <td>1207029</td>
        </tr>
        <tr>
          <th>2021-12-02 10:30:00-05:00</th>
          <td>94.339996</td>
          <td>94.510002</td>
          <td>93.625000</td>
          <td>94.440002</td>
          <td>94.440002</td>
          <td>1074436</td>
        </tr>
        <tr>
          <th>2021-12-02 11:30:00-05:00</th>
          <td>94.480003</td>
          <td>95.260002</td>
          <td>93.980003</td>
          <td>95.169998</td>
          <td>95.169998</td>
          <td>667522</td>
        </tr>
        <tr>
          <th>2021-12-02 12:30:00-05:00</th>
          <td>95.180000</td>
          <td>95.220001</td>
          <td>94.709999</td>
          <td>94.820000</td>
          <td>94.820000</td>
          <td>714349</td>
        </tr>
        <tr>
          <th>2021-12-02 13:30:00-05:00</th>
          <td>94.820000</td>
          <td>95.714996</td>
          <td>94.730003</td>
          <td>95.699997</td>
          <td>95.699997</td>
          <td>403899</td>
        </tr>
        <tr>
          <th>2021-12-02 14:30:00-05:00</th>
          <td>95.669998</td>
          <td>95.779999</td>
          <td>95.330498</td>
          <td>95.529999</td>
          <td>95.529999</td>
          <td>565112</td>
        </tr>
        <tr>
          <th>2021-12-02 15:30:00-05:00</th>
          <td>95.540001</td>
          <td>95.690002</td>
          <td>95.029999</td>
          <td>95.269997</td>
          <td>95.269997</td>
          <td>810805</td>
        </tr>
        <tr>
          <th>2021-12-03 09:30:00-05:00</th>
          <td>95.129997</td>
          <td>95.349998</td>
          <td>93.099998</td>
          <td>93.360001</td>
          <td>93.360001</td>
          <td>1482932</td>
        </tr>
        <tr>
          <th>2021-12-03 10:30:00-05:00</th>
          <td>93.345001</td>
          <td>93.345001</td>
          <td>92.320000</td>
          <td>93.004997</td>
          <td>93.004997</td>
          <td>1106707</td>
        </tr>
        <tr>
          <th>2021-12-03 11:30:00-05:00</th>
          <td>92.989998</td>
          <td>93.639999</td>
          <td>92.430000</td>
          <td>93.430000</td>
          <td>93.430000</td>
          <td>833332</td>
        </tr>
        <tr>
          <th>2021-12-03 12:30:00-05:00</th>
          <td>93.419998</td>
          <td>93.790001</td>
          <td>92.919998</td>
          <td>92.959999</td>
          <td>92.959999</td>
          <td>630788</td>
        </tr>
        <tr>
          <th>2021-12-03 13:30:00-05:00</th>
          <td>92.930000</td>
          <td>92.945000</td>
          <td>91.949997</td>
          <td>92.120003</td>
          <td>92.120003</td>
          <td>737376</td>
        </tr>
        <tr>
          <th>2021-12-03 14:30:00-05:00</th>
          <td>92.120003</td>
          <td>92.550003</td>
          <td>91.730003</td>
          <td>92.419998</td>
          <td>92.419998</td>
          <td>915324</td>
        </tr>
        <tr>
          <th>2021-12-03 15:30:00-05:00</th>
          <td>92.410004</td>
          <td>92.863403</td>
          <td>92.279404</td>
          <td>92.809998</td>
          <td>92.809998</td>
          <td>1465678</td>
        </tr>
      </tbody>
    </table>
    <p>144 rows × 6 columns</p>
    </div>



.. code:: ipython3

    yf.download('GE',period='1mo',interval='5m')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Datetime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-04 09:30:00-04:00</th>
          <td>105.870003</td>
          <td>106.330002</td>
          <td>105.820000</td>
          <td>105.969902</td>
          <td>105.969902</td>
          <td>134010</td>
        </tr>
        <tr>
          <th>2021-11-04 09:35:00-04:00</th>
          <td>105.885002</td>
          <td>106.230003</td>
          <td>105.800003</td>
          <td>105.870003</td>
          <td>105.870003</td>
          <td>25002</td>
        </tr>
        <tr>
          <th>2021-11-04 09:40:00-04:00</th>
          <td>105.900002</td>
          <td>106.169998</td>
          <td>105.820000</td>
          <td>105.966003</td>
          <td>105.966003</td>
          <td>33432</td>
        </tr>
        <tr>
          <th>2021-11-04 09:45:00-04:00</th>
          <td>105.940002</td>
          <td>106.040001</td>
          <td>105.620003</td>
          <td>105.650002</td>
          <td>105.650002</td>
          <td>74334</td>
        </tr>
        <tr>
          <th>2021-11-04 09:50:00-04:00</th>
          <td>105.610001</td>
          <td>105.900002</td>
          <td>105.580002</td>
          <td>105.690002</td>
          <td>105.690002</td>
          <td>64964</td>
        </tr>
        <tr>
          <th>2021-11-04 09:55:00-04:00</th>
          <td>105.660004</td>
          <td>105.800003</td>
          <td>105.517899</td>
          <td>105.535004</td>
          <td>105.535004</td>
          <td>32898</td>
        </tr>
        <tr>
          <th>2021-11-04 10:00:00-04:00</th>
          <td>105.559998</td>
          <td>105.639999</td>
          <td>105.510002</td>
          <td>105.589996</td>
          <td>105.589996</td>
          <td>25440</td>
        </tr>
        <tr>
          <th>2021-11-04 10:05:00-04:00</th>
          <td>105.550003</td>
          <td>105.730003</td>
          <td>105.410004</td>
          <td>105.440002</td>
          <td>105.440002</td>
          <td>73144</td>
        </tr>
        <tr>
          <th>2021-11-04 10:10:00-04:00</th>
          <td>105.459999</td>
          <td>105.529999</td>
          <td>105.190002</td>
          <td>105.209999</td>
          <td>105.209999</td>
          <td>67682</td>
        </tr>
        <tr>
          <th>2021-11-04 10:15:00-04:00</th>
          <td>105.190002</td>
          <td>105.470001</td>
          <td>105.190002</td>
          <td>105.320000</td>
          <td>105.320000</td>
          <td>52040</td>
        </tr>
        <tr>
          <th>2021-11-04 10:20:00-04:00</th>
          <td>105.320000</td>
          <td>105.440002</td>
          <td>105.199997</td>
          <td>105.205002</td>
          <td>105.205002</td>
          <td>41990</td>
        </tr>
        <tr>
          <th>2021-11-04 10:25:00-04:00</th>
          <td>105.180000</td>
          <td>105.199997</td>
          <td>104.910004</td>
          <td>104.930000</td>
          <td>104.930000</td>
          <td>99565</td>
        </tr>
        <tr>
          <th>2021-11-04 10:30:00-04:00</th>
          <td>104.955002</td>
          <td>105.029999</td>
          <td>104.860001</td>
          <td>104.904999</td>
          <td>104.904999</td>
          <td>102590</td>
        </tr>
        <tr>
          <th>2021-11-04 10:35:00-04:00</th>
          <td>104.910004</td>
          <td>104.910004</td>
          <td>104.629997</td>
          <td>104.860001</td>
          <td>104.860001</td>
          <td>203693</td>
        </tr>
        <tr>
          <th>2021-11-04 10:40:00-04:00</th>
          <td>104.820000</td>
          <td>104.879997</td>
          <td>104.589996</td>
          <td>104.739998</td>
          <td>104.739998</td>
          <td>71509</td>
        </tr>
        <tr>
          <th>2021-11-04 10:45:00-04:00</th>
          <td>104.730003</td>
          <td>104.849998</td>
          <td>104.669998</td>
          <td>104.785004</td>
          <td>104.785004</td>
          <td>55954</td>
        </tr>
        <tr>
          <th>2021-11-04 10:50:00-04:00</th>
          <td>104.764999</td>
          <td>104.764999</td>
          <td>104.533401</td>
          <td>104.540001</td>
          <td>104.540001</td>
          <td>62715</td>
        </tr>
        <tr>
          <th>2021-11-04 10:55:00-04:00</th>
          <td>104.559898</td>
          <td>104.633904</td>
          <td>104.529999</td>
          <td>104.610001</td>
          <td>104.610001</td>
          <td>27212</td>
        </tr>
        <tr>
          <th>2021-11-04 11:00:00-04:00</th>
          <td>104.580002</td>
          <td>104.599998</td>
          <td>104.519997</td>
          <td>104.570000</td>
          <td>104.570000</td>
          <td>35744</td>
        </tr>
        <tr>
          <th>2021-11-04 11:05:00-04:00</th>
          <td>104.570000</td>
          <td>104.589996</td>
          <td>104.440002</td>
          <td>104.589996</td>
          <td>104.589996</td>
          <td>52538</td>
        </tr>
        <tr>
          <th>2021-11-04 11:10:00-04:00</th>
          <td>104.584999</td>
          <td>104.584999</td>
          <td>104.339996</td>
          <td>104.389999</td>
          <td>104.389999</td>
          <td>52901</td>
        </tr>
        <tr>
          <th>2021-11-04 11:15:00-04:00</th>
          <td>104.410004</td>
          <td>104.440002</td>
          <td>104.330002</td>
          <td>104.370003</td>
          <td>104.370003</td>
          <td>33266</td>
        </tr>
        <tr>
          <th>2021-11-04 11:20:00-04:00</th>
          <td>104.370003</td>
          <td>104.471001</td>
          <td>104.339996</td>
          <td>104.362099</td>
          <td>104.362099</td>
          <td>38782</td>
        </tr>
        <tr>
          <th>2021-11-04 11:25:00-04:00</th>
          <td>104.379997</td>
          <td>104.419998</td>
          <td>104.290001</td>
          <td>104.324997</td>
          <td>104.324997</td>
          <td>48960</td>
        </tr>
        <tr>
          <th>2021-11-04 11:30:00-04:00</th>
          <td>104.309998</td>
          <td>104.580002</td>
          <td>104.309998</td>
          <td>104.529999</td>
          <td>104.529999</td>
          <td>172929</td>
        </tr>
        <tr>
          <th>2021-11-04 11:35:00-04:00</th>
          <td>104.544998</td>
          <td>104.870003</td>
          <td>104.529999</td>
          <td>104.699997</td>
          <td>104.699997</td>
          <td>162829</td>
        </tr>
        <tr>
          <th>2021-11-04 11:40:00-04:00</th>
          <td>104.708504</td>
          <td>104.718903</td>
          <td>104.559998</td>
          <td>104.610001</td>
          <td>104.610001</td>
          <td>25973</td>
        </tr>
        <tr>
          <th>2021-11-04 11:45:00-04:00</th>
          <td>104.610001</td>
          <td>104.610001</td>
          <td>104.480003</td>
          <td>104.500000</td>
          <td>104.500000</td>
          <td>35933</td>
        </tr>
        <tr>
          <th>2021-11-04 11:50:00-04:00</th>
          <td>104.500000</td>
          <td>104.580002</td>
          <td>104.430000</td>
          <td>104.535004</td>
          <td>104.535004</td>
          <td>33560</td>
        </tr>
        <tr>
          <th>2021-11-04 11:55:00-04:00</th>
          <td>104.550003</td>
          <td>104.959999</td>
          <td>104.540001</td>
          <td>104.940002</td>
          <td>104.940002</td>
          <td>49667</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-12-03 13:30:00-05:00</th>
          <td>92.930000</td>
          <td>92.945000</td>
          <td>92.809998</td>
          <td>92.845001</td>
          <td>92.845001</td>
          <td>38271</td>
        </tr>
        <tr>
          <th>2021-12-03 13:35:00-05:00</th>
          <td>92.860001</td>
          <td>92.860001</td>
          <td>92.639999</td>
          <td>92.680000</td>
          <td>92.680000</td>
          <td>48736</td>
        </tr>
        <tr>
          <th>2021-12-03 13:40:00-05:00</th>
          <td>92.680000</td>
          <td>92.730003</td>
          <td>92.410004</td>
          <td>92.459999</td>
          <td>92.459999</td>
          <td>102858</td>
        </tr>
        <tr>
          <th>2021-12-03 13:45:00-05:00</th>
          <td>92.470001</td>
          <td>92.580002</td>
          <td>92.349998</td>
          <td>92.440002</td>
          <td>92.440002</td>
          <td>61500</td>
        </tr>
        <tr>
          <th>2021-12-03 13:50:00-05:00</th>
          <td>92.410004</td>
          <td>92.660004</td>
          <td>92.410004</td>
          <td>92.519997</td>
          <td>92.519997</td>
          <td>39659</td>
        </tr>
        <tr>
          <th>2021-12-03 13:55:00-05:00</th>
          <td>92.500099</td>
          <td>92.649002</td>
          <td>92.415001</td>
          <td>92.459999</td>
          <td>92.459999</td>
          <td>50193</td>
        </tr>
        <tr>
          <th>2021-12-03 14:00:00-05:00</th>
          <td>92.440002</td>
          <td>92.519997</td>
          <td>92.360001</td>
          <td>92.510002</td>
          <td>92.510002</td>
          <td>57826</td>
        </tr>
        <tr>
          <th>2021-12-03 14:05:00-05:00</th>
          <td>92.510002</td>
          <td>92.514397</td>
          <td>92.260002</td>
          <td>92.269997</td>
          <td>92.269997</td>
          <td>38952</td>
        </tr>
        <tr>
          <th>2021-12-03 14:10:00-05:00</th>
          <td>92.279999</td>
          <td>92.529999</td>
          <td>92.279999</td>
          <td>92.434998</td>
          <td>92.434998</td>
          <td>41895</td>
        </tr>
        <tr>
          <th>2021-12-03 14:15:00-05:00</th>
          <td>92.440002</td>
          <td>92.440002</td>
          <td>92.139999</td>
          <td>92.146103</td>
          <td>92.146103</td>
          <td>76700</td>
        </tr>
        <tr>
          <th>2021-12-03 14:20:00-05:00</th>
          <td>92.160004</td>
          <td>92.290001</td>
          <td>91.949997</td>
          <td>92.260002</td>
          <td>92.260002</td>
          <td>110911</td>
        </tr>
        <tr>
          <th>2021-12-03 14:25:00-05:00</th>
          <td>92.239998</td>
          <td>92.260002</td>
          <td>92.099998</td>
          <td>92.120003</td>
          <td>92.120003</td>
          <td>69875</td>
        </tr>
        <tr>
          <th>2021-12-03 14:30:00-05:00</th>
          <td>92.120003</td>
          <td>92.169998</td>
          <td>91.959999</td>
          <td>92.129997</td>
          <td>92.129997</td>
          <td>76190</td>
        </tr>
        <tr>
          <th>2021-12-03 14:35:00-05:00</th>
          <td>92.120003</td>
          <td>92.199997</td>
          <td>91.930000</td>
          <td>91.974998</td>
          <td>91.974998</td>
          <td>77434</td>
        </tr>
        <tr>
          <th>2021-12-03 14:40:00-05:00</th>
          <td>91.970001</td>
          <td>92.269997</td>
          <td>91.970001</td>
          <td>92.220001</td>
          <td>92.220001</td>
          <td>59679</td>
        </tr>
        <tr>
          <th>2021-12-03 14:45:00-05:00</th>
          <td>92.209999</td>
          <td>92.250000</td>
          <td>92.040001</td>
          <td>92.044998</td>
          <td>92.044998</td>
          <td>47194</td>
        </tr>
        <tr>
          <th>2021-12-03 14:50:00-05:00</th>
          <td>92.040001</td>
          <td>92.089996</td>
          <td>91.879997</td>
          <td>91.900002</td>
          <td>91.900002</td>
          <td>92012</td>
        </tr>
        <tr>
          <th>2021-12-03 14:55:00-05:00</th>
          <td>91.889999</td>
          <td>92.000000</td>
          <td>91.839996</td>
          <td>91.940002</td>
          <td>91.940002</td>
          <td>88343</td>
        </tr>
        <tr>
          <th>2021-12-03 15:00:00-05:00</th>
          <td>91.919998</td>
          <td>92.019997</td>
          <td>91.760002</td>
          <td>91.989998</td>
          <td>91.989998</td>
          <td>67894</td>
        </tr>
        <tr>
          <th>2021-12-03 15:05:00-05:00</th>
          <td>91.982300</td>
          <td>92.160004</td>
          <td>91.730003</td>
          <td>91.750000</td>
          <td>91.750000</td>
          <td>77125</td>
        </tr>
        <tr>
          <th>2021-12-03 15:10:00-05:00</th>
          <td>91.739998</td>
          <td>92.070000</td>
          <td>91.739998</td>
          <td>92.044998</td>
          <td>92.044998</td>
          <td>121073</td>
        </tr>
        <tr>
          <th>2021-12-03 15:15:00-05:00</th>
          <td>92.029999</td>
          <td>92.080002</td>
          <td>91.955002</td>
          <td>92.019997</td>
          <td>92.019997</td>
          <td>63836</td>
        </tr>
        <tr>
          <th>2021-12-03 15:20:00-05:00</th>
          <td>92.040001</td>
          <td>92.430000</td>
          <td>92.040001</td>
          <td>92.390099</td>
          <td>92.390099</td>
          <td>79554</td>
        </tr>
        <tr>
          <th>2021-12-03 15:25:00-05:00</th>
          <td>92.410004</td>
          <td>92.550003</td>
          <td>92.360001</td>
          <td>92.419998</td>
          <td>92.419998</td>
          <td>64990</td>
        </tr>
        <tr>
          <th>2021-12-03 15:30:00-05:00</th>
          <td>92.410004</td>
          <td>92.769997</td>
          <td>92.410004</td>
          <td>92.769997</td>
          <td>92.769997</td>
          <td>146707</td>
        </tr>
        <tr>
          <th>2021-12-03 15:35:00-05:00</th>
          <td>92.761002</td>
          <td>92.769997</td>
          <td>92.309998</td>
          <td>92.449997</td>
          <td>92.449997</td>
          <td>112696</td>
        </tr>
        <tr>
          <th>2021-12-03 15:40:00-05:00</th>
          <td>92.470001</td>
          <td>92.559998</td>
          <td>92.290001</td>
          <td>92.430000</td>
          <td>92.430000</td>
          <td>127157</td>
        </tr>
        <tr>
          <th>2021-12-03 15:45:00-05:00</th>
          <td>92.430000</td>
          <td>92.480003</td>
          <td>92.279404</td>
          <td>92.480003</td>
          <td>92.480003</td>
          <td>205523</td>
        </tr>
        <tr>
          <th>2021-12-03 15:50:00-05:00</th>
          <td>92.500000</td>
          <td>92.808998</td>
          <td>92.379997</td>
          <td>92.709999</td>
          <td>92.709999</td>
          <td>262390</td>
        </tr>
        <tr>
          <th>2021-12-03 15:55:00-05:00</th>
          <td>92.699997</td>
          <td>92.863403</td>
          <td>92.639999</td>
          <td>92.809998</td>
          <td>92.809998</td>
          <td>611205</td>
        </tr>
      </tbody>
    </table>
    <p>1603 rows × 6 columns</p>
    </div>



.. code:: ipython3

    GE = yf.download('GE',period='5d',interval='5m')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed


.. code:: ipython3

    GE.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Datetime</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2021-11-29 09:30:00-05:00</th>
          <td>99.269997</td>
          <td>100.430000</td>
          <td>99.269997</td>
          <td>99.589996</td>
          <td>99.589996</td>
          <td>509164</td>
        </tr>
        <tr>
          <th>2021-11-29 09:35:00-05:00</th>
          <td>99.500000</td>
          <td>99.650002</td>
          <td>98.769997</td>
          <td>98.820000</td>
          <td>98.820000</td>
          <td>190351</td>
        </tr>
        <tr>
          <th>2021-11-29 09:40:00-05:00</th>
          <td>98.839996</td>
          <td>98.900002</td>
          <td>98.300003</td>
          <td>98.389999</td>
          <td>98.389999</td>
          <td>115060</td>
        </tr>
        <tr>
          <th>2021-11-29 09:45:00-05:00</th>
          <td>98.394997</td>
          <td>98.540001</td>
          <td>98.269997</td>
          <td>98.269997</td>
          <td>98.269997</td>
          <td>122068</td>
        </tr>
        <tr>
          <th>2021-11-29 09:50:00-05:00</th>
          <td>98.245003</td>
          <td>98.480003</td>
          <td>97.970001</td>
          <td>98.000099</td>
          <td>98.000099</td>
          <td>89666</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    #Pre or post market data
    GE=yf.download('GE',prepost=True,period='5d',interval='5m')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed


 ### Stock Split and dividends

.. code:: ipython3

    ticker = "AAPL"

.. code:: ipython3

    # action = True for dividend and Stock Split
    AAPL = yf.download(ticker, period="10y", actions = True)


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed


.. code:: ipython3

    AAPL.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
          <th>Dividends</th>
          <th>Stock Splits</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2011-12-05</th>
          <td>14.053214</td>
          <td>14.157500</td>
          <td>13.942500</td>
          <td>14.036071</td>
          <td>12.034039</td>
          <td>357210000</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2011-12-06</th>
          <td>14.018214</td>
          <td>14.093929</td>
          <td>13.906429</td>
          <td>13.962500</td>
          <td>11.970958</td>
          <td>283598000</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2011-12-07</th>
          <td>13.926071</td>
          <td>13.962143</td>
          <td>13.812857</td>
          <td>13.896071</td>
          <td>11.914004</td>
          <td>304746400</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2011-12-08</th>
          <td>13.980357</td>
          <td>14.125000</td>
          <td>13.936786</td>
          <td>13.952143</td>
          <td>11.962079</td>
          <td>376356400</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2011-12-09</th>
          <td>14.030357</td>
          <td>14.072857</td>
          <td>13.965357</td>
          <td>14.057857</td>
          <td>12.052718</td>
          <td>296993200</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    AAPL[AAPL["Dividends"]>0]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
          <th>Dividends</th>
          <th>Stock Splits</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2012-08-09</th>
          <td>22.066071</td>
          <td>22.204643</td>
          <td>22.064285</td>
          <td>22.168928</td>
          <td>19.088470</td>
          <td>221642400</td>
          <td>0.094643</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2012-11-07</th>
          <td>20.494286</td>
          <td>20.519285</td>
          <td>19.848213</td>
          <td>19.928572</td>
          <td>17.237795</td>
          <td>793648800</td>
          <td>0.094643</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2013-02-07</th>
          <td>16.544643</td>
          <td>16.785713</td>
          <td>16.218571</td>
          <td>16.722143</td>
          <td>14.548601</td>
          <td>704580800</td>
          <td>0.094643</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2013-05-09</th>
          <td>16.421785</td>
          <td>16.535713</td>
          <td>16.270714</td>
          <td>16.313213</td>
          <td>14.286768</td>
          <td>398487600</td>
          <td>0.108929</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2013-08-08</th>
          <td>16.566429</td>
          <td>16.575001</td>
          <td>16.355356</td>
          <td>16.464643</td>
          <td>14.514593</td>
          <td>255777200</td>
          <td>0.108929</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2013-11-06</th>
          <td>18.719643</td>
          <td>18.745001</td>
          <td>18.507143</td>
          <td>18.604286</td>
          <td>16.496580</td>
          <td>223375600</td>
          <td>0.108929</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2014-02-06</th>
          <td>18.216429</td>
          <td>18.339287</td>
          <td>18.136070</td>
          <td>18.303928</td>
          <td>16.327394</td>
          <td>257765200</td>
          <td>0.108929</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2014-05-08</th>
          <td>21.008928</td>
          <td>21.228930</td>
          <td>20.942858</td>
          <td>20.999643</td>
          <td>18.836641</td>
          <td>230297200</td>
          <td>0.117500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2014-08-07</th>
          <td>23.732500</td>
          <td>23.987499</td>
          <td>23.525000</td>
          <td>23.620001</td>
          <td>21.292488</td>
          <td>186844000</td>
          <td>0.117500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2014-11-06</th>
          <td>27.150000</td>
          <td>27.197500</td>
          <td>26.950001</td>
          <td>27.174999</td>
          <td>24.603403</td>
          <td>139874000</td>
          <td>0.117500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2015-02-05</th>
          <td>30.004999</td>
          <td>30.057501</td>
          <td>29.812500</td>
          <td>29.985001</td>
          <td>27.254631</td>
          <td>168984800</td>
          <td>0.117500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2015-05-07</th>
          <td>31.192499</td>
          <td>31.520000</td>
          <td>31.004999</td>
          <td>31.315001</td>
          <td>28.582411</td>
          <td>175763600</td>
          <td>0.130000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2015-08-06</th>
          <td>28.992500</td>
          <td>29.125000</td>
          <td>28.530001</td>
          <td>28.782499</td>
          <td>26.389818</td>
          <td>211612000</td>
          <td>0.130000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2015-11-05</th>
          <td>30.462500</td>
          <td>30.672501</td>
          <td>30.045000</td>
          <td>30.230000</td>
          <td>27.835629</td>
          <td>158210800</td>
          <td>0.130000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2016-02-04</th>
          <td>23.965000</td>
          <td>24.332500</td>
          <td>23.797501</td>
          <td>24.150000</td>
          <td>22.357862</td>
          <td>185886800</td>
          <td>0.130000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2016-05-05</th>
          <td>23.500000</td>
          <td>23.517500</td>
          <td>23.170000</td>
          <td>23.309999</td>
          <td>21.711586</td>
          <td>143562000</td>
          <td>0.142500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2016-08-04</th>
          <td>26.395000</td>
          <td>26.500000</td>
          <td>26.320000</td>
          <td>26.467501</td>
          <td>24.786121</td>
          <td>109634800</td>
          <td>0.142500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2016-11-03</th>
          <td>27.745001</td>
          <td>27.865000</td>
          <td>27.387501</td>
          <td>27.457500</td>
          <td>25.845245</td>
          <td>107730400</td>
          <td>0.142500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2017-02-09</th>
          <td>32.912498</td>
          <td>33.112499</td>
          <td>32.779999</td>
          <td>33.105000</td>
          <td>31.296234</td>
          <td>113399600</td>
          <td>0.142500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2017-05-11</th>
          <td>38.112499</td>
          <td>38.517502</td>
          <td>38.077499</td>
          <td>38.487499</td>
          <td>36.534824</td>
          <td>109020400</td>
          <td>0.157500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2017-08-10</th>
          <td>39.974998</td>
          <td>40.000000</td>
          <td>38.657501</td>
          <td>38.830002</td>
          <td>37.004711</td>
          <td>163217200</td>
          <td>0.157500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2017-11-10</th>
          <td>43.777500</td>
          <td>43.845001</td>
          <td>43.567501</td>
          <td>43.667500</td>
          <td>41.764412</td>
          <td>100582000</td>
          <td>0.157500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2018-02-09</th>
          <td>39.267502</td>
          <td>39.472500</td>
          <td>37.560001</td>
          <td>39.102501</td>
          <td>37.550842</td>
          <td>282690400</td>
          <td>0.157500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2018-05-11</th>
          <td>47.372501</td>
          <td>47.514999</td>
          <td>46.862499</td>
          <td>47.147499</td>
          <td>45.451180</td>
          <td>104848800</td>
          <td>0.182500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2018-08-10</th>
          <td>51.840000</td>
          <td>52.275002</td>
          <td>51.667500</td>
          <td>51.882500</td>
          <td>50.191235</td>
          <td>98444800</td>
          <td>0.182500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2018-11-08</th>
          <td>52.494999</td>
          <td>52.529999</td>
          <td>51.687500</td>
          <td>52.122501</td>
          <td>50.599346</td>
          <td>101450400</td>
          <td>0.182500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-02-08</th>
          <td>42.247501</td>
          <td>42.665001</td>
          <td>42.105000</td>
          <td>42.602501</td>
          <td>41.534920</td>
          <td>95280000</td>
          <td>0.182500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-05-10</th>
          <td>49.355000</td>
          <td>49.712502</td>
          <td>48.192501</td>
          <td>49.294998</td>
          <td>48.244789</td>
          <td>164834800</td>
          <td>0.192500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-09</th>
          <td>50.325001</td>
          <td>50.689999</td>
          <td>49.822498</td>
          <td>50.247501</td>
          <td>49.363842</td>
          <td>98478800</td>
          <td>0.192500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-11-07</th>
          <td>64.684998</td>
          <td>65.087502</td>
          <td>64.527496</td>
          <td>64.857498</td>
          <td>63.908211</td>
          <td>94940400</td>
          <td>0.192500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2020-02-07</th>
          <td>80.592499</td>
          <td>80.849998</td>
          <td>79.500000</td>
          <td>80.007500</td>
          <td>79.023567</td>
          <td>117684000</td>
          <td>0.192500</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2020-05-08</th>
          <td>76.410004</td>
          <td>77.587502</td>
          <td>76.072502</td>
          <td>77.532501</td>
          <td>76.786301</td>
          <td>133838400</td>
          <td>0.205000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2020-08-07</th>
          <td>113.205002</td>
          <td>113.675003</td>
          <td>110.292503</td>
          <td>111.112503</td>
          <td>110.241516</td>
          <td>198045600</td>
          <td>0.205000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2020-11-06</th>
          <td>118.320000</td>
          <td>119.199997</td>
          <td>116.129997</td>
          <td>118.690002</td>
          <td>117.962784</td>
          <td>114457900</td>
          <td>0.205000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2021-02-05</th>
          <td>137.350006</td>
          <td>137.419998</td>
          <td>135.860001</td>
          <td>136.759995</td>
          <td>136.125168</td>
          <td>75693800</td>
          <td>0.205000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2021-05-07</th>
          <td>130.850006</td>
          <td>131.259995</td>
          <td>129.479996</td>
          <td>130.210007</td>
          <td>129.825745</td>
          <td>78973300</td>
          <td>0.220000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2021-08-06</th>
          <td>146.350006</td>
          <td>147.110001</td>
          <td>145.630005</td>
          <td>146.139999</td>
          <td>145.927017</td>
          <td>54067400</td>
          <td>0.220000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>151.889999</td>
          <td>152.199997</td>
          <td>150.059998</td>
          <td>151.279999</td>
          <td>151.279999</td>
          <td>65414600</td>
          <td>0.220000</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    AAPL.loc["2019-08-05":"2019-08-15"]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
          <th>Dividends</th>
          <th>Stock Splits</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2019-08-05</th>
          <td>49.497501</td>
          <td>49.662498</td>
          <td>48.145000</td>
          <td>48.334999</td>
          <td>47.305237</td>
          <td>209572000</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-06</th>
          <td>49.077499</td>
          <td>49.517502</td>
          <td>48.509998</td>
          <td>49.250000</td>
          <td>48.200752</td>
          <td>143299200</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-07</th>
          <td>48.852501</td>
          <td>49.889999</td>
          <td>48.455002</td>
          <td>49.759998</td>
          <td>48.699883</td>
          <td>133457600</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-08</th>
          <td>50.049999</td>
          <td>50.882500</td>
          <td>49.847500</td>
          <td>50.857498</td>
          <td>49.773998</td>
          <td>108038000</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-09</th>
          <td>50.325001</td>
          <td>50.689999</td>
          <td>49.822498</td>
          <td>50.247501</td>
          <td>49.363842</td>
          <td>98478800</td>
          <td>0.1925</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-12</th>
          <td>49.904999</td>
          <td>50.512501</td>
          <td>49.787498</td>
          <td>50.119999</td>
          <td>49.238579</td>
          <td>89927600</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-13</th>
          <td>50.255001</td>
          <td>53.035000</td>
          <td>50.119999</td>
          <td>52.242500</td>
          <td>51.323757</td>
          <td>188874000</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-14</th>
          <td>50.790001</td>
          <td>51.610001</td>
          <td>50.647499</td>
          <td>50.687500</td>
          <td>49.796104</td>
          <td>146189600</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-15</th>
          <td>50.865002</td>
          <td>51.285000</td>
          <td>49.917500</td>
          <td>50.435001</td>
          <td>49.548046</td>
          <td>108909600</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    AAPL.loc["2019-08-05":"2019-08-15"].diff()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
          <th>Dividends</th>
          <th>Stock Splits</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2019-08-05</th>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2019-08-06</th>
          <td>-0.420002</td>
          <td>-0.144997</td>
          <td>0.364998</td>
          <td>0.915001</td>
          <td>0.895515</td>
          <td>-66272800.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-07</th>
          <td>-0.224998</td>
          <td>0.372498</td>
          <td>-0.054996</td>
          <td>0.509998</td>
          <td>0.499130</td>
          <td>-9841600.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-08</th>
          <td>1.197498</td>
          <td>0.992500</td>
          <td>1.392498</td>
          <td>1.097500</td>
          <td>1.074116</td>
          <td>-25419600.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-09</th>
          <td>0.275002</td>
          <td>-0.192501</td>
          <td>-0.025002</td>
          <td>-0.609997</td>
          <td>-0.410156</td>
          <td>-9559200.0</td>
          <td>0.1925</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-12</th>
          <td>-0.420002</td>
          <td>-0.177498</td>
          <td>-0.035000</td>
          <td>-0.127502</td>
          <td>-0.125263</td>
          <td>-8551200.0</td>
          <td>-0.1925</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-13</th>
          <td>0.350002</td>
          <td>2.522499</td>
          <td>0.332500</td>
          <td>2.122501</td>
          <td>2.085178</td>
          <td>98946400.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-14</th>
          <td>0.535000</td>
          <td>-1.424999</td>
          <td>0.527500</td>
          <td>-1.555000</td>
          <td>-1.527653</td>
          <td>-42684400.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2019-08-15</th>
          <td>0.075001</td>
          <td>-0.325001</td>
          <td>-0.730000</td>
          <td>-0.252499</td>
          <td>-0.248058</td>
          <td>-37280000.0</td>
          <td>0.0000</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    AAPL[AAPL["Stock Splits"] > 0]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
          <th>Dividends</th>
          <th>Stock Splits</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-06-09</th>
          <td>23.174999</td>
          <td>23.469999</td>
          <td>22.9375</td>
          <td>23.424999</td>
          <td>21.012186</td>
          <td>301660000</td>
          <td>0.0</td>
          <td>7.0</td>
        </tr>
        <tr>
          <th>2020-08-31</th>
          <td>127.580002</td>
          <td>131.000000</td>
          <td>126.0000</td>
          <td>129.039993</td>
          <td>128.028488</td>
          <td>225702700</td>
          <td>0.0</td>
          <td>4.0</td>
        </tr>
      </tbody>
    </table>
    </div>



 ### Importing many stocks

.. code:: ipython3

    ticker = ['GE', 'AAPL','FB']

.. code:: ipython3

     yf.download(ticker, period="5y")


.. parsed-literal::

    [*********************100%***********************]  3 of 3 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead tr th {
            text-align: left;
        }

        .dataframe thead tr:last-of-type th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <th colspan="3" halign="left">Adj Close</th>
          <th colspan="3" halign="left">Close</th>
          <th colspan="3" halign="left">High</th>
          <th colspan="3" halign="left">Low</th>
          <th colspan="3" halign="left">Open</th>
          <th colspan="3" halign="left">Volume</th>
        </tr>
        <tr>
          <th></th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
          <th>AAPL</th>
          <th>FB</th>
          <th>GE</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2016-12-05</th>
          <td>25.675814</td>
          <td>117.430000</td>
          <td>220.920135</td>
          <td>27.277500</td>
          <td>117.430000</td>
          <td>239.307693</td>
          <td>27.507500</td>
          <td>117.570000</td>
          <td>241.923080</td>
          <td>27.062500</td>
          <td>115.070000</td>
          <td>238.923080</td>
          <td>27.500000</td>
          <td>115.949997</td>
          <td>241.769226</td>
          <td>137298000</td>
          <td>20201500</td>
          <td>2877979</td>
        </tr>
        <tr>
          <th>2016-12-06</th>
          <td>25.873487</td>
          <td>117.309998</td>
          <td>221.346146</td>
          <td>27.487499</td>
          <td>117.309998</td>
          <td>239.769226</td>
          <td>27.590000</td>
          <td>117.800003</td>
          <td>240.307693</td>
          <td>27.297501</td>
          <td>116.330002</td>
          <td>238.538467</td>
          <td>27.375000</td>
          <td>117.690002</td>
          <td>239.923080</td>
          <td>104782000</td>
          <td>19131200</td>
          <td>2284529</td>
        </tr>
        <tr>
          <th>2016-12-07</th>
          <td>26.127632</td>
          <td>117.949997</td>
          <td>224.399719</td>
          <td>27.757500</td>
          <td>117.949997</td>
          <td>243.076920</td>
          <td>27.797501</td>
          <td>117.949997</td>
          <td>243.076920</td>
          <td>27.290001</td>
          <td>116.570000</td>
          <td>237.923080</td>
          <td>27.315001</td>
          <td>117.000000</td>
          <td>238.538467</td>
          <td>119994800</td>
          <td>21913700</td>
          <td>4276610</td>
        </tr>
        <tr>
          <th>2016-12-08</th>
          <td>26.384127</td>
          <td>118.910004</td>
          <td>223.902618</td>
          <td>28.030001</td>
          <td>118.910004</td>
          <td>242.538467</td>
          <td>28.107500</td>
          <td>119.500000</td>
          <td>243.846161</td>
          <td>27.650000</td>
          <td>117.639999</td>
          <td>241.538467</td>
          <td>27.715000</td>
          <td>117.980003</td>
          <td>243.076920</td>
          <td>108273200</td>
          <td>22442800</td>
          <td>3658863</td>
        </tr>
        <tr>
          <th>2016-12-09</th>
          <td>26.814768</td>
          <td>119.680000</td>
          <td>225.677917</td>
          <td>28.487499</td>
          <td>119.680000</td>
          <td>244.461533</td>
          <td>28.674999</td>
          <td>119.940002</td>
          <td>245.538467</td>
          <td>28.077499</td>
          <td>118.949997</td>
          <td>241.153839</td>
          <td>28.077499</td>
          <td>119.220001</td>
          <td>241.923080</td>
          <td>137610400</td>
          <td>17464700</td>
          <td>4059562</td>
        </tr>
        <tr>
          <th>2016-12-12</th>
          <td>26.661814</td>
          <td>117.769997</td>
          <td>226.246033</td>
          <td>28.325001</td>
          <td>117.769997</td>
          <td>245.076920</td>
          <td>28.750000</td>
          <td>119.239998</td>
          <td>246.076920</td>
          <td>28.122499</td>
          <td>117.650002</td>
          <td>243.538467</td>
          <td>28.322500</td>
          <td>119.220001</td>
          <td>243.615387</td>
          <td>105497600</td>
          <td>17805500</td>
          <td>4035291</td>
        </tr>
        <tr>
          <th>2016-12-13</th>
          <td>27.106567</td>
          <td>120.309998</td>
          <td>225.393845</td>
          <td>28.797501</td>
          <td>120.309998</td>
          <td>244.153839</td>
          <td>28.980000</td>
          <td>121.519997</td>
          <td>246.153839</td>
          <td>28.437500</td>
          <td>117.610001</td>
          <td>243.153839</td>
          <td>28.459999</td>
          <td>117.860001</td>
          <td>245.384613</td>
          <td>174935200</td>
          <td>29768000</td>
          <td>4485052</td>
        </tr>
        <tr>
          <th>2016-12-14</th>
          <td>27.106567</td>
          <td>120.209999</td>
          <td>223.689606</td>
          <td>28.797501</td>
          <td>120.209999</td>
          <td>242.307693</td>
          <td>29.049999</td>
          <td>121.690002</td>
          <td>246.000000</td>
          <td>28.745001</td>
          <td>118.849998</td>
          <td>241.846161</td>
          <td>28.760000</td>
          <td>120.000000</td>
          <td>243.153839</td>
          <td>136127200</td>
          <td>25913100</td>
          <td>5677789</td>
        </tr>
        <tr>
          <th>2016-12-15</th>
          <td>27.254816</td>
          <td>120.570000</td>
          <td>221.985291</td>
          <td>28.955000</td>
          <td>120.570000</td>
          <td>240.461533</td>
          <td>29.182501</td>
          <td>122.500000</td>
          <td>245.769226</td>
          <td>28.807501</td>
          <td>119.629997</td>
          <td>239.461533</td>
          <td>28.844999</td>
          <td>120.080002</td>
          <td>242.230774</td>
          <td>186098000</td>
          <td>20139600</td>
          <td>5639062</td>
        </tr>
        <tr>
          <th>2016-12-16</th>
          <td>27.290112</td>
          <td>119.870003</td>
          <td>225.464935</td>
          <td>28.992500</td>
          <td>119.870003</td>
          <td>244.230774</td>
          <td>29.125000</td>
          <td>121.500000</td>
          <td>245.153839</td>
          <td>28.912500</td>
          <td>119.269997</td>
          <td>242.000000</td>
          <td>29.117500</td>
          <td>120.900002</td>
          <td>242.461533</td>
          <td>177404400</td>
          <td>25324300</td>
          <td>9356906</td>
        </tr>
        <tr>
          <th>2016-12-19</th>
          <td>27.447777</td>
          <td>119.239998</td>
          <td>226.672119</td>
          <td>29.160000</td>
          <td>119.239998</td>
          <td>245.538467</td>
          <td>29.344999</td>
          <td>120.360001</td>
          <td>246.153839</td>
          <td>28.937500</td>
          <td>118.510002</td>
          <td>243.923080</td>
          <td>28.950001</td>
          <td>119.849998</td>
          <td>244.307693</td>
          <td>111117600</td>
          <td>15918100</td>
          <td>4543734</td>
        </tr>
        <tr>
          <th>2016-12-20</th>
          <td>27.520727</td>
          <td>119.089996</td>
          <td>229.015518</td>
          <td>29.237499</td>
          <td>119.089996</td>
          <td>248.076920</td>
          <td>29.375000</td>
          <td>119.769997</td>
          <td>249.076920</td>
          <td>29.170000</td>
          <td>118.800003</td>
          <td>245.461533</td>
          <td>29.184999</td>
          <td>119.500000</td>
          <td>245.538467</td>
          <td>85700000</td>
          <td>13684400</td>
          <td>5176366</td>
        </tr>
        <tr>
          <th>2016-12-21</th>
          <td>27.546614</td>
          <td>119.040001</td>
          <td>228.163361</td>
          <td>29.264999</td>
          <td>119.040001</td>
          <td>247.153839</td>
          <td>29.350000</td>
          <td>119.199997</td>
          <td>248.000000</td>
          <td>29.195000</td>
          <td>118.480003</td>
          <td>246.538467</td>
          <td>29.200001</td>
          <td>118.919998</td>
          <td>247.692307</td>
          <td>95132800</td>
          <td>10767600</td>
          <td>3635411</td>
        </tr>
        <tr>
          <th>2016-12-22</th>
          <td>27.365419</td>
          <td>117.400002</td>
          <td>227.662552</td>
          <td>29.072500</td>
          <td>117.400002</td>
          <td>244.769226</td>
          <td>29.127501</td>
          <td>118.989998</td>
          <td>245.769226</td>
          <td>28.910000</td>
          <td>116.930000</td>
          <td>244.461533</td>
          <td>29.087500</td>
          <td>118.860001</td>
          <td>245.461533</td>
          <td>104343600</td>
          <td>16258600</td>
          <td>3145194</td>
        </tr>
        <tr>
          <th>2016-12-23</th>
          <td>27.419542</td>
          <td>117.269997</td>
          <td>228.091827</td>
          <td>29.129999</td>
          <td>117.269997</td>
          <td>245.230774</td>
          <td>29.129999</td>
          <td>117.559998</td>
          <td>245.692307</td>
          <td>28.897499</td>
          <td>116.300003</td>
          <td>244.384613</td>
          <td>28.897499</td>
          <td>117.000000</td>
          <td>245.153839</td>
          <td>56998000</td>
          <td>10890000</td>
          <td>1948518</td>
        </tr>
        <tr>
          <th>2016-12-27</th>
          <td>27.593674</td>
          <td>118.010002</td>
          <td>228.234955</td>
          <td>29.315001</td>
          <td>118.010002</td>
          <td>245.384613</td>
          <td>29.450001</td>
          <td>118.680000</td>
          <td>246.538467</td>
          <td>29.122499</td>
          <td>116.860001</td>
          <td>245.000000</td>
          <td>29.129999</td>
          <td>116.959999</td>
          <td>245.307693</td>
          <td>73187600</td>
          <td>12051500</td>
          <td>2035267</td>
        </tr>
        <tr>
          <th>2016-12-28</th>
          <td>27.476015</td>
          <td>116.919998</td>
          <td>226.803986</td>
          <td>29.190001</td>
          <td>116.919998</td>
          <td>243.846161</td>
          <td>29.504999</td>
          <td>118.250000</td>
          <td>245.923080</td>
          <td>29.049999</td>
          <td>116.650002</td>
          <td>243.615387</td>
          <td>29.379999</td>
          <td>118.190002</td>
          <td>244.923080</td>
          <td>83623600</td>
          <td>12087400</td>
          <td>2455141</td>
        </tr>
        <tr>
          <th>2016-12-29</th>
          <td>27.468962</td>
          <td>116.349998</td>
          <td>226.875519</td>
          <td>29.182501</td>
          <td>116.349998</td>
          <td>243.923080</td>
          <td>29.277500</td>
          <td>117.529999</td>
          <td>245.230774</td>
          <td>29.100000</td>
          <td>116.059998</td>
          <td>243.846161</td>
          <td>29.112499</td>
          <td>117.000000</td>
          <td>244.153839</td>
          <td>60158000</td>
          <td>9934900</td>
          <td>2091973</td>
        </tr>
        <tr>
          <th>2016-12-30</th>
          <td>27.254816</td>
          <td>115.050003</td>
          <td>226.088516</td>
          <td>28.955000</td>
          <td>115.050003</td>
          <td>243.076920</td>
          <td>29.299999</td>
          <td>116.830002</td>
          <td>244.615387</td>
          <td>28.857500</td>
          <td>114.769997</td>
          <td>242.384613</td>
          <td>29.162500</td>
          <td>116.599998</td>
          <td>243.307693</td>
          <td>122345200</td>
          <td>18684100</td>
          <td>3309176</td>
        </tr>
        <tr>
          <th>2017-01-03</th>
          <td>27.332474</td>
          <td>116.860001</td>
          <td>226.732422</td>
          <td>29.037500</td>
          <td>116.860001</td>
          <td>243.769226</td>
          <td>29.082500</td>
          <td>117.839996</td>
          <td>244.923080</td>
          <td>28.690001</td>
          <td>115.510002</td>
          <td>241.538467</td>
          <td>28.950001</td>
          <td>116.029999</td>
          <td>243.615387</td>
          <td>115127600</td>
          <td>20663900</td>
          <td>4179435</td>
        </tr>
        <tr>
          <th>2017-01-04</th>
          <td>27.301880</td>
          <td>118.690002</td>
          <td>226.803986</td>
          <td>29.004999</td>
          <td>118.690002</td>
          <td>243.846161</td>
          <td>29.127501</td>
          <td>119.660004</td>
          <td>244.846161</td>
          <td>28.937500</td>
          <td>117.290001</td>
          <td>243.230774</td>
          <td>28.962500</td>
          <td>117.550003</td>
          <td>244.230774</td>
          <td>84472400</td>
          <td>19630900</td>
          <td>2787577</td>
        </tr>
        <tr>
          <th>2017-01-05</th>
          <td>27.440723</td>
          <td>120.669998</td>
          <td>225.516144</td>
          <td>29.152500</td>
          <td>120.669998</td>
          <td>242.461533</td>
          <td>29.215000</td>
          <td>120.949997</td>
          <td>244.230774</td>
          <td>28.952499</td>
          <td>118.320000</td>
          <td>240.846161</td>
          <td>28.980000</td>
          <td>118.860001</td>
          <td>242.846161</td>
          <td>88774400</td>
          <td>19492200</td>
          <td>3361384</td>
        </tr>
        <tr>
          <th>2017-01-06</th>
          <td>27.746635</td>
          <td>123.410004</td>
          <td>226.160049</td>
          <td>29.477501</td>
          <td>123.410004</td>
          <td>243.153839</td>
          <td>29.540001</td>
          <td>123.879997</td>
          <td>244.384613</td>
          <td>29.117500</td>
          <td>120.029999</td>
          <td>241.230774</td>
          <td>29.195000</td>
          <td>120.980003</td>
          <td>242.923080</td>
          <td>127007600</td>
          <td>28545300</td>
          <td>2875704</td>
        </tr>
        <tr>
          <th>2017-01-09</th>
          <td>28.000782</td>
          <td>124.900002</td>
          <td>225.086868</td>
          <td>29.747499</td>
          <td>124.900002</td>
          <td>242.000000</td>
          <td>29.857500</td>
          <td>125.430000</td>
          <td>243.538467</td>
          <td>29.485001</td>
          <td>123.040001</td>
          <td>241.769226</td>
          <td>29.487499</td>
          <td>123.550003</td>
          <td>243.384613</td>
          <td>134247600</td>
          <td>22880400</td>
          <td>2764125</td>
        </tr>
        <tr>
          <th>2017-01-10</th>
          <td>28.029020</td>
          <td>124.349998</td>
          <td>224.442947</td>
          <td>29.777500</td>
          <td>124.349998</td>
          <td>241.307693</td>
          <td>29.844999</td>
          <td>125.500000</td>
          <td>243.230774</td>
          <td>29.575001</td>
          <td>124.279999</td>
          <td>241.307693</td>
          <td>29.692499</td>
          <td>124.820000</td>
          <td>242.000000</td>
          <td>97848400</td>
          <td>17324600</td>
          <td>3536325</td>
        </tr>
        <tr>
          <th>2017-01-11</th>
          <td>28.179625</td>
          <td>126.089996</td>
          <td>225.158386</td>
          <td>29.937500</td>
          <td>126.089996</td>
          <td>242.076920</td>
          <td>29.982500</td>
          <td>126.120003</td>
          <td>242.461533</td>
          <td>29.650000</td>
          <td>124.059998</td>
          <td>240.307693</td>
          <td>29.684999</td>
          <td>124.349998</td>
          <td>240.307693</td>
          <td>110354400</td>
          <td>18356500</td>
          <td>3690063</td>
        </tr>
        <tr>
          <th>2017-01-12</th>
          <td>28.061968</td>
          <td>126.620003</td>
          <td>224.586029</td>
          <td>29.812500</td>
          <td>126.620003</td>
          <td>241.461533</td>
          <td>29.825001</td>
          <td>126.730003</td>
          <td>242.076920</td>
          <td>29.552500</td>
          <td>124.800003</td>
          <td>239.461533</td>
          <td>29.725000</td>
          <td>125.610001</td>
          <td>241.923080</td>
          <td>108344800</td>
          <td>18653900</td>
          <td>3889093</td>
        </tr>
        <tr>
          <th>2017-01-13</th>
          <td>28.012543</td>
          <td>128.339996</td>
          <td>224.371384</td>
          <td>29.760000</td>
          <td>128.339996</td>
          <td>241.230774</td>
          <td>29.905001</td>
          <td>129.270004</td>
          <td>241.923080</td>
          <td>29.702499</td>
          <td>127.370003</td>
          <td>240.384613</td>
          <td>29.777500</td>
          <td>127.489998</td>
          <td>241.230774</td>
          <td>104447600</td>
          <td>24884300</td>
          <td>3162094</td>
        </tr>
        <tr>
          <th>2017-01-17</th>
          <td>28.238459</td>
          <td>127.870003</td>
          <td>223.727493</td>
          <td>30.000000</td>
          <td>127.870003</td>
          <td>240.538467</td>
          <td>30.059999</td>
          <td>128.339996</td>
          <td>241.923080</td>
          <td>29.555000</td>
          <td>127.400002</td>
          <td>239.692307</td>
          <td>29.584999</td>
          <td>128.039993</td>
          <td>239.769226</td>
          <td>137759200</td>
          <td>15294500</td>
          <td>3747549</td>
        </tr>
        <tr>
          <th>2017-01-18</th>
          <td>28.236099</td>
          <td>127.919998</td>
          <td>223.441284</td>
          <td>29.997499</td>
          <td>127.919998</td>
          <td>240.230774</td>
          <td>30.125000</td>
          <td>128.429993</td>
          <td>241.076920</td>
          <td>29.927500</td>
          <td>126.839996</td>
          <td>239.461533</td>
          <td>30.000000</td>
          <td>128.410004</td>
          <td>240.076920</td>
          <td>94852000</td>
          <td>13145900</td>
          <td>3211182</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-22</th>
          <td>148.473312</td>
          <td>324.609985</td>
          <td>104.050003</td>
          <td>148.690002</td>
          <td>324.609985</td>
          <td>104.050003</td>
          <td>150.179993</td>
          <td>329.630005</td>
          <td>104.510002</td>
          <td>148.639999</td>
          <td>321.109985</td>
          <td>102.550003</td>
          <td>149.690002</td>
          <td>326.350006</td>
          <td>103.050003</td>
          <td>58883400</td>
          <td>35224500</td>
          <td>5355000</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>148.423386</td>
          <td>328.690002</td>
          <td>105.300003</td>
          <td>148.639999</td>
          <td>328.690002</td>
          <td>105.300003</td>
          <td>149.369995</td>
          <td>329.559998</td>
          <td>105.989998</td>
          <td>147.619995</td>
          <td>319.720001</td>
          <td>103.330002</td>
          <td>148.679993</td>
          <td>320.299988</td>
          <td>103.639999</td>
          <td>50720600</td>
          <td>38409000</td>
          <td>6496200</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>149.102402</td>
          <td>315.809998</td>
          <td>107.440002</td>
          <td>149.320007</td>
          <td>315.809998</td>
          <td>107.440002</td>
          <td>150.839996</td>
          <td>330.209991</td>
          <td>110.970001</td>
          <td>149.009995</td>
          <td>309.600006</td>
          <td>105.220001</td>
          <td>149.330002</td>
          <td>328.260010</td>
          <td>105.760002</td>
          <td>60893400</td>
          <td>65654000</td>
          <td>11701000</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>148.633087</td>
          <td>312.220001</td>
          <td>103.849998</td>
          <td>148.850006</td>
          <td>312.220001</td>
          <td>103.849998</td>
          <td>149.729996</td>
          <td>319.250000</td>
          <td>108.279999</td>
          <td>148.490005</td>
          <td>312.059998</td>
          <td>103.690002</td>
          <td>149.360001</td>
          <td>314.190002</td>
          <td>107.879997</td>
          <td>56094900</td>
          <td>29971800</td>
          <td>8984300</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>152.347656</td>
          <td>316.920013</td>
          <td>105.260002</td>
          <td>152.570007</td>
          <td>316.920013</td>
          <td>105.260002</td>
          <td>153.169998</td>
          <td>325.519989</td>
          <td>105.379997</td>
          <td>149.720001</td>
          <td>308.109985</td>
          <td>103.099998</td>
          <td>149.820007</td>
          <td>312.989990</td>
          <td>103.389999</td>
          <td>100077900</td>
          <td>50806800</td>
          <td>5910800</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>149.581696</td>
          <td>323.570007</td>
          <td>104.870003</td>
          <td>149.800003</td>
          <td>323.570007</td>
          <td>104.870003</td>
          <td>149.940002</td>
          <td>326.000000</td>
          <td>105.239998</td>
          <td>146.410004</td>
          <td>319.600006</td>
          <td>104.120003</td>
          <td>147.220001</td>
          <td>320.190002</td>
          <td>104.949997</td>
          <td>124850400</td>
          <td>37059400</td>
          <td>5617100</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>148.742920</td>
          <td>329.980011</td>
          <td>106.230003</td>
          <td>148.960007</td>
          <td>329.980011</td>
          <td>106.230003</td>
          <td>149.699997</td>
          <td>333.450012</td>
          <td>106.769997</td>
          <td>147.800003</td>
          <td>326.000000</td>
          <td>105.279999</td>
          <td>148.990005</td>
          <td>326.040009</td>
          <td>105.760002</td>
          <td>74588300</td>
          <td>31518900</td>
          <td>4887100</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>149.801376</td>
          <td>328.079987</td>
          <td>106.690002</td>
          <td>150.020004</td>
          <td>328.079987</td>
          <td>106.690002</td>
          <td>151.570007</td>
          <td>334.790009</td>
          <td>107.139999</td>
          <td>148.649994</td>
          <td>323.799988</td>
          <td>105.300003</td>
          <td>148.660004</td>
          <td>331.380005</td>
          <td>106.339996</td>
          <td>69122000</td>
          <td>28353000</td>
          <td>4480800</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>151.269241</td>
          <td>331.619995</td>
          <td>105.970001</td>
          <td>151.490005</td>
          <td>331.619995</td>
          <td>105.970001</td>
          <td>151.970001</td>
          <td>332.149994</td>
          <td>106.339996</td>
          <td>149.820007</td>
          <td>323.200012</td>
          <td>104.820000</td>
          <td>150.389999</td>
          <td>327.489990</td>
          <td>106.160004</td>
          <td>54511500</td>
          <td>20786500</td>
          <td>4111700</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>150.740005</td>
          <td>335.850006</td>
          <td>105.209999</td>
          <td>150.960007</td>
          <td>335.850006</td>
          <td>105.209999</td>
          <td>152.429993</td>
          <td>337.269989</td>
          <td>106.400002</td>
          <td>150.639999</td>
          <td>332.649994</td>
          <td>104.290001</td>
          <td>151.580002</td>
          <td>334.010010</td>
          <td>105.870003</td>
          <td>60394600</td>
          <td>22495300</td>
          <td>4675800</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>151.279999</td>
          <td>341.130005</td>
          <td>108.739998</td>
          <td>151.279999</td>
          <td>341.130005</td>
          <td>108.739998</td>
          <td>152.199997</td>
          <td>346.790009</td>
          <td>109.650002</td>
          <td>150.059998</td>
          <td>339.640015</td>
          <td>106.849998</td>
          <td>151.889999</td>
          <td>340.309998</td>
          <td>106.930000</td>
          <td>65414600</td>
          <td>26852100</td>
          <td>7600000</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>150.440002</td>
          <td>338.619995</td>
          <td>108.419998</td>
          <td>150.440002</td>
          <td>338.619995</td>
          <td>108.419998</td>
          <td>151.570007</td>
          <td>344.790009</td>
          <td>110.309998</td>
          <td>150.160004</td>
          <td>338.339996</td>
          <td>108.320000</td>
          <td>151.410004</td>
          <td>344.420013</td>
          <td>109.400002</td>
          <td>55020900</td>
          <td>18342500</td>
          <td>5174500</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>150.809998</td>
          <td>335.369995</td>
          <td>111.290001</td>
          <td>150.809998</td>
          <td>335.369995</td>
          <td>111.290001</td>
          <td>151.429993</td>
          <td>341.309998</td>
          <td>116.169998</td>
          <td>150.059998</td>
          <td>334.470001</td>
          <td>110.480003</td>
          <td>150.199997</td>
          <td>340.000000</td>
          <td>114.730003</td>
          <td>56787900</td>
          <td>17556700</td>
          <td>25123700</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>147.919998</td>
          <td>327.640015</td>
          <td>108.959999</td>
          <td>147.919998</td>
          <td>327.640015</td>
          <td>108.959999</td>
          <td>150.130005</td>
          <td>333.190002</td>
          <td>112.680000</td>
          <td>147.850006</td>
          <td>325.510010</td>
          <td>108.110001</td>
          <td>150.020004</td>
          <td>332.489990</td>
          <td>112.500000</td>
          <td>65187100</td>
          <td>21872600</td>
          <td>8692600</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>147.869995</td>
          <td>327.739990</td>
          <td>107.000000</td>
          <td>147.869995</td>
          <td>327.739990</td>
          <td>107.000000</td>
          <td>149.429993</td>
          <td>332.459991</td>
          <td>109.599998</td>
          <td>147.679993</td>
          <td>327.000000</td>
          <td>106.779999</td>
          <td>148.960007</td>
          <td>329.820007</td>
          <td>108.550003</td>
          <td>41000000</td>
          <td>12376600</td>
          <td>5512800</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>149.990005</td>
          <td>340.890015</td>
          <td>107.589996</td>
          <td>149.990005</td>
          <td>340.890015</td>
          <td>107.589996</td>
          <td>150.399994</td>
          <td>341.859985</td>
          <td>107.930000</td>
          <td>147.479996</td>
          <td>329.779999</td>
          <td>106.459999</td>
          <td>148.429993</td>
          <td>330.179993</td>
          <td>107.400002</td>
          <td>63632600</td>
          <td>25387200</td>
          <td>7621900</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>150.000000</td>
          <td>347.559998</td>
          <td>106.669998</td>
          <td>150.000000</td>
          <td>347.559998</td>
          <td>106.669998</td>
          <td>151.880005</td>
          <td>353.649994</td>
          <td>108.669998</td>
          <td>149.429993</td>
          <td>343.200012</td>
          <td>106.199997</td>
          <td>150.369995</td>
          <td>344.339996</td>
          <td>108.029999</td>
          <td>59222800</td>
          <td>25076600</td>
          <td>6124900</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>151.000000</td>
          <td>342.959991</td>
          <td>103.349998</td>
          <td>151.000000</td>
          <td>342.959991</td>
          <td>103.349998</td>
          <td>151.490005</td>
          <td>346.649994</td>
          <td>106.209999</td>
          <td>149.339996</td>
          <td>340.869995</td>
          <td>102.820000</td>
          <td>149.940002</td>
          <td>343.829987</td>
          <td>106.150002</td>
          <td>59256200</td>
          <td>18181100</td>
          <td>11997700</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>153.490005</td>
          <td>340.769989</td>
          <td>101.989998</td>
          <td>153.490005</td>
          <td>340.769989</td>
          <td>101.989998</td>
          <td>155.000000</td>
          <td>347.299988</td>
          <td>103.879997</td>
          <td>150.990005</td>
          <td>340.100006</td>
          <td>101.419998</td>
          <td>151.000000</td>
          <td>344.239990</td>
          <td>103.699997</td>
          <td>88807000</td>
          <td>13602800</td>
          <td>8307600</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>157.869995</td>
          <td>338.690002</td>
          <td>100.669998</td>
          <td>157.869995</td>
          <td>338.690002</td>
          <td>100.669998</td>
          <td>158.669998</td>
          <td>342.459991</td>
          <td>101.800003</td>
          <td>153.050003</td>
          <td>335.299988</td>
          <td>99.180000</td>
          <td>153.710007</td>
          <td>339.720001</td>
          <td>101.430000</td>
          <td>137827700</td>
          <td>17487200</td>
          <td>8530900</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>160.550003</td>
          <td>345.299988</td>
          <td>99.959999</td>
          <td>160.550003</td>
          <td>345.299988</td>
          <td>99.959999</td>
          <td>161.020004</td>
          <td>352.100006</td>
          <td>100.739998</td>
          <td>156.529999</td>
          <td>339.899994</td>
          <td>99.300003</td>
          <td>157.649994</td>
          <td>342.200012</td>
          <td>99.800003</td>
          <td>117305600</td>
          <td>26488500</td>
          <td>6603300</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>161.020004</td>
          <td>341.010010</td>
          <td>101.040001</td>
          <td>161.020004</td>
          <td>341.010010</td>
          <td>101.040001</td>
          <td>165.699997</td>
          <td>353.829987</td>
          <td>101.970001</td>
          <td>161.000000</td>
          <td>340.510010</td>
          <td>100.279999</td>
          <td>161.679993</td>
          <td>349.049988</td>
          <td>100.470001</td>
          <td>117467900</td>
          <td>27116800</td>
          <td>6206600</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>161.410004</td>
          <td>337.250000</td>
          <td>102.080002</td>
          <td>161.410004</td>
          <td>337.250000</td>
          <td>102.080002</td>
          <td>161.800003</td>
          <td>341.399994</td>
          <td>102.209999</td>
          <td>159.059998</td>
          <td>333.500000</td>
          <td>101.150002</td>
          <td>161.119995</td>
          <td>338.929993</td>
          <td>101.779999</td>
          <td>96041900</td>
          <td>17225000</td>
          <td>6011400</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>161.940002</td>
          <td>341.059998</td>
          <td>102.230003</td>
          <td>161.940002</td>
          <td>341.059998</td>
          <td>102.230003</td>
          <td>162.139999</td>
          <td>341.779999</td>
          <td>102.320000</td>
          <td>159.639999</td>
          <td>332.809998</td>
          <td>101.309998</td>
          <td>160.750000</td>
          <td>336.000000</td>
          <td>101.860001</td>
          <td>69463600</td>
          <td>13566200</td>
          <td>5572100</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>156.809998</td>
          <td>333.119995</td>
          <td>97.839996</td>
          <td>156.809998</td>
          <td>333.119995</td>
          <td>97.839996</td>
          <td>160.449997</td>
          <td>337.750000</td>
          <td>98.099998</td>
          <td>156.360001</td>
          <td>331.899994</td>
          <td>95.510002</td>
          <td>159.570007</td>
          <td>335.799988</td>
          <td>96.660004</td>
          <td>76959800</td>
          <td>14750700</td>
          <td>8607600</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>160.240005</td>
          <td>338.029999</td>
          <td>98.400002</td>
          <td>160.240005</td>
          <td>338.029999</td>
          <td>98.400002</td>
          <td>161.190002</td>
          <td>340.670013</td>
          <td>100.430000</td>
          <td>158.789993</td>
          <td>335.309998</td>
          <td>96.830002</td>
          <td>159.369995</td>
          <td>336.890015</td>
          <td>99.269997</td>
          <td>88748200</td>
          <td>16650900</td>
          <td>9776600</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>165.300003</td>
          <td>324.459991</td>
          <td>94.989998</td>
          <td>165.300003</td>
          <td>324.459991</td>
          <td>94.989998</td>
          <td>165.520004</td>
          <td>335.809998</td>
          <td>97.430000</td>
          <td>159.919998</td>
          <td>323.429993</td>
          <td>94.470001</td>
          <td>159.990005</td>
          <td>335.000000</td>
          <td>96.639999</td>
          <td>174048100</td>
          <td>25390000</td>
          <td>11409400</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>164.770004</td>
          <td>310.600006</td>
          <td>93.000000</td>
          <td>164.770004</td>
          <td>310.600006</td>
          <td>93.000000</td>
          <td>170.300003</td>
          <td>330.500000</td>
          <td>96.889999</td>
          <td>164.529999</td>
          <td>310.290009</td>
          <td>92.940002</td>
          <td>167.479996</td>
          <td>330.290009</td>
          <td>96.550003</td>
          <td>152052500</td>
          <td>30329600</td>
          <td>8657100</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>163.759995</td>
          <td>310.390015</td>
          <td>95.230003</td>
          <td>163.759995</td>
          <td>310.390015</td>
          <td>95.230003</td>
          <td>164.199997</td>
          <td>314.600006</td>
          <td>95.779999</td>
          <td>157.800003</td>
          <td>307.200012</td>
          <td>92.809998</td>
          <td>158.740005</td>
          <td>311.399994</td>
          <td>94.199997</td>
          <td>136739200</td>
          <td>24396200</td>
          <td>6094600</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>161.839996</td>
          <td>306.839996</td>
          <td>92.769997</td>
          <td>161.839996</td>
          <td>306.839996</td>
          <td>92.769997</td>
          <td>164.960007</td>
          <td>313.750000</td>
          <td>95.349998</td>
          <td>159.720001</td>
          <td>299.500000</td>
          <td>91.730003</td>
          <td>164.020004</td>
          <td>313.730011</td>
          <td>95.129997</td>
          <td>117938300</td>
          <td>27448700</td>
          <td>8079800</td>
        </tr>
      </tbody>
    </table>
    <p>1259 rows × 18 columns</p>
    </div>



.. code:: ipython3

     stock=yf.download(ticker, period="5y").Close


.. parsed-literal::

    [*********************100%***********************]  3 of 3 completed


.. code:: ipython3

    import matplotlib.pyplot as plt

.. code:: ipython3

    stock.plot()
    plt.show()



.. image:: output_35_0.png


 ### FInancial Indices

.. code:: ipython3

    index = ['^DJI', '^GSPC']

.. code:: ipython3

    stock = yf.download(index,period='10y').Close


.. parsed-literal::

    [*********************100%***********************]  2 of 2 completed


.. code:: ipython3

    stock.plot()
    plt.show()



.. image:: output_39_0.png


.. code:: ipython3

    #Total Return
    index = ['^DJITR', '^SP500TR']

.. code:: ipython3

    indexes = yf.download(index,period='10y').Close


.. parsed-literal::

    [*********************100%***********************]  2 of 2 completed


.. code:: ipython3

    indexes




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>^DJITR</th>
          <th>^SP500TR</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2011-12-05</th>
          <td>NaN</td>
          <td>2154.679932</td>
        </tr>
        <tr>
          <th>2011-12-06</th>
          <td>NaN</td>
          <td>2157.100098</td>
        </tr>
        <tr>
          <th>2011-12-07</th>
          <td>NaN</td>
          <td>2162.070068</td>
        </tr>
        <tr>
          <th>2011-12-08</th>
          <td>NaN</td>
          <td>2116.409912</td>
        </tr>
        <tr>
          <th>2011-12-09</th>
          <td>NaN</td>
          <td>2152.149902</td>
        </tr>
        <tr>
          <th>2011-12-12</th>
          <td>NaN</td>
          <td>2120.149902</td>
        </tr>
        <tr>
          <th>2011-12-13</th>
          <td>NaN</td>
          <td>2102.149902</td>
        </tr>
        <tr>
          <th>2011-12-14</th>
          <td>NaN</td>
          <td>2078.510010</td>
        </tr>
        <tr>
          <th>2011-12-15</th>
          <td>NaN</td>
          <td>2085.439941</td>
        </tr>
        <tr>
          <th>2011-12-16</th>
          <td>NaN</td>
          <td>2092.179932</td>
        </tr>
        <tr>
          <th>2011-12-19</th>
          <td>NaN</td>
          <td>2067.669922</td>
        </tr>
        <tr>
          <th>2011-12-20</th>
          <td>NaN</td>
          <td>2129.669922</td>
        </tr>
        <tr>
          <th>2011-12-21</th>
          <td>NaN</td>
          <td>2133.860107</td>
        </tr>
        <tr>
          <th>2011-12-22</th>
          <td>NaN</td>
          <td>2152.040039</td>
        </tr>
        <tr>
          <th>2011-12-23</th>
          <td>NaN</td>
          <td>2171.500000</td>
        </tr>
        <tr>
          <th>2011-12-27</th>
          <td>NaN</td>
          <td>2171.709961</td>
        </tr>
        <tr>
          <th>2011-12-28</th>
          <td>NaN</td>
          <td>2145.090088</td>
        </tr>
        <tr>
          <th>2011-12-29</th>
          <td>NaN</td>
          <td>2168.120117</td>
        </tr>
        <tr>
          <th>2011-12-30</th>
          <td>NaN</td>
          <td>2158.939941</td>
        </tr>
        <tr>
          <th>2012-01-03</th>
          <td>NaN</td>
          <td>2192.399902</td>
        </tr>
        <tr>
          <th>2012-01-04</th>
          <td>NaN</td>
          <td>2193.280029</td>
        </tr>
        <tr>
          <th>2012-01-05</th>
          <td>NaN</td>
          <td>2199.729980</td>
        </tr>
        <tr>
          <th>2012-01-06</th>
          <td>NaN</td>
          <td>2194.979980</td>
        </tr>
        <tr>
          <th>2012-01-09</th>
          <td>NaN</td>
          <td>2200.000000</td>
        </tr>
        <tr>
          <th>2012-01-10</th>
          <td>NaN</td>
          <td>2219.580078</td>
        </tr>
        <tr>
          <th>2012-01-11</th>
          <td>NaN</td>
          <td>2220.479980</td>
        </tr>
        <tr>
          <th>2012-01-12</th>
          <td>NaN</td>
          <td>2225.739990</td>
        </tr>
        <tr>
          <th>2012-01-13</th>
          <td>NaN</td>
          <td>2214.729980</td>
        </tr>
        <tr>
          <th>2012-01-17</th>
          <td>NaN</td>
          <td>2222.590088</td>
        </tr>
        <tr>
          <th>2012-01-18</th>
          <td>NaN</td>
          <td>2247.639893</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-22</th>
          <td>NaN</td>
          <td>9496.860352</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>NaN</td>
          <td>9541.990234</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>NaN</td>
          <td>9559.389648</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>NaN</td>
          <td>9511.269531</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>NaN</td>
          <td>9605.230469</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>NaN</td>
          <td>9625.019531</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>NaN</td>
          <td>9642.440430</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>NaN</td>
          <td>9677.950195</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>NaN</td>
          <td>9740.469727</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>NaN</td>
          <td>9782.480469</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>NaN</td>
          <td>9819.980469</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>NaN</td>
          <td>9828.809570</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>NaN</td>
          <td>9795.120117</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>NaN</td>
          <td>9716.719727</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>NaN</td>
          <td>9722.080078</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>NaN</td>
          <td>9793.219727</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>NaN</td>
          <td>9793.530273</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>NaN</td>
          <td>9831.910156</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>NaN</td>
          <td>9808.269531</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>NaN</td>
          <td>9842.349609</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>NaN</td>
          <td>9828.799805</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>NaN</td>
          <td>9798.290039</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>NaN</td>
          <td>9814.650391</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>NaN</td>
          <td>9837.599609</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>NaN</td>
          <td>9614.250000</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>NaN</td>
          <td>9741.780273</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>NaN</td>
          <td>9558.330078</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>NaN</td>
          <td>9446.209961</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>NaN</td>
          <td>9581.790039</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>81429.140625</td>
          <td>9501.280273</td>
        </tr>
      </tbody>
    </table>
    <p>2517 rows × 2 columns</p>
    </div>



 ### Currencies

.. code:: ipython3

    #Tickers
    ticker1 = "EURUSD=X"
    ticker2 = "USDEUR=X"

.. code:: ipython3

    yf.download(ticker1,period='5y')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2016-12-05</th>
          <td>1.057083</td>
          <td>1.074114</td>
          <td>1.054185</td>
          <td>1.058201</td>
          <td>1.058201</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-06</th>
          <td>1.075847</td>
          <td>1.078516</td>
          <td>1.072600</td>
          <td>1.075732</td>
          <td>1.075732</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-07</th>
          <td>1.071926</td>
          <td>1.076900</td>
          <td>1.071352</td>
          <td>1.072041</td>
          <td>1.072041</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-08</th>
          <td>1.076009</td>
          <td>1.085658</td>
          <td>1.061000</td>
          <td>1.076195</td>
          <td>1.076195</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-09</th>
          <td>1.062135</td>
          <td>1.063151</td>
          <td>1.053841</td>
          <td>1.062135</td>
          <td>1.062135</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-12</th>
          <td>1.054630</td>
          <td>1.062699</td>
          <td>1.052742</td>
          <td>1.054741</td>
          <td>1.054741</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-13</th>
          <td>1.064283</td>
          <td>1.065303</td>
          <td>1.060670</td>
          <td>1.064169</td>
          <td>1.064169</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-14</th>
          <td>1.063038</td>
          <td>1.066667</td>
          <td>1.061500</td>
          <td>1.062925</td>
          <td>1.062925</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-15</th>
          <td>1.051525</td>
          <td>1.052521</td>
          <td>1.040366</td>
          <td>1.051414</td>
          <td>1.051414</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-16</th>
          <td>1.041775</td>
          <td>1.047230</td>
          <td>1.040366</td>
          <td>1.041884</td>
          <td>1.041884</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-19</th>
          <td>1.044823</td>
          <td>1.048196</td>
          <td>1.041341</td>
          <td>1.044998</td>
          <td>1.044998</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-20</th>
          <td>1.040475</td>
          <td>1.041992</td>
          <td>1.035518</td>
          <td>1.040583</td>
          <td>1.040583</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-21</th>
          <td>1.039393</td>
          <td>1.045151</td>
          <td>1.038530</td>
          <td>1.039047</td>
          <td>1.039047</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-22</th>
          <td>1.042753</td>
          <td>1.049759</td>
          <td>1.042753</td>
          <td>1.042862</td>
          <td>1.042862</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-23</th>
          <td>1.043950</td>
          <td>1.046792</td>
          <td>1.042970</td>
          <td>1.043765</td>
          <td>1.043765</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-26</th>
          <td>1.045588</td>
          <td>1.047011</td>
          <td>1.044600</td>
          <td>1.045478</td>
          <td>1.045478</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-27</th>
          <td>1.045577</td>
          <td>1.046134</td>
          <td>1.043536</td>
          <td>1.045697</td>
          <td>1.045697</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-28</th>
          <td>1.046244</td>
          <td>1.048218</td>
          <td>1.038745</td>
          <td>1.046233</td>
          <td>1.046233</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-29</th>
          <td>1.041775</td>
          <td>1.049098</td>
          <td>1.041775</td>
          <td>1.041699</td>
          <td>1.041699</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-30</th>
          <td>1.056904</td>
          <td>1.059098</td>
          <td>1.051000</td>
          <td>1.057530</td>
          <td>1.057530</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-02</th>
          <td>1.053075</td>
          <td>1.054074</td>
          <td>1.046572</td>
          <td>1.052698</td>
          <td>1.052698</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-03</th>
          <td>1.045916</td>
          <td>1.049208</td>
          <td>1.034768</td>
          <td>1.046003</td>
          <td>1.046003</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-04</th>
          <td>1.041840</td>
          <td>1.047889</td>
          <td>1.039134</td>
          <td>1.041992</td>
          <td>1.041992</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-05</th>
          <td>1.049869</td>
          <td>1.060895</td>
          <td>1.048658</td>
          <td>1.050089</td>
          <td>1.050089</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-06</th>
          <td>1.060558</td>
          <td>1.060895</td>
          <td>1.053963</td>
          <td>1.060592</td>
          <td>1.060592</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-09</th>
          <td>1.053408</td>
          <td>1.056078</td>
          <td>1.051348</td>
          <td>1.053186</td>
          <td>1.053186</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-10</th>
          <td>1.058761</td>
          <td>1.062586</td>
          <td>1.056189</td>
          <td>1.058862</td>
          <td>1.058862</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-11</th>
          <td>1.055409</td>
          <td>1.056747</td>
          <td>1.045697</td>
          <td>1.055242</td>
          <td>1.055242</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-12</th>
          <td>1.059659</td>
          <td>1.068604</td>
          <td>1.057530</td>
          <td>1.059771</td>
          <td>1.059771</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-13</th>
          <td>1.061797</td>
          <td>1.066780</td>
          <td>1.060000</td>
          <td>1.061684</td>
          <td>1.061684</td>
          <td>0</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>1.164131</td>
          <td>1.166861</td>
          <td>1.159326</td>
          <td>1.164009</td>
          <td>1.164009</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>1.161170</td>
          <td>1.162900</td>
          <td>1.158587</td>
          <td>1.161170</td>
          <td>1.161170</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>1.159824</td>
          <td>1.162439</td>
          <td>1.158534</td>
          <td>1.159824</td>
          <td>1.159824</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>1.159891</td>
          <td>1.169317</td>
          <td>1.158319</td>
          <td>1.160012</td>
          <td>1.160012</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>1.168374</td>
          <td>1.169180</td>
          <td>1.154668</td>
          <td>1.168361</td>
          <td>1.168361</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>1.155936</td>
          <td>1.159326</td>
          <td>1.154668</td>
          <td>1.155668</td>
          <td>1.155668</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>1.160174</td>
          <td>1.161500</td>
          <td>1.157917</td>
          <td>1.159958</td>
          <td>1.159958</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>1.158078</td>
          <td>1.159900</td>
          <td>1.156363</td>
          <td>1.157943</td>
          <td>1.157943</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>1.161575</td>
          <td>1.161710</td>
          <td>1.152924</td>
          <td>1.161575</td>
          <td>1.161575</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>1.155668</td>
          <td>1.156470</td>
          <td>1.151410</td>
          <td>1.155535</td>
          <td>1.155535</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>1.156845</td>
          <td>1.159555</td>
          <td>1.155175</td>
          <td>1.156885</td>
          <td>1.156885</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>1.158869</td>
          <td>1.160901</td>
          <td>1.157019</td>
          <td>1.159152</td>
          <td>1.159152</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>1.159366</td>
          <td>1.159824</td>
          <td>1.151344</td>
          <td>1.159555</td>
          <td>1.159555</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>1.148567</td>
          <td>1.149161</td>
          <td>1.145489</td>
          <td>1.148594</td>
          <td>1.148594</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>1.144780</td>
          <td>1.145987</td>
          <td>1.143406</td>
          <td>1.145082</td>
          <td>1.145082</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>1.144230</td>
          <td>1.146421</td>
          <td>1.141696</td>
          <td>1.144165</td>
          <td>1.144165</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>1.136738</td>
          <td>1.138701</td>
          <td>1.133067</td>
          <td>1.136648</td>
          <td>1.136648</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>1.131618</td>
          <td>1.133400</td>
          <td>1.127053</td>
          <td>1.132118</td>
          <td>1.132118</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>1.131811</td>
          <td>1.135976</td>
          <td>1.131503</td>
          <td>1.132118</td>
          <td>1.132118</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>1.137010</td>
          <td>1.137010</td>
          <td>1.125239</td>
          <td>1.136842</td>
          <td>1.136842</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>1.127574</td>
          <td>1.129050</td>
          <td>1.123823</td>
          <td>1.127574</td>
          <td>1.127574</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>1.124354</td>
          <td>1.127345</td>
          <td>1.122712</td>
          <td>1.124215</td>
          <td>1.124215</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>1.124391</td>
          <td>1.125454</td>
          <td>1.118781</td>
          <td>1.124493</td>
          <td>1.124493</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-25</th>
          <td>1.120699</td>
          <td>1.123091</td>
          <td>1.120398</td>
          <td>1.120298</td>
          <td>1.120298</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>1.120900</td>
          <td>1.132200</td>
          <td>1.120800</td>
          <td>1.120963</td>
          <td>1.120963</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>1.129114</td>
          <td>1.129801</td>
          <td>1.125885</td>
          <td>1.129318</td>
          <td>1.129318</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>1.129357</td>
          <td>1.138174</td>
          <td>1.124606</td>
          <td>1.129344</td>
          <td>1.129344</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>1.133003</td>
          <td>1.135847</td>
          <td>1.130416</td>
          <td>1.133029</td>
          <td>1.133029</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>1.131964</td>
          <td>1.134816</td>
          <td>1.130186</td>
          <td>1.131952</td>
          <td>1.131952</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>1.130684</td>
          <td>1.133183</td>
          <td>1.126735</td>
          <td>1.130621</td>
          <td>1.130621</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    <p>1302 rows × 6 columns</p>
    </div>



.. code:: ipython3

    yf.download(ticker2,period='5y')


.. parsed-literal::

    [*********************100%***********************]  1 of 1 completed




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Adj Close</th>
          <th>Volume</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2016-12-05</th>
          <td>0.94600</td>
          <td>0.948600</td>
          <td>0.931000</td>
          <td>0.94500</td>
          <td>0.94500</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-06</th>
          <td>0.92950</td>
          <td>0.932314</td>
          <td>0.927200</td>
          <td>0.92960</td>
          <td>0.92960</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-07</th>
          <td>0.93290</td>
          <td>0.933400</td>
          <td>0.928591</td>
          <td>0.93280</td>
          <td>0.93280</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-08</th>
          <td>0.92936</td>
          <td>0.942507</td>
          <td>0.921100</td>
          <td>0.92920</td>
          <td>0.92920</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-09</th>
          <td>0.94150</td>
          <td>0.948910</td>
          <td>0.940600</td>
          <td>0.94150</td>
          <td>0.94150</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-12</th>
          <td>0.94820</td>
          <td>0.949900</td>
          <td>0.941000</td>
          <td>0.94810</td>
          <td>0.94810</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-13</th>
          <td>0.93960</td>
          <td>0.942800</td>
          <td>0.938700</td>
          <td>0.93970</td>
          <td>0.93970</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-14</th>
          <td>0.94070</td>
          <td>0.942063</td>
          <td>0.937500</td>
          <td>0.94080</td>
          <td>0.94080</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-15</th>
          <td>0.95100</td>
          <td>0.961200</td>
          <td>0.950100</td>
          <td>0.95110</td>
          <td>0.95110</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-16</th>
          <td>0.95990</td>
          <td>0.961200</td>
          <td>0.954900</td>
          <td>0.95980</td>
          <td>0.95980</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-19</th>
          <td>0.95710</td>
          <td>0.960300</td>
          <td>0.954020</td>
          <td>0.95694</td>
          <td>0.95694</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-20</th>
          <td>0.96110</td>
          <td>0.965700</td>
          <td>0.959700</td>
          <td>0.96100</td>
          <td>0.96100</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-21</th>
          <td>0.96210</td>
          <td>0.962900</td>
          <td>0.956800</td>
          <td>0.96242</td>
          <td>0.96242</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-22</th>
          <td>0.95900</td>
          <td>0.959000</td>
          <td>0.952600</td>
          <td>0.95890</td>
          <td>0.95890</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-23</th>
          <td>0.95790</td>
          <td>0.958800</td>
          <td>0.955300</td>
          <td>0.95807</td>
          <td>0.95807</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-26</th>
          <td>0.95640</td>
          <td>0.957304</td>
          <td>0.955100</td>
          <td>0.95650</td>
          <td>0.95650</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-27</th>
          <td>0.95641</td>
          <td>0.958280</td>
          <td>0.955900</td>
          <td>0.95630</td>
          <td>0.95630</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-28</th>
          <td>0.95580</td>
          <td>0.962700</td>
          <td>0.954000</td>
          <td>0.95581</td>
          <td>0.95581</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-29</th>
          <td>0.95990</td>
          <td>0.959900</td>
          <td>0.953200</td>
          <td>0.95997</td>
          <td>0.95997</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-30</th>
          <td>0.94616</td>
          <td>0.951475</td>
          <td>0.944200</td>
          <td>0.94560</td>
          <td>0.94560</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-02</th>
          <td>0.94960</td>
          <td>0.955500</td>
          <td>0.948700</td>
          <td>0.94994</td>
          <td>0.94994</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-03</th>
          <td>0.95610</td>
          <td>0.966400</td>
          <td>0.953100</td>
          <td>0.95602</td>
          <td>0.95602</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-04</th>
          <td>0.95984</td>
          <td>0.962340</td>
          <td>0.954300</td>
          <td>0.95970</td>
          <td>0.95970</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-05</th>
          <td>0.95250</td>
          <td>0.953600</td>
          <td>0.942600</td>
          <td>0.95230</td>
          <td>0.95230</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-06</th>
          <td>0.94290</td>
          <td>0.948800</td>
          <td>0.942600</td>
          <td>0.94287</td>
          <td>0.94287</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-09</th>
          <td>0.94930</td>
          <td>0.951160</td>
          <td>0.946900</td>
          <td>0.94950</td>
          <td>0.94950</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-10</th>
          <td>0.94450</td>
          <td>0.946800</td>
          <td>0.941100</td>
          <td>0.94441</td>
          <td>0.94441</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-11</th>
          <td>0.94750</td>
          <td>0.956300</td>
          <td>0.946300</td>
          <td>0.94765</td>
          <td>0.94765</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-12</th>
          <td>0.94370</td>
          <td>0.945600</td>
          <td>0.935800</td>
          <td>0.94360</td>
          <td>0.94360</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2017-01-13</th>
          <td>0.94180</td>
          <td>0.943396</td>
          <td>0.937400</td>
          <td>0.94190</td>
          <td>0.94190</td>
          <td>0</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2021-10-25</th>
          <td>0.85901</td>
          <td>0.862570</td>
          <td>0.857000</td>
          <td>0.85910</td>
          <td>0.85910</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-26</th>
          <td>0.86120</td>
          <td>0.863120</td>
          <td>0.859919</td>
          <td>0.86120</td>
          <td>0.86120</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-27</th>
          <td>0.86220</td>
          <td>0.863160</td>
          <td>0.860260</td>
          <td>0.86220</td>
          <td>0.86220</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-28</th>
          <td>0.86215</td>
          <td>0.863320</td>
          <td>0.855200</td>
          <td>0.86206</td>
          <td>0.86206</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-10-29</th>
          <td>0.85589</td>
          <td>0.866050</td>
          <td>0.855300</td>
          <td>0.85590</td>
          <td>0.85590</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-01</th>
          <td>0.86510</td>
          <td>0.866050</td>
          <td>0.862570</td>
          <td>0.86530</td>
          <td>0.86530</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-02</th>
          <td>0.86194</td>
          <td>0.863620</td>
          <td>0.860956</td>
          <td>0.86210</td>
          <td>0.86210</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-03</th>
          <td>0.86350</td>
          <td>0.864780</td>
          <td>0.862143</td>
          <td>0.86360</td>
          <td>0.86360</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-04</th>
          <td>0.86090</td>
          <td>0.867360</td>
          <td>0.860800</td>
          <td>0.86090</td>
          <td>0.86090</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-05</th>
          <td>0.86530</td>
          <td>0.868500</td>
          <td>0.864700</td>
          <td>0.86540</td>
          <td>0.86540</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-08</th>
          <td>0.86442</td>
          <td>0.865670</td>
          <td>0.862400</td>
          <td>0.86439</td>
          <td>0.86439</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-09</th>
          <td>0.86291</td>
          <td>0.864290</td>
          <td>0.861400</td>
          <td>0.86270</td>
          <td>0.86270</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-10</th>
          <td>0.86254</td>
          <td>0.868550</td>
          <td>0.862200</td>
          <td>0.86240</td>
          <td>0.86240</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-11</th>
          <td>0.87065</td>
          <td>0.872990</td>
          <td>0.870200</td>
          <td>0.87063</td>
          <td>0.87063</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-12</th>
          <td>0.87353</td>
          <td>0.874580</td>
          <td>0.872610</td>
          <td>0.87330</td>
          <td>0.87330</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-15</th>
          <td>0.87395</td>
          <td>0.875890</td>
          <td>0.872280</td>
          <td>0.87400</td>
          <td>0.87400</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-16</th>
          <td>0.87971</td>
          <td>0.882560</td>
          <td>0.878194</td>
          <td>0.87978</td>
          <td>0.87978</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-17</th>
          <td>0.88369</td>
          <td>0.887270</td>
          <td>0.882301</td>
          <td>0.88330</td>
          <td>0.88330</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-18</th>
          <td>0.88354</td>
          <td>0.883780</td>
          <td>0.880300</td>
          <td>0.88330</td>
          <td>0.88330</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-19</th>
          <td>0.87950</td>
          <td>0.888700</td>
          <td>0.879500</td>
          <td>0.87963</td>
          <td>0.87963</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-22</th>
          <td>0.88686</td>
          <td>0.889820</td>
          <td>0.885700</td>
          <td>0.88686</td>
          <td>0.88686</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-23</th>
          <td>0.88940</td>
          <td>0.890700</td>
          <td>0.887040</td>
          <td>0.88951</td>
          <td>0.88951</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-24</th>
          <td>0.88937</td>
          <td>0.893830</td>
          <td>0.888530</td>
          <td>0.88929</td>
          <td>0.88929</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-25</th>
          <td>0.89230</td>
          <td>0.892540</td>
          <td>0.890400</td>
          <td>0.89262</td>
          <td>0.89262</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-26</th>
          <td>0.89214</td>
          <td>0.892220</td>
          <td>0.883236</td>
          <td>0.89209</td>
          <td>0.89209</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-29</th>
          <td>0.88565</td>
          <td>0.888190</td>
          <td>0.885112</td>
          <td>0.88549</td>
          <td>0.88549</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-11-30</th>
          <td>0.88546</td>
          <td>0.889200</td>
          <td>0.878600</td>
          <td>0.88547</td>
          <td>0.88547</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-01</th>
          <td>0.88261</td>
          <td>0.884630</td>
          <td>0.880400</td>
          <td>0.88259</td>
          <td>0.88259</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-02</th>
          <td>0.88342</td>
          <td>0.884810</td>
          <td>0.881200</td>
          <td>0.88343</td>
          <td>0.88343</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2021-12-03</th>
          <td>0.88442</td>
          <td>0.887520</td>
          <td>0.882470</td>
          <td>0.88447</td>
          <td>0.88447</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    <p>1302 rows × 6 columns</p>
    </div>



 ### Crypto

.. code:: ipython3

    #Tickers
    ticker1 = ["BTC-USD", "ETH-USD"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')


.. parsed-literal::

    [*********************100%***********************]  2 of 2 completed


.. code:: ipython3

    data.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead tr th {
            text-align: left;
        }

        .dataframe thead tr:last-of-type th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <th colspan="2" halign="left">Adj Close</th>
          <th colspan="2" halign="left">Close</th>
          <th colspan="2" halign="left">High</th>
          <th colspan="2" halign="left">Low</th>
          <th colspan="2" halign="left">Open</th>
          <th colspan="2" halign="left">Volume</th>
        </tr>
        <tr>
          <th></th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
          <th>BTC-USD</th>
          <th>ETH-USD</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2019-08-01</th>
          <td>10399.668945</td>
          <td>217.808441</td>
          <td>10399.668945</td>
          <td>217.808441</td>
          <td>10446.919922</td>
          <td>218.812653</td>
          <td>9922.019531</td>
          <td>212.914505</td>
          <td>10077.442383</td>
          <td>218.554596</td>
          <td>17165337858</td>
          <td>5965442642</td>
        </tr>
        <tr>
          <th>2019-08-02</th>
          <td>10518.174805</td>
          <td>217.871567</td>
          <td>10518.174805</td>
          <td>217.871567</td>
          <td>10657.953125</td>
          <td>222.182571</td>
          <td>10371.013672</td>
          <td>215.975830</td>
          <td>10402.042969</td>
          <td>217.884460</td>
          <td>17489094082</td>
          <td>6159440229</td>
        </tr>
        <tr>
          <th>2019-08-03</th>
          <td>10821.726562</td>
          <td>222.490341</td>
          <td>10821.726562</td>
          <td>222.490341</td>
          <td>10946.781250</td>
          <td>224.623230</td>
          <td>10503.504883</td>
          <td>217.331741</td>
          <td>10519.278320</td>
          <td>217.895554</td>
          <td>15352685061</td>
          <td>5697798687</td>
        </tr>
        <tr>
          <th>2019-08-04</th>
          <td>10970.184570</td>
          <td>222.669724</td>
          <td>10970.184570</td>
          <td>222.669724</td>
          <td>11009.207031</td>
          <td>224.227295</td>
          <td>10620.278320</td>
          <td>218.492172</td>
          <td>10821.632812</td>
          <td>222.580811</td>
          <td>16530894787</td>
          <td>5238542572</td>
        </tr>
        <tr>
          <th>2019-08-05</th>
          <td>11805.653320</td>
          <td>234.215027</td>
          <td>11805.653320</td>
          <td>234.215027</td>
          <td>11895.091797</td>
          <td>235.635284</td>
          <td>10960.735352</td>
          <td>222.603882</td>
          <td>10960.735352</td>
          <td>222.650879</td>
          <td>23875988832</td>
          <td>7765060287</td>
        </tr>
      </tbody>
    </table>
    </div>



 ### Mutual Funds

.. code:: ipython3

    #Tickers
    #20+Y Treasury Bobd ETF and Vivoldi Multi-Strategy Fund Class
    ticker1 = ["TLT", "OMOIX"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')


.. parsed-literal::

    [*********************100%***********************]  2 of 2 completed


.. code:: ipython3

    data.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead tr th {
            text-align: left;
        }

        .dataframe thead tr:last-of-type th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <th colspan="2" halign="left">Adj Close</th>
          <th colspan="2" halign="left">Close</th>
          <th colspan="2" halign="left">High</th>
          <th colspan="2" halign="left">Low</th>
          <th colspan="2" halign="left">Open</th>
          <th colspan="2" halign="left">Volume</th>
        </tr>
        <tr>
          <th></th>
          <th>OMOIX</th>
          <th>TLT</th>
          <th>OMOIX</th>
          <th>TLT</th>
          <th>OMOIX</th>
          <th>TLT</th>
          <th>OMOIX</th>
          <th>TLT</th>
          <th>OMOIX</th>
          <th>TLT</th>
          <th>OMOIX</th>
          <th>TLT</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2019-08-01</th>
          <td>23.186359</td>
          <td>130.281784</td>
          <td>27.34</td>
          <td>135.259995</td>
          <td>27.34</td>
          <td>135.389999</td>
          <td>27.34</td>
          <td>133.259995</td>
          <td>27.34</td>
          <td>133.389999</td>
          <td>0.0</td>
          <td>26664800.0</td>
        </tr>
        <tr>
          <th>2019-08-02</th>
          <td>23.245722</td>
          <td>131.485764</td>
          <td>27.41</td>
          <td>136.509995</td>
          <td>27.41</td>
          <td>136.509995</td>
          <td>27.41</td>
          <td>135.399994</td>
          <td>27.41</td>
          <td>135.660004</td>
          <td>0.0</td>
          <td>15143100.0</td>
        </tr>
        <tr>
          <th>2019-08-05</th>
          <td>23.186359</td>
          <td>133.758911</td>
          <td>27.34</td>
          <td>138.869995</td>
          <td>27.34</td>
          <td>138.889999</td>
          <td>27.34</td>
          <td>137.660004</td>
          <td>27.34</td>
          <td>138.139999</td>
          <td>0.0</td>
          <td>18543000.0</td>
        </tr>
        <tr>
          <th>2019-08-06</th>
          <td>23.169395</td>
          <td>134.828049</td>
          <td>27.32</td>
          <td>139.979996</td>
          <td>27.32</td>
          <td>139.979996</td>
          <td>27.32</td>
          <td>138.089996</td>
          <td>27.32</td>
          <td>138.199997</td>
          <td>0.0</td>
          <td>12747400.0</td>
        </tr>
        <tr>
          <th>2019-08-07</th>
          <td>23.177877</td>
          <td>134.876205</td>
          <td>27.33</td>
          <td>140.029999</td>
          <td>27.33</td>
          <td>143.059998</td>
          <td>27.33</td>
          <td>139.779999</td>
          <td>27.33</td>
          <td>142.399994</td>
          <td>0.0</td>
          <td>32582000.0</td>
        </tr>
      </tbody>
    </table>
    </div>



 ### Treasury Rates

.. code:: ipython3

    #10Y and 5Y Treasury Rates
    ticker1 = ["^TNX", "^FVX"]

.. code:: ipython3

    data = yf.download(ticker1,period="5y")


.. parsed-literal::

    [*********************100%***********************]  2 of 2 completed


.. code:: ipython3

    data.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead tr th {
            text-align: left;
        }

        .dataframe thead tr:last-of-type th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <th colspan="2" halign="left">Adj Close</th>
          <th colspan="2" halign="left">Close</th>
          <th colspan="2" halign="left">High</th>
          <th colspan="2" halign="left">Low</th>
          <th colspan="2" halign="left">Open</th>
          <th colspan="2" halign="left">Volume</th>
        </tr>
        <tr>
          <th></th>
          <th>^FVX</th>
          <th>^TNX</th>
          <th>^FVX</th>
          <th>^TNX</th>
          <th>^FVX</th>
          <th>^TNX</th>
          <th>^FVX</th>
          <th>^TNX</th>
          <th>^FVX</th>
          <th>^TNX</th>
          <th>^FVX</th>
          <th>^TNX</th>
        </tr>
        <tr>
          <th>Date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2016-12-05</th>
          <td>1.844</td>
          <td>2.387</td>
          <td>1.844</td>
          <td>2.387</td>
          <td>1.887</td>
          <td>2.449</td>
          <td>1.813</td>
          <td>2.362</td>
          <td>1.860</td>
          <td>2.423</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-06</th>
          <td>1.841</td>
          <td>2.396</td>
          <td>1.841</td>
          <td>2.396</td>
          <td>1.851</td>
          <td>2.403</td>
          <td>1.827</td>
          <td>2.378</td>
          <td>1.832</td>
          <td>2.385</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-07</th>
          <td>1.798</td>
          <td>2.347</td>
          <td>1.798</td>
          <td>2.347</td>
          <td>1.828</td>
          <td>2.376</td>
          <td>1.796</td>
          <td>2.346</td>
          <td>1.821</td>
          <td>2.371</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-08</th>
          <td>1.819</td>
          <td>2.387</td>
          <td>1.819</td>
          <td>2.387</td>
          <td>1.856</td>
          <td>2.425</td>
          <td>1.811</td>
          <td>2.371</td>
          <td>1.833</td>
          <td>2.393</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2016-12-09</th>
          <td>1.881</td>
          <td>2.464</td>
          <td>1.881</td>
          <td>2.464</td>
          <td>1.894</td>
          <td>2.478</td>
          <td>1.821</td>
          <td>2.398</td>
          <td>1.836</td>
          <td>2.413</td>
          <td>0</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    </div>



 ### Stock Fundamentals

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

.. code:: ipython3

    dis.ticker




.. parsed-literal::

    'DIS'



.. code:: ipython3

    data=dis.history()

.. code:: ipython3

    dis.info




.. parsed-literal::

    {'zip': '91521',
     'sector': 'Communication Services',
     'fullTimeEmployees': 152000,
     'longBusinessSummary': 'The Walt Disney Company, together with its subsidiaries, operates as an entertainment company worldwide. It operates through two segments, Disney Media and Entertainment Distribution; and Disney Parks, Experiences and Products. The company engages in the film and episodic television content production and distribution activities, as well as operates television broadcast networks under the ABC, Disney, ESPN, Freeform, FX, Fox, National Geographic, and Star brands; and studios that produces motion pictures under the Walt Disney Pictures, Twentieth Century Studios, Marvel, Lucasfilm, Pixar, and Searchlight Pictures banners. It also offers direct-to-consumer streaming services through Disney+, Disney+ Hotstar, ESPN+, Hulu, and Star+; sale/licensing of film and television content to third-party television and subscription video-on-demand services; theatrical, home entertainment, and music distribution services; staging and licensing of live entertainment events; and post-production services by Industrial Light & Magic and Skywalker Sound. In addition, the company operates theme parks and resorts, such as Walt Disney World Resort in Florida; Disneyland Resort in California; Disneyland Paris; Hong Kong Disneyland Resort; and Shanghai Disney Resort; Disney Cruise Line, Disney Vacation Club, National Geographic Expeditions, and Adventures by Disney as well as Aulani, a Disney resort and spa in Hawaii; licenses its intellectual property to a third party for the operations of the Tokyo Disney Resort; and provides consumer products, which include licensing of trade names, characters, visual, literary, and other IP for use on merchandise, published materials, and games. Further, it sells branded merchandise through retail, online, and wholesale businesses; and develops and publishes books, comic books, and magazines. The Walt Disney Company was founded in 1923 and is based in Burbank, California.',
     'city': 'Burbank',
     'phone': '818 560 1000',
     'state': 'CA',
     'country': 'United States',
     'companyOfficers': [],
     'website': 'https://www.thewaltdisneycompany.com',
     'maxAge': 1,
     'address1': '500 South Buena Vista Street',
     'industry': 'Entertainment',
     'ebitdaMargins': 0.12761,
     'profitMargins': 0.029590001,
     'grossMargins': 0.33058,
     'operatingCashflow': 5567000064,
     'revenueGrowth': 0.26,
     'operatingMargins': 0.051799998,
     'ebitda': 8602999808,
     'targetLowPrice': None,
     'recommendationKey': 'buy',
     'grossProfits': 22287000000,
     'freeCashflow': 7388250112,
     'targetMedianPrice': None,
     'currentPrice': 146.22,
     'earningsGrowth': None,
     'currentRatio': 1.083,
     'returnOnAssets': 0.0107700005,
     'numberOfAnalystOpinions': None,
     'targetMeanPrice': None,
     'debtToEquity': 57.044,
     'returnOnEquity': 0.025390001,
     'targetHighPrice': None,
     'totalCash': 15959000064,
     'totalDebt': 58312998912,
     'totalRevenue': 67418001408,
     'totalCashPerShare': 8.78,
     'financialCurrency': 'USD',
     'revenuePerShare': 37.124,
     'quickRatio': 0.944,
     'recommendationMean': 2,
     'exchange': 'NYQ',
     'shortName': 'Walt Disney Company (The)',
     'longName': 'The Walt Disney Company',
     'exchangeTimezoneName': 'America/New_York',
     'exchangeTimezoneShortName': 'EST',
     'isEsgPopulated': False,
     'gmtOffSetMilliseconds': '-18000000',
     'quoteType': 'EQUITY',
     'symbol': 'DIS',
     'messageBoardId': 'finmb_191564',
     'market': 'us_market',
     'annualHoldingsTurnover': None,
     'enterpriseToRevenue': 4.773,
     'beta3Year': None,
     'enterpriseToEbitda': 37.406,
     '52WeekChange': -0.04854244,
     'morningStarRiskRating': None,
     'forwardEps': 5.03,
     'revenueQuarterlyGrowth': None,
     'sharesOutstanding': 1817660032,
     'fundInceptionDate': None,
     'annualReportExpenseRatio': None,
     'totalAssets': None,
     'bookValue': 48.709,
     'sharesShort': 22380668,
     'sharesPercentSharesOut': 0.0123000005,
     'fundFamily': None,
     'lastFiscalYearEnd': 1633132800,
     'heldPercentInstitutions': 0.66523004,
     'netIncomeToCommon': 2024000000,
     'trailingEps': 1.094,
     'lastDividendValue': 0.88,
     'SandP52WeekChange': 0.22927392,
     'priceToBook': 3.0019093,
     'heldPercentInsiders': 0.00096000003,
     'nextFiscalYearEnd': 1696204800,
     'yield': None,
     'mostRecentQuarter': 1633132800,
     'shortRatio': 1.69,
     'sharesShortPreviousMonthDate': 1634256000,
     'floatShares': 1815711056,
     'beta': 1.16935,
     'enterpriseValue': 321802665984,
     'priceHint': 2,
     'threeYearAverageReturn': None,
     'lastSplitDate': 1181692800,
     'lastSplitFactor': '10000:9865',
     'legalType': None,
     'lastDividendDate': 1576195200,
     'morningStarOverallRating': None,
     'earningsQuarterlyGrowth': None,
     'priceToSalesTrailing12Months': 3.9422445,
     'dateShortInterest': 1636934400,
     'pegRatio': 0.98,
     'ytdReturn': None,
     'forwardPE': 29.069582,
     'lastCapGain': None,
     'shortPercentOfFloat': 0.0123000005,
     'sharesShortPriorMonth': 24561619,
     'impliedSharesOutstanding': None,
     'category': None,
     'fiveYearAverageReturn': None,
     'previousClose': 147.2,
     'regularMarketOpen': 147.81,
     'twoHundredDayAverage': 177.8214,
     'trailingAnnualDividendYield': 0.005978261,
     'payoutRatio': 0,
     'volume24Hr': None,
     'regularMarketDayHigh': 148.315,
     'navPrice': None,
     'averageDailyVolume10Day': 16995350,
     'regularMarketPreviousClose': 147.2,
     'fiftyDayAverage': 166.4474,
     'trailingAnnualDividendRate': 0.88,
     'open': 147.81,
     'toCurrency': None,
     'averageVolume10days': 16995350,
     'expireDate': None,
     'algorithm': None,
     'dividendRate': None,
     'exDividendDate': 1576195200,
     'circulatingSupply': None,
     'startDate': None,
     'regularMarketDayLow': 144.32,
     'currency': 'USD',
     'trailingPE': 133.65631,
     'regularMarketVolume': 14975619,
     'lastMarket': None,
     'maxSupply': None,
     'openInterest': None,
     'marketCap': 265778249728,
     'volumeAllCurrencies': None,
     'strikePrice': None,
     'averageVolume': 11795436,
     'dayLow': 144.32,
     'ask': 146.98,
     'askSize': 1000,
     'volume': 14975619,
     'fiftyTwoWeekHigh': 203.02,
     'fromCurrency': None,
     'fiveYearAvgDividendYield': None,
     'fiftyTwoWeekLow': 142.04,
     'bid': 146.8,
     'tradeable': False,
     'dividendYield': None,
     'bidSize': 800,
     'dayHigh': 148.315,
     'regularMarketPrice': 146.22,
     'preMarketPrice': None,
     'logo_url': 'https://logo.clearbit.com/thewaltdisneycompany.com'}



.. code:: ipython3

    import pandas as pd
    df = pd.Series(dis.info,name="DIS").to_frame().T
    df




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>zip</th>
          <th>sector</th>
          <th>fullTimeEmployees</th>
          <th>longBusinessSummary</th>
          <th>city</th>
          <th>phone</th>
          <th>state</th>
          <th>country</th>
          <th>companyOfficers</th>
          <th>website</th>
          <th>...</th>
          <th>fiveYearAvgDividendYield</th>
          <th>fiftyTwoWeekLow</th>
          <th>bid</th>
          <th>tradeable</th>
          <th>dividendYield</th>
          <th>bidSize</th>
          <th>dayHigh</th>
          <th>regularMarketPrice</th>
          <th>preMarketPrice</th>
          <th>logo_url</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>DIS</th>
          <td>91521</td>
          <td>Communication Services</td>
          <td>152000</td>
          <td>The Walt Disney Company, together with its sub...</td>
          <td>Burbank</td>
          <td>818 560 1000</td>
          <td>CA</td>
          <td>United States</td>
          <td>[]</td>
          <td>https://www.thewaltdisneycompany.com</td>
          <td>...</td>
          <td>None</td>
          <td>142.04</td>
          <td>146.8</td>
          <td>False</td>
          <td>None</td>
          <td>800</td>
          <td>148.315</td>
          <td>146.22</td>
          <td>None</td>
          <td>https://logo.clearbit.com/thewaltdisneycompany...</td>
        </tr>
      </tbody>
    </table>
    <p>1 rows × 152 columns</p>
    </div>



.. code:: ipython3

    ticker = ["MSFT","FB"]

.. code:: ipython3

    for i in ticker:
        df.loc["{}".format(i)] = pd.Series(yf.Ticker(i).info)

.. code:: ipython3

    df.info()

 ### Import Financials

.. code:: ipython3

    dis

.. code:: ipython3

    dis.balance_sheet

.. code:: ipython3

    dis.financials

.. code:: ipython3

    dis.cashflow

 ### Put Call Option

.. code:: ipython3

    dis

.. code:: ipython3

    dis.option_chain()

.. code:: ipython3

    calls = dis.option_chain()[0]
    calls

.. code:: ipython3

    puts = dis.option_chain()[1]
    puts

 ### Stream Realtime Data

.. code:: ipython3

    import time

.. code:: ipython3

    ticker1 ="EURUSD=X"

.. code:: ipython3

    data = yf.download(ticker1,interval = '1m', period='1d')

.. code:: ipython3

    print(data.index[-1], data.iloc[-1,3])

.. code:: ipython3

    #Every 5 second data corresponding to 5 seconds
    while True:
        time.sleep(5)
        data = yf.download(ticker1,interval = '1m', period='1d')
        print(data.index[-1], data.iloc[-1,3])




Callback Collection
-------------------

Stable Baselines provides you with a set of common callbacks for:

- saving the model periodically (:ref:`CheckpointCallback`)
- evaluating the model periodically and saving the best one (:ref:`EvalCallback`)
- chaining callbacks (:ref:`CallbackList`)
- triggering callback on events (:ref:`EventCallback`, :ref:`EveryNTimesteps`)
- stopping the training early based on a reward threshold (:ref:`StopTrainingOnRewardThreshold <StopTrainingCallback>`)


.. _CheckpointCallback:

CheckpointCallback
^^^^^^^^^^^^^^^^^^

Callback for saving a model every ``save_freq`` steps, you must specify a log folder (``save_path``)
and optionally a prefix for the checkpoints (``rl_model`` by default).


.. code-block:: python

    from stable_baselines import SAC
    from stable_baselines.common.callbacks import CheckpointCallback
    # Save a checkpoint every 1000 steps
    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./logs/',
                                             name_prefix='rl_model')

    model = SAC('MlpPolicy', 'Pendulum-v0')
    model.learn(2000, callback=checkpoint_callback)


.. _EvalCallback:

EvalCallback
^^^^^^^^^^^^

Evaluate periodically the performance of an agent, using a separate test environment.
It will save the best model if ``best_model_save_path`` folder is specified and save the evaluations results in a numpy archive (`evaluations.npz`) if ``log_path`` folder is specified.


.. note::

	You can pass a child callback via the ``callback_on_new_best`` argument. It will be triggered each time there is a new best model.



.. code-block:: python

    import gym

    from stable_baselines import SAC
    from stable_baselines.common.callbacks import EvalCallback

    # Separate evaluation env
    eval_env = gym.make('Pendulum-v0')
    # Use deterministic actions for evaluation
    eval_callback = EvalCallback(eval_env, best_model_save_path='./logs/',
                                 log_path='./logs/', eval_freq=500,
                                 deterministic=True, render=False)

    model = SAC('MlpPolicy', 'Pendulum-v0')
    model.learn(5000, callback=eval_callback)


.. _Callbacklist:

CallbackList
^^^^^^^^^^^^

Class for chaining callbacks, they will be called sequentially.
Alternatively, you can pass directly a list of callbacks to the `learn()` method, it will be converted automatically to a ``CallbackList``.


.. code-block:: python

    import gym

    from stable_baselines import SAC
    from stable_baselines.common.callbacks import CallbackList, CheckpointCallback, EvalCallback

    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./logs/')
    # Separate evaluation env
    eval_env = gym.make('Pendulum-v0')
    eval_callback = EvalCallback(eval_env, best_model_save_path='./logs/best_model',
                                 log_path='./logs/results', eval_freq=500)
    # Create the callback list
    callback = CallbackList([checkpoint_callback, eval_callback])

    model = SAC('MlpPolicy', 'Pendulum-v0')
    # Equivalent to:
    # model.learn(5000, callback=[checkpoint_callback, eval_callback])
    model.learn(5000, callback=callback)


.. _StopTrainingCallback:

StopTrainingOnRewardThreshold
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop the training once a threshold in episodic reward (mean episode reward over the evaluations) has been reached (i.e., when the model is good enough).
It must be used with the :ref:`EvalCallback` and use the event triggered by a new best model.


.. code-block:: python

    import gym

    from stable_baselines import SAC
    from stable_baselines.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold

    # Separate evaluation env
    eval_env = gym.make('Pendulum-v0')
    # Stop training when the model reaches the reward threshold
    callback_on_best = StopTrainingOnRewardThreshold(reward_threshold=-200, verbose=1)
    eval_callback = EvalCallback(eval_env, callback_on_new_best=callback_on_best, verbose=1)

    model = SAC('MlpPolicy', 'Pendulum-v0', verbose=1)
    # Almost infinite number of timesteps, but the training will stop
    # early as soon as the reward threshold is reached
    model.learn(int(1e10), callback=eval_callback)


.. _EveryNTimesteps:

EveryNTimesteps
^^^^^^^^^^^^^^^

An :ref:`EventCallback` that will trigger its child callback every ``n_steps`` timesteps.


.. note::

	Because of the way ``PPO1`` and ``TRPO`` work (they rely on MPI), ``n_steps`` is a lower bound between two events.


.. code-block:: python

  import gym

  from stable_baselines import PPO2
  from stable_baselines.common.callbacks import CheckpointCallback, EveryNTimesteps

  # this is equivalent to defining CheckpointCallback(save_freq=500)
  # checkpoint_callback will be triggered every 500 steps
  checkpoint_on_event = CheckpointCallback(save_freq=1, save_path='./logs/')
  event_callback = EveryNTimesteps(n_steps=500, callback=checkpoint_on_event)

  model = PPO2('MlpPolicy', 'Pendulum-v0', verbose=1)

  model.learn(int(2e4), callback=event_callback)


.. automodule:: stable_baselines.common.callbacks
  :members:


  Legacy: A functional approach
  -----------------------------

  .. warning::

  	This way of doing callbacks is deprecated in favor of the object oriented approach.



  A callback function takes the ``locals()`` variables and the ``globals()`` variables from the model, then returns a boolean value for whether or not the training should continue.

  Thanks to the access to the models variables, in particular ``_locals["self"]``, we are able to even change the parameters of the model without halting the training, or changing the model's code.


  .. code-block:: python

      from typing import Dict, Any

      from stable_baselines import PPO2


      def simple_callback(_locals: Dict[str, Any], _globals: Dict[str, Any]) -> bool:
          """
          Callback called at each step (for DQN and others) or after n steps (see ACER or PPO2).
          This callback will save the model and stop the training after the first call.

          :param _locals: (Dict[str, Any])
          :param _globals: (Dict[str, Any])
          :return: (bool) If your callback returns False, training is aborted early.
          """
          print("callback called")
          # Save the model
          _locals["self"].save("saved_model")
          # If you want to continue training, the callback must return True.
          # return True # returns True, training continues.
          print("stop training")
          return False # returns False, training stops.

      model = PPO2('MlpPolicy', 'CartPole-v1')
      model.learn(2000, callback=simple_callback)
