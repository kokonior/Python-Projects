import pandas as pd
from datetime import datetime, timedelta
from prettytable import PrettyTable
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use("fivethirtyeight")
plt.style.use("seaborn")


def time_series( data, y_label, dates1):
    dates = dates1
    plt.xlabel("time")
    plt.ylabel(y_label)
    plt.plot_date(dates, data, linestyle='solid')
    plt.show()


def qualitative_analysis(year, exports, imports):
    result = sum(exports) - sum(imports)
    if result > 0:
        table.add_row([year, sum(exports), sum(imports), sum(exports)-sum(imports), "Profit"])
    else:
        table.add_row([year, sum(exports), sum(imports),sum(exports)-sum(imports), "Loss"])


def shw_imports(data, year):
    year = "Pakistan Imports: " + year
    custom_bins = [400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000]
    plt.title(year)
    plt.xlabel("Revenue Spent (In PKR-CRORES)")
    plt.ylabel("Maximum Frequency")
    plt.hist(data, bins=custom_bins, edgecolor="White", color="red")
    plt.show()
    plt.tight_layout()


def shw_exports(data, year):
    year = "Pakistan Exports: " + year
    custom_bins = [100000, 200000, 300000, 400000, 500000]
    plt.title(year)
    plt.xlabel("Revenue Generated (in PKR-LACS)")
    plt.ylabel("Maximum Frequency")
    plt.hist(data, bins = custom_bins, edgecolor="white", color="orange")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    yy = [2017, 2018, 2019, 2020, 2021]
    xx = ["jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]
    x21 = ["jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sep"]
    start_date = datetime(2017, 1, 1)
    end_date = datetime(2021, 1, 1)
    emd_date2 = datetime(2022,1,1)
    table = PrettyTable(["YEAR", "EXPORTS", "IMPORTS","BALANCE OF TRADE", "PROFIT/LOSS"])
    exports = [186384, 171511, 188606, 189092, 170422, 200293, 171952, 196454, 176427, 198911, 208036, 214877,  # 2017
               217588, 209775, 250065, 246167, 247534, 224324, 204688, 249657, 214367, 248126, 246015, 287198,  # 2018
               283372, 261669, 275384, 295541, 306303, 266540, 200875, 293933, 276276, 315698, 312420, 308697,  # 2019
               305986, 330188, 287411, 157412, 223546, 263988, 336677, 265605, 313324, 342539, 346063, 378792,  # 2020
               343612, 329116, 368976, 339618, 256115, 426126, 373430, 368847, 401191]  # 2021
    """        jan     feb     mar     apr     may     june    july    aug     sep     oct     nov     dec      """
    imports = [496057, 462764, 524669, 523558, 533324, 475050, 509727, 521496, 471136, 591189, 516015, 533670,  # 2017
               618979, 529775, 591741, 599741, 661212, 676992, 601586, 617949, 549708, 631246, 617646, 615030,  # 2018
               624644, 579039, 578273, 670895, 734578, 677510, 638338, 578294, 591111, 635282, 612215, 625463,  # 2019
               639572, 645648, 525410, 526880, 458272, 614004, 614934, 557418, 716717, 636036, 686349, 801162,  # 2020
               771939, 735609, 883175, 805180, 813622, 995843, 893960, 1081961, 1092235]  # 2021

    imports17 = [496057, 462764, 524669, 523558, 533324, 475050, 509727, 521496, 471136, 591189, 516015, 533670]
    imports18 = [618979, 529775, 591741, 599741, 661212, 676992, 601586, 617949, 549708, 631246, 617646, 615030]
    imports19 = [624644, 579039, 578273, 670895, 734578, 677510, 638338, 578294, 591111, 635282, 612215, 625463]
    imports20 = [639572, 645648, 525410, 526880, 458272, 614004, 614934, 557418, 716717, 636036, 686349, 801162]
    imports21 = [771939, 735609, 883175, 805180, 813622, 995843, 893960, 1081961, 1092235]

    exports17 = [186384, 171511, 188606, 189092, 170422, 200293, 171952, 196454, 176427, 198911, 208036, 214877]
    exports18 = [217588, 209775, 250065, 246167, 247534, 224324, 204688, 249657, 214367, 248126, 246015, 287198]
    exports19 = [283372, 261669, 275384, 295541, 306303, 266540, 200875, 293933, 276276, 315698, 312420, 308697]
    exports20 = [305986, 330188, 287411, 157412, 223546, 263988, 336677, 265605, 313324, 342539, 346063, 378792]
    exports21 = [343612, 329116, 368976, 339618, 256115, 426126, 373430, 368847, 401191]
    exports_label = "Exports Revenue (in PKR-LACS)"
    imports_label = "Imports Revenie Spent (in PKR-CRORES)"
    yearly_exports = [sum(exports17),sum(exports18),sum(exports19),sum(exports20),sum(exports21)]
    yearly_imports = [sum(imports17), sum(imports18), sum(imports19), sum(imports20), sum(imports21)]

    shw_exports(exports, "2017-2021")
    time_series(yearly_exports, exports_label, yy)
    shw_imports(imports, "2017-2021")
    time_series(yearly_exports, imports_label, yy)
    shw_exports(exports17, "2017")
    time_series(exports17, exports_label, xx)
    shw_imports(imports17, "2017")
    time_series(imports17, exports_label, xx)
    shw_exports(exports18, "2018")
    time_series(exports18, exports_label, xx)
    shw_imports(imports18, "2018")
    time_series(imports18, exports_label, xx)
    shw_exports(exports19, "2019")
    time_series(exports19, exports_label, xx)
    shw_imports(imports19, "2019")
    time_series(imports19, exports_label, xx)
    shw_exports(exports20, "2020")
    time_series(exports20, exports_label, xx)
    shw_imports(imports20, "2020")
    time_series(imports20, exports_label, xx)
    shw_exports(exports21, "2021")
    time_series(exports21, exports_label, x21)
    shw_imports(imports21, "2021")
    time_series(imports21, exports_label, x21)

    qualitative_analysis("2017-2021", exports, imports)
    qualitative_analysis("2017", exports17, imports17)
    qualitative_analysis("2018", exports18, imports18)
    qualitative_analysis("2019", exports19, imports19)
    qualitative_analysis("2020", exports20, imports20)
    qualitative_analysis("2021", exports21, imports21)
    print("\t\t\t***QUALITATIVE ANALYSIS OF EXPORTS AND IMPORTS***")
    print(table)
